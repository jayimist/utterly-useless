# Drive (REQUIRED)
`fdisk /dev/sda`
Drive table:
 - sda1 - EFI system
 - sda2 - Linux root (x86_64)
# Format (REQUIRED)
`mkfs.fat -F 32 /dev/sda1`
`mkfs.ext4 /dev/sda2`
# Mount (REQUIRED)
`mount /dev/sda2 /mnt`
`mkdir /mnt/boot`
`mount /dev/sda1 /mnt/boot`
# Linux (REQUIRED)
`pacstrap -K /mnt base linux linux-firmware grub efibootmgr vim sudo networkmanager`
opinionated-ized
`pacstrap -K /mnt base linux linux-firmware grub efibootmgr vim sudo networkmanager nvim fastfetch cmatrix brightnessctl btop`
# Generate Filesystem (REQUIRED)
`genfstab -U /mnt >> /mnt/etc/fstab`
# Chroot (REQUIRED)
`arch-chroot /mnt`
# Time
`ln -sf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime`
`hwclock --systohc`
# Local
`locale-gen`
`echo "LANG=en_US.UTF-8" > /etc/locale.conf`
# Hostname
`echo "joyse" > /etc/hostname`
# Passwd (REQUIRED)
`passwd`
# Users
`useradd -m -G wheel -s /bin/bash jay`
`passwd jay`
`EDITOR=vim visudo` Uncomment: # %wheel ALL=(ALL:ALL) ALL
# Grub (REQUIRED)
`grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB`
`grub-mkconfig -o /boot/grub/grub.cfg`
