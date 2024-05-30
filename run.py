import gspread
from google.oauth2.service_account import Credentials
import uuid

# Define the scope and credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

try:
    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('mark_sheet')
except Exception as e:
    print(f"Failed to initialize Google Sheets client: {e}")
    exit(1)


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
        int_values = [int(value) for value in values]
        if len(int_values) != 7:
            raise ValueError(
                f"Exactly 7 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def generate_student_id():
    """
    Generate a unique student ID.
    """
    # Shorten the UUID for simplicity
    return str(uuid.uuid4())[:8]


def update_mark_worksheet(data):
    """
    Update mark worksheet, add new row with the list data provided
    """
    try:
        print("Updating mark worksheet...\n")
        mark_worksheet = SHEET.worksheet("mark")
        mark_worksheet.append_row(data)
        print("Mark worksheet updated successfully.\n")
    except Exception as e:
        print(f"Failed to update mark worksheet: {e}")


def calculate_and_update_total_marks():
    """
    Calculate the total marks for each student and update the result worksheet
    """
    try:
        print("Updating Result worksheet...\n")
        mark_worksheet = SHEET.worksheet("mark")
        result_worksheet = SHEET.worksheet("result")

        marks = mark_worksheet.get_all_values()
        # Get existing student IDs
        existing_results = result_worksheet.col_values(1)
        results = []

        for row in marks[1:]:  # Skip the header row
            student_id = row[0]
            # Check if the result already exists
            if student_id not in existing_results:
                total = sum(
                    int(mark) for mark in row[1:] if mark.strip() != '')
                results.append([student_id, total])

        for result in results:
            result_worksheet.append_row(result)
        print("Result worksheet updated successfully.\n")
    except Exception as e:
        print(f"Failed to update result worksheet: {e}")


def assign_grades():
    """
    Assign grades based on the total marks and update the grade worksheet
    """
    try:
        print("Updating Grades worksheet...\n")
        result_worksheet = SHEET.worksheet("result")
        grade_worksheet = SHEET.worksheet("grade")

        results = result_worksheet.get_all_values()
        # Get existing student IDs
        existing_grades = grade_worksheet.col_values(1)
        grades = []

        for row in results[1:]:  # Skip the header row
            student_id = row[0]
            # Check if the grade already exists
            if student_id not in existing_grades:
                total = int(row[1])
                if 651 <= total <= 700:
                    grade = "A+"
                elif 601 <= total <= 650:
                    grade = "A"
                elif 551 <= total <= 600:
                    grade = "A-"
                elif 501 <= total <= 550:
                    grade = "B"
                elif 451 <= total <= 500:
                    grade = "C"
                elif 401 <= total <= 450:
                    grade = "D"
                elif total <= 400:
                    grade = "F"
                grades.append([student_id, grade])

        for grade in grades:
            grade_worksheet.append_row(grade)

        print("Grade worksheet updated successfully.\n")
    except Exception as e:
        print(f"Failed to update grade worksheet: {e}")


def main():
    """
    Run all program functions.
    """
    try:
        data = get_mark_data()
        mark_data = [int(num) for num in data]
        student_id = generate_student_id()
        mark_data_with_id = [student_id] + mark_data
        update_mark_worksheet(mark_data_with_id)

        calculate_and_update_total_marks()
        assign_grades()
    except Exception as e:
        print(f"An error occurred: {e}")


print("Welcome to the Mark Sheet Automation Program.\n")
main()
