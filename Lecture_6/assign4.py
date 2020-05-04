#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import actionlib
import geometry_msgs
from omtp_gazebo.msg import LogicalCameraImage
from omtp_gazebo.srv import VacuumGripperControl
import tf2_ros
import tf2_geometry_msgs
import geometry_msgs



def logical_camera1_callback(data):
    # Check if the logical camera has seen our box which has the name 'object'.
    if (data.models[-1].type == 'object'):
        # Create a pose stamped message type from the camera image topic.
        global object_pose
        object_pose = geometry_msgs.msg.PoseStamped()
        object_pose.header.stamp = rospy.Time.now()
        object_pose.header.frame_id = "logical_camera_1_frame"
        object_pose.pose.position.x = data.models[-1].pose.position.x
        object_pose.pose.position.y = data.models[-1].pose.position.y
        object_pose.pose.position.z = data.models[-1].pose.position.z
        object_pose.pose.orientation.x = data.models[-1].pose.orientation.x
        object_pose.pose.orientation.y = data.models[-1].pose.orientation.y
        object_pose.pose.orientation.z = data.models[-1].pose.orientation.z
        object_pose.pose.orientation.w = data.models[-1].pose.orientation.w
        while True:
            try:
                global object_gripper_pose
                object_gripper_pose = tf_buffer.transform(object_pose, "vacuum_gripper1_suction_cup")
                global object_world_pose
                object_world_pose = tf_buffer.transform(object_pose, "world")
                break
            except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
                continue
        #rospy.loginfo('Pose of the object in the vacuum_gripper2_suction_cup reference frame is: %s', object_world_pose)
        #rospy.loginfo('Pose of the object in the reference framecamera of logical camera2 is: %s', object_pose)

def gripper_grasp(choice):
    rospy.wait_for_service('/gripper1/control')
    try:
        grasp = rospy.ServiceProxy('/gripper1/control', VacuumGripperControl)
        grasp = grasp(choice)
    except rospy.ServiceException, e:
        print "Service call failed: %s"



def pick_and_place():
  ## First initialize moveit_commander and rospy.
  moveit_commander.roscpp_initialize(sys.argv)
  #rospy.init_node('pick_and_place', anonymous=True)

  ## Instantiate a MoveGroupCommander object.  This object is an interface
  ## to one group of joints.  In this case the group refers to the joints of
  ## robot1. This interface can be used to plan and execute motions on robot1.
  robot1_group = moveit_commander.MoveGroupCommander("robot1")
  ## MoveGroup Commander Object for robot2.
  robot2_group = moveit_commander.MoveGroupCommander("robot2")

  ## Action clients to the ExecuteTrajectory action server.
  robot1_client = actionlib.SimpleActionClient('execute_trajectory',
    moveit_msgs.msg.ExecuteTrajectoryAction)
  robot1_client.wait_for_server()
  rospy.loginfo('Execute Trajectory server is available for robot1')

  robot2_client = actionlib.SimpleActionClient('execute_trajectory',
    moveit_msgs.msg.ExecuteTrajectoryAction)
  robot2_client.wait_for_server()
  rospy.loginfo('Execute Trajectory server is available for robot2')

  ## Set a named joint configuration as the goal to plan for a move group.
  ## Named joint configurations are the robot poses defined via MoveIt! Setup Assistant.
  robot1_group.set_named_target("R1Home")

  ## Plan to the desired joint-space goal using the default planner (RRTConnect).
  robot1_plan_home = robot1_group.plan()
  ## Create a goal message object for the action server.
  robot1_goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
  ## Update the trajectory in the goal message.
  robot1_goal.trajectory = robot1_plan_home

  ## Send the goal to the action server.
  robot1_client.send_goal(robot1_goal)
  robot1_client.wait_for_result()

  robot1_group.set_named_target("R1PreGrasp")
  robot1_plan_pregrasp = robot1_group.plan()
  robot1_goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
  robot1_goal.trajectory = robot1_plan_pregrasp
  robot1_client.send_goal(robot1_goal)
  robot1_client.wait_for_result()

  ## Cartesian Paths
  ## ^^^^^^^^^^^^^^^
  ## You can plan a cartesian path directly by specifying a list of waypoints
  ## for the end-effector to go through.
  waypoints = []
  # start with the current pose
  current_pose = robot1_group.get_current_pose()
  rospy.sleep(0.5)
  current_pose = robot1_group.get_current_pose()
  gripper_grasp(True)
  ## create linear offsets to the current pose
  new_eef_pose = geometry_msgs.msg.Pose()

  # USE THIS:
  #new_eef_pose.position.x = current_pose.pose.position.x - object_gripper_pose.pose.position.x 
  #new_eef_pose.position.y = current_pose.pose.position.y + object_gripper_pose.pose.position.y 
  #new_eef_pose.position.z = current_pose.pose.position.z - object_gripper_pose.pose.position.z +0.16

  # OR THIS:
  new_eef_pose.position.x = object_world_pose.pose.position.x 
  new_eef_pose.position.y = object_world_pose.pose.position.y 
  new_eef_pose.position.z = object_world_pose.pose.position.z + 0.16


  # Retain orientation of the current pose.
  new_eef_pose.orientation = copy.deepcopy(current_pose.pose.orientation)

  waypoints.append(new_eef_pose)
  waypoints.append(current_pose.pose)
  print(new_eef_pose.position)
  print(current_pose.pose.position)

  ## We want the cartesian path to be interpolated at a resolution of 1 cm
  ## which is why we will specify 0.01 as the eef_step in cartesian
  ## translation.  We will specify the jump threshold as 0.0, effectively
  ## disabling it.
  fraction = 0.0
  for count_cartesian_path in range(0,3):
    if fraction < 1.0:
      (plan_cartesian, fraction) = robot1_group.compute_cartesian_path(
                                   waypoints,   # waypoints to follow
                                   0.01,        # eef_step
                                   0.0)         # jump_threshold
    else:
      break

  robot1_goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
  robot1_goal.trajectory = plan_cartesian
  robot1_client.send_goal(robot1_goal)
  robot1_client.wait_for_result()
  

  robot1_group.set_named_target("R1Place")
  robot1_plan_place = robot1_group.plan()
  robot1_goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
  robot1_goal.trajectory = robot1_plan_place
  robot1_client.send_goal(robot1_goal)
  robot1_client.wait_for_result()
  gripper_grasp(False)

  ## When finished shut down moveit_commander.
  moveit_commander.roscpp_shutdown()

def listener():
    # Initialize ROS node to transform object pose.

    # Create a TF buffer in the global scope

    # Subscribe to the logical camera topic.
    rospy.Subscriber('/omtp/logical_camera_1', LogicalCameraImage, logical_camera1_callback)



if __name__=='__main__':
  rospy.init_node('listener_node', anonymous=True)
  tf_buffer = tf2_ros.Buffer()
  tf_listener = tf2_ros.TransformListener(tf_buffer)

  try:
      listener()
      pick_and_place()
      rospy.spin()
  except rospy.ROSInterruptException:
      pass      

