#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


def callback(self,msg):
    print "Linear X of Twist message"+ str(msg.linear.x)

def run_motor():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('DC_Motors', anonymous=True)

    rospy.Subscriber("cmd_vel", Twist,self.callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
if __name__ == '__main__':
    run_motor()
