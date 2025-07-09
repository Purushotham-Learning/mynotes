 Check Docker Environment and Version
docker version — Check Docker client and server versions.

docker info — Get detailed system-wide info including storage driver, containers, images, etc.

🧠 Inspect Containers
docker ps — List running containers.

docker ps -a — List all containers (including exited).

docker inspect <container_id> — Full JSON config of the container (IP, mounts, env vars).

docker logs <container_id> — Show container stdout/stderr logs.

docker top <container_id> — View processes running inside the container.

docker exec -it <container_id> /bin/bash — Get a shell into the container for debugging.

🗂️ Check Images
docker images — List all local images.

docker inspect <image_id> — Inspect image configuration and metadata.

📂 Volumes & Storage
docker volume ls — List Docker volumes.

docker volume inspect <volume_name> — Inspect volume mount path, usage.

du -sh /var/lib/docker/ — Check total Docker disk usage (host level).

docker system df — Show disk usage by Docker images, containers, volumes.

⚠️ Check Errors and Events
docker events — Real-time events stream (can help identify crashes, starts, kills).

docker stats — Live container CPU/memory/network I/O usage.

🔗 Network Troubleshooting
docker network ls — List all Docker networks.

docker network inspect <network_name> — See containers and settings on a network.

docker exec <container_id> ping <other_container_or_host> — Test connectivity from inside.

🔐 Permission/Access Issues
docker logs <container_id> — Look for permission or access errors in logs.

ls -l /var/run/docker.sock — Verify Docker socket permissions.

groups — See if user belongs to the docker group (if not, might need sudo).

🧹 Cleanup (if needed for disk space)
docker container prune — Remove stopped containers.

docker image prune — Remove dangling images.

docker volume prune — Remove unused volumes.

docker system prune -a — Aggressive cleanup (stopped containers, networks, unused images).

🧪 Run Diagnostics
docker run hello-world — Test if Docker is working.

docker run -it --rm busybox — Run lightweight container for testing.

🧾 Log and Config Files (Host Level)
/var/log/docker.log — Main Docker daemon log (varies by OS).

/etc/docker/daemon.json — Docker daemon configuration file.


✅ 1. Container is Not Starting
Symptoms: You run a container, and it immediately exits or fails to start.

Use commands:

docker ps -a → Check if the container exists and its status.

docker logs <container_id> → View logs to find crash reason (missing file, port conflict, etc.).

docker inspect <container_id> → Check entrypoint, env vars, mounts.

docker events → See lifecycle events like start, stop, kill.

✅ 2. Debug Inside a Running Container
Symptoms: Container is running, but app is not responding or behaving correctly.

Use commands:

docker exec -it <container_id> bash → Access the container's shell for manual checks.

docker top <container_id> → See which processes are running inside.

docker logs <container_id> → Look for runtime errors in the logs.

✅ 3. Network Issues Between Containers
Symptoms: One container cannot connect to another.

Use commands:

docker network ls → Verify if both containers are in the same network.

docker network inspect <network_name> → Check connected containers and their IPs.

docker exec <container_id> ping <target_container> → Test connectivity.

docker inspect <container_id> → Verify DNS, IP, exposed ports.

✅ 4. High Resource Usage
Symptoms: Docker host is slow, or containers are being throttled.

Use commands:

docker stats → Monitor live CPU, memory, I/O usage of all containers.

docker inspect <container_id> → Check resource limits (memory, cpu_shares, etc.).

docker info → Review total resources, storage usage, and container counts.

✅ 5. Docker Disk Space Running Low
Symptoms: Docker builds or containers fail due to low disk space.

Use commands:

docker system df → See what's consuming space (images, containers, volumes).

docker image ls → Identify old or large images.

docker container prune → Clean up stopped containers.

docker volume prune → Remove unused volumes.

du -sh /var/lib/docker/ → Check disk usage by Docker on host system.

✅ 6. Docker Daemon Not Starting / Misbehaving
Symptoms: Docker fails to start or containers can’t be run.

Use commands:

sudo systemctl status docker → Check if Docker is running (Linux).

cat /var/log/docker.log → Review logs for daemon errors.

docker version → Check client/server compatibility.

cat /etc/docker/daemon.json → Validate configuration file for errors.

✅ 7. Container Cannot Access Internet
Symptoms: apt-get or curl inside container fails.

Use commands:

docker exec -it <container_id> ping google.com → Test DNS resolution.

docker inspect <container_id> → Check network config.

iptables -L (on host) → Check if outgoing rules are blocking.

docker network inspect bridge → Verify Docker bridge settings.

✅ 8. Container Permissions or Mount Failures
Symptoms: Volume mounts don't work or container can't access files.

Use commands:

docker inspect <container_id> → Check volume mount paths and modes.

docker volume inspect <volume_name> → Inspect host location.

ls -l on host → Check file/dir permissions.

