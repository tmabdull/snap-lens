# SnapLens
Frictionless Translation for social good

## The Team
Taha Abdullah, Computer Science @ UC Davis '24 [[in]](https://www.linkedin.com/in/taha-m-abdullah/) <br>
Yahya Qteishat, Electrical Engineering & Computer Sciences @ UC Berkeley '24 [[in]](https://www.linkedin.com/in/yahyaq/) <br>
Youssef Qteishat, Computer Science @ UC Davis '24 [[in]](https://www.linkedin.com/in/youssef-qteishat/) <br>
Nour Zahzah, Mechanical Engineering @ UC Berkeley '27 [[in]](https://www.linkedin.com/in/nourzahzah/) <br>

## Inspiration
- Struggles of immigrants and refugees navigating language barriers
- Hands-off user experiences offered by commercial smart glasses (Meta glasses, Google Glass, AR, etc.)

## What it does

- Glasses capture a live stream of the user's POV via CAM module attached to glasses frame
- Snapshot triggered on dev GUI
- ESP32 sends POV image to Flask backend hosted on Render (mocked in demo video bc of SSL cert issues)
- Gemini interprets the language and translates into English, and vice versa
- Translated text is displayed in server console and LCD display (WIP)

## How we built it 

Hardware:
- Nour custom modeled and printed the following components: glasses frame with integrated camera housing, LCD display mount

Middleware:
- Youssef and Taha wrote the Python (Flask) middleware server, hosted on Render, that integrates with Gemini for multimodal translation of uploaded image

Electronics:
- Yahya integrated the ESP32-CAM micro-controller with a 2 MP camera and the FTDI USB-to-TTL adapter
- Programmed the ESP32 to capture the image through the camera and pass that as the body of a POST request to the api endpoint. (mocked in the demo bc running into cert issues on ESP32)


## Challenges we ran into

- Getting a snap fit when attaching the camera module to its holder on the frame
- Handling latency when making API calls from ESP32 to Flask Server
- ESP32-CAM doesn't have a usb chip. First tried using the usb chip from a second USB-32 but we didn't have a micro-usb data transfer cable. so we switched to the FTDI approach.
- HTML on ESP32 is a zipped archive thats cut up into a C byte array, very cumbersome to change
- Displaying languages with non-Latin and especially cursive scripts

## Accomplishments that we're proud of

- The quality of the hardware! Nour did an amazing amazing job.
- Establishing a wifi connection between the ESP32 and Flask backend
- Getting live video feed from CAM module
- Hosting Flask servers on Render

## What we learned

- Prompt Engineering
- Integrating an ESP32-CAM micro-controller with an FTDI USB-TTL Adapter
- Designing CAD models in Fusion 360
- 3D printing models


## Refinements
- Triggering image capture and translation from button on the side instead of from a dev GUI on laptop
- Finishing the integration of our LCD screen so we can display the output there isntead of in server console

## What's next for SnapLens
- Integrating a GPS module to get the location to account for differences between standard and colloquial language, updating the user prompt accordingly
- Utilizing a microphone, speaker, and STT/TTS provider to translate a conversation in real-time
- Bigger display and additional buttons for custom user configuration
