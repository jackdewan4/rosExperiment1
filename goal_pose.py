#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# Callbacks definition

def active_cb():
    rospy.loginfo("Goal pose being processed")

def feedback_cb(feedback):
    # rospy.loginfo("Current location: "+str(feedback))
    pass


def done_cb(status, result):
    if status == 3:
        rospy.loginfo("Goal reached")
    if status == 2 or status == 8:
        rospy.loginfo("Goal cancelled")
    if status == 4:
        rospy.loginfo("Goal aborted")
    

rospy.init_node('goal_pose')



def moveToPose(x, y, z, qx, qy, qz ,qw):
    # 7th intermediate pose
    navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    navclient.wait_for_server()


    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.position.z = z
    goal.target_pose.pose.orientation.x = qx
    goal.target_pose.pose.orientation.y = qy
    goal.target_pose.pose.orientation.z = qz
    goal.target_pose.pose.orientation.w = qw

    navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
    finished = navclient.wait_for_result()

    navclient.wait_for_server()


rospy.loginfo("moving to point 1 \n")
moveToPose(-1.54, -1.207, 0, 0, 0, 0.1577, 0.987)
rospy.loginfo("moving to point 2 \n")
moveToPose(0.2038, -2.9377, 0, 0, 0, 0.937, 0.3488)
rospy.loginfo("moving to point 3 \n")
moveToPose(-0.877, -0.55, 0, 0, 0, 0.9855, 0.16909)
rospy.loginfo("moving to point 4 \n")
moveToPose(-0.288, 0.819, 0, 0, 0, -0.1185, 0.992)



if not finished:
    rospy.logerr("Action server not available!")
else:
    rospy.loginfo ( navclient.get_result())