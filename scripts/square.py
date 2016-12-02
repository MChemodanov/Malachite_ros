#!/usr/bin/python

import rospy
import math
from geometry_msgs.msg import Twist

def straight(p, distance, angle):
  msg = Twist()
  msg.linear.x = distance
  msg.angular.z = angle
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

angle = math.pi/2	
delta = math.pi/40
while not rospy.is_shutdown():
  straight(p,0.5, angle)
  angle -= delta
  # turn(p,2*math.pi/3)
