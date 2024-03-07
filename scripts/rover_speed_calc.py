#!/usr/bin/env python3
import rospy

# The value is in meters
WHEEL_RADIUS = rospy.get_param('/rover-wheel-radius')
PI = rospy.get_param('/pi-value')

# To recieve messages in Integer Values and send messages in String values
from std_msgs.msg import Int16, String

# Calculate the speed from the RPM recieved
def calcSpeed(rpm, pub):
    rosRoverSpeed = (2 * PI * WHEEL_RADIUS) * (int(rpm.data) / 60)

    # Publish the speed to another topic
    rosRoverSpeedPublisher(rosRoverSpeed, pub)

# Publish the calculated 
def rosRoverSpeedPublisher(wheelSpeed, pub):
    pub.publish("Rover speed is " + str(wheelSpeed) + " m/s")

# The Subscriber
def rosRoverSubPubInit():
    #  Init Node
    rospy.init_node("rover_speed_subscriber_publisher")

    # Init the Publisher topic here as it needs to be initilised only once
    pub = rospy.Publisher("speed", String, queue_size=10)
    
    # Get the data published by /rpm
    rospy.Subscriber("rpm", Int16, calcSpeed, (pub))

# Main function
if __name__ == '__main__':
    rosRoverSubPubInit()
    rospy.spin()