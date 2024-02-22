# Face Detection Script

This script is designed to process images in a specified folder, detect faces using OpenCV's Haar Cascades, and then save the processed images with detected faces highlighted by rectangles of different colors. It's written in Python 3.10 and utilizes the OpenCV library for image processing.

## Setup and Installation

Before running the script, ensure you have Python 3.10 or newer installed on your system. You will also need to install the required Python packages:

    pip install -r requirements.txt

To generate a new `requirements.txt` file based on the current project's dependencies, use:

    pip install pipreqs
    pipreqs . --force

## How to Use

1. **Prepare Your Images**: Place all the images you want to process in a folder named `work_images` located in the same directory as the script. The script currently supports `.jpg` images.

2. **Run the Script**: Simply execute the script with Python. It will automatically create a new folder named `computed_images` in the script's directory to store the processed images. Within this folder, images are saved in a subfolder named with the current date and time to avoid overwriting previous results.

3. **View Results**: After the script finishes processing, check the `computed_images` directory for the output. Each image will have faces highlighted with rectangles in various colors.

## Features

- **Multiple Haar Cascades**: The script uses a variety of Haar Cascades to improve face detection, including cascades for frontal faces, eyes with glasses, profile faces, and upper bodies.

- **Dynamic Folder Creation**: Processed images are saved in a dynamically created folder based on the current date and time, making it easy to organize and find results.

- **Color-Coded Detection**: Each type of detected object (e.g., faces, eyes) can be highlighted with a different color rectangle for easy identification.

## Customization

- **Screen Resolution**: The default screen resolution for displaying images is set to 1920x1080. This can be adjusted in the script to match your screen size for any display functionality you might add.

- **Output Folder**: You can change the `output_folder` path in the script to save the results in a different location.

- **Haar Cascades**: It's possible to add or remove Haar Cascade files from the `cascades_paths` list to customize the detection process. Ensure any added cascades are available in your OpenCV installation's `data/haarcascades` directory.

## Note

The script includes commented-out code for resizing and displaying the processed images with OpenCV's `imshow` function. This can be enabled by removing the comments and adjusting as necessary for your display preferences.

## Dependencies

- OpenCV (cv2)
- os
- datetime

Ensure all dependencies are installed using the `requirements.txt` file as mentioned in the setup section.

## Disclaimer

This script is for educational and development purposes. Accuracy and performance may vary based on the images processed and the Haar Cascades used.