import smtplib
mail = smtplib.SMTP("smtp.gmail.com",587)
send = ""
try:
    amount = int(input("How many do you wanna send"))
    if amount < 1 or amount >30:
        raise Exception
    recipients = []
    number = 1
    while (len(recipients) < amount):
        add = (input(f"{number}.)")).strip()
        if add == "enough":
            break
        recipients.append(add)
        number += 1
    sending = input("Enter message\n\n")
    while sending.upper() !="SEND":
        send += sending+"\n"
        sending = input("Enter 'send' to finish")

except Exception as e:
    print("Please try again and enter a valid number because:",e)
    exit()
subjekt = input("Subject")
mail.ehlo()
mail.starttls()
mail.login("mcnalbania@gmail.com","yllcaka1516457")
mail.sendmail("mcnalbania@gmail.com",recipients,f"Subject: {subjekt} \n\n{send}")
mail.quit()
