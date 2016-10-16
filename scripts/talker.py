#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 kirmani <sean@kirmani.io>
#
# Distributed under terms of the MIT license.

import rospy
import random
from geometry_msgs.msg import Twist

def talker():
  pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
  rospy.init_node('talker', anonymous=True)
  rate = rospy.Rate(10)  # 10 Hz
  while not rospy.is_shutdown():
    msg = Twist()
    msg.linear.x = random.uniform(0.0, 3.0)
    msg.angular.z = random.uniform(-5.0, 5.0)
    rospy.loginfo("Drunk walking: Speed = %f and angle = %s" % (msg.linear.x, msg.angular.z))
    pub.publish(msg)
    rate.sleep()

if __name__ == '__main__':
  try:
    talker()
  except rospy.ROSInterruptException:
    pass
