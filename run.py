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

    data_str = input("Enter your data here: ")
    mark_data = data_str.split(",")
    validate_data(mark_data)


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 7 values.
    """
    try:
        if len(values) != 7:
            raise ValueError(
                f"Exactly 7 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


get_mark_data()
