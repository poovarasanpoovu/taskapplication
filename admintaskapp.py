import mysql.connector
import time
from tabulate import tabulate

NEGATIVE = "\033[7m"
RESET = '\033[0m'
BOLD = "\033[1m"
ITALIC = "\033[3m"
YELLOW = "\033[1;33m"
RED = '\033[91m'
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"

smile_emoji='\U0001F60A'
verify_emoji ='\U0001F914'
success_emoji='\U0001F60E'
thanks_emoji='\U0001F64F'
hand_emoji='\U0001F44D'
heart_emoji='\U00002764'
smile_mouth='\U0001F603'

cat_art = r'''
 /\_/\  
( o.o ) 
 > ^ <
'''

db_connect=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythondb"
)

cursorss=db_connect.cursor()

def admin_portal(admin_name,admin_pass):
    detail_query = "SELECT * FROM taskapptable WHERE user_name = %s AND user_password = %s"
    cursorss.execute(detail_query, (admin_name, admin_pass))
    result = cursorss.fetchall()
    if result:
          if admin_name=="Tom" and admin_pass=="Welcome@123$":
              print(f"{BOLD}{ITALIC}Hi! welcome '{RED + admin_name + heart_emoji + RESET}'")
              print("\t", cat_art)
              time.sleep(2)
              while True:
                  print(BOLD, ITALIC)
                  print(BLUE, "Menu's".center(30, "*"))
                  print("1.User's Details")
                  print("2.User's Task")
                  print("3.User's Info Changes")
                  print("4.Sign Out")
                  try:
                      print(PURPLE)
                      choose = int(input("Enter the option(1/2/3/4): "))
                      print(RESET)
                  except Exception:
                      print(NEGATIVE, "Only Numeric!!!", RESET, verify_emoji)
                  else:
                      if choose==1:
                          user_details()
                      elif choose==2:
                          task_details()
                      elif choose==3:
                          userinfo_changes(admin_name)
                      elif choose==4:
                          print(BOLD, ITALIC)
                          print("Thanks for coming!!!",admin_name, smile_emoji)
                          break
                      else:
                          print(BOLD, ITALIC, NEGATIVE,"''If would like to continue this task please choose (1 To 3) numbers!!!''", RESET)
                          time.sleep(2)
          else:
            print(BOLD, ITALIC, NEGATIVE, "User_name or Password wrong,Please try again!!!", RESET, smile_mouth)
            time.sleep(1)
            print(BOLD, ITALIC, YELLOW)
            admin_name = input("Admin_Name : ")
            admin_pass = input("Admin_Password : ")
            print(RESET)
            admin_portal(admin_name, admin_pass)
    else:
        print(BOLD, ITALIC, NEGATIVE, "User_name or Password wrong,Please try again!!!", RESET, smile_mouth)
        time.sleep(1)
        print(BOLD, ITALIC, YELLOW)
        admin_name = input("Admin_Name : ")
        admin_pass = input("Admin_Password : ")
        print(RESET)
        admin_portal(admin_name, admin_pass)



def user_details():
   cursorss.execute("SELECT * FROM taskapptable WHERE NOT user_name= 'Tom'")
   result=cursorss.fetchall()
   if not result:
       print(NEGATIVE, "No Task's Found!!!", RESET, hand_emoji)
       time.sleep(2)
   else:
       table_format = []
       for j in result:
           table_format.append(j)
       print(tabulate(table_format, headers=["User_ID", "User_Name","User_Password"], tablefmt="grid", numalign="center"))
       time.sleep(2)


def task_details():
    cursorss.execute("SELECT task_name,TIME_FORMAT(task_time,'%h:%i:%s %p') FROM taskinsert")
    result = cursorss.fetchall()
    if not result:
        print(NEGATIVE, "No Task's Found!!!", RESET, hand_emoji)
        time.sleep(2)
    else:
        table_format = []
        for j in result:
            table_format.append(j)
        print(tabulate(table_format, headers=["Task_Name", "Task_time"], tablefmt="grid",numalign="center"))
        time.sleep(2)
def userinfo_changes(admin_name):
    print(f"{BOLD}{ITALIC}Hi! welcome User Information Changes portal '{RED + admin_name + heart_emoji + RESET}'")
    time.sleep(2)
    while True:
        print(BOLD, ITALIC)
        print(BLUE, "Menu's".center(30, "*"))
        print("1.User's Password Changes")
        print("2.User's Task Changes")
        print("3.Sign Out")
        try:
            print(PURPLE)
            choose = int(input("Enter the option(1/2/3): "))
            print(RESET)
        except Exception:
            print(NEGATIVE, "Only Numeric!!!", RESET, verify_emoji)
        else:
            if choose == 1:
                userpass_change()
            elif choose == 2:
                usertask_change()
            elif choose == 3:
                print(BOLD, ITALIC)
                print("Thanks for coming!!!", smile_emoji)
                print("---------------Page Re-direct To Admin Portal----------------")
                time.sleep(1)
                break
            else:
                print(BOLD, ITALIC, NEGATIVE,"''If would like to continue this task please choose (1 To 3) numbers!!!''", RESET)
                time.sleep(2)

def userpass_change():
    print(f"{BOLD}{ITALIC}Hi! welcome User Password's Changes portal{RESET}")
    time.sleep(2)
    print(BOLD, ITALIC, YELLOW)
    username = input("Name : ")
    passkey = input("Password : ")
    print(RESET)
    detail_query = "SELECT * FROM taskapptable WHERE user_name = %s AND user_password = %s"
    cursorss.execute(detail_query, (username, passkey))
    result = cursorss.fetchall()
    if result:
        change_pass=input(f"{BOLD}{ITALIC}New Password : ")
        insert_query="UPDATE taskapptable SET user_password=(%s) WHERE user_name =(%s)"
        cursorss.execute(insert_query,(change_pass,username))
        db_connect.commit()
        print("")
        print(f"Password Successfully Changed!!! {username}{RESET}{smile_mouth}")
        time.sleep(2)
    else:
        print(BOLD, ITALIC, NEGATIVE, "User_name or Password wrong,Please try again!!!", RESET, smile_mouth)
        time.sleep(1)
        userpass_change()


def usertask_change():
   pass
