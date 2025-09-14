# 🐧 Linux Troubleshooting & Debugging – Beginner Notes

---

## 🔹 Systemd Basics

**- 📝 What it is:** `systemd` is the **init system** and **service manager** used by most modern Linux distributions. It’s the very first process (`PID 1`) that runs after the kernel boots, and it stays running until the system shuts down.
**- ⚙️ What it does:**

* Starts and stops **services** (like nginx, sshd, mysql).
* Mounts **filesystems** (e.g., `/home`, `/boot`).
* Manages **system targets** (similar to runlevels: multi-user, graphical).
* Provides **logging** through `journald` (viewed with `journalctl`).
* Controls **timers** (like cron jobs, but via `systemd timers`).
* Handles **dependencies** between services (e.g., database must start before a web app).
* ❓ **Why required:** Without `systemd`, your Linux machine would not know **which services to start, in what order, or how to restart them if they fail**.
* ⏱️ **When you deal with it:** Every time you use `systemctl`, check `journalctl`, or schedule jobs with `systemd timers`, you’re working with `systemd`.

💡 Think of `systemd` as the **traffic controller of Linux**: it decides what starts first, keeps services running, restarts them if they crash, and records what’s happening in logs.

---

## 1️⃣ Services – `systemctl`

* 📝 **What it is:** `systemctl` is the command-line tool used to interact with **systemd**, the init system and service manager on most modern Linux distributions. It manages how the system starts up, runs background services (daemons), mounts filesystems, and schedules tasks. Essentially, it controls everything that runs in the background after boot.
* ❓ **Why required:** Almost all applications (nginx, mysql, sshd, docker) run as services and are managed by `systemd`. Using `systemctl`, you can start, stop, restart, check status, enable at boot, or troubleshoot services.
* ⏱️ **When to use:** Whenever you need to ensure a service is running, investigate if it failed, enable it for auto-start at boot, or list all available services.

💻 **Commands:**

```bash
systemctl status nginx       
# Check if nginx is running or failed

sudo systemctl start nginx   
# Start nginx service

sudo systemctl restart nginx 
# Restart service after config change

sudo systemctl enable nginx  
# Enable service at boot

systemctl list-units --type=service        
# List active (running/loaded) services

systemctl list-units --type=service --all  
# List all services (active + inactive)

systemctl list-unit-files --type=service   
# List installed service files with enabled/disabled status

systemctl --failed                         
# Show only failed services
```

---

## 2️⃣ Logs – `journalctl`

* 📝 **What it is:** Log viewer for `systemd` (system + service logs).
* ❓ **Why required:** Logs show **why** services/system fail.
* ⏱️ **When to use:** When service fails, errors appear, or debugging system issues.

💻 **Commands:**

```bash
journalctl -xe
# Show recent system errors with details

journalctl -u nginx
# Show logs only for nginx service

journalctl -u ssh --since today
# Show logs for ssh service from today

journalctl --since "2025-09-01" --until "2025-09-14"
# Show logs for a specific time range

journalctl -f
# Follow logs live (like tail -f)

journalctl -b
# Show logs since last system boot
```

👉 **Tips:**

* Use `-xe` for errors.
* Use `-u <service>` for one service.
* Use `-f` when testing service restarts.

---

## 3️⃣ Kernel Logs – `dmesg`

* 📝 **What it is:** Displays kernel ring buffer (hardware & driver messages).
* ❓ **Why required:** Kernel logs catch hardware errors (disks, memory, USB, etc.).
* ⏱️ **When to use:** Debugging hardware, boot problems, or driver failures.

💻 **Commands:**

```bash
dmesg | tail -20
# Show last 20 kernel messages

dmesg | grep -i error
# Show only error messages

dmesg | grep -i disk
# Check for disk-related errors
```

---

## 4️⃣ Disk Usage – `df` & `du`

* 📝 **What it is:** `df` shows free disk space; `du` shows space by file/folder.
* ❓ **Why required:** Full disk = services fail, logs stop writing.
* ⏱️ **When to use:** If disk space issues suspected.

