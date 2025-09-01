# The AI Medical Consultant Bot

## Sagicious is a smart AI-powered medical assistant built with Flask.
It provides quick, reliable, and user-friendly 
answers to health-related queries — designed to bridge 
the gap between users and instant medical guidance.

## Disclaimer: Sagicious is not a substitute for a professional doctor’s diagnosis. 
Always consult a certified medical practitioner for serious health concerns.

# Features

## AI Q&A: Ask medical questions, get instant answers.

## Flask Backend: Lightweight and scalable backend powered by Flask.

## Cross-Platform: Compatible with web frontends and mobile apps.

## Secure Sessions: Uses Flask-Login for secure user handling.

## Fast & Reliable: Deployed on Render with Gunicorn for production.

# Tech Stack

## Backend: Flask, Flask-CORS, Flask-Login, Flask-SQLAlchemy

## Frontend: (HTML/CSS/JS or React — depending on setup)

## Server: Gunicorn (production WSGI server)

## Deployment: Render


# Installation (Local Dev)

##Clone the repo:

###git clone https://github.com/DANKIEIN117/Medical_Bot.git
###cd Medical_Bot


##Create a virtual environment & activate:

###python -m venv venv
###source venv/bin/activate   # Linux/Mac
###venv\Scripts\activate      # Windows


##Install dependencies:

###pip install -r requirements.txt


###Run Flask dev server:

###python AI.py

# Deployment (Render)

##Render automatically installs requirements and runs:

###gunicorn AI:app


##After deployment, your app will be live at:

###https://medical-bot-2-frc5.onrender.com

#Contributing

##Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

#License

##This project is licensed under the MIT License.

#Sagicious – Your trusted AI medical companion, just a question away!
