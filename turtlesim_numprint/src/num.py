#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

# Starts a new node
rospy.init_node('robot_num', anonymous=True)
velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()


def move(speed,distance,isForward):
    print("Move function called successfully")

    #Checking if the movement is forward or backwards
    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    #moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    t0 = rospy.Time.now().to_sec()
    current_distance = 0

        #Loop to move the turtle in an specified distance
    while(current_distance < distance):
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_distance= speed*(t1-t0)

vel_msg.linear.x = 0

def rotate(speed,angle,clockwise):
    print("Rotate function called successfully")

    #Converting from angles to radians
    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360

    #no  linear components
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    # Checking if our movement is CW or CCW
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)

    vel_msg.angular.z = 0

def one():
    rotate(30,60,0)
    move(1,1,1)
    rotate(30,30,0)
    move(1,3,0)
    rotate(30,90,0)
    move(1,1,1)
    move(1,2,0)


def five():
    move(1,1,0)
    rotate(30,90,0)
    move(1,1,0)
    rotate(30,90,0)
    move(1,1,0)
    rotate(50,90,1)
    move(1,1,0)
    rotate(30,90,1)
    move(1,1,0)


def num(val):
   if val==5:
       five()
   if val==1:
       one()

if __name__ == '__main__':
    val = input("Enter your value: ")
    print(val)
    num(val)




