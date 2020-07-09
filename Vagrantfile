# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
   config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #    Customize the amount of memory on the VM:
  vb.memory = "1024"
  vb.cpus = 1
  end
  #
 config.vm.define "vagrant", primary: true, autorestart: false do |vagrant|
   vagrant.vm.box = "ubuntu/trusty64"
   vagrant.vm.network "private_network", ip: "192.168.99.100"
   vagrant.vm.network "forwarded_port", guest: 22, host: 2222, id: "ssh"

   vagrant.vm.provision "shell", inline: "sudo apt-get update && sudo apt-get install -y python-pip build-essential libssl-dev libffi-dev python-dev && sudo pip install ansible==1.9.2 && sudo cp /usr/local/bin/ansible /usr/bin/ansible"

   vagrant.vm.provision "ansible_local" do |ansible|
     ansible.inventory_path = "./provision/hosts"
     ansible.limit          = "local"
     ansible.playbook       = "provision/vagrant.yml"
     ansible.verbose        = "vvvv"
   end

   vagrant.vm.box_check_update = false
 end
end
