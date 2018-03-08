#!/usr/bin/env python

import rospy
import mavros
from std_msgs.msg import String, Header
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros import command, utils, setpoint
from mavros_msgs.srv import CommandBool, SetMode, SetModeRequest

from mavros.utils import *



def main():
    rospy.init_node('px4_offboard_python', anonymous=True)
    #state_sub = rospy.Subscriber("mavros/state", )

    #while not rospy.is_shutdown() and not current_state.connected:
    #        rospy.Rate(20)     
    #rospy.loginfo('FCU connection successful')


    #rospy.Subscriber("chatter", String, callback)
    pub = rospy.Publisher('/mavros/setpoint_position/local', PoseStamped, queue_size=10)
    #local_pos_pub = get_pub_position_local(queue_size=10)

    #arming_client = rospy.ServiceProxy("/mavros/arming", CommandBool)
    set_mode = rospy.ServiceProxy("/mavros/set_mode", SetMode)
    rate = rospy.Rate(20)

    msg = PoseStamped()
    msg.header = Header()
    msg.header.stamp = rospy.Time.now()

    msg.pose.position.x = 0
    msg.pose.position.y = 0
    msg.pose.position.z = 0.5 

    #for i in range(100):
    #    local_pos_pub.Publish(msg)
    #    rate.sleep()

    #offb_set_mode = SetMode()
    #offb_set_mode.request.custom_mode('OFFBOARD')
    #rospy.loginfo("Drone offboard!")

    req = SetModeRequest()
    req.custom_mode = 'OFFBOARD'

    set_mode.call(req)
    print 'mode: ' + State().mode 

    mavros.set_namespace()
    command.arming(True)
    rospy.loginfo("Drone armed!")



    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass 