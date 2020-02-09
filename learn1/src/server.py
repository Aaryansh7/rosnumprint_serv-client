#!/usr/bin/env python
import rospy
from learn1.srv import TurtleMessage, TurtleMessageResponse
from geometry_msgs.msg import Twist

PI = 3.1415926535897


def rotate(speed, angle, clockwise):
    #Starts a new node
    
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Converting from angles to radians
    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360

    #We wont use linear components
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
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)


    #Forcing our robot to stop
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    



def move(speed,distance,isForward):
    # Starts a new node
   
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Checking if the movement is forward or backwards
    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
        #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0

        #Loop to move the turtle in an specified distance
    while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_distance= speed*(t1-t0)
        #After the loop, stops the robot
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)
	
def handle_string_usr(request):
    response=TurtleMessageResponse()
    response.a2=request.a1
    n=response.a2
    if n==1:
        #print "running case 1"
        move(1,1,1)
	rotate(50,90,1)
	move(1,3,1)
    if n==5:
        #print "running case 5"
	move(1,2,1)
 	rotate(50,90,1)
    	move(1,2,1)
 	rotate(50,90,1)
    	move(1,2,1)
 	rotate(50,90,1)
    	move(1,2,1)
 	rotate(50,90,1)
    
    print "returning %s\n"%(c)
    
    return response

def main():
    rospy.init_node('server')
    num = rospy.Service('printnum', TurtleMessage, handle_string_usr)
    rospy.spin()

if __name__ == "__main__":
    main() 
