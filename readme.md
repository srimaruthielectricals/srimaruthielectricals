# Startup Venture

## Project Overview
Startup Venture is a web application designed to promote entrepreneurial ideas and projects, focusing on engaging users through informative articles and project showcases. The application features a clean and user-friendly interface for navigating content related to entrepreneurship.

## Folder Structure

startup-venture/
├── static/                          # Folder for static assets
│   ├── css/                         # CSS stylesheets
│   │   └── style.css                # Main CSS stylesheet
│   └── images/                      # Folder for image assets
│
├── templates/                       # Folder for HTML templates
│   ├── article/                     # Articles section
│   │   ├── article_list.html        # List of articles
│   │   ├── early_exposure_entrepreneurship.html  # Article on 
│   │   └── Preparing_for_first_pitch.html        # Article on 
│   |
|   |
|   |── projects/                    # Projects section
│   |   ├── Eco-friendly_planter.html            
│   |   ├── Generational_Collaboration.html               
│   |      
│   |
|   |────────|──aboutus.html  # About Us page
|            ├── base.html    # Base template for other pages
|            ├── home.html    # Home page
|            ├── career.html
|            ├── contactus.html
|            ├── loginpage.html
|
├── venv/                         # Virtual environment folder
│
├── app.py                           # Main application file
│
└── readme.md                        # Project documentation file


## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd startup-venture

   python -m venv venv  #Create a virtual environment

   source venv/bin/activate  #Activate the virtual environment

   pip install -r requirements.txt #Install dependencies

   python app.py  #Run the application





