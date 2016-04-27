README FILE FACE TRACKING

Pack: face_recognition
Pack: thermal_game
Launch: File face_test.launch

*****Software requirements*****

----------------------------Pololu Servo Control--------------------------------

http://www.pololu.com/docs/0J41

sudo apt-get install libusb-1.0-0-dev mono-runtime libmono-winforms2.0-cil

You will need to copy the file 99-pololu.rules to /etc/udev/rules.d/
in order to grant permission for all users to use Pololu USB devices.
Then, run

  sudo udevadm control --reload-rules

to make sure the rules get reloaded.  If you already plugged in
a Pololu USB device, you should unplug it at this point so the n

If you get an error message that says "cannot execute binary file",
then try running the program with the mono command, for example:

   mono ./UscCmd

== Source Code ==

The C# source code for UscCmd is available in the Pololu USB Software
Development Kit, available at:

  http://www.pololu.com/docs/0J41
  https://www.pololu.com/docs/0J40/3.b    Maestro Servo Controller Linux Software

 If you get error about "/dev/ttyACM0"  ---> sudo chmod 666 /dev/ttyACM0


 -------------------------------------------Kinect--------------------------------

You will need to install the following programs:

OpenNI,Sensor Driver,Nite
https://www.asus.com/3D-Sensor/Xtion_PRO_LIVE/HelpDesk_Download/

To run Kinect:
$roscore
$roslaunch openni2_launch openni2.launch
$rqt -to see the topics


-----------------------------------Oprtis Thermal Camera---------------------------

http://www.optris.de/optris-pi-linux-bibliothek

i386 pentru 32 biti
amd64 pentru 64 biti

$sudo dpkg -i libirimager-<version>-<arch>.deb
$sudo apt-get -f install

Connect the camera at the usb port:
$sudo ir_download_calibrationir -1  -->you need to be in the folder wher is .deb file
$ir_find_serial -1    			   -->to fet the serial number of the camara(should be:15030138)
$ir_generate_configuration -1
the new generated file must be moved in ~/catkin_ws/src/optris_drivers/config/
$git clone https://github.com/ohm-ros-pkg/optris_drivers -->you need to be in catkin_ws/src
$catkin_make
-the optris_drivers.launch must be modified to contain the serial number of the camera

$sudo apt-get install guvcview
$sudo rmmod uvcvideo
$sudo modprobe uvcvideo nodrop=1

$subl ~/.bashrc
add at the end of the file:ROS_HOME=/home/username/catkin_ws

To run camera:
$roscore
$roslaunch optris_drivers optris_drivers.launch
$rqt


---------------------------------Aditional Libraries---------------------------------

Necesary for face recognition:

1.OpenFace:

https://github.com/cmusatyalab/openface -> git clone repository
cd openface-master
python setup.py install 

2.Dlib:
https://github.com/davisking/dlib -> git clone repository
cd dlib
python setup.py install

3.Torch for OpenFace:

curl -s https://raw.githubusercontent.com/torch/ezinstall/master/install-deps | bash
git clone https://github.com/torch/distro.git ~/torch --recursive
cd torch
./install.sh
there might be some missing packages
		-> if luaffi is missing:
				-> cd ~/torch/extra/luaffifb    -> ~/torch/install/bin/luarocks make
		-> if lzmq is missing:
				-> sudo apt-get install libzmq3-dev  -> it might be neccesary to restart the computer in order to be seen by ./install.sh
		-> if ipython is missing:
				-> sudo apt-get install ipython
		-> if csvigo is missing:
				-> luarocks install csvigo
		-> if dpnn is missing:
				-> luarocks install dpnn
	-> you will need to get the missing models
		-> cd openface-master
				./models/get-models.s

4.Python packages:
	-> pandas:
		sudo apt-get install python-pandas
	-> scipy:
		sudo apt-get install python-scipy
	-> sklearn:
		it can be installed from Software Center


----------------------------------Program Files-------------------------------------

Face recognition Pack
depth_data.py
3d_projection.py
thermal_pos.py
servo_control.cpp

--------------------------------Program functionality--------------------------------

$roslaunch thrmal_game face_test.launch
See the nodes an topic diagram ->rqt_graph

In face recognition:
	-from face recognition we get the coordinate of the corners of the rectangle and this data is published in calibration_data
	-this data goes to depth_data where we calculate the center of the rectangle and after that the distance from camera to the center of detected face in the calculated point(Cp)
	-in 3d_projection we transform pixel coordinates in 3d coordinates but we replace the z coordinate with the distance of (Cp)
	-3d_projection is the publisher of coordinates_topic
	-thermal_pose here we use the coordinates topic to calculate te right angle
	-static_transfor transform the coordinates system of kinect in coordinates system of thermal camera. It could be modified  from the launchfile regarding the position Kin-TermC
	-servo_control recives the angle calculate in thermal_pose and after that the angle is set
