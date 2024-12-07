Sri Maruthi Electricals

This repository contains the website for Sri Maruthi Electricals, designed to showcase the company's services, milestones, and more. The website uses Flask for local development to serve static files and test changes before deploying.

Project Structure

Root Directory
app.py: The main Flask application that serves the website locally.
index.html: The main entry point for the website, representing the home page.
contactus.html: The "Contact Us" page for inquiries.
carrer.html: The "Careers" page with job opportunities.
Folders
static/images

Contains all images used across the website, such as logos, banners, and other visuals.
css

CSS Files:
style.css: Global styles for the website.
aboutus.css: Styles for the "About Us" section.
client_company_logo.css: Styles for showcasing client logos.
image_slide.css: Styles for image sliders.
milestone.css: Styles for the milestones section.
our_work.css: Styles for displaying completed projects.
services.css: Styles for the services page.
How to Clone and Run Locally

Step 1: Clone the Repository
To clone the repository to your local system, use:

git clone https://github.com/srimaruthielectricals/srimaruthielectricals.git
Step 2: Set Up Environment
Ensure you have Python 3.x and pip installed.
Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate       # On Linux/Mac
venv\Scripts\activate          # On Windows
Install dependencies:
pip install flask
Step 3: Add app.py
Create a file named app.py in the root directory with the following content:

from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    # Serve the main HTML file (index.html) from the root directory
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    # Serve other files (HTML, CSS, JS, etc.) from the root directory
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True)
Step 4: Run the Application
Run the Flask application:
python app.py
Open your browser and navigate to:
http://127.0.0.1:5000/
Notes

Static Files: All images and CSS files are already organized in their respective folders (static/images and css).
CSS Integration: Ensure all file paths are relative, e.g.:
<link rel="stylesheet" href="css/style.css">
Troubleshooting

CSS/Images Not Loading:
Verify that the file paths in your HTML files match the project structure.
Example for linking a CSS file in index.html:
<link rel="stylesheet" href="css/style.css">
Flask Issues:
Ensure Flask is installed with:
pip install flask
Run the app in a virtual environment for a cleaner setup.
