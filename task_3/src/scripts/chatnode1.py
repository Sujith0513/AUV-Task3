#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from task_3.msg import mydata1
from task_3.msg import mydata2

started=False

def callback(data):
    rospy.loginfo("Node 1 recieved '%s' from Node 2",data.node2data2)
    
def listener():
    rospy.Subscriber("chatter", mydata2, callback)

def talker():
    global started
    pub = rospy.Publisher('chatter', mydata1, queue_size=10)
    rospy.init_node("Node_1", anonymous=True)
    rate = rospy.Rate(10)
    listener()
    msg=mydata1()
    while not rospy.is_shutdown():
        msg1=input("")
        msg.node1data1=msg1
        started=True
        pub.publish(msg)
        rospy.loginfo(msg.node1data1)
        rate.sleep

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass