#Libraries used for navigation task
import rospy
import actionlib
import time
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
PI = 3.14159265359

def stop(vel_msg, velocity_publisher):  
    vel_msg.linear.x = 0 #set linear x to zero  
    vel_msg.angular.z = 0 #set angular z to zero  
    # Publish the velocity to stop the robot
    velocity_publisher.publish(vel_msg) 
    time.sleep(1) #stop for 1 second

def movingForward(vel_msg, velocity_publisher, t0, current_distance, distance, speed, forwardSpeed, front):  
    vel_msg.linear.x = forwardSpeed  
    vel_msg.angular.z = 0 #initialize angular z to zero   
    print('Is moving')  
    while(current_distance < distance):
        velocity_publisher.publish(vel_msg)#Publish the velocity  
        #Take actual time to velocity calculation
        t1 = rospy.Time.now().to_sec()
        current_distance = speed*(t1-t0)#calculates distance
        #Stop the robot when the front distance from obstacle is smaller than 1.0  
        # if (front < 1.0):   
        #     stop(vel_msg, velocity_publisher)

    time.sleep(1) # stop for 1 second

# def movingBackward(vel_msg, velocity_publisher, t0, current_distance, distance, speed, backwardSpeed, front):

#     vel_msg.linear.x = backwardSpeed
#     vel_msg.angular.z = 0 #initialize angular z to zero
#     print('Is backing')  
#     while(current_distance < (distance/2)):
#         velocity_publisher.publish(vel_msg)#Publish the velocity
#         #Take actual time to vel calculation  
#         t1 = rospy.Time.now().to_sec()
#         current_distance = speed*(t1-t0)#calculates distance
#     if (front < 1.0):
#         stop(vel_msg, velocity_publisher)
#     time.sleep(1) # stop for 1 second


# function to turn 90 degree clockwise
def turnCW(vel_msg, velocity_publisher, t0, current_angle, turningSpeed, angle):
    #converting from angle to radian
    angular_speed = round(turningSpeed*2*PI/360, 1)
    #converting from angle to radian
    relative_angle = round(angle*2*PI/360, 1)
    vel_msg.linear.x = 0 #initialize linear x to zero
    #initialize angular z with angular_speed  
    vel_msg.angular.z = -abs(angular_speed)
    print('Turning')
    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)#Publish the velocity  
        #Take actual time to vel calculation
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)#calculates distance
    time.sleep(1)#stop the robot for 1 second

def turnCCW(vel_msg, velocity_publisher, t0, current_angle, turningSpeed, angle):

    #converting from angle to radian
    angular_speed = round(turningSpeed*2*PI/360, 1)
    #converting from angle to radian
    relative_angle = round(angle*2*PI/360, 1)
    vel_msg.linear.x = 0 #initialize linear x to zero
    #initialize angular z with angular_speed  
    vel_msg.angular.z = abs(angular_speed)
    print('Turning')
    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)#Publish the velocity  
        #Take actual time to vel calculation
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)#calculates distance

    time.sleep(1)#stop the robot for 1 second


