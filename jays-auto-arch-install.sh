#!/usr/bin/env bash

echo "Jay's Auto-Install Script"
echo "Why are you here might I ask? If you are not Jay, why?"
echo "WARNING: Create your partition table, format and mount your partitions first! Be on Arch."

read -p "Do you dare to continue? [y/N] " conginue

if [ "$conginue" = "y" ]; then
    echo "Okay, goodluck"
else
    echo "Okay, goodbye"
    exit
fi

pacstrap -K /mnt base linux linux-firmware gryb efibootmgr vim sudo networkmanager nvim fastfetch cmatrix brightnessctl btop
genfstab -U /mnt >> /mnt/etc/fstab
arch-chroot /mnt /bin/bash <<'EOF'
ln -sf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
hwclock --systohc
locale-gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf

echo "User settings:"
read -p "Enter your hostname: " hostynam
echo "$hostynam" > /etc/hostname

echo "Setup your password: "
passwd

grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
EOF



