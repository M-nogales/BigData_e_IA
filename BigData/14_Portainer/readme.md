# What´s portainer
**Portainer** is a lightweight, open-source management tool for Docker environments. It provides a user-friendly web-based interface that simplifies the management of Docker containers, images, networks, and volumes. Portainer is designed to make it easier for both beginners and experienced users to interact with Docker without needing to use the command line.

---

### **Key Features of Portainer**
1. **Container Management**:
   - Start, stop, restart, and remove containers.
   - View logs, inspect container details, and access container consoles.

2. **Image Management**:
   - Pull, build, and delete Docker images.
   - Manage image repositories.

3. **Network Management**:
   - Create, inspect, and manage Docker networks.

4. **Volume Management**:
   - Create, inspect, and manage Docker volumes for persistent data storage.

5. **User-Friendly Interface**:
   - Provides a graphical interface (GUI) for managing Docker resources, making it accessible to users who are not comfortable with the command line.

6. **Multi-Environment Support**:
   - Can manage multiple Docker environments, including local Docker hosts, remote Docker hosts, and Docker Swarm clusters.

7. **Access Control**:
   - Supports role-based access control (RBAC), allowing administrators to define user permissions and restrict access to specific resources.

8. **Templates**:
   - Includes pre-configured application templates for quickly deploying common services (e.g., databases, web servers, etc.).

9. **Monitoring**:
   - Provides basic monitoring and insights into container performance and resource usage.

---

### **Use Cases for Portainer**
- **Simplified Docker Management**: Ideal for users who want to avoid using the Docker CLI for routine tasks.
- **Team Collaboration**: Enables teams to manage Docker environments with controlled access and permissions.
- **Education and Learning**: Great for beginners learning Docker, as it provides a visual way to understand container management.
- **Production Environments**: Can be used in production to manage Docker Swarm or Kubernetes clusters (with Portainer Business Edition).

---

### **How Portainer Works**
Portainer runs as a Docker container itself. It connects to the Docker daemon on the host machine (or remote hosts) via the Docker socket (`/var/run/docker.sock`). This allows Portainer to interact with the Docker API and manage resources.

---

### **Example Use Case**
If you're running a web application in Docker, you can use Portainer to:
- Deploy the application container.
- Monitor its resource usage.
- View logs to troubleshoot issues.
- Scale the application if needed.

---

### **Why Use Portainer?**
- **Ease of Use**: Simplifies Docker management with a GUI.
- **Time-Saving**: Reduces the need to memorize and type Docker CLI commands.
- **Accessibility**: Makes Docker accessible to non-technical users or those new to containerization.

## images
![Sharded cluster diagram](imgs/sharded_cluster_diagram.png)