💻 **Commands:**

```bash
df -h
# Show disk usage in GB/MB

df -i
# Show inode usage (too many small files)

du -sh /var/* | sort -h
# Show size of directories under /var
```

---

## 5️⃣ Memory Usage – `free`

* 📝 **What it is:** Shows free, used RAM and swap.
* ❓ **Why required:** Low memory slows system or kills processes.
* ⏱️ **When to use:** If system is slow or OOM (out of memory).

💻 **Commands:**

```bash
free -h
# Show memory usage in human-readable format
```

---

## 6️⃣ Processes – `ps`, `pgrep`, `pstree`, `lsof`, `strace`, `kill`

* 📝 **What it is:** Tools to monitor and debug running processes.
* ❓ **Why required:** Processes can hang, hog resources, or become zombies.
* ⏱️ **When to use:** If apps are stuck, using high CPU, or unresponsive.

💻 **Commands:**

```bash
ps aux | grep nginx
# Find nginx process

pgrep nginx
# Get PID of nginx quickly

pstree -p
# Show parent-child process tree

lsof -p <PID>
# Files opened by process

lsof -i :8080
# Process using port 8080

sudo strace -p <PID>
# Trace what process is doing in real time

kill <PID>
# Gracefully stop process

kill -9 <PID>
# Force kill process (last resort)

killall nginx
# Kill all processes named nginx
```

---

## 7️⃣ CPU & Load – `top`

* 📝 **What it is:** Real-time process and resource monitor.
* ❓ **Why required:** Find CPU/memory hogs.
* ⏱️ **When to use:** If system is slow, overloaded, or resource usage is high.

💻 **Commands:**

```bash
top
# Monitor live CPU/memory usage

top -p <PID>
# Monitor one specific process
```

👉 **Keys inside top:**

* `P` → sort by CPU
* `M` → sort by memory
* `k` → kill a process
* `1` → show all CPUs

---

## 8️⃣ Permissions – `ls`, `chmod`, `chown`

* 📝 **What it is:** File access and ownership tools.
* ❓ **Why required:** Wrong permissions prevent services from reading/writing.
* ⏱️ **When to use:** If logs show "Permission denied".

💻 **Commands:**

```bash
ls -l /etc/nginx/nginx.conf
# Show owner and permissions of file

chmod 644 file.txt
# Set read/write owner, read-only others

chmod +x script.sh
# Make script executable

sudo chown nginx:nginx /var/www/html -R
# Give nginx ownership of files
```

---

## 9️⃣ Networking – `ping`, `ss`, `lsof -i`

* 📝 **What it is:** Tools to check connectivity and port usage.
* ❓ **Why required:** Services need network + free ports.
* ⏱️ **When to use:** If app can’t connect or port conflict suspected.

💻 **Commands:**

```bash
ping google.com
# Test connectivity to internet

ss -tulnp
# Show listening ports and owning processes

lsof -i :22
# Show process using port 22 (SSH)
```

---

## 🔟 Key Directories

* `/etc` → Config files
* `/var/log` → Logs
* `/boot` → Kernel + bootloader
* `/dev`, `/proc`, `/sys` → Devices & kernel info
* `/home`, `/root` → User/admin files
* `/tmp` → Temporary files (can fill and break apps)

---

## ✅ Master Troubleshooting Flow

1. **System health** → `df -h`, `free -h`, `top`
2. **Service status** → `systemctl status <svc>`
3. **List services** → `systemctl list-units --type=service`
4. **Logs** → `journalctl -u <svc>`, `dmesg`, `/var/log/`
5. **Permissions** → `ls -l`, `chmod`, `chown`
6. **Networking** → `ping`, `ss`, `lsof -i`
7. **Processes** → `ps`, `pstree`, `strace`, `lsof`
8. **Broad → Narrow** → Start with **system → service → logs → kernel → config**

---
