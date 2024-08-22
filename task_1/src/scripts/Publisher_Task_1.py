#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('t1', String, queue_size=10)
    rospy.init_node('talk1', anonymous=True)
    rate = rospy.Rate(10)
    msg=String()
    while not rospy.is_shutdown():
        msg=input("Enter the msg : ")
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass