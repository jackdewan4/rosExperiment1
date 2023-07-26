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

# navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
# navclient.wait_for_server()

# # first intermediate pose
# goal = MoveBaseGoal()
# goal.target_pose.header.frame_id = "map"
# goal.target_pose.header.stamp = rospy.Time.now()

# goal.target_pose.pose.position.x = -0.505
# goal.target_pose.pose.position.y = -0.0852
# goal.target_pose.pose.position.z = 0.0
# goal.target_pose.pose.orientation.x = 0.0
# goal.target_pose.pose.orientation.y = 0.0
# goal.target_pose.pose.orientation.z = 0.164
# goal.target_pose.pose.orientation.w = 0.986

# navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
# finished = navclient.wait_for_result()

# navclient.wait_for_server()




# navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
# navclient.wait_for_server()

# # 2nd intermediate pose
# goal = MoveBaseGoal()
# goal.target_pose.header.frame_id = "map"
# goal.target_pose.header.stamp = rospy.Time.now()

# goal.target_pose.pose.position.x = -0.536
# goal.target_pose.pose.position.y = -0.005
# goal.target_pose.pose.position.z = 0.0
# goal.target_pose.pose.orientation.x = 0.0
# goal.target_pose.pose.orientation.y = 0.0
# goal.target_pose.pose.orientation.z = -0.0466
# goal.target_pose.pose.orientation.w = 0.999

# navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
# finished = navclient.wait_for_result()

# navclient.wait_for_server()


# navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
# navclient.wait_for_server()

# # third intermediate pose
# goal = MoveBaseGoal()
# goal.target_pose.header.frame_id = "map"
# goal.target_pose.header.stamp = rospy.Time.now()

# goal.target_pose.pose.position.x = -1.187
# goal.target_pose.pose.position.y = -0.04434
# goal.target_pose.pose.position.z = 0.0
# goal.target_pose.pose.orientation.x = 0.0
# goal.target_pose.pose.orientation.y = 0.0
# goal.target_pose.pose.orientation.z = -0.0708
# goal.target_pose.pose.orientation.w = 0.997

# navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
# finished = navclient.wait_for_result()

# navclient.wait_for_server()

# # 4th intermediate pose
# navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
# navclient.wait_for_server()


# goal = MoveBaseGoal()
# goal.target_pose.header.frame_id = "map"
# goal.target_pose.header.stamp = rospy.Time.now()

# goal.target_pose.pose.position.x = -1.6598
# goal.target_pose.pose.position.y = -0.02166
# goal.target_pose.pose.position.z = 0.0
# goal.target_pose.pose.orientation.x = 0.0
# goal.target_pose.pose.orientation.y = 0.0
# goal.target_pose.pose.orientation.z = -0.0407
# goal.target_pose.pose.orientation.w = 0.999

# navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
# finished = navclient.wait_for_result()

# navclient.wait_for_server()


# # 5th intermediate pose
# navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
# navclient.wait_for_server()


# goal = MoveBaseGoal()
# goal.target_pose.header.frame_id = "map"
# goal.target_pose.header.stamp = rospy.Time.now()

# goal.target_pose.pose.position.x = -1.852
# goal.target_pose.pose.position.y = -0.2124
# goal.target_pose.pose.position.z = 0.0
# goal.target_pose.pose.orientation.x = 0.0
# goal.target_pose.pose.orientation.y = 0.0
# goal.target_pose.pose.orientation.z = 0.644
# goal.target_pose.pose.orientation.w = 0.7646

# navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
# finished = navclient.wait_for_result()

# navclient.wait_for_server()


# # 7th intermediate pose
# navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
# navclient.wait_for_server()


# goal = MoveBaseGoal()
# goal.target_pose.header.frame_id = "map"
# goal.target_pose.header.stamp = rospy.Time.now()

# goal.target_pose.pose.position.x = -1.8744
# goal.target_pose.pose.position.y = -0.0704
# goal.target_pose.pose.position.z = 0.0
# goal.target_pose.pose.orientation.x = 0.0
# goal.target_pose.pose.orientation.y = 0.0
# goal.target_pose.pose.orientation.z = 0.7212
# goal.target_pose.pose.orientation.w = 0.6927

# navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
# finished = navclient.wait_for_result()

# navclient.wait_for_server()

# # 8th intermediate pose
# navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
# navclient.wait_for_server()


# goal = MoveBaseGoal()
# goal.target_pose.header.frame_id = "map"
# goal.target_pose.header.stamp = rospy.Time.now()

# goal.target_pose.pose.position.x = -1.866
# goal.target_pose.pose.position.y = -1.2807
# goal.target_pose.pose.position.z = 0.0
# goal.target_pose.pose.orientation.x = 0.0
# goal.target_pose.pose.orientation.y = 0.0
# goal.target_pose.pose.orientation.z = 0.6088
# goal.target_pose.pose.orientation.w = 0.7933

# navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
# finished = navclient.wait_for_result()

# navclient.wait_for_server()


# # 7th intermediate pose
# navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
# navclient.wait_for_server()


# goal = MoveBaseGoal()
# goal.target_pose.header.frame_id = "map"
# goal.target_pose.header.stamp = rospy.Time.now()

# goal.target_pose.pose.position.x = -1.8744
# goal.target_pose.pose.position.y = -0.0704
# goal.target_pose.pose.position.z = 0.0
# goal.target_pose.pose.orientation.x = 0.0
# goal.target_pose.pose.orientation.y = 0.0
# goal.target_pose.pose.orientation.z = 0.7212
# goal.target_pose.pose.orientation.w = 0.6927

# navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
# finished = navclient.wait_for_result()

# navclient.wait_for_server()

def moveToPose(x, y, z, qx, qy, qz ,qw):
    # 7th intermediate pose
    navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    navclient.wait_for_server()


    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = -1.8744
    goal.target_pose.pose.position.y = -0.0704
    goal.target_pose.pose.position.z = 0.0
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 0.7212
    goal.target_pose.pose.orientation.w = 0.6927

    navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
    finished = navclient.wait_for_result()

    navclient.wait_for_server()


# rospy.loginfo("moving to point 1 \n")
# moveToPose(-0.505, -0.0852, 0, 0, 0, 0.164, 0.986)
rospy.loginfo("moving to point 2 \n")
moveToPose(-0.536, -0.005, 0, 0, 0, -0.0466, 0.999)
rospy.loginfo("moving to point 3 \n")
moveToPose(-1.187, -0.04434, 0, 0, 0, -0.0708, 0.997)
rospy.loginfo("moving to point 4 \n")
moveToPose(-1.6598, -0.02166, 0, 0, 0, -0.0407, 0.997)
rospy.loginfo("moving to point 5 \n")
moveToPose(-1.852, -0.2124, 0, 0, 0, 0.644, 0.7646)
rospy.loginfo("moving to point 6 \n")
moveToPose(-0.44886207580566406, -0.736985445022583, 0, 0, 0, 0.740792989730835, 0.6717333793640137)
rospy.loginfo("moving to point 7 \n")
moveToPose(-0.514585554599762, -1.68500816822052, 0, 0, 0, 0.9999986290931702, 0.0016612561885267496)
rospy.loginfo("moving to point 8 \n")
moveToPose( 0.5090101957321167, -1.7542341947555542, 0, 0, 0, 0.9977326989173889, -0.0673016682267189)




if not finished:
    rospy.logerr("Action server not available!")
else:
    rospy.loginfo ( navclient.get_result())