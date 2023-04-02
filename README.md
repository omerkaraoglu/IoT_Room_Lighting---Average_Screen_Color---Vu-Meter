#AmbiRoom

SUMMARY

The python code gathers pixel data of the screen and calculates the average color.
To make the code run fast yet accurate, it takes screenshots at 72x128 px resolution.
NodeMCU creates a local web server
Python code sends data (average RGB of the pixels) over UDP
NodeMCU reads incoming data and drives the LEDs

IMPORTANT
- Find the IP addresses of your NodeMCU board (local IP, gateway IP, subnet mask, DNS)
- Change the IP addresses in the .ino file with them
- !!! Use IRLZ44 mosfets or TIP122 transistors to drive a common anode LED strip
- 12V 5A power supply is recommended for a 5m strip

FOR VU-METER
- You have to install and configure "VB-Audio Virtual Cable" software --> https://vb-audio.com/Cable/
- Configure as default output, so it transfers output data to a virtual input (necessary for gathering audio with code)
- Check "Listen to this device" box on the CABLE and select your desired listening device
- Don't forget to set the correct bit & sample rates for your devices