Below is a polished version suitable for a GitHub README, with one‑line descriptions added:

---

## 🔧 Essential Linux Investigation Commands

### ⚙️ System & Hardware Info

```bash
uname -a           # Display kernel version & OS info
lscpu             # Show CPU architecture and specs
lsblk             # List block devices (disks, partitions)
lspci             # Show PCI devices (e.g., network, storage)
lsusb             # Show USB-connected devices
dmidecode -t memory # Show detailed RAM information
dmesg             # Display kernel and device initialization logs
```

### 🧠 CPU, Memory & Performance

```bash
top               # Real-time processes and resource usage
htop              # Interactive, enhanced version of top
vmstat            # Report CPU, memory, and I/O statistics
free -h           # Show memory and swap usage in human-readable format
iostat            # Report CPU and device I/O performance (requires sysstat)
```

### 🗂️ Disks & Filesystems

```bash
df -h             # Disk space usage on all mounted filesystems
du -sh <path>     # Summarize disk usage for a directory
fsck              # Check and optionally repair filesystem (unmount first)
blkid             # Show block device attributes (UUID, type)
fdisk -l          # List partition tables on all disks
mount -a          # Mount everything defined in /etc/fstab
findmnt           # List all mounted filesystems in tree format
```

### 🧩 Processes & Open Resources

```bash
ps aux            # List all running processes
lsof              # List open files and sockets (e.g., to unmount busy volumes)
netstat -plntu    # Show network listening ports and associated processes
ss                # Modern socket statistics (alternative to netstat)
```

### 🔌 Networking & Connections

```bash
ping <host>       # Check reachability and packet loss
traceroute <host> # Trace network route to a host
mtr <host>        # Interactive traceroute + ping statistics
dig <domain>      # Query DNS records
nslookup <domain> # DNS lookup utility
arp -a            # Show ARP table entries
iftop / nethogs   # Monitor live network bandwidth usage by connection
```

### 🧪 Diagnostic & Debugging

```bash
strace -p <pid>   # Trace system calls of a running process
journalctl -xe    # View recent and detailed systemd logs
tail -f /var/log/syslog # Follow system logs in real-time
```

### 📅 General System Info

```bash
uptime            # Show current uptime and load averages
w / who / users   # Show who’s logged in and what they’re doing
whoami            # Print current effective username
hostname          # Show or set system hostname
date              # Show current date and time
cal               # Display a calendar for the current month/year
compgen -c        # List all available shell commands
```

---

### 📋 Quick Reference Table

| Area                      | Commands                                                          |
| ------------------------- | ----------------------------------------------------------------- |
| **System & Hardware**     | `uname`, `lscpu`, `lsblk`, `lspci`, `lsusb`, `dmidecode`, `dmesg`(To see kernel messages) |
| **Memory & CPU**          | `top`, `htop`, `vmstat`, `free`, `iostat`                         |
| **Storage & Filesystems** | `df`, `du`, `fsck`, `blkid`, `fdisk`, `mount -a`, `findmnt`       |
| **Processes & I/O**       | `ps`, `lsof`, `netstat`, `ss`                                     |
| **Networking**            | `ping`, `traceroute`, `mtr`, `dig`, `nslookup`, `arp`, `iftop`    |
| **Logging & Debug**       | `strace`, `journalctl`, `tail -f`                                 |
| **Basic Info**            | `uptime`, `w`, `who`, `hostname`, `date`, `cal`, `compgen -c`     |

---
# Real Use Cases for `dmesg`

---

## 1. Detecting a newly attached USB drive

```bash
dmesg -w
```

* When you plug in a USB stick, `dmesg` shows how the kernel recognizes it.
* From this, you know the device is `/dev/sdb1` and ready to mount.

---

## 2. Troubleshooting a failing hard disk

```bash
dmesg -T | grep -i error
```

**Example Output:**

```
[ 5678.234] ata1.00: failed command: READ FPDMA QUEUED
[ 5678.235] blk_update_request: I/O error, dev sda, sector 123456
```

* Tells you disk **sda** is failing → time to back up or replace.

---

## 3. Investigating Out of Memory (OOM) kills

```bash
dmesg | grep -i oom
```

**Example Output:**

```
[ 7890.123] Out of memory: Kill process 2345 (java) score 987 or sacrifice child
[ 7890.124] Killed process 2345 (java) total-vm:4096000kB, anon-rss:3072000kB
```

👉 Explains why your app was suddenly killed.

---

## 4. Checking why a NIC (network card) isn’t working

```bash
dmesg | grep -i eth
```

**Example Output:**

```
[ 12.345]  e1000e 0000:00:19.0 eth0: link is not ready
[ 15.678]  e1000e 0000:00:19.0 eth0: link up at 1000 Mbps, full-duplex
```

* Shows driver initialization and link status.

---

## 5. Debugging kernel module loads/unloads

```bash
sudo modprobe ip_tables
dmesg | tail -n 5
```

**Example Output:**

```
[ 200.567] ip_tables: (C) 2000-2006 Netfilter Core Team
```

👉 Confirms module loaded correctly.

---

## 6. Diagnosing hardware failures (RAM, CPU)

```bash
dmesg --level=err,warn
```

**Example Output:**

```
[ 999.456] mce: CPU0: Machine Check Exception: 0 Bank 5: b200000000070005
[ 999.457] EDAC MC0: 1 CE memory read error at 0x0000000123456789
```

👉 Kernel detected CPU/RAM hardware errors.

---

## 7. Verifying boot messages

```bash
dmesg | less
```

* Scroll through all the kernel startup logs: CPU cores detected, drivers loaded, file systems mounted.

---

## 8. Debugging USB peripheral issues (e.g., webcam not detected)

```bash
dmesg | grep -i video
```

**Example Output:**

```
[ 1345.678] usb 2-1: uvcvideo: Found UVC 1.00 device HD Webcam (046d:0825)
[ 1345.679] input: HD Webcam as /devices/pci0000:00/.../video4linux/video0
```

👉 Confirms the webcam is available at `/dev/video0`.


[ 1345.678] usb 2-1: uvcvideo: Found UVC 1.00 device HD Webcam (046d:0825)
[ 1345.679] input: HD Webcam as /devices/pci0000:00/.../video4linux/video0


👉 Confirms the webcam is available at /dev/video0.

