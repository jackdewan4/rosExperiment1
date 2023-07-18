
#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback_receive_radio_data(msg):
	rospy.loginfo("Message received : ")
	
	rospy.loginfo(msg)

if __name__ == '__main__':
	rospy.init_node('Sub2')
	sub = rospy.Subscriber("/Topic", String, callback_receive_radio_data)
	
	rospy.spin()
