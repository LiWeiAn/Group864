#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from omtp_factory_flexbe_states.moveit_to_joints_dyn_state import MoveitToJointsDynState
from omtp_factory_flexbe_states.detect_part_camera_state import DetectPartCameraState
from omtp_factory_flexbe_states.compute_grasp_state import ComputeGraspState
from omtp_factory_flexbe_states.vacuum_gripper_control_state import VacuumGripperControlState
from omtp_factory_flexbe_states.set_conveyor_power_state import SetConveyorPowerState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 07 2020
@author: Vivian Li
'''
class Graspanobjectwithrobot1SM(Behavior):
	'''
	This behaviour will make robot1 go to its home position. When an object is detected from the conveyor, the robot will pick it up and go to the configured place position.
	'''


	def __init__(self):
		super(Graspanobjectwithrobot1SM, self).__init__()
		self.name = 'Grasp an object with robot1'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		pick_group = 'robot1'
		home1 = [1.57, -1.57, 1.24, -1.57, -1.57, 0]
		joint_names1 = ['robot1_elbow_joint', 'robot1_shoulder_lift_joint', 'robot1_shoulder_pan_joint', 'robot1_wrist_1_joint', 'robot1_wrist_2_joint', 'robot1_wrist_3_joint']
		pre_grasp1 = [1.57, -1.44, -0.01, -1.61, -1.54, 1.30]
		speed1 = 100.0
		speed_stop = 0.0
		# x:1224 y:566, x:50 y:669
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.home1 = home1
		_state_machine.userdata.joint_names = joint_names1
		_state_machine.userdata.object_pose = []
		_state_machine.userdata.grasp_joint_values = home1
		_state_machine.userdata.pre_grasp1 = pre_grasp1
		_state_machine.userdata.speed_stop = speed_stop
		_state_machine.userdata.speed1 = speed1

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:37 y:46
			OperatableStateMachine.add('Move to home position',
										MoveitToJointsDynState(move_group=pick_group, offset=0.01, tool_link='vacuum_gripper1_suction_cup', action_topic='/move_group'),
										transitions={'reached': 'Start conveyor', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'home1', 'joint_names': 'joint_names'})

			# x:424 y:38
			OperatableStateMachine.add('Detect object on conveyor',
										DetectPartCameraState(ref_frame='robot1_base_link', camera_topic='/omtp/logical_camera', camera_frame='logical_camera_frame'),
										transitions={'continue': 'Stop conveyor', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'object_pose'})

			# x:957 y:165
			OperatableStateMachine.add('Compute joint configuration for grasp',
										ComputeGraspState(group='robot1', offset=0.0, joint_names=joint_names1, tool_link='vacuum_gripper1_suction_cup', rotation=3.1415),
										transitions={'continue': 'Move robot1 to pick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'object_pose', 'joint_values': 'grasp_joint_values', 'joint_names': 'joint_names'})

			# x:1003 y:281
			OperatableStateMachine.add('Move robot1 to pick',
										MoveitToJointsDynState(move_group=pick_group, offset=0.00, tool_link='vacuum_gripper1_suction_cup', action_topic='/move_group'),
										transitions={'reached': 'Activate gripper', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'grasp_joint_values', 'joint_names': 'joint_names'})

			# x:997 y:405
			OperatableStateMachine.add('Activate gripper',
										VacuumGripperControlState(enable='true', service_name='/gripper1/control'),
										transitions={'continue': 'Move to home position_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1000 y:528
			OperatableStateMachine.add('Move to home position_2',
										MoveitToJointsDynState(move_group=pick_group, offset=0.01, tool_link='vacuum_gripper1_suction_cup', action_topic='/move_group'),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'home1', 'joint_names': 'joint_names'})

			# x:873 y:24
			OperatableStateMachine.add('Move to pre-grasp position',
										MoveitToJointsDynState(move_group=pick_group, offset=0.01, tool_link='vacuum_gripper1_suction_cup', action_topic='/move_group'),
										transitions={'reached': 'Compute joint configuration for grasp', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'pre_grasp1', 'joint_names': 'joint_names'})

			# x:165 y:122
			OperatableStateMachine.add('Start conveyor',
										SetConveyorPowerState(stop=False),
										transitions={'succeeded': 'Detect object on conveyor', 'failed': 'failed'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'speed': 'speed1'})

			# x:650 y:23
			OperatableStateMachine.add('Stop conveyor',
										SetConveyorPowerState(stop=True),
										transitions={'succeeded': 'Move to pre-grasp position', 'failed': 'failed'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'speed': 'speed_stop'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
