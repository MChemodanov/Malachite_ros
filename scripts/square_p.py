#!/usr/bin/python

import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

desired_heading = 0
desired_speed = 1
min_error = 0.001
k_p = 10

def angle_diff(a1, a2):
    a = a1-a2
    return (a+math.pi)%(2*math.pi)-math.pi

rospy.init_node("square")
p = rospy.Publisher("turtle1/cmd_vel", Twist)
  
def callback(msg):
  error = angle_diff(desired_heading, msg.theta)
  rospy.logwarn("Error: %s", error)
  msg = Twist()
  msg.linear.x = desired_speed        
  if abs(error) > min_error:
      msg.angular.z = error*k_p
  p.publish(msg)

s = rospy.Subscriber("turtle1/pose", Pose, callback)

r = rospy.Rate(1.0/3.0)

while not rospy.is_shutdown():
    desired_heading += math.pi/3
    r.sleep()  
