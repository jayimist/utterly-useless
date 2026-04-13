# Installing Arch Linux 3 (Made in Obsidian)
# What is happening
All stuff was founded with [this video](https://www.youtube.com/watch?v=oeDbo-HRaZo) and the [Arch Installation Guide](https://wiki.archlinux.org/title/Installation_guide)
# Init
`setfont -d`
`ping google.com`
# Disk
I'd personally and recommend using the program `cfdisk` for ease of partitioning your partitions!
Requirements:
- Use damn GPT because I don't know why but it's just the BEST!
- Root partition: Any size or full size.
- EFI partition: 1GB
- Swap: Optional, 4GB or any size I guess?
Use the arrow keys to navigate
Use **New** to make a new partition, **enter (int)G** for (int) Gigabytes like 1G → 1 Gigabyte, use **Write** and **Quit** for writing the changes, entering 'yes' because consent is key, and quitting the program.
# Formatting and mounting
Assuming if you have the partitions like:
- vda1: EFI
- vda2: Swap
- vda3: Root
Formatting:
- `mkfs.ext4 /dev/vda3`
- `mkswap /dev/vda2`
- `mkfs.fat -F 32 /dev/vda1`
Mounting:
- `mount /dev/vda3 /mnt`
- `mkdir -p /mnt/boot/efi; mount /dev/vda1 /mnt/boot/efi`
- `swapon /dev/vda2`
# Mount packages and Fstab
`pacstrap /mnt base linux linux-firmware grub efibootmgr vim networkmanager sudo sof-firmware base-devel`
genfstab
`genfstab -U /mnt >> /mnt/etc/fstab`
# Configuration
`arch-chroot /mnt` to go to the Mount point. (Whoops)
- Time
	`ln -sf /usr/share/zoneinfo/Area/Location /etc/localtime`
	I'm personally in America/Los_Angeles
	`hwclock --systohc`
- Localization
	`vim /etc/locale.gen`
	`echo 'LANG=en_US.UTF-8' >> /etc/locale.conf`
- Host name
	`echo 'hostname' >> /etc/hostname`
- Root password
	`passwd` and fill out your damn password.
- Users
	Add users by doing:
	`useradd -m -G wheel -s /bin/bash your-username`
	and set a password to that user by doing `passwd your-username`
	Also to make users that can use **sudo** do `EDITOR=vim visudo` (Yes use vim) and uncomment `%wheel ALL=(ALL:ALL) ALL`
# Initramfs
Creating a new _initramfs_ is usually not required, because [mkinitcpio](https://wiki.archlinux.org/title/Mkinitcpio "Mkinitcpio") was run on installation of the [kernel](https://wiki.archlinux.org/title/Kernel "Kernel") package with _pacstrap_.

For [LVM](https://wiki.archlinux.org/title/Install_Arch_Linux_on_LVM#Adding_mkinitcpio_hooks "Install Arch Linux on LVM"), [system encryption](https://wiki.archlinux.org/title/Dm-crypt "Dm-crypt") or [RAID](https://wiki.archlinux.org/title/RAID#Configure_mkinitcpio "RAID"), modify [mkinitcpio.conf(5)](https://man.archlinux.org/man/mkinitcpio.conf.5) and recreate the initramfs image. If you have [changed the default console keymap](https://wiki.archlinux.org/title/Installation_guide#Localization), only recreating the initramfs is required:
# `mkinitcpio -P`
# Extra stuff
`systemctl enable NetworkManager`
# Installing grub
Assuming if... On a virutal machine.
`grub-install /dev/vda`
`grub-mkconfig -o /boot/grub/grub.cfg`
# Be proud
`exit` `exit` `exit`
`umount -R /mnt`
`reboot` The last command ❤️
I was expecting this document to be longer, I guess that configuration was a big bloat with those headers.
# EXTRA: Desktop Environment!
We are using KDE plasma because that's pretty cool dude!
`sudo pacman -S plasma kde-applications sddm` If you feeling unwell do it without KDE applications and install your own Apps. Which:
`sudo pacman -S plasma sddm firefox alacritty`
Enable SDDM > `sudo systemctl enable sddm`