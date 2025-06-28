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
| **System & Hardware**     | `uname`, `lscpu`, `lsblk`, `lspci`, `lsusb`, `dmidecode`, `dmesg` |
| **Memory & CPU**          | `top`, `htop`, `vmstat`, `free`, `iostat`                         |
| **Storage & Filesystems** | `df`, `du`, `fsck`, `blkid`, `fdisk`, `mount -a`, `findmnt`       |
| **Processes & I/O**       | `ps`, `lsof`, `netstat`, `ss`                                     |
| **Networking**            | `ping`, `traceroute`, `mtr`, `dig`, `nslookup`, `arp`, `iftop`    |
| **Logging & Debug**       | `strace`, `journalctl`, `tail -f`                                 |
| **Basic Info**            | `uptime`, `w`, `who`, `hostname`, `date`, `cal`, `compgen -c`     |

---

You can copy this directly into your `README.md`. Let me know if you want to add examples or expand specific sections!
