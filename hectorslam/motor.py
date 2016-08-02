#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def forward(move):
    ##put forward function here
    ##PWM will be determined by move value
    print "moving forward",move

def backward(move):
    #put backward here
    move=abs(move)
    print "moving Backward",move


def right(move):
    print "moving Right",move

def left(move):
    move=abs(move)
    print "moving Left",move

def stop():
    print"stopped"

#lint:enable

def callback(msg):
    print "Linear X of Twist message" + str(msg.linear.x)
    print "Angular Z of Twist message" + str(msg.angular.z)
    move = msg.linear.x
    pwm_value_move = (move*50)

    turn = msg.angular.z
    pwm_value_turn = (turn*30)
    if (move > 0):
        forward(pwm_value_move)
    else:
        if (move < 0) :
            backward(pwm_value_move)
        else:
            if (turn>0):
                right(pwm_value_turn)
            else:
                if (turn<0):
                    left(pwm_value_turn)
                else:
                    stop()


def run_motor():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('DC_Motors', anonymous=True)

    rospy.Subscriber("cmd_vel", Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
if __name__ == '__main__':
    run_motor()
