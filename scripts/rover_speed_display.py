#!/usr/bin/env python3

import rospy

# To recieve messages in String
from std_msgs.msg import String

# Calculate the speed from the RPM recieved
def displaySpeed(speed):
    rospy.loginfo(speed.data)

# The Subscriber
def rosRoverSpeedSubscriber():
    rospy.init_node("rover_speed_subscriber")
    rospy.Subscriber("speed", String, displaySpeed)

# Main function
if __name__ == '__main__':
    rosRoverSpeedSubscriber()
    rospy.spin()