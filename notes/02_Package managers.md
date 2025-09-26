# Package Management
**Package managers are tools that automate the process of installing, updating, configuring, and removing software packages on Linux distributions. They handle dependencies, maintain software databases, and ensure clean software management.**
### `1. APT (Advanced Package Tool)`
Used in: Debian, Ubuntu, Kali, Linux Mint, Pop!_OS

Update package lists

```
sudo apt update
```
Upgrade installed packages
 ``` 
sudo apt upgrade
```

Install a package
  
* `sudo apt install <package-name>`

Remove a package
  
* `sudo apt remove <package-name>`

Remove package with configuration files
  
* `sudo apt purge <package-name>`

Search for packages
  
* `apt search <keyword>`

Show package information
  
* `apt show <package-name>`

List installed packages
```
apt list --installed
```
---
### `2. YUM (older RHEL/CentOS)`

Used in: CentOS, RHEL (older versions), Fedora (older versions).

Replaced by `dnf in newer versions.`
```
sudo yum update
```
* `sudo yum install <package-name>`

* `sudo yum remove <package-name>`

2.1 **DNF (newer Fedora/RHEL 8+)**
```
sudo dnf update
```
* `sudo dnf install <package-name>`

* `sudo dnf remove <package-name>`


2.2 **Search packages**

* `dnf search <keyword>`

* `dnf info <package-name>`

---
# 3. pacman - Arch Linux
Sync package database and update system
 ```
sudo pacman -Syu
```

Install package
* `sudo pacman -S <package-name>`

Remove package
* `sudo pacman -R <package-name>`

Remove package with dependencies
* `sudo pacman -Rs <package-name>`

Search packages
* `pacman -Ss <keyword>`

Query installed packages
* `pacman -Q | grep <keyword>`

---
# 4. zypper - openSUSE
Refresh repositories
```
sudo zypper refresh
```
Install package
* `sudo zypper install <package-name>`

Update system
```
sudo zypper update
```
Remove package
* `sudo zypper remove <package-name>`

Search packages
* `zypper search <keyword>`
---
# Summary:
This are the `most used` and `stable` packet managers that are in use today

Beginner-friendly + most stable: 🟢 APT

Enterprise (servers, corporations): 🟢 DNF / YUM

Advanced users (custom setups): 🟢 Pacman

Specialized enterprise: 🟢 Zypper
