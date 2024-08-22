#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    if data._connection_header['callerid'] != rospy.get_name():
        rospy.loginfo("Node 2 recieved '%s' from Node 1",data.data)
    
def listener():
    rospy.Subscriber("chatter", String, callback)

def talker():
    global started
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node("Node_2", anonymous=True)
    rate = rospy.Rate(10)
    listener()
    msg=String()
    while not rospy.is_shutdown():
        msg=input("")
        started=True
        pub.publish(msg)
        rospy.loginfo(msg)
        rate.sleep

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass