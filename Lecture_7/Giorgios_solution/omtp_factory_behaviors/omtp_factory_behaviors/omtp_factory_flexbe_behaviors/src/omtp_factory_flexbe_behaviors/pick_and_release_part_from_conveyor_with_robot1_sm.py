#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_manipulation_states.moveit_to_joints_state import MoveitToJointsState
from omtp_factory_flexbe_states.detect_part_camera_state import DetectPartCameraState
from omtp_factory_flexbe_states.compute_grasp_state import ComputeGraspState
from omtp_factory_flexbe_states.vacuum_gripper_control_state import VacuumGripperControlState
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun May 10 2020
@author: Giorgio Frego
'''
class Pick_and_release_part_from_conveyor_with_robot1SM(Behavior):
	'''
	This behaviour will make robot 1 pick a part from the conveyor in our factory
	'''


	def __init__(self):
		super(Pick_and_release_part_from_conveyor_with_robot1SM, self).__init__()
		self.name = 'Pick_and_release_part_from_conveyor_with_robot1'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		RobotName = 'robot1'
		home1 = [ -1.57, -1.57, -1.57, -1.57, 1.57, 0.0]
		base_frame = 'robot1_base_link'
		cam_topic = '/omtp/logical_camera'
		cam_frame = 'logical_camera_frame'
		joint_names = ['robot1_shoulder_pan_joint','robot1_shoulder_lift_joint', 'robot1_elbow_joint','robot1_wrist_1_joint','robot1_wrist_2_joint','robot1_wrist_3_joint']
		tool_link_name = 'vacuum_gripper1_suction_cup'
		gripper_service = '/gripper1/control'
		R1Place = [1.57,-0.75,1.0 , -1.95, -1.57, 0.0]
		# x:107 y:426, x:11 y:229
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.part_pose = [ ]
		_state_machine.userdata.pick_configuration = home1
		_state_machine.userdata.udhome1 = home1
		_state_machine.userdata.udR1Place = R1Place

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:87 y:27
			OperatableStateMachine.add('move_home_pose',
										MoveitToJointsState(move_group=RobotName, joint_names=joint_names, action_topic='/move_group'),
										transitions={'reached': 'Detect_object_on_conveyor', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_config': 'udhome1'})

			# x:647 y:35
			OperatableStateMachine.add('move_pre-grasp_pose',
										MoveitToJointsState(move_group=RobotName, joint_names=joint_names, action_topic='/move_group'),
										transitions={'reached': 'Activate_gripper', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_config': 'pregrasp_joint_values'})

			# x:948 y:178
			OperatableStateMachine.add('move_grasp',
										MoveitToJointsState(move_group=RobotName, joint_names=joint_names, action_topic='/move_group'),
										transitions={'reached': 'move_place', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_config': 'grasp_joint_values'})

			# x:800 y:289
			OperatableStateMachine.add('move_place',
										MoveitToJointsState(move_group=RobotName, joint_names=joint_names, action_topic='/move_group'),
										transitions={'reached': 'deactivate_gripper', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_config': 'udR1Place'})

			# x:546 y:424
			OperatableStateMachine.add('Move_home_2',
										MoveitToJointsState(move_group=RobotName, joint_names=joint_names, action_topic='/move_group'),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_config': 'udhome1'})

			# x:285 y:23
			OperatableStateMachine.add('Detect_object_on_conveyor',
										DetectPartCameraState(ref_frame=base_frame, camera_topic=cam_topic, camera_frame=cam_frame),
										transitions={'continue': 'compute_pre_grasp', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'part_pose'})

			# x:473 y:29
			OperatableStateMachine.add('compute_pre_grasp',
										ComputeGraspState(group=RobotName, offset=0.25, joint_names=joint_names, tool_link=tool_link_name, rotation=3.14),
										transitions={'continue': 'move_pre-grasp_pose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'part_pose', 'joint_values': 'pregrasp_joint_values', 'joint_names': 'pregrasp_joint_names'})

			# x:956 y:105
			OperatableStateMachine.add('compute_grasp',
										ComputeGraspState(group=RobotName, offset=0.11, joint_names=joint_names, tool_link=tool_link_name, rotation=3.14),
										transitions={'continue': 'move_grasp', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'part_pose', 'joint_values': 'grasp_joint_values', 'joint_names': 'grasp_joint_names'})

			# x:849 y:38
			OperatableStateMachine.add('Activate_gripper',
										VacuumGripperControlState(enable='true', service_name=gripper_service),
										transitions={'continue': 'compute_grasp', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:799 y:365
			OperatableStateMachine.add('deactivate_gripper',
										VacuumGripperControlState(enable=0, service_name=gripper_service),
										transitions={'continue': 'wait_griper_off', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:751 y:439
			OperatableStateMachine.add('wait_griper_off',
										WaitState(wait_time=2.0),
										transitions={'done': 'Move_home_2'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
