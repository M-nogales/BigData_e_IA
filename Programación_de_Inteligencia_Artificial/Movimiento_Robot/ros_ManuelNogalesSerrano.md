# Tutorial: Configuración de ROS 2 Humble y TurtleBot3 en Ubuntu

**Nota: ROS2 no funciona en la version LTS o Noble en mi experiencia**

## 1. Configuración del locale (UTF-8)

Primero verifica tu configuración actual de locale:
```bash
locale
```

Instala los paquetes necesarios y configura el locale en UTF-8:
```bash
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

Verifica que los cambios se hayan aplicado:
```bash
locale
```

## 2. Configuración de los repositorios

### Habilitar el repositorio Universe
```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

### Añadir la clave GPG de ROS 2
```bash
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

### Añadir el repositorio de ROS 2 a la lista de fuentes
```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

## 3. Instalación de paquetes ROS 2

### Actualizar los repositorios
```bash
sudo apt update
```

### Actualizar el sistema
```bash
sudo apt upgrade
```

**Nota importante:** Es fundamental actualizar los paquetes del sistema, especialmente `systemd` y paquetes relacionados con `udev`, antes de instalar ROS 2 para evitar problemas.

### Opciones de instalación:

1. **Instalación de Escritorio (Recomendada):** Incluye ROS, RViz, demos y tutoriales.
```bash
sudo apt install ros-humble-desktop
```

2. **Instalación Básica:** Solo bibliotecas de comunicación, paquetes de mensajes y herramientas de línea de comandos.
```bash
sudo apt install ros-humble-ros-base
```

3. **Herramientas de desarrollo:** Compiladores y otras herramientas para construir paquetes ROS.
```bash
sudo apt install ros-dev-tools
```

## 4. Configuración del entorno

### Configurar el entorno
Dependiendo de tu shell, ejecuta uno de los siguientes comandos:

Para bash (**Mi caso**):
```bash
source /opt/ros/humble/setup.bash
```

Para zsh:
```bash
source /opt/ros/humble/setup.zsh
```

Para sh:
```bash
source /opt/ros/humble/setup.sh
```

## 5. Ejemplos de demostración

### Ejemplo talker-listener

1. En un terminal, ejecuta el nodo C++ talker:
```bash
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp talker
```

2. En otro terminal, ejecuta el nodo Python listener:
```bash
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_py listener
```

Deberías ver el talker publicando mensajes y el listener mostrando los mensajes recibidos. Esto verifica que tanto las APIs de C++ como Python están funcionando correctamente.

## 6. Instalación y configuración de TurtleBot3

### Instalación de paquetes dependientes

1. Instalar Gazebo:
```bash
sudo apt install ros-humble-gazebo-*
```

2. Instalar Cartographer:
```bash
sudo apt install ros-humble-cartographer
sudo apt install ros-humble-cartographer-ros
```

3. Instalar Navigation2:
```bash
sudo apt install ros-humble-navigation2
sudo apt install ros-humble-nav2-bringup
```

### Instalación de paquetes TurtleBot3

1. Crear el espacio de trabajo y clonar los repositorios:
```bash
source /opt/ros/humble/setup.bash
mkdir -p ~/turtlebot3_ws/src
cd ~/turtlebot3_ws/src/
git clone -b humble https://github.com/ROBOTIS-GIT/DynamixelSDK.git
git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3.git
```

2. Instalar colcon y construir el espacio de trabajo:
```bash
sudo apt install python3-colcon-common-extensions
cd ~/turtlebot3_ws
colcon build --symlink-install
```

3. Configurar el entorno:
```bash
echo 'source ~/turtlebot3_ws/install/setup.bash' >> ~/.bashrc
source ~/.bashrc
```

### Configuración del entorno para TurtleBot3

1. Configurar el ROS_DOMAIN_ID y otras variables:
```bash
echo 'export ROS_DOMAIN_ID=30 #TURTLEBOT3' >> ~/.bashrc
echo 'source /usr/share/gazebo/setup.sh' >> ~/.bashrc
echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc
source ~/.bashrc
```

## 7. Verificación final

Para verificar que todo está configurado correctamente:
```bash
printenv | grep ROS
```

# 8. Movimiento del robot
```bash
mkdir -p ~/turtlebot3_ws/src/turtlebot3_control/scripts
cd ~/turtlebot3_ws/src/turtlebot3_control/scripts
nano turtlebot3_controller.py
```
```bash
chmod +x turtlebot3_controller.py
```

```Python
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
```


# Tutorial: Movimiento de TurtleBot3 en ROS 2 Humble

## 1. Instalación del paquete de simulación

Primero, asegúrate de tener instalado el paquete de simulaciones:

```bash
cd ~/turtlebot3_ws/src/
git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/turtlebot3_ws && colcon build --symlink-install
```

## 2. Creación del script Python para mover el robot

Crea un nuevo archivo Python llamado `turtlebot3_controller.py` en tu espacio de trabajo:

```bash
mkdir -p ~/turtlebot3_ws/src/turtlebot3_control/scripts
cd ~/turtlebot3_ws/src/turtlebot3_control/scripts
touch turtlebot3_controller.py
chmod +x turtlebot3_controller.py
```

Edita el archivo con el siguiente contenido:

```python
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
```

## 3. Ejecución

**TurtleBot3 World**:
```bash
export TURTLEBOT3_MODEL=waffle
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```
