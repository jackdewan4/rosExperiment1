import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion


def shutdown():
    
    rospy.on_shutdown(shutdown)

    rospy.loginfo("Shutting Down")
    rospy.sleep(1)




def navToPoint(pos, quat):

    goal_sent = True

    goal = MoveBaseGoal()

    goal.target_pose.header.frame_id = '/map'
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose = Pose(Point(pos['x'], pos['y'], 0.00), Quaternion(quat['r1'], quat['r2'], quat['r3'], quat['r4']))

    move_base.send_goal(goal)

    success = move_base.wait_for_result(rospy.Duration(60))

    state = move_base.get_state()

    result = False

    if success and state == GoalStatus.SUCCEEDED:

        result = True
    else:
        move_base.cancel_goal()

    goal_sent = False


    return result







if __name__ == '__main__':
    try:
        
        rospy.init_node('navigate_from_ptA_to_ptB', anonymous=False)

        goal_sent = False
        # shutdown = shutdown()
        rospy.on_shutdown(shutdown)

        move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)

        rospy.loginfo("Wait for the action server to come up")

        # Allow up to 5 seconds for the action server to come up
        move_base.wait_for_server(rospy.Duration(5))



        # the location of point b found from rviz 
        position = {'x': 0.085, 'y' : 1.41}
        #0.000, 0.000, 0.833, 0.553
        quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.833, 'r4' : 0.553}


        rospy.loginfo("Go to (%s, %s) pose", position['x'], position['y'])

        moveDone = navToPoint(position, quaternion)

        if moveDone:

            rospy.loginfo("successfully navigated from point A to point B")
        else:
            rospy.loginfo("the planner failed")

        rospy.sleep(1)


    except rospy.ROSInterruptException:
        rospy.loginfo("Quitting")