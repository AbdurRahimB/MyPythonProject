import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('mark_sheet')


def get_mark_data():
    """
    Get Mark figures input from the user.
    """
    print("Please enter Mark data.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 90,80,95,80,70,30\n")

    data_str = input("Enter your Mark here: ")
    print(f"The data provided is {data_str}")


get_mark_data()