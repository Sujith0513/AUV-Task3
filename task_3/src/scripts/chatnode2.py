#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from task_3.msg import mydata1
from task_3.msg import mydata2

def callback(data):
    rospy.loginfo("Node 2 recieved '%s' from Node 1",data.node1data1)
    
def listener():
    rospy.Subscriber("chatter", mydata1, callback)

def talker():
    global started
    pub = rospy.Publisher('chatter', mydata2, queue_size=10)
    rospy.init_node("Node_2", anonymous=True)
    rate = rospy.Rate(10)
    listener()
    msg=mydata2()
    while not rospy.is_shutdown():
        msg1=input("")
        msg.node2data2=msg1
        started=True
        pub.publish(msg)
        rospy.loginfo(msg.node2data2)
        rate.sleep

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass