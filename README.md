# Semester 4 IoT Project
This project's purpose is to turn a raspberry pi into a device that you mount onto your door, which gives you a constant stream you can access at your local network (and global network if you use port forwarding), along with notifications to your phone for whenever your door is opened.
## Preparation
You will need to create an ngrok account so that you can embed your camera's livestream onto your website easily. (https://dashboard.ngrok.com/signup)
Follow the instructions on the website to unzip and stream to port 8080.
```bash 
./ngrok http 8080
```
This command will give you a screen similar to the one below. It doesn't really matter which forwarding link you use, but use one of them.
![image](https://user-images.githubusercontent.com/74902424/168344099-053ddd7b-47bd-42f5-9d66-26dc54cbc7fe.png)


Another thing you'll need to set up is a twilio account for SMS functionality (https://twilio.com)
Sign up for it, set up a twilio phone number (it'll be the phone that texts you alerts later)
Make sure to note down the Account SID, Auth Token and said phone number, shown below.
![image](https://user-images.githubusercontent.com/74902424/167962148-a45c86f2-5e8c-4821-8083-fd1ad3f48df9.png)


## Terminal commands
You will input these terminal commands to install an apache server, ngrok, mjpeg streamer and any python dependencies related to twilio.
Twilio:
```bash
pip3 install twilio
```
This will install the python dependency needed for twilio code.

Apache:
```bash
sudo apt install apache2 -y
```
This will install and run an apache server on your raspberry pi whenever your raspberry pi is on. /var/www is going to be the folder in which we drop our HTML files, and we can access the website by simply going on http://localhost. If you wish to access the website from another device on the same network as the pi, you can do so by typing in http://RASPBERRYPINAME.local, in this case it'll be http://streaming.local.

Mjpg-Streamer(setup):
```bash
git clone https://github.com/jacksonliam/mjpg-streamer.git
sudo apt-get install cmake libjpeg8-dev
sudo apt-get install gcc g++
cd mjpg-streamer-experimental
make
sudo make install
```

Ngrok:
```bash
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
unzip ngrok-stable-linux-arm.zip
```

## Setting up the camera
HTML:
You will navigate to the /var/www folder and replace the index.html present there with the one provided in this github, along with the background.png (for aesthetic purposes). Replace the embed in the code with your own embed that you got using the ```bash .ngrok http 8080``` command.
MJPG-Streamer(running):
You will then run this code in a terminal that will be constantly open in the background.
```bash
mkdir /tmp/stream
raspistill --nopreview -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 &
```
The code below will then be ran after, outputting the stream above onto an accessible website which you can embed easily.
```bash
cd mjpg-streamer/mjpg-streamer-experimental
export LD_LIBRARY_PATH=.
./mjpg_streamer -i "input_file.so -f /tmp/stream -n pic.jpg" -o "output_http.so -w ./www"
```
Python:
A python file is supplied in this github, it is responsible for messaging you whenever your door is opened. All you need to do is change the twilio variables with ones you recorded previously during setup (auth token, UID, to and from phone numbers).

## Closing
If you run the python, mjpg streamer and have set up everything correctly (embedding stream into HTML, getting it to work in the first place, and set up twilio variables properly), then you will have a website which can be easily accessed on any device on a local network with ease, showing a constant video stream of what's in front of your door, along with a messaging system that will notify you whenever said door is opened. All you really need to do at this point is physically attach the raspberry pi along with the camera to a door, with a power supply present.
