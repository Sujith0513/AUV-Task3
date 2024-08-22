#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I heard %s from talk1", data.data)
    
def listener():
    rospy.init_node('list1', anonymous=True)
    rospy.Subscriber("t1", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()