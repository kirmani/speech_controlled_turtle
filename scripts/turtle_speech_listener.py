#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 kirmani <sean@kirmani.io>
#
# Distributed under terms of the MIT license.

"""

"""

import rospkg
import rospy


class TurtleSpeechListener:

  def __init__(self):

  # COMMAND_TOPIC_PARAM = "/speech/publish_topic"
  # SERVICE_TOPIC_PARAM = "/speech/service_topic"
  # KEYWORDS_PARAM = "/speech/keywords"
  # COMMAND_TYPE = "/speech/command_type"

  # def __init__(self, commandBuffSize=10, init_node=True):
  #   if (init_node):
  #     # Initialize the ROS node.
  #     rospy.init_node("speech_listener")

  #   # Default values for speech listener.
  #   rospack = rospkg.RosPack()
  #   default_pub_topic = 'hlpr_speech_commands'
  #   default_yaml_files = [rospack.get_path('speech_controlled_turtle')+'/data/speech_controlled_turtle.yaml']
  #   default_service_topic = 'get_last_speech_cmd'

  #   # Pull values from rosparam.
  #   self.recog_topic = rospy.get_param(TurtleSpeechListener.COMMAND_TOPIC_PARAM, default_pub_topic)
  #   self.yaml_files = rospy.get_param("~yaml_list", default_yaml_files)
  #   self.service_topic = rospy.get_param(TurtleSpeechListener.SERVICE_TOPIC_PARAM, default_service_topic)
  #   self.msg_type = eval(rospy.get_param(TurtleSpeechListener.COMMAND_TYPE, 'StampedString'))

  #   rospy.Subscriber(self.recog_topic, self.msg_type, self.callback)

  #   # Converts the yaml files into keywords to store into the dictionary
  #   self.keywords_to_commands = {}
  #   for kps_path in self.yaml_files:
  #     for data in yaml.load_all(file(kps_path,'r')):
  #       self.keywords_to_commands[str(data['tag'])] = data['speech']

  #   # Store this on the rosparam server now
  #   rospy.set_param(TurtleSpeechListener.KEYWORDS_PARAM, self.keywords_to_commands)

  # def callback(self):
  #   if self.msg_type == StampedString:
  #     self.last_string = msg.keyphrase
  #     self.last_ts = msg.stamp
  #   else:
  #     self.last_string = msg.data

  #   self.last_command = self._map_keyword_to_command(self.last_string)
  #   self.last_command_fresh = True

  # def spin(self):
  #   self.spinning = True
  #   rospy.spin()

  # # method to extract command string from msg
  # def _map_keyword_to_command(self, data):
  #   for (command, keywords) in self.keywords_to_commands.iteritems():
  #     for word in keywords:
  #       if data.find(word) > -1:
  #         return command

def listener():
  listener = TurtleSpeechListener()
  listener.spin()

if __name__ == '__main__':
  listener()
