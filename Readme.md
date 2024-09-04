# One week to learn FAST API 

## Purpose

    Learn web development with FastAPI in one week.
    During this program, I will share my progress and everything I learn every day

## Python

### Virtual Environment

    First of all, the traditional approch is to isolate the Python application in a virtual environment, to avoice global package installation conflits. By this way, your application dependencies can be accessed within your virtual environment. To create a virtual environment, enter your application folder and run this command:

        `python3 -m venv .env`

    To activate the virtual environment, run this command:

    (MacOS & Linux): `source .env/bin/activate`

    (Windows): `.\.env\Scripts\activate`

    And to deactivate it, run `deactivate`

    To enable the virtual environment install your application dependencies, create `requirements.txt` file and write all your package there. For the installation, run the following command:

        `pip3 install -r requirements.txt`

### FastAPI

    To install FastAPI, add it on your requirements.txt file. After that, activate your virtual env and run the installation of your requirements packages. Then, run this command

        `pip install fastapi uvicorn`