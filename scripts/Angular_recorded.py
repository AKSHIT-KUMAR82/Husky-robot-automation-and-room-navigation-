#!/usr/bin/env python3

import rospy
import csv
from nav_msgs.msg import Odometry

class TrajectoryRecorder:
    def __init__(self):
        rospy.init_node('trajectory_recorder', anonymous=True)
        self.file = open('/home/akshit/catkin_workspace/src/husky_trajectory/husky data/record_trajectory.csv', 'w')
        self.csv_writer = csv.writer(self.file)
        self.csv_writer.writerow(['time', 'position_x', 'velocity_x', 'position_y', 'velocity_y', 'angular_velocity_z'])
        self.last_time = rospy.Time.now()
        rospy.Subscriber('/odometry/filtered', Odometry, self.callback)

    def callback(self, data):
        current_time = rospy.Time.now()
        # Ensure at least 0.1 seconds (10 Hz) between recorded entries
        if (current_time - self.last_time).to_sec() >= 0.1:
            pos_x = data.pose.pose.position.x
            pos_y = data.pose.pose.position.y
            vel_x = data.twist.twist.linear.x
            vel_y = data.twist.twist.linear.y
            ang_vel_z = data.twist.twist.angular.z
            self.csv_writer.writerow([current_time.to_sec(), pos_x, vel_x, pos_y, vel_y, ang_vel_z])
            self.last_time = current_time

    def __del__(self):
        self.file.close()

if __name__ == '__main__':
    try:
        recorder = TrajectoryRecorder()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
