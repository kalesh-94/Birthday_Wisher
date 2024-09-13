import pandas as pd #type: ignore
import datetime
import smtplib
import os

os.chdir(r"C:\Users\kales\OneDrive\Desktop\B'day wisher")


# Enter your details
GMAILID = 'drivermike3131@gmail.com'
GPASS = 'ooki uoaw ksms wxty'

def sendemail(to, sub, msg):
    print(f"Email to {to} sent with subject {sub} and message {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAILID, GPASS)
    # Encode the subject and message using UTF-8
    subject = sub.encode('utf-8')
    message = msg.encode('utf-8')
    s.sendmail(GMAILID, to, f"Subject:{subject}\n\n{message}")
    s.quit()

if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")

    today = datetime.datetime.now().strftime("%d-%m")  # Get today's date without the year
    Yearnow = datetime.datetime.now().strftime("%Y")   # Get the current year

    writeInd = []

    for index, item in df.iterrows():
        # Ensure that 'Birthday' is read as datetime
        Bday = item['Birthday'].strftime("%d-%m")
        # Check if today's date matches with the birthday and the year has not been recorded
        if today == Bday and Yearnow not in str(item['Year']):
            sendemail(item['Email'],'Happy Birthday' " " + item['Name']  + " from your friend__Kalesh" , item['Dialogue'])
            writeInd.append(index)

    for i in writeInd:
        yr = df.loc[i, 'Year']
        # Append the current year to the existing years
        df.loc[i, 'Year'] = str(yr) + ', ' + str(Yearnow)

    # Save the updated DataFrame to Excel
    df.to_excel('data.xlsx', index=False)
