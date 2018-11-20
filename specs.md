# The One_Minute_Pitch API Specification

Last modified: 19th November 2018

Version: **1.0 **

I have tried my best to make the specification easy to read and implement, so if you come across any inconsistencies or experience any difficulty, do let me know by sending an email here, or by reporting an issue in the specification repo.

Table of Contents
- Introduction
- System Overview
- Usage
- Future Directions and Open - Questions

# 1. Introduction
## 1.1. Scope

This document describes an interactive app whereby users can share on their creative pitches

## 1.2. Goals

As a user, I would like to see the pitches other people have posted.

* Users should be signed in for me to leave a comment
* Users should receive a welcoming email once I sign up.
* Users should the pitches created on their profile page.
* Users should see comments on the different pitches and leave feedback
*Users can view the different categories.

# 2. System overview
1. Fair/Good internet connection.
2. Before Running this Project
  i. run  > pip install -r requirements.txt.


  Steps
1. Clone or download the Repo
2. Create a virtual environment
3. Read the specs and requirements files and Install all the requirements.
4. Edit the start.sh file with your email account and password
6. Run chmod a+x start.py
7. Run ./start.py
8. Access the application through `localhost:5000`
  **You can also choose to use the live link**

## 2.1 How the system works
The following are the steps on how The News Web app works, (This is an error-free case.)

   - Fetching data:
       Data is fetched from the user

  - Processing data:
        Data is stored in the Postgres database
  - Displaying data:
        Data is displayed using html templates


## 2.2. Usage

Minimum Requirements(if working on a local environment)
1. Fair/Good internet connection.
2. Before Running this Project
  i. run  > pip install -r requirements.txt.


  Steps
1. Clone or download the Repo
2. Create a virtual environment
3. Read the specs and requirements files and Install all the requirements.
4. Edit the start.sh file with your email account and password
6. Run chmod a+x start.py
7. Run ./start.py
8. Access the application through `localhost:5000`
  **You can also choose to use the live link**
### Disclaimer

The data contained is not filtered by contents, hence the news app won't be responsible for any rude or unfriendly wordings or images.

### Compatibility issues

The app is works as expected across all platforms, incase you face any compatibility issue feel free to reach out.

## 2.3. Future Directions and Open Questions

In the discussion of future directions and open questions, it is important to remember that The News app has been designed to allow a large amount of flexibility for many different future use cases. This is because it is implemented using an approved Python(FLASK) app structure. Any suggestions and changes are welcomed