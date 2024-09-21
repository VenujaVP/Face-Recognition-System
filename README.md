# Face Recognition System

## Overview

#### This project includes two main functions:
- #####  *Register a New Member*
    + ##### Allows you to add a new member by capturing their face and saving their details.
- #####   *Recognize and Identify Faces*
    + ##### Detect and identify faces using a webcam. Some people's face details have already been added to the system, so it is ready to recognize these faces.

## File Structure
##### The project folder contains the following files and directories:

- *members/*: Directory where member folders are stored. Each folder contains:
  - details.txt: Text file with member's details.
  - face_encoding.pkl: File with the member's face encoding.
- *register_new_member.py*: Script for registering a new member.
- *recognize_faces.py*: Script for recognizing and identifying faces.

## Installation
1. Clone this repository
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
2. Install the required libraries
   ```bash
   pip install opencv-python face_recognition
   ```
3. Navigate to the project directory
   ```bash
   cd face-recognition-project
   ```
## Usage
##### 1.  Registering New Members
1. Run the register_new_member.py script
   ```bash
   python register_new_member.py
   ```
2. Enter the required details (name, age, ID number) when prompted.
3.  Press 'q' to capture the face.

##### 1.  Recognize and Identify Faces
1. Run the recognize_faces.py script
   ```bash
   python recognize_faces.py
   ```
2. Press 'q' to stop the face detection.
## Contributing
- Feel free to contribute to this project by submitting issues or pull requests.
