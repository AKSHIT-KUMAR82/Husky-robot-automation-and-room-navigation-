#!/usr/bin/env python3

import rospy
import csv
from nav_msgs.msg import Odometry
from time import time

class TrajectoryRecorder:
    def __init__(self):
        rospy.init_node('trajectory_recorder', anonymous=True)
        self.file = open('/home/akshit/catkin_workspace/src/Husky_trajectory/record.csv', 'w')
        self.csv_writer = csv.writer(self.file)
        self.csv_writer.writerow(['time', 'position_x','velocity_x', 'position_y', 'velocity_y'])
        rospy.Subscriber('/odometry/filtered', Odometry, self.callback)
        self.last_time = 0

    def callback(self, data):
        current_time = time()
        if current_time - self.last_time >= 1:  # Ensure 1-second interval
            pos_x = data.pose.pose.position.x
            pos_y = data.pose.pose.position.y
            vel_x = data.twist.twist.linear.x
            vel_y = data.twist.twist.linear.y
            self.csv_writer.writerow([current_time, pos_x, pos_y, vel_x, vel_y])
            self.last_time = current_time

    def __del__(self):
        self.file.close()

if __name__ == '__main__':
    try:
        recorder = TrajectoryRecorder()
        rospy.spin()  # Keep the node alive
    except rospy.ROSInterruptException:
        pass
