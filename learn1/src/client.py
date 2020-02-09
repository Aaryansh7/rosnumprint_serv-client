#!/usr/bin/env python
import sys
import rospy
from learn1.srv import TurtleMessage, TurtleMessageRequest

def main():
    rospy.init_node('client')
    rospy.wait_for_service('printnum')
    num = rospy.ServiceProxy('printnum', TurtleMessage)
    x = int(input("Enter Number : "))  
    request=TurtleMessageRequest(x)
    response=num(request)
    print "Requesting %s"%(x)
    return response

if __name__ == "__main__":
	main()
