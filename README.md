# Image Editor

This image editing application consists of two key components: a graphical user interface (GUI) for single-image editing and a text-based interface for batch processing multiple images at once.

## Prerequisites

To use this application, ensure you have the following dependencies installed:

- **Python 2**
- **Pillow (Python Imaging Library)**: Install using the following command:
  ```sh
  pip install pillow
  ```
- **Pytesseract (OCR tool)**: Install with:
  ```sh
  pip install pytesseract
  ```

Additionally, you must download and place the **Tesseract-OCR** database in `C:\Program Files (x86)`. This repository includes the necessary files. Once installed, you must either set the Tesseract-OCR path as an environment variable or include the following line in your script:

```python
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
```

## Features & Functionality

### GUI Mode

The graphical interface provides an intuitive way to edit individual images. Upon launching the application, the following window appears:

![image](https://github.com/user-attachments/assets/dde3bad4-a408-403b-9fe9-d2ef0438e4bd)



For example, applying the **Gray** effect results in:

![image](https://github.com/user-attachments/assets/940b00bf-6979-47ac-9fc6-cb25bee6105d)


The application also supports Optical Character Recognition (OCR), allowing text extraction from images with recognizable fonts.

### Batch Processing Mode

The text-based interface enables efficient batch processing of multiple images without requiring user interaction. For example here you choose the folder with the images:
![image](https://github.com/user-attachments/assets/bdc30c75-135b-4fba-bb32-26454ba4ac39)

**After Processing and Selecting Blur All Images:**

![image](https://github.com/user-attachments/assets/39c6e8ab-b085-406c-90af-974c592e8e70)


## Acknowledgements

Some parts of this project were inspired by solutions found on Stack Overflow, although the exact references are not recalled. Contributions from the open-source community have also played a significant role in refining this tool.

This application aims to simplify image editing, whether for individual or bulk modifications, with a user-friendly approach and powerful processing capabilities.

