#!/usr/bin/python

import rospy
import math
from geometry_msgs.msg import Twist

def straight(p, distance):
  msg = Twist()
  msg.linear.x = distance
  r = rospy.Rate(1)
  p.publish(msg)
  r.sleep()
  p.publish(Twist())

def turn(p, angle):
  msg = Twist()
  msg.angular.z = angle
  r = rospy.Rate(1)
  p.publish(msg)
  r.sleep()
  p.publish(Twist())


rospy.init_node("square")
p = rospy.Publisher("turtle1/cmd_vel", Twist)

while not rospy.is_shutdown():
  straight(p,3)
  turn(p,math.pi/2)
