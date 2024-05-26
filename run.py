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
    Get mark figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 7 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter Mark data.")
        print("Data should be seven numbers, separated by commas.")
        print("Example: 90,80,95,80,70,30,76\n")

        data_str = input("Enter your data here: ")

        mark_data = data_str.split(",")

        if validate_data(mark_data):
            print("Data is valid!")
            break

    return mark_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 7 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 7:
            raise ValueError(
                f"Exactly 7 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_mark_worksheet(data):
    """
    Update mark worksheet, add new row with the list data provided
    """
    print("Updating mark worksheet...\n")
    mark_worksheet = SHEET.worksheet("mark")
    mark_worksheet.append_row(data)
    print("Mark worksheet updated successfully.\n")


def calculate_and_update_total_marks():
    """
    Calculate the total marks for each student and update the result worksheet
    """
    mark_worksheet = SHEET.worksheet("mark")
    result_worksheet = SHEET.worksheet("result")    

    marks = mark_worksheet.get_all_values()
    results = []

    for row in marks[1:]:  # Skip the header row
        total = sum(int(mark) for mark in row)
        results.append([total])
        

    for result in results:
        result_worksheet.append_row(result)
       



def calculate_and_update_total_marks():
    """
    Calculate the total marks for each student and update the result worksheet
    """
    mark_worksheet = SHEET.worksheet("mark")
    result_worksheet = SHEET.worksheet("result")

    print("Updating Result worksheet...\n")
    marks = mark_worksheet.get_all_values()
    results = []
    

    for row in marks[1:]:  # Skip the header row
        total = sum(int(mark) for mark in row if mark.strip() != '')
        results.append([total])

    for result in results:
        result_worksheet.append_row(result)
        
    print("Result worksheet updated successfully.\n")


def assign_grades():
    """
    Assign grades based on the total marks and update the grade worksheet
    """
    print("Updating Grades worksheet...\n")
    result_worksheet = SHEET.worksheet("result")
    grade_worksheet = SHEET.worksheet("grade")

    results = result_worksheet.get_all_values()
    grades = []

    for row in results[1:]:  # Skip the header row
        total = int(row[0])
        if total >= 651 <=700:
            grade = "A+"
        elif total >= 651 <=700:
            grade = "A"
        elif total >= 601 <= 650:
            grade = "A-"
        elif total >= 551 <= 600:
            grade = "B"
        elif total >= 501 <= 550:
            grade = "C"
        elif total >= 651 <=700:
            grade = "D"
        elif total >= 500 <=650:
            grade = "E"
        else:
            grade = "F"
        grades.append([grade])

    for grade in grades:
        grade_worksheet.append_row(grade)

    print("Grade worksheet updated successfully.\n")

def main():
    """
    Run all program functions.
    """
    data = get_mark_data()
    mark_data = [int(num) for num in data]
    update_mark_worksheet(mark_data)

    calculate_and_update_total_marks()

    assign_grades()

print("Welcome to the Mark Sheet Automation Program.\n")
main()