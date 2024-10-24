# PanoGen: Panorama Maker

PanoGen is a user-friendly web application that allows you to easily create stunning panoramic images by stitching multiple photos together. Built with Streamlit and OpenCV, this app provides a simple interface for uploading images, generating panoramas, and downloading the final result.

## Features

- **Image Upload**: Upload multiple images in JPG, PNG, or JPEG formats from your local device.
- **Panorama Generation**: Automatically stitch your uploaded images into a seamless panoramic view.
- **Download Option**: Download the generated panorama as a high-quality JPEG image.
- **Responsive Design**: Optimized layout for both desktop and mobile devices.

## Technologies Used

- **Python**: The primary programming language used for building the application.
- **Streamlit**: A powerful framework for building web applications easily.
- **OpenCV**: A library for computer vision tasks, specifically used for stitching images.
- **NumPy**: A library for numerical operations in Python.
- **Pillow**: A library for image processing and handling.

### How to Use PanoGen Locally

Follow these simple steps to get SNAPnFIX up and running on your local machine:

1. **Clone the Repository**  
   Start by cloning the SNAPnFIX repository (you'll need to have Git installed):
   ```bash
   git clone <https://github.com/GeeteshPaidi/PanoGen.git>
2. **Install the Dependencies**   
   Install the required Python packages listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
3. **Run the Application**   
   Once everything is set up, you can run the Streamlit app:
   ```bash
   streamlit run app.py
4. **Access the App**     
   After running the command, your browser should automatically open the SNAPnFIX app. If not, visit the local URL provided in the terminal (usually `http://localhost:8501`).
