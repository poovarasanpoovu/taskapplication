import mysql.connector
import taskapp
import time
import admintaskapp
from datetime import datetime

NEGATIVE = "\033[7m"
RESET = '\033[0m'
BOLD = "\033[1m"
ITALIC = "\033[3m"
YELLOW = "\033[1;33m"
RED = '\033[91m'
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
smile_emoji = '\U0001F60A'
verify_emoji = '\U0001F914'
success_emoji = '\U0001F60E'
thanks_emoji = '\U0001F64F'
hand_emoji = '\U0001F44D'
heart_emoji = '\U00002764'
smile_mouth = '\U0001F603'

WRONG = "\u274C"
RIGHT = "\u2705"

cat_art = r'''
 /\_/\  
( o.o ) 
 > ^ <
'''

database_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythondb"
)
cursors = database_connection.cursor()
def table_creation():

    table_create = '''
    CREATE TABLE IF NOT EXISTS taskapptable(
      user_id INT PRIMARY KEY AUTO_INCREMENT,
      user_name VARCHAR(30),
      user_password VARCHAR(30)
      user_date DATE
    )'''
    cursors.execute(table_create)
#table_creation()
username = ''
passkey = ''
name = ''
password = ''
def insert_table(name,password):
        detail_query = "SELECT user_name,user_password FROM taskapptable WHERE user_name = %s AND user_password = %s"
        cursors.execute(detail_query, (name, password))
        result = cursors.fetchall()
        if result:
            print("")
            print(NEGATIVE, "Already Available? Please try again!!!", RESET, WRONG)
            time.sleep(1)
            user_enter()
        else:
            insert_query = "INSERT INTO taskapptable (user_name,user_password,user_date) VALUES (%s, %s, %s)"
            date = datetime.now()
            cur_date = date.strftime("%Y-%m-%d")
            insert_item = (name,password,cur_date)
            cursors.execute(insert_query,insert_item)
            database_connection.commit()
            print(BOLD,ITALIC,"\nAccount Successfully Created!!!",RESET,RIGHT,success_emoji,"\n")
            time.sleep(2)
            number=int(input(f"{BOLD}{ITALIC}If would you like to Signing Up now? Press (1) (or) Exit (2){RESET} {smile_emoji}:  "))
            if number == 1:
               checking_table(name,password)
            elif number == 2:
               print(f"\n{BOLD}{ITALIC}Thanks for using our Application {RED+name}{RESET}{thanks_emoji}")
            else:
               print(NEGATIVE,"Choose Correct Number!!! Your sign out",RESET,hand_emoji)
        cursors.close()
        database_connection.close()


#insert_table(name,password)


def checking_table(name,passkey):
      detail_query = "SELECT user_name,user_password FROM taskapptable WHERE user_name = %s AND user_password = %s"
      cursors.execute(detail_query,(name,passkey))
      result = cursors.fetchall()
      if result:
        if name == "Tom" and passkey == "Welcome@123$":
          print(NEGATIVE, "User_name or Password wrong,Please try again!!!", RESET,WRONG)
          time.sleep(2)
          user_enter()
        else:
            taskapp.main(name)
      else:
          print(NEGATIVE,"User_name or Password wrong,Please try again!!!",RESET,WRONG)
          time.sleep(2)
          user_enter()
      cursors.close()
      database_connection.close()


def user_enter():
   print(BOLD,ITALIC,BLUE)
   print("1.Create an account")
   print("2.Sign Up ")
   print("3. Admin Portal",RESET)
   start = time.time()
   while True:
       if time.time() - start > 5:
          print("Timeout reached. Program stopped.")
          break
       try:
          print(PURPLE)
          choose = int(input("Enter The Option (1/2/3) : "))
          print(RESET)
       except Exception:
           print(f"\n{RESET+NEGATIVE}Only Numeric!!!{RESET+WRONG}")
           time.sleep(1)
       else:
         if choose == 1:
          print(BOLD,ITALIC,YELLOW)
          name = input("Name : ")
          password = input("Create password : ")
          print(RESET)
          insert_table(name,password)
         elif choose == 2:
           print(BOLD,ITALIC,YELLOW)
           username=input("Name : ")
           passkey = input("Password : ")
           print(RESET)
           checking_table(username,passkey)
         elif choose==3:
             print(BOLD, ITALIC, YELLOW)
             admin_name = input("Admin_Name : ")
             admin_pass = input("Admin_Password : ")
             print(RESET)
             admintaskapp.admin_portal(admin_name,admin_pass)
         else:
             print(NEGATIVE, "''If would like to continue this task please choose (1 To 3) numbers!!!''",RESET)
             time.sleep(1)
             user_enter()


user_enter()

def show_table():
    cursors.execute("SELECT * FROM taskapptable")
    result=cursors.fetchall()
    for i in result:
        print(i)
    cursors.close()
    database_connection.close()

#show_table()