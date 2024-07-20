#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Header
import numpy as np

def generate_trajectory(ax, ax_new, beta, alpha, steps):
    trajectory = []
    for t in range(steps):
        x = np.sin(ax * t / steps) * np.exp(-beta * t / steps)
        y = np.cos(ax_new * t / steps) * np.exp(-alpha * t / steps)
        trajectory.append((x, y))
    return trajectory

class TrajectoryPublisher:
    def __init__(self):
        rospy.init_node('trajectory_publisher', anonymous=True)
        self.pub = rospy.Publisher('/husky/dmp_trajectory', PoseStamped, queue_size=10)
        self.rate = rospy.Rate(10)  # 10 Hz

    def publish_trajectory(self, trajectory):
        for point in trajectory:
            pose = PoseStamped()
            pose.header = Header()
            pose.header.stamp = rospy.Time.now()
            pose.pose.position.x = point[0]
            pose.pose.position.y = point[1]
            pose.pose.position.z = 0  # Assuming 2D trajectory
            self.pub.publish(pose)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        best_params = (5.822907575701987, 8.614542308990474, 12.876585280801248, 20.977074359273495)
        trajectory = generate_trajectory(*best_params, steps=100)
        tp = TrajectoryPublisher()
        tp.publish_trajectory(trajectory)
    except rospy.ROSInterruptException:
        pass

