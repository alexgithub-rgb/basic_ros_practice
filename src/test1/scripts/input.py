#!/usr/bin/env python
# license removed for brevity
import rospy
from test1.msg import input_msg

def input():
	pub=rospy.Publisher('input_node',input_msg,queue_size=10)
	rospy.init_node('input',anonymous=True)
	rate=rospy.Rate(10)
	msg=input_msg()
	id1=rospy.get_param("id1")
	height=rospy.get_param("height")
	weight=rospy.get_param("weight")
	rospy.loginfo(rospy.get_caller_id())
	
	while not rospy.is_shutdown():
		hello_str = "hello world id: %s height: %s weight: %s" % (id1,height,weight)
		rospy.loginfo(hello_str)
		
		msg.id=id1 
		msg.height=height
		msg.weight=weight
		pub.publish(msg)
		rate.sleep()
if __name__=='__main__':
	try:
		input()
	except rospy.ROSInterruptException:
		pass
