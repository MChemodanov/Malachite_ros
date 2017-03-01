#!/usr/bin/python

import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

rospy.init_node("square")

desired_heading = 0
desired_speed = 0
speed_step = rospy.get_param("~speed")
min_error = 0.001
k_p = rospy.get_param("~k_p")
k_i = rospy.get_param("~k_i")
k_d = rospy.get_param("~k_d")

def angle_diff(a1, a2):
    a = a1-a2
    return (a+math.pi)%(2*math.pi)-math.pi

rospy.init_node("square")
p = rospy.Publisher("turtle1/dynamics", Twist)

sum_error = 0  
prev_error = 0
def callback(msg):
  error = angle_diff(desired_heading, msg.theta)
  speed_err = desired_speed - msg.linear_velocity
  global sum_error, prev_error
  sum_error += speed_err
  delta = error - prev_error
  prev_error = error
  msg = Twist()

  msg.linear.x = speed_err*k_p + sum_error*k_i + delta*k_d
  msg.angular.z = error*k_p   

  p.publish(msg)

s = rospy.Subscriber("turtle1/pose", Pose, callback)

r = rospy.Rate(1.0/10.0)

while not rospy.is_shutdown():
    desired_heading += math.pi/2
    desired_speed += speed_step
    sum_error = 0
    r.sleep() 
    if desired_speed >= 5*speed_step:
        desired_speed = 0
    k_p = rospy.get_param("~k_p")
    k_i = rospy.get_param("~k_i")
    k_d = rospy.get_param("~k_d")
