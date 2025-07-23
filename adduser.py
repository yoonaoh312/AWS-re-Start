"""
Your module description
"""
import os

def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input('enter the name of the user to add').upper()
        print('use the username'+username+"?"+'(Y/N)')
        confirm=input().upper()
        print(confirm)
    os.system('sudo adduser'+username)
    
new_user()
    