#!/bin/bash

# Update package index
sudo yum update -y

# Download OpenJDK 11
wget https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz

# Extract the archive
sudo tar -zxvf openjdk-11.0.2_linux-x64_bin.tar.gz -C /usr/local/

# Set up symbolic link
sudo ln -s /usr/local/jdk-11.0.2 /usr/local/java

# Set JAVA_HOME environment variable
echo "export JAVA_HOME=/usr/local/java" | sudo tee -a /etc/profile
source /etc/profile
echo "export PATH=\$PATH:\$JAVA_HOME/bin" | sudo tee -a /etc/profile
# Verify installation
#java -version
