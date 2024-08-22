#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

name=input("Enter the node name : ")

started=False

def callback(data):
    global started
    if (started):
        rospy.loginfo("I heard %s from %s",data.data,name)
        started=False
    
def listener():
    rospy.Subscriber("chatter", String, callback)

def talker():
    global started
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node(name, anonymous=True)
    rate = rospy.Rate(10)
    listener()
    msg=String()
    while not rospy.is_shutdown():
        msg=input("Enter the msg : ")
        started=True
        pub.publish(msg)
        rospy.loginfo(msg)
        rate.sleep
        print("1")

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass