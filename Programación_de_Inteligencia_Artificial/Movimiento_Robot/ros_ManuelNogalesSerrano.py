#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MoveTurtleBot(Node):
    def __init__(self):
        super().__init__('move_turtlebot')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move_robot)
        self.step = 0

    def move_robot(self):
        msg = Twist()

        if self.step < 50:  # Mover en línea recta por 5 segundos (50 * 0.1s)
            msg.linear.x = 0.2
        elif self.step < 70:  # Girar 90 grados por 2 segundos (20 * 0.1s)
            msg.linear.x = 0.0
            msg.angular.z = 0.5
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.get_logger().info('Movimiento finalizado')
            self.destroy_timer(self.timer)

        self.publisher_.publish(msg)
        self.step += 1

def main(args=None):
    rclpy.init(args=args)
    node = MoveTurtleBot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()