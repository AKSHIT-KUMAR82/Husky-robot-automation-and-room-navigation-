#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry

class TrajectoryExecutor:
    def __init__(self):
        rospy.init_node('trajectory_executor', anonymous=True)
        self.sub = rospy.Subscriber('/husky/dmp_trajectory', PoseStamped, self.callback)
        self.pub = rospy.Publisher('/husky_velocity_controller/cmd_vel', Twist, queue_size=10)
        self.current_pose = None
        self.speed_factor = 10.0

    def callback(self, data):
        self.current_pose = data.pose
        self.execute_trajectory()

    def execute_trajectory(self):
        if self.current_pose is not None:
            twist = Twist()
            twist.linear.x = self.current_pose.position.x  # Example: directly setting velocity
            twist.linear.y = self.current_pose.position.y  # Example: directly setting velocity
            twist.angular.z = 0  # Assuming no rotation for simplicity
            self.pub.publish(twist)

if __name__ == '__main__':
    try:
        te = TrajectoryExecutor()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

