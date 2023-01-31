import pandas as pd

creds = pd.read_csv("creds.csv")


def checkPass(inpuser, inppass):
    accept = False
    creds = pd.read_csv("creds.csv")

    is_correct_user = (creds['username'] == inpuser)
    # print(is_correct_user)
    is_correct_pass = (creds['password'] == inppass)
    # print(is_correct_pass)

    for i in range(0, len(creds)):
        if is_correct_user[i]:
            user = True
            break
    else:
        user = False

    for i in range(0, len(creds)):
        if is_correct_pass[i]:
            passw = True
            break
    else:
        passw = False

    if user == True and passw == True:
        accept = True

    return accept


def addUser(userN, userP):
    data = {
        'username': [userN],
        'password': [userP],
    }
    df = pd.DataFrame(data)
    df.to_csv('creds.csv', mode='a', index=False, header=False)
    print("Data appended successfully.")


add = input("Login or Add New User: L/A\n\t")

if add == "L":
    inpuser = input("Enter your username\n\t")
    inppass = input("Enter you password\n\t")
    check = checkPass(inpuser, inppass)
    print(check)
elif add == "A":
    newuser = input("Enter your new username\n\t")
    newpass = input("Enter your new password\n\t")
    addUser(newuser, newpass)

print("-----")
df = pd.read_csv('creds.csv')
print(df.to_string())