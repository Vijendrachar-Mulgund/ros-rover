#!/usr/bin/env python3
import rospy
import random

# To send messages in Integer Values
from std_msgs.msg import Int16

# Generate random values for the RPM of the rover
def generateRpm():
    return random.randint(50, 100)

# The Publisher
def rosRoverPublisher():
    rospy.init_node("rover_rpm_publisher")
    pub = rospy.Publisher("rpm", Int16, queue_size=10)
    
    # 1 Message is being published every second
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        pub.publish(generateRpm())
        rate.sleep()

# Main function
if __name__ == "__main__":
    try:
        rosRoverPublisher()
    except rospy.ROSInterruptException: 
        print("The Publisher has been shutdown!")