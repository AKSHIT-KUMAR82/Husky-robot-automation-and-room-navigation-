#!/usr/bin/env python3

import rospy
import csv
from geometry_msgs.msg import Twist

class TrajectoryReplayer:
    def __init__(self, csv_file_path):
        rospy.init_node('trajectory_replayer', anonymous=True)
        self.csv_file_path = csv_file_path
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(10)  # 10 Hz

    def replay(self):
        with open(self.csv_file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            next(csv_reader)  # Skip the header
            for row in csv_reader:
                if rospy.is_shutdown():
                    break

                # Create the twist message
                twist = Twist()
                twist.linear.x = float(row['velocity_x'])
                twist.linear.y = float(row['velocity_y'])
                twist.angular.z = float(row['angular_velocity_z'])

                # Publish the message
                self.pub.publish(twist)
                self.rate.sleep()

if __name__ == '__main__':
    try:
        replayer = TrajectoryReplayer('/home/akshit/catkin_workspace/src/husky_trajectory/husky data/record_trajectory.csv')
        replayer.replay()
    except rospy.ROSInterruptException:
        pass
