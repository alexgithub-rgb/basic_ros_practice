#!/usr/bin/env python
# license removed for brevity
import rospy
from test1.msg import output_msg
def callback(data):
  info_str="id: %s bmi: %s" %(data.id,data.bmi)
  rospy.loginfo(info_str)
    
def output():
  rospy.init_node('output',anonymous=True)
  rospy.Subscriber('output_node',output_msg,callback)
  rospy.spin()
  
  
if __name__=='__main__':
  try:
    output()
  except rospy.ROSInterruptException:
    pass
