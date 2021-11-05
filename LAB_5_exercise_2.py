def is_email(e_mail):
    e_mail =input("Enter an e-mail= ")
    if e_mail.__contains__("@") and e_mail.__contains__("."):
        print("Your e-mail is correct.")
    else:
        print("Your e-mail is incorrect.")

is_email("e_mail")