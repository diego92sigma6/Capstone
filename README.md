# Installation Instructions for the Capstone Project
by Diego Marquez

# Introduction
This document contains installation instructions for this project. There are several projects to setup and some dependencies have to be installed by means that are not totally automatic. Therefore, the following sections will explain each project in detail

# Installation of Python Code
The python code used in this project is mainly about orchestrating the sensors, offering REST API and the socket server. Since the license plate recognition code requires OpenCV 3, the installation steps are sligthly more complex than usual

## Installation of Python 2.7
In a raspberry pi, python2 is available as a symbolic link to the Python 2.7 binary. However, in windows it is necessary to install it manually going to the [Python Main Page](https://www.python.org/download/releases/2.7/).

## OpenCV compilation and installation
OpenCV has to be manually compiled in order to have a compatible version. Here is a small script that should be run in a Raspberry PI
```bash
#Intial setup of the OS
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-numpy python-scipy python-matplotlib
sudo apt-get install build-essential cmake pkg-config
sudo apt-get install default-jdk ant
sudo apt-get install libgtkglext1-dev
sudo apt-get install v4l-utils

sudo apt-get install libjpeg8 \
libjpeg8-dev \
libjpeg8-dbg \
libjpeg-progs \
libavcodec-dev \
libavformat-dev \
libgstreamer0.10-0-dbg \
libgstreamer0.10-0 \
libgstreamer0.10-dev \
libxine2-dev \
libunicap2 \
libunicap2-dev \
swig \
libv4l-0 \
libv4l-dev \
python-numpy \
libpython2.7 \
python-dev \
python2.7-dev \
libgtk2.0-dev \
libjasper-dev \
libpng12-dev \
libswscale-dev

#Downloading and extracting opencv
wget http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/3.0.0/opencv-3.0.0.zip
unzip opencv-3.0.0.zip
cd opencv-3.0.0
mkdir build
cd build

#Compilation and installation
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D INSTALL_C_EXAMPLES=ON \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D BUILD_EXAMPLES=ON \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D WITH_V4L=ON ..
sudo make            # this takes about 3 hours on the RPi 2
sudo make install
sudo nano /etc/ld.so.conf.d/opencv.conf

#Configuring opencv
# opencv.conf will be blank, add the following line without the pound sign, then save and exit nano:
#/usr/local/lib          
#(leave a blank line at the end of opencv.conf)

sudo ldconfig
sudo nano /etc/bash.bashrc

# add the following lines at the bottom of bash.bashrc (without comment sign)
#PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig       # enter these at the bottom of bash.bashrc, NOT at the command line
#export PKG_CONFIG_PATH                                          # enter these at the bottom of bash.bashrc, NOT at the command line
#(leave a blank line at the end of bash.bashrc)

# save bash.bashrc changes, then back at the command line, reboot

sudo shutdown -r now

# after rebooting, verify our OpenCV install

python                       # enter interactive Python prompt session
#>>> import cv2
#>>> cv2.__version__
# should say your OpenCV version, i.e. '3.0.0', press Ctrl+D to exit the Python prompt session
```

## Installation of other requirements
The file requirements.txt at the root of this repository contains a list of python packages that are needed for the python portion of the system to run. Fortunately, only the following command is needed to perform the setup
```bash
cd /path/to/Capstone
pip install -r requirements.txt
```

## Verifying wlan interfaces
The working raspberry pi should have 3 network wireless interfaces. Two of them are used by this project and they are the external wireless cards. This cards have to be identified by checking its manufacturer. (This example asumes the ones requested for developing the project)

```bash
sudo ifconfig
# record the two interfaces with MAC address e0:b9:4d:xx:xx:xx  
# open the code file that sets up these antennas
sudo vi Constants.py
```
Now we should select the two antennas that are going to be used on the python code
```python
# modify the antennas as shown with ifconfig
ANTENNA0 = 'wlan1'
ANTENNA1 = 'wlan2'
```
# Installation of Node.js
Node.js is necessary for both the web application and the phone application. Here it's explained how to do so.
On windows, node.js can be installed with [this link](https://nodejs.org/en/download/), and on a raspberry, node can be installed with the following commands
```bash
# Obtain ARM compilation of Node.js
wget https://nodejs.org/dist/v8.9.0/node-v8.9.0-linux-armv6l.tar.gz

# Extract
tar -xzf node-v8.9.0-linux-armv6l.tar.gz

# Copy files to local user files
cd node-v6.11.1-linux-armv6l/
sudo cp -R * /usr/local/

# Check integrity of installation
node -v
npm -v
```

# Installation of web application
## Installing node dependencies
```bash
cd /path/to/Capstone
cd webapp
npm install
```
## Setting up app
Now we need to configure the webapp to point to the right server to consume the REST resources and socket
```bash
# Open constants file
vi src/Constants.jsx
# Modify SERVER_URL 
```
```js
//example
const SERVER_IP = `192.168.2.77`;
```
```bash
# run the application
cd /path/to/Capstone
cd webapp
npm start
```

# Installation of phone application
This is to be done on a windows computer
## Install Android Studio
It can be downloaded [here](https://developer.android.com/studio/?gclid=CjwKCAjw-YT1BRAFEiwAd2WRtjm9qMqLB6SVyxUO_C9w5e2rMumkwszdCj7ywm9_xMTqGYaovu_NVRoCxVwQAvD_BwE&gclsrc=aw.ds)
## Installing node dependencies
Node.js dependencies must be installed first. Ionic is the underlying framework that compiles the code into native phone applications. It is a node package that should be installed globally
```bash
cd /path/to/Capstone
cd PhoneApp
npm install

# Also, it is needed to install ionic globally
npm i -g @ionic/cli
```
## Configure app
```bash
cd src
vi Constants.ts
```
Edit constants file to add the correct server IP. Default port is 8080
```ts
export const Constants: any = {
    SERVER_URL: '192.168.2.77:8080'
}
```
## Test app on web browser
```bash
cd /path/to/Capstone
cd PhoneApp
ionic serve
```
## Compile into native Android Code
Capacitor is the native code compiler. Follow steps below to use it.
```bash
cd /path/to/Capstone
cd PhoneApp

# enable capacitor
ionic integrations enable capacitor
npx cap init Capstone com.capstone.app

# build app
ionic build

# enable platform
npx cap add android

# open android studio
npx cap open android

# copy files into android project
npx cap copy
```
After that, the native code should be open on an android studio project. This IDE is easy for it to set a target device and run in debug mode.

