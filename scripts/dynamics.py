#!/usr/bin/python

import rospy
import math
from geometry_msgs.msg import Twist

rospy.init_node("dynamics")

inertia_moment = rospy.get_param("~moment_inertia")
mass = rospy.get_param("~mass")
gamma = rospy.get_param("~gamma")

frequency = 100

state = Twist()
effort = Twist()

def callback(msg):
  global effort
  effort = msg

p = rospy.Publisher("turtle1/cmd_vel", Twist)
s = rospy.Subscriber("turtle1/dynamics", Twist, callback)

rate = rospy.Rate(frequency)

def calculate_step():
  linear_a = effort.linear.x  - gamma*(state.linear.x**2)
  linear_a /= mass
  state.linear.x += linear_a/frequency

  angular_a = effort.angular.z - gamma*(state.angular.z**2)
  angular_a /= inertia_moment
  state.angular.z += angular_a/frequency
  
  p.publish(state)

while not rospy.is_shutdown():
  calculate_step()
  rate.sleep()
