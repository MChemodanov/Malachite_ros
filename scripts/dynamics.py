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
  rospy.logwarn("EFFORT %s", msg.linear.x)

p = rospy.Publisher("turtle1/cmd_vel", Twist)
s = rospy.Subscriber("turtle1/dynamics", Twist, callback)

rate = rospy.Rate(frequency)	

def calculate_step():
  global effort
  g = math.copysign(gamma*(state.linear.x**2), state.linear.x)
  linear_a = effort.linear.x  - g
  rospy.logwarn("g %s",   g) 
  rospy.logwarn("effort.linear.x %s", effort.linear.x)  
  rospy.logwarn("linear_a %s",  linear_a)  
  rospy.logwarn("state.linear.x %s",  state.linear.x)  
  linear_a /= mass
  state.linear.x += linear_a/frequency
	
  angular_a = effort.angular.z - math.copysign(gamma*(state.angular.z**2), state.angular.z)
  angular_a /= inertia_moment
  state.angular.z += angular_a/frequency
  #rospy.logwarn("angular_a %s", angular_a)
  #rospy.logwarn("state.angular.z %s", state.angular.z)
  p.publish(state)
  effort = Twist()


while not rospy.is_shutdown():
  calculate_step()
  rate.sleep()
