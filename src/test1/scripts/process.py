#!/usr/bin/env python
# license removed for brevity
import rospy
from test1.msg import input_msg
from test1.msg import output_msg


id1=0
bmi=float(0)
msg=output_msg()
pub=rospy.Publisher('output_node',output_msg,queue_size=10)
def callback(data):
	##rospy.loginfo("id: %s height %s weight %s " %(data.id,data.height,data.weight))
	id1=data.id
	height=data.height
	weight=data.weight
	bmi=float(weight)/float(((height/100)**2))

	msg.id=id1
	msg.bmi=bmi
	pub.publish(msg)
	rospy.loginfo(msg)
  
def process():

	rospy.init_node('process',anonymous=True)
	rospy.Subscriber('input_node',input_msg,callback)
	

	rospy.spin()
  
  
if __name__=='__main__':
	try:
		process()
	except rospy.ROSInterruptException:
		pass
