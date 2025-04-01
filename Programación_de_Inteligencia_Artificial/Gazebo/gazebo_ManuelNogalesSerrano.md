## **1. Instalación de Gazebo y Dependencias**
Previamente instalado en el ejercicio anterior de Ros y TurtleBot3

## **2. Lanzar Gazebo con TurtleBot3**
Ejecuta este comando para iniciar **Gazebo** con un entorno vacío:

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Esto abrirá **Gazebo** con un TurtleBot en un mundo básico.

---

## **3. Diseñar un Escenario con Obstáculos**
Para agregar obstáculos, edita un archivo **SDF** o usa la herramienta de edición de Gazebo.

1. **Abrir la consola de Gazebo:**  
   Presiona `Ctrl + Shift + I` para abrir la consola.  
2. **Agregar obstáculos:**  
   - Haz clic en **Insert**.  
   - Selecciona objetos como **cajas** o **paredes** y colócalos en el entorno.  
   - Guarda la configuración si deseas reutilizarla.

Para editar un archivo **SDF**, usa este código (`mi_mundo.sdf`):
```xml
<?xml version="1.0"?>
<sdf version="1.6">
  <world name="mi_mundo">
    <include>
      <uri>model://sun</uri>
    </include>
    <include>
      <uri>model://ground_plane</uri>
    </include>
    
    <model name="caja1">
      <static>true</static>
      <link name="link">
        <collision name="collision">
          <geometry>
            <box><size>1 1 1</size></box>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <box><size>1 1 1</size></box>
          </geometry>
          <material><ambient>0.7 0 0 1</ambient></material>
        </visual>
      </link>
    </model>

    <model name="caja2">
      <static>true</static>
      <pose>2 2 0</pose>
      <link name="link">
        <collision name="collision">
          <geometry>
            <box><size>1 1 1</size></box>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <box><size>1 1 1</size></box>
          </geometry>
          <material><ambient>0 0.7 0 1</ambient></material>
        </visual>
      </link>
    </model>
  </world>
</sdf>
```

Ejecuta:
```bash
gazebo --verbose mi_mundo.sdf
```

---

## **4. Programar el Robot para Evitar Obstáculos**
Usaremos **LIDAR** para detectar obstáculos y ajustar el movimiento. Crea el archivo `gazebo_custom.py`:

```python
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
```

### **Ejecutar el Script**
Guarda el archivo y ejecútalo con:
```bash
python3 gazebo_custom.py
```
