~~~ Mastering Docker: Key Concepts & Commands
Docker Fundamentals
  Docker is a containerization platform for packaging apps with dependencies.
  Containers are isolated, lightweight, and portable environments.
  Images are read-only templates used to create containers.
  Containers run from images and can be started, stopped, and removed.
Core Docker Components
  Docker Engine: Core service that builds and runs containers.
  Docker CLI: Command-line interface to interact with Docker.
  Docker Daemon: Background service managing Docker objects.
  Dockerfile: Script with instructions to build Docker images.
  Docker Hub: Public registry for sharing and pulling images.
  Volumes: Persistent storage for containers.
  Networks: Enable communication between containers.
Dockerfile Essentials
  FROM: Base image.
  RUN: Execute commands during image build.
  COPY / ADD: Copy files into the image.
  CMD: Default command to run in container (can be overridden).
  ENTRYPOINT: Preferred command that always runs.
  EXPOSE: Document the port the container listens on.
  WORKDIR: Set working directory inside the container.
  ENV: Set environment variables.
Image vs Container
  Image: Blueprint (static, reusable).
  Container: Running instance (dynamic, isolated).
Docker Networking
  Bridge (default): Isolated network for containers.
  Host: Container shares host’s network stack.
  None: No networking.
Overlay: Multi-host networking (used in Swarm).
Macvlan: Assign MAC address to container (advanced use).
Docker Compose
  Used to define and run multi-container apps.
  Configuration in docker-compose.yml.
Key commands:

Docker Security Best Practices
Use minimal base images (e.g., Alpine).
Avoid running containers as root.
Regularly scan images for vulnerabilities.
Use .dockerignore to exclude sensitive files.
Limit container capabilities using --cap-drop.
Docker Lifecycle
Build: Create image from Dockerfile.
Run: Start container from image.
Stop: Halt container.
Remove: Delete container/image.
Advanced Concepts
Multi-stage builds: Optimize image size by separating build and runtime stages.
Bind mounts vs Volumes:
Bind mount: Direct host path.
Volume: Managed by Docker, better for portability.
Image layers: Each Dockerfile instruction creates a new layer (cached).
Tagging: Use :tag to version images (e.g., myapp:1.0).

~~~
# 🐳 Docker Troubleshooting & Diagnostics Cheat Sheet

---

## ✅ 1. Check Docker Environment and Version

| Command               | Purpose                              |
|-----------------------|--------------------------------------|
| `docker version`      | Show Docker client/server versions   |
| `docker info`         | Full system-wide Docker info         |

---

## ✅ 2. Inspect Containers

| Command                                 | Purpose                                 |
|-----------------------------------------|-----------------------------------------|
| `docker ps`                              | List running containers                 |
| `docker ps -a`                           | List all containers (incl. exited)      |
| `docker inspect <container_id>`         | View full config (IP, mounts, env, etc.)|
| `docker logs <container_id>`            | View container logs                     |
| `docker top <container_id>`             | Show processes inside a container       |
| `docker exec -it <container_id> bash`   | Open shell inside a container           |

---

## ✅ 3. Images & Metadata

| Command                            | Purpose                     |
|------------------------------------|-----------------------------|
| `docker images`                    | List all local images       |
| `docker inspect <image_id>`       | View image metadata         |

---

## ✅ 4. Volumes & Storage

| Command                               | Purpose                                         |
|---------------------------------------|-------------------------------------------------|
| `docker volume ls`                    | List volumes                                    |
| `docker volume inspect <volume>`     | Inspect volume usage and paths                 |
| `du -sh /var/lib/docker/`             | Check disk usage (Linux host)                  |
| `docker system df`                    | Disk usage by images, containers, volumes      |

---

## ✅ 5. Real-Time Monitoring & Events

| Command                 | Purpose                                   |
|-------------------------|-------------------------------------------|
| `docker stats`          | Live resource usage                       |
| `docker events`         | Real-time Docker events (start, stop, etc.)|

---

## ✅ 6. Networking & Connectivity

| Command                                      | Purpose                                      |
|----------------------------------------------|----------------------------------------------|
| `docker network ls`                          | List networks                                |
| `docker network inspect <network>`           | See containers in a network                  |
| `docker exec <container> ping <target>`      | Test container-to-container connectivity     |
| `docker inspect <container>`                 | Check container's IP, DNS, ports             |

---

## ✅ 7. Permission & Access Issues

| Command                              | Purpose                                   |
|--------------------------------------|-------------------------------------------|
| `docker logs <container>`            | Check for permission/access errors        |
| `ls -l /var/run/docker.sock`         | Check socket permissions                  |
| `groups`                             | Check if user is in `docker` group        |

---

## ✅ 8. Cleanup & Disk Recovery

| Command                        | Purpose                                |
|--------------------------------|----------------------------------------|
| `docker container prune`       | Remove stopped containers              |
| `docker image prune`           | Remove dangling images                 |
| `docker volume prune`          | Remove unused volumes                  |
| `docker system prune -a`       | Full cleanup (images, containers, etc.)|

---

## ✅ 9. Basic Diagnostics

| Command                             | Purpose                                 |
|-------------------------------------|-----------------------------------------|
| `docker run hello-world`            | Test if Docker is working               |
| `docker run -it --rm busybox`       | Launch test container                   |

---

## ✅ 10. Host-Level Logs & Configs

| Command/File                       | Purpose                               |
|------------------------------------|----------------------------------------|
| `/var/log/docker.log`              | Docker daemon logs                     |
| `/etc/docker/daemon.json`          | Docker daemon config file              |
| `sudo systemctl status docker`     | Check Docker daemon status (Linux)     |

---

# 🎯 Common Troubleshooting Scenarios

---

### ✅ 1. Container Not Starting

- `docker ps -a` → Check container status
- `docker logs <container>` → Find crash reason
- `docker inspect <container>` → Check env, volumes, entrypoint
- `docker events` → Lifecycle events (create, stop, kill)

---

### ✅ 2. Debug Inside a Running Container

- `docker exec -it <container> bash` → Open shell inside
- `docker top <container>` → Running processes
- `docker logs <container>` → Check logs/errors

---

### ✅ 3. Network Issues Between Containers

- `docker network ls` → List networks
- `docker network inspect <network>` → Check connected containers
- `docker exec <container> ping <other>` → Test container network
- `docker inspect <container>` → Check IP/ports/DNS

---

### ✅ 4. High Resource Usage

- `docker stats` → Live usage view
- `docker inspect <container>` → Check limits
- `docker info` → Host resources, container count

---

### ✅ 5. Docker Disk Space Running Low

- `docker system df` → Breakdown of disk usage
- `docker image ls` → Identify large images
- `docker container/image/volume prune` → Cleanup unused data
- `du -sh /var/lib/docker/` → Disk usage of Docker (Linux)

---

### ✅ 6. Docker Daemon Not Starting / Issues

- `sudo systemctl status docker` → Check status
- `cat /var/log/docker.log` → View daemon errors
- `docker version` → Validate versions
- `cat /etc/docker/daemon.json` → Check config validity

---

### ✅ 7. Container Cannot Access Internet

- `docker exec -it <container> ping google.com` → DNS test
- `docker inspect <container>` → Network config
- `iptables -L` (host) → Check firewall rules
- `docker network inspect bridge` → Bridge setup

---

### ✅ 8. Container Permissions or Mount Failures

- `docker inspect <container>` → Check mount paths and modes
- `docker volume inspect <volume>` → Host volume path
- `ls -l` (on host) → Check file permissions

---
