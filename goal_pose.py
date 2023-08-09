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
moveToPose(-2.7051225004041233, 1.2064674155134756, 0, 0, 0, 0.7306749834986939, 0.6827254708073981)
rospy.loginfo("moving to point 2 \n")
moveToPose(-2.4157673513102913, 0.6662914215701816, 0, 0, 0, 0.9036751513280833, 0.42821866011672793)
rospy.loginfo("moving to point 3 \n")
moveToPose(-2.3564888186656185, 0.3913601741706412, 0, 0, 0, 0.739715924610392, 0.6729192751569781)
rospy.loginfo("moving to point 4 \n")
moveToPose(-2.184496218905593, -0.041726512821755456, 0, 0, 0, 0.9548389148590191, 0.2971239584261945)
rospy.loginfo("moving to point 5 \n")
moveToPose( -1.187316483875341,-0.33944837831928615 , 0, 0, 0, -0.975745899677974, 0.2189062339487413 )

rospy.loginfo("moving to point 7 \n")
moveToPose( -2.6888254109381586, -0.0013153617494855861, 0, 0, 0, 0.861563757178341 , 0.5076493793128685)
rospy.loginfo("moving to point 8 \n")
moveToPose( -2.5719514000162573, -0.1529117915345567, 0, 0, 0,  0.9509127063898171, 0.30945924582470236)
rospy.loginfo("moving to point 9\n")
moveToPose( -1.5443325834409476, -0.4219353508991305, 0, 0, 0, 0.9803253071630279, 0.19738868289675343)
rospy.loginfo("moving to point 10\n")
moveToPose( -1.4044177039851033, -0.36272601167156715 , 0, 0, 0, -0.9734707218234292, 0.22881161192686822)
rospy.loginfo("moving to point 11\n")
moveToPose( -1.3104098526696581, -0.28835911812870735 , 0, 0, 0,-0.9059335207065622 , 0.42341995236433166)
rospy.loginfo("moving to point 12\n")
moveToPose( -1.0049378290449986,  0.584983809714324, 0, 0, 0, -0.7427391124625305 , 0.6695809217849418 )
rospy.loginfo("moving to point 13\n")
moveToPose( -0.9964453421033779,  0.7509695989634422, 0, 0, 0, -0.5068434400143613 ,  0.8620381240492838 )
rospy.loginfo("moving to point 14\n")
moveToPose( -1.0635665709475075, 0.8816278130391528 , 0, 0, 0, -0.21908304585032176 ,  0.975706215528499 )
rospy.loginfo("moving to point 15\n")
moveToPose( -1.2445573189669434,  0.9606564233144422, 0, 0, 0,  -0.19505961335878427,  0.9807913882351953)



if not finished:
    rospy.logerr("Action server not available!")
else:
    rospy.loginfo ( navclient.get_result())