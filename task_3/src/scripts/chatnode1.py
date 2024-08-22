#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

started=False

def callback(data):
    global started
    if (started):
        rospy.loginfo("Node 1 recieved '%s' from Node 2",data.data)
        started=False
    
def listener():
    rospy.Subscriber("chat2", String, callback)

def talker():
    global started
    pub = rospy.Publisher('chat1', String, queue_size=10)
    rospy.init_node("Node_1", anonymous=True)
    rate = rospy.Rate(10)
    msg=String()
    while not rospy.is_shutdown():
        msg=input("")
        started=True
        pub.publish(msg)
        rospy.loginfo(msg)
        rate.sleep
        listener()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass