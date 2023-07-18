
#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
	rospy.init_node('Pub2')
	pub = rospy.Publisher("/Topic", String, queue_size=10)
	
	rate = rospy.Rate(2)

while not rospy.is_shutdown():
	msg = String()
	msg.data = "Im the second Pub"
	pub.publish(msg)
	rate.sleep()
	
rospy.loginfo("Node was stopped")
