#Python Birthday Wisher 
Overview
Python Birthday Wisher is a Python script designed to automate sending birthday wishes via email. It reads birthdays from an Excel file and sends personalized greetings to contacts on their birthdays.

Features
Automated Emails: Sends birthday wishes via Gmail.
Excel Integration: Reads and updates birthday information from an Excel file.
Customizable Messages: Personalize messages and subjects for each contact.
Installation
Clone the Repository:

git clone https://github.com/yourusername/Python_Birthday_Wisher.git
Navigate to the Project Directory:

cd Python_Birthday_Wisher
Install Dependencies:
Make sure you have pandas installed:

pip install pandas
Configuration
Set Up Email Credentials:
Update the GMAILID and GPASS variables in the script with your Gmail address and app password.

Update the File Path:
Ensure data.xlsx is located at the specified path: C:\Users\kales\OneDrive\Desktop\B'day wisher.

Prepare Your Excel File:

Format: Must include columns Birthday, Email, Name, Dialogue, and Year.
Birthday Column: Dates should be in datetime format.
Usage
Run the Script:

python main.py
Script Operation:

Reads data.xlsx to check for today’s birthdays.
Sends a birthday email if today matches the contact’s birthday and the year is not yet recorded.
Updates the Excel file to include the current year.
