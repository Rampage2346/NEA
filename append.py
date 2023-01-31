import pandas as pd

userN = "wee"
userP = "woo"

# data of new user
data = {
    'username': [userN],
    'password': [userP],
}

# Make data frame of above data
df = pd.DataFrame(data)

# append data frame to CSV file
df.to_csv('creds.csv', mode='a', index=False, header=False)

# print message
print("Data appended successfully.")
