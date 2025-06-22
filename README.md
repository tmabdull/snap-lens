# snap-lens
Frictionless Translation for social good

## Inspiration

- Struggles of immigrants and refugees navigating language barriers
- Hands-off user experiences offered by commercial smart glasses (Meta glasses, Google Glass, AR, etc.)

## What it does

- Captures a snapshot of a live video feed via CAM module attached to glasses frame
- Sends image to Flask backend via API call
- Gemini interprets the language and translates into English, and vice versa
- Translated text is sent back to ESP32 microcontroller and displayed on LCD

## How we built it

- 3D printed frame, CAM module holder, LCD mount

## Challenges we ran into

- Getting a snap fit when attaching the camera module to its holder on the frame
- Handling latency when making API calls from ESP32 to Flask Server
- Displaying languages with non-Latin and especially cursive scripts

## Accomplishments that we're proud of

- Establishing a wifi connection between the ESP32 and Flask backend
- Getting live video feed from CAM module
- Hosting Flask servers on Render

## What we learned

- Prompt Engineering
- Programming an ESP32 microcontroller
- Designing CAD models in Fusion 360
- 3D printing models

## What's next for SnapLens

- Integrating a GPS module to get the location to account for differences between standard and colloquial language, updating the user prompt accordingly
- Utilizing a microphone, speaker, and STT/TTS provider to translate a conversation in real-time
- Bigger display and additional buttons for custom user configuration
