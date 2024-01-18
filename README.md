# Pixel Art Generator

The Pixel Art Generator is a Python application that utilizes Tkinter and OpenCV to convert images into pixel art. The primary functionality of the application involves automatically separating an image into pixel blocks and assigning dominant colors to each block. The project leverages the capabilities of Raspberry Pi for image processing.

## Features

- Upload an image and convert it into pixel art.
- Automatic pixelation using OpenCV.
- Customize block sizes for pixelation.

## Requirements

- Python 3.x
- Tkinter
- Pillow
- OpenCV
- NumPy

## Installation

1. **Install Required Packages:**
    ```bash
    pip install pillow numpy opencv-python
    ```

2. **Clone the Project:**
    ```bash
    git clone https://github.com/yourusername/pixel-art-generator.git
    cd pixel-art-generator
    ```

3. **Run the Application:**
    ```bash
    python pixel_art_generator.py
    ```

## Usage

1. Click the "YÜKLE" (UPLOAD) button to upload an image.
2. Click the "HAZIRLA" (PREPARE) button to process the image and display the pixel art.

## Customization

- Adjust block sizes in the code to achieve different levels of pixelation.
- Explore and modify color mapping options based on your preferences.

## Contribution

If you want to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push your branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Thanks to the contributors and libraries used in this project.
