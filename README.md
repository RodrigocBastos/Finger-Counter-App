<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS --> <!-- *** Replace "yourusername" with your GitHub username and "your-repo" with your repository name. *** Reference style links allow for neat code. -->



The Finger Counter App is a Python script that detects how many fingers are held up in front of a webcam in real-time. It utilizes the powerful hand tracking capabilities of MediaPipe and processes video frames using OpenCV.

This application can serve as a foundational project for gesture recognition, sign language interpretation, or interactive games that require hand gesture inputs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
🛠 Built With
The project is built using the following technologies:

<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- GETTING STARTED -->
🚀 Getting Started
To get a local copy up and running, follow these simple steps.

📎 Prerequisites
Python 3.6 or higher
A webcam connected to your computer
💾 Installation
Clone the Repository

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/Finger-counter-App.py
   ```
3. Install NPM packages
   ```sh
   npm install
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

A window displaying the webcam feed will open.
Ensure your hand is within the camera frame for detection.
The number of fingers detected as "up" will be displayed on the screen.
Press the 'q' key to exit the program.
<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- HOW IT WORKS -->
🧠 How It Works
The application uses MediaPipe Hands to detect and track hand landmarks in real-time. By analyzing the positions of these landmarks, the script determines which fingers are raised.

Thumb Detection: The script checks the relative position of the thumb tip to determine if it's extended.
Other Fingers: For each finger, it compares the vertical positions of the fingertip and the joint two points below it.
