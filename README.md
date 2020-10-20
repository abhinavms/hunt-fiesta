# Hunt Fiesta
Hunt Fiesta is an online hunt app built on Django.

Features : 
- There is a superuser account. Only the superuser can grant or revoke other admin rights.
- Currently user registration can only be done using admin. This is done because this was a closed event.
- Admin interface for all user details, level and question upload.
- Logs for answer tries, with user details and IP address.
- Question can be of image, text, link or even a hidden HTML block.
- Passwords are encrypted in the database.

Technical Specs:
- Bootstrap 4.5
- Django 3.1
- Rest of the packages used can be found in `requirements.txt`

# How to Setup
- Clone the repo
- Run pip install -r requirements.txt
- Run python manage.py runserver

# To Do
1. Using Facebook and Google OAuth instead of storing passwords
2. Add leaderboard
3. Add option to shuffle questions

# Known Issue
None as of now. Feel free to open an issue if any !