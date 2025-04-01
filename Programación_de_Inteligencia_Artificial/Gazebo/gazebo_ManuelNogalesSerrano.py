#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class AvoidObstacles(Node):
    def __init__(self):
        super().__init__('avoid_obstacles')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.twist = Twist()

    def scan_callback(self, msg):
        min_distance = min(msg.ranges[0:30] + msg.ranges[330:360])  # Detecta adelante

        if min_distance < 0.5:  # Si hay un obstáculo cerca
            self.twist.linear.x = 0.0
            self.twist.angular.z = 0.5  # Gira
        else:
            self.twist.linear.x = 0.2
            self.twist.angular.z = 0.0  # Avanza recto

        self.publisher_.publish(self.twist)

def main(args=None):
    rclpy.init(args=args)
    node = AvoidObstacles()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()