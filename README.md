# OpenCV Basic Scripts

This repository contains a collection of basic Python scripts demonstrating fundamental image processing and computer vision techniques using OpenCV. These scripts cover topics such as image manipulation, webcam capture, drawing shapes, color detection, and corner detection.

## Prerequisites

- Python 3.x
- OpenCV (cv2) library
- NumPy library

### Installation

Install the required libraries using pip:

```bash
pip install opencv-python numpy
```

## Scripts Overview

### basic1.py
Loads an image (`image.png`), resizes it to half the original size, rotates it 90 degrees clockwise, saves the modified image as `modified_image.jpeg`, and displays it in a window.

<img width="529" height="260" alt="Screenshot 2025-11-03 195707" src="https://github.com/user-attachments/assets/3c96edff-af2b-4989-9ee0-e97e03e0848a" />

**Usage:**
```bash
python basic1.py
```
- Press any key to close the window.

### basic2.py
Loads an image (`image.png`) and modifies the first 100 rows by setting random RGB values for each pixel, then displays the modified image.

<img width="519" height="357" alt="Screenshot 2025-11-03 195739" src="https://github.com/user-attachments/assets/b4ee372a-0124-4625-97f8-b50917cc18b1" />


**Usage:**
```bash
python basic2.py
```
- Press any key to close the window.

### basic3.py
Captures video from the default webcam (index 0) and creates a composite image by placing rotated smaller versions of the frame in different quadrants, then displays the result in real-time.

<img width="716" height="500" alt="Screenshot 2025-11-03 195812" src="https://github.com/user-attachments/assets/7e2c69fc-2ad9-4c61-8567-8ea235bfd03b" />


**Usage:**
```bash
python basic3.py
```
- Press 'q' to quit the video capture.

### basic4.py
Captures video from the default webcam and draws various shapes (lines, rectangle, circle) and text on each frame, displaying the annotated video in real-time.

<img width="713" height="517" alt="Screenshot 2025-11-03 195843" src="https://github.com/user-attachments/assets/fd2e1b48-874b-4577-917e-bbeef290eaea" />

**Usage:**
```bash
python basic4.py
```
- Press 'q' to quit the video capture.

### basic5.py
Captures video from the default webcam, converts frames to HSV color space, applies a mask to detect blue colors, and displays both the mask and the masked result.

<img width="548" height="612" alt="Screenshot 2025-11-03 195905" src="https://github.com/user-attachments/assets/b3f26656-8508-457c-9a08-e7639c69d415" />

**Usage:**
```bash
python basic5.py
```
- Press 'q' to quit the video capture.

### basic6.py
Loads an image (`image.png`), resizes it to half the size, detects up to 10 corners using the Shi-Tomasi corner detection algorithm, draws circles on the detected corners, connects them with random colored lines, saves the result as `corner_detection_andline.png`, and displays it.

<img width="618" height="536" alt="Screenshot 2025-11-03 195919" src="https://github.com/user-attachments/assets/5607f4fd-fbbb-4287-be51-4f5bdee68817" />

**Usage:**
```bash
python basic6.py
```
- Press any key to close the window.
- The detected corners are also printed to the console.

## Notes

- Ensure that `image.png` is present in the same directory for scripts that require it.
- Webcam access is required for video capture scripts (basic3.py, basic4.py, basic5.py).
- Output images (`modified_image.jpeg`, `corner_detection_andline.png`) will be saved in the current directory.
- These scripts are for educational purposes and demonstrate basic OpenCV functionalities.

## Dependencies

- opencv-python
- numpy

No additional setup is required beyond installing the prerequisites.
