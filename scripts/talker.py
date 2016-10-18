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
from hlpr_speech_msgs.srv import SpeechService
from hlpr_speech_recognition.speech_listener import SpeechListener

HALF_PI = 3.1415926 / 2.0
RANDOMLY_WALKING = False

def get_cmd():
  rospy.wait_for_service('get_last_speech_cmd')
  try:
    speech_service = rospy.ServiceProxy('get_last_speech_cmd', SpeechService)
    return speech_service().speech_cmd
  except rospy.ServiceException, e:
    pass

def talker():
  global RANDOMLY_WALKING
  pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
  rospy.init_node('talker', anonymous=True)
  rate = rospy.Rate(10)  # 10 Hz
  while not rospy.is_shutdown():
    cmd = get_cmd()
    if cmd:
      RANDOMLY_WALKING = False
      msg = Twist()
      if cmd == "MOVE_FORWARD":
        msg.linear.x = 1.0
      elif cmd == "TURN_90":
        msg.angular.z = HALF_PI
      elif cmd == "TURN_180":
        msg.angular.z = 2.0 * HALF_PI if random.randint(0, 1) == 0 else -2.0 * HALF_PI
      elif cmd == "TURN_270":
        msg.angular.z = -HALF_PI
      elif cmd == "RANDOM_WALK":
        RANDOMLY_WALKING = True
      pub.publish(msg)
    elif RANDOMLY_WALKING:
      msg = Twist()
      msg.linear.x = random.uniform(0.0, 3.0)
      msg.angular.z = random.uniform(-5.0, 5.0)
      pub.publish(msg)
    rate.sleep()

if __name__ == '__main__':
  try:
    talker()
  except rospy.ROSInterruptException:
    pass