def leftWallFollowing():
    #initialize the node   
    rospy.init_node('tape_avoider', anonymous=True)
    #set topic for publisher
    velocity_publisher = rospy.Publisher('cmd_vel', Twist,queue_size=10)

    vel_msg = Twist() 
    print("starting to move using leftWallFollowing algorithm")

    #define the local speed 
    speed = 0.2
    #define the distance
    distance = [0.10, 0.20, 0.29]
    #set all the linear and angular motion of each dimension to zero        
    vel_msg.linear.x = 0  
    vel_msg.linear.y = 0  
    vel_msg.linear.z = 0  
    vel_msg.angular.x = 0  
    vel_msg.angular.y = 0  
    vel_msg.angular.z = 0  
    #Execute the movement when the robot is active
    count = 0
    while not rospy.is_shutdown():
        count += 1
        if (count < 2):

            t0 = rospy.Time.now().to_sec()
            current_distance = 0
            scan_msg = rospy.wait_for_message("scan", LaserScan)
            front = scan_msg.ranges[1] 
            print('first corridor')
            # from start to end of first corridor
            distance_req = 1.1
            movingForward(vel_msg,velocity_publisher, t0,  current_distance, distance_req, speed,0.3, front)
            t0 = rospy.Time.now().to_sec()
            # adjust for error in driving staright
            turnCCW(vel_msg, velocity_publisher, t0, 0, 40, 3)
            t0 = rospy.Time.now().to_sec()
            distance_req = 1.1
            movingForward(vel_msg,velocity_publisher, t0,  current_distance, distance_req, speed,0.3, front)
            # # adjust for error in driving staright
            # turnCCW(vel_msg, velocity_publisher, t0, 0, 40, 3)
            # turn left
            print('turning to next corridor')
            t0 = rospy.Time.now().to_sec()
            turnCCW(vel_msg, velocity_publisher, t0, 0, 40, 70)

            # turn from first corridor to second corridor

            # t0 = rospy.Time.now().to_sec()
            # # distance_req = 100
            # # from end of first corridor to end of second corridor 
            # movingForward(vel_msg,velocity_publisher, t0,  current_distance, distance_req, speed,0.3, front)
            # # turn from second corridor to third
            # t0 = rospy.Time.now().to_sec()
            # turnCCW(vel_msg, velocity_publisher, t0, 0, 40, 90)

            # from first to second corridor
            print('travelling down second corridor')
            distance_req = 1.1
            movingForward(vel_msg,velocity_publisher, t0,  current_distance, distance_req, speed,0.3, front)
            t0 = rospy.Time.now().to_sec()
            # adjust for error in driving staright
            # turnCCW(vel_msg, velocity_publisher, t0, 0, 40, 3)
            t0 = rospy.Time.now().to_sec()
            distance_req = 0.95
            print('travelling second half of the second corridor')
            movingForward(vel_msg,velocity_publisher, t0,  current_distance, distance_req, speed,0.3, front)
            # # adjust for error in driving staright
            # turnCCW(vel_msg, velocity_publisher, t0, 0, 40, 3)
            # turn left
            print('turning to third corridor')
            t0 = rospy.Time.now().to_sec()
            turnCCW(vel_msg, velocity_publisher, t0, 0, 40, 80)
            print('travelling second half of the third corridor')

            t0 = rospy.Time.now().to_sec()
            distance_req = 0.8
            movingForward(vel_msg,velocity_publisher, t0,  current_distance, distance_req, speed,0.3, front)
            t0 = rospy.Time.now().to_sec()
            # adjust for error in driving staright
            # turnCCW(vel_msg, velocity_publisher, t0, 0, 40, 3)
            t0 = rospy.Time.now().to_sec()
            distance_req = 0.8
            movingForward(vel_msg,velocity_publisher, t0,  current_distance, distance_req, speed,0.3, front)

            print('turning to fourth corridor')
            t0 = rospy.Time.now().to_sec()
            turnCCW(vel_msg, velocity_publisher, t0, 0, 40, 75)

            print('travelling down fourth corridor')
            t0 = rospy.Time.now().to_sec()
            distance_req = 1
            movingForward(vel_msg,velocity_publisher, t0,  current_distance, distance_req, speed,0.3, front)
            t0 = rospy.Time.now().to_sec()
            # adjust for error in driving staright
            # turnCCW(vel_msg, velocity_publisher, t0, 0, 40, 3)
            t0 = rospy.Time.now().to_sec()
            distance_req = 0.8
            movingForward(vel_msg,velocity_publisher, t0,  current_distance, distance_req, speed,0.3, front)

            t0 = rospy.Time.now().to_sec()
            turnCCW(vel_msg, velocity_publisher, t0, 0, 40, 70)
        else:
            rospy.shutdown()
        
        
        
        
        
        
        
        
        
        
        
leftWallFollowing()  
        
        
        
        
        # #define the variable to determine the existance of the right wall
        # no_right_wall = None
        # #define the variable to determine the existance of the front wall
        # no_front_wall = None
        # #set current time for distance calculate  
        # t0 = rospy.Time.now().to_sec()
        # #define the variable for current distance
        # current_distance = 0
        # #read the input from lazer scan
        # scan_msg = rospy.wait_for_message("scan", LaserScan)
        # #read the input distance between robot and obstacles in the   
        # #front, left, right, top left, and top right direction

        # front = scan_msg.ranges[1]  
        # left = scan_msg.ranges[90]  
        # top_left = scan_msg.ranges[45]  
        # right = scan_msg.ranges[270]  
        # top_right = scan_msg.ranges[315]

        




# algorithm: follow left wall until dont see anymore travel forward until theres 0.2 m in front
# then turn left 90 deg
# then follow left wall until not there anymore, then after short time delay, turn 90 deg left,
# at this point we could probably use goal position to navigate to the final position
