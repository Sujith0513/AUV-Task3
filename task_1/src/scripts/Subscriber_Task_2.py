#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I heard %s from talk2", data.data)
    
def listener():
    rospy.init_node('list2', anonymous=True)
    rospy.Subscriber("t2", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()