

# Welcome to Mark-Sheet Grade Producer App

## Table of Contents

+ [Introduction](#introduction)
+ [Purpose](#purpose)
+ [Usage](#usage)
+ [Features](#features)
+ [Prerequisites](#prerequisites)
+ [Installation](#installation)
+ [Error Handling](#error-handling)
+ [Testing](#testing)
+ [Bugs](#bugs)
+ [Validation](#validation)
+ [Credits](#credits)
+ [Technologies Used](#technologies-used)
+ [Languages Used](#language-used)
+ [License](#license)
+ [Deployment](#deployment)
+ [Conclusion](#conclusion)
+ [Contact](#contact)
 
## Introduction

Wellcome to Mark-Sheet Grade Producer Automation App. This tool automates the process of collecting, validating, and recording student marks, calculating total marks and assigning grades based on given criteria.

## Purpose

The Mark-Sheet Automation Program is designed to streamline the management of student marks obtained from the exams. It interacts with Google Sheets to:
- Collect and validate mark data.
- Calculate total marks.
- Assign grades based on the total marks.

## Usage

## Features

- **Data Collection**: Secure and validated collection of student marks obtained by subjects.
- **Mark Calculation**: Automated calculation of total marks.
- **Grade Assignment**: Grades assigned based on predefined criteria.
- **Produces Unique Student IDst**: It produces unique student IDs and maintain throughout the wholw dataset worksheet.
- **Google Sheets Integration**: Seamless interaction with Google Sheets for data storage and retrieval.

## Prerequisites

User of this app need to ensure that they have the following:
- Python 3.6 or later
- Google Cloud project with Sheets API and Drive API enabled
- `creds.json` file for Google Service Account credentials

## Installation

1. **Install required Python packages**:
install the libraries to the python terminal (pip install gspread google-auth)

2. **Set up Google Service Account**:
    - Create a Google Cloud project.
    - Enable Sheets API and Drive API.
    - Create a service account, download the credential file, rename it to `creds.json`  and upload it to the root directory of the github.
    - Share Google Sheets with the service account email with editor access.

3. **Security of Credentials**: add creds file to the .gitignore so that no third party app have access to private information.

4. **Dependencies**: Install dependancie to the terminal (pip3 freeze > requirements.txt) 

## Error Handling

All the functions have been wrapped with error handling mechanisms. During the use of this app, if it face with any unexpected encounter, it will produce an error message rather than chrashing.

## Testing

I have tested the App manually which looked fine with no error found. I checked the App through linter. It successfully submitted to the server and communicate with user. Fields needs to have inputs with seven set of data separated by a comma, data type validates integers and set as minlength in the fileds. 

|  | Test | Result |
|---|:---|---|
| 1 | Implement a given algorithom as a computer program | Pass |
| 2 | Pass through Python Linter eg pep8 | Pass |
| 3 | All intended functionality works as per critical project objectives | Pass |
| 4 | Code meets minimum readability | Pass |
| 5 | Code handles empty or invalid input | Pass |
| 6 | Consistant and effective markdown formatting when writing README file | Pass |
| 7 | Identify and repair coding error| Pass |
| 8 | Basic manual Testing | Pass |
| 9 | Implement the use of external Python Libraries | Pass |
| 10| Use git & Github for version control | Pass |
| 11| Deploy final version Python code to Cloud-based platform | Pass |
| 12| Check for commented out code | Pass |
| 13| Use Exception Error handling | Pass |


## Bugs

This app run through linter which produces no errors. Image is given below.

## Validation

I have manually checked with python code checker linter and found no error

+ Python Validation by [Linter](https://pep8ci.herokuapp.com/)

## Credits

I gained a lot of knowledge from doing the Python programme with [Code Institute](https://learn.codeinstitute.net/)


## Technologies Used

 + GitHub
 + GitPod
 + LMS

## Language Used

This app is built with only with following language.
  + Python


## License

This app can be licensed under any licensing authority for a user or company or corporation.

## Deployment

Here is the step by step process to deploy this app to Heroku.
1. First we need to go to related repository [My Repo](https://github.com/AbdurRahimB/MyPythonProject)
2. Copy the repository link.
3. Login to Heroku.com website
4. Go to Dashboard
5. Create New App
6. Give a name of the App, In this case I named as "Mark Sheet Grade Producer App"
7. Choose a region, In this case, I chose, Europe
8. Go to Settings
9. Add config Var
10. In this case add CREDS as key and paste in the value in the value
11. Add PORT as key and 8000 as value
12. Add Buildspacks
13. Add Python
14. Add nodejs
15. Go to Deploy tab
16. Select Github deployment method
17. Search my depository from the github and select and connect it.
18. Deploy Manually
19. Open the 'view link' to see into the terminal.
20. Deployed and operating successfully

## Conclusion


