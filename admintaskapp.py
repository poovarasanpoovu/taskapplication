import mysql.connector
import time
from datetime import datetime as d
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

WRONG="\u274C"
RIGHT="\u2705"

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
              date=d.now()
              print(BOLD,ITALIC,"\rDate & time : ", date.strftime("%d/%m/%Y; %H:%M:%S %p"),RESET)
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
                      print(f"\n{RESET+NEGATIVE}Only Numeric!!!{RESET+WRONG}")
                      time.sleep(1)
                  else:
                      if choose==1:
                          user_details()
                      elif choose==2:
                          task_details()
                      elif choose==3:
                          userinfo_changes(admin_name)
                      elif choose==4:
                          print(BOLD, ITALIC)
                          print(f"Thanks for coming!!!{RED+admin_name+RED+RESET+smile_emoji}")
                          break
                      else:
                          print(NEGATIVE,"''If would like to continue this task please choose (1 To 4) numbers!!!''", RESET)
                          time.sleep(2)
          else:
            print(NEGATIVE, "User_name or Password wrong,Please try again!!!", RESET,WRONG)
            time.sleep(1)
            print(BOLD, ITALIC, YELLOW)
            admin_name = input("Admin_Name : ")
            admin_pass = input("Admin_Password : ")
            print(RESET)
            admin_portal(admin_name, admin_pass)
    else:
        print(NEGATIVE, "User_name or Password wrong,Please try again!!!", RESET,WRONG)
        time.sleep(1)
        print(BOLD, ITALIC, YELLOW)
        admin_name = input("Admin_Name : ")
        admin_pass = input("Admin_Password : ")
        print(RESET)
        admin_portal(admin_name, admin_pass)



def user_details():
   cursorss.execute("SELECT user_id,user_name,user_password,DATE_FORMAT(user_date,'%d/%m/%Y') FROM taskapptable WHERE NOT user_name= 'Tom'")
   result=cursorss.fetchall()
   if not result:
       print(NEGATIVE, "No Task's Found!!!", RESET, hand_emoji)
       time.sleep(2)
   else:
       table_format = []
       print(f"\t\t\t\t{BOLD+ITALIC}Total user's : {RED}{len(result)}{RESET}")
       for j in result:
           table_format.append(j)
       print(tabulate(table_format, headers=["User_ID", "User_Name","User_Password","User_Date"], tablefmt="grid", numalign="center"))
       time.sleep(2)


def task_details():
    cursorss.execute("SELECT user_name,task_name,TIME_FORMAT(task_time,'%h:%i:%s %p') FROM taskinsert")
    result = cursorss.fetchall()
    if not result:
        print(NEGATIVE, "No Task's Found!!!", RESET, hand_emoji)
        time.sleep(2)
    else:
        table_format = []
        for j in result:
            table_format.append(j)
        print(tabulate(table_format, headers=["User_Name","Task_Name", "Task_time"], tablefmt="grid",numalign="center"))
        time.sleep(2)
def userinfo_changes(admin_name):
    print(f"\t\t\t{BOLD}{ITALIC}User Information Changes portal{RESET}")
    date = d.now()
    print(BOLD,ITALIC,"\t\t\tDate & time : ", date.strftime("%d/%m/%Y; %H:%M:%S %p"),RESET)
    time.sleep(1)
    while True:
        print(BOLD, ITALIC)
        print(BLUE, "Menu's".center(30, "*"))
        print("1.User's Password Changes")
        print("2.User's Task Changes")
        print("3.User's Details Removed")
        print("4.Sign Out")
        try:
            print(PURPLE)
            choose = int(input("Enter the option(1/2/3): "))
            print(RESET)
        except Exception:
            print(f"\n{RESET+NEGATIVE}Only Numeric!!!", RESET,WRONG)
            time.sleep(1)
        else:
            if choose == 1:
                userpass_change()
            elif choose == 2:
                usertask_change()
            elif choose == 3:
                user_removed()
            elif choose == 4:
                print(BOLD, ITALIC)
                print("Thanks for coming!!!", smile_emoji)
                print("---------------Page Re-direct To Admin Portal----------------")
                time.sleep(1)
                break
            else:
                print(NEGATIVE,"''If would like to continue this task please choose (1 To 4) numbers!!!''", RESET)
                time.sleep(1)

def userpass_change():
    print(f"\t\t\t{BOLD}{ITALIC}User Password's Changes portal")
    date = d.now()
    print("\t\t\tDate & time : ", date.strftime("%d/%m/%Y; %H:%M:%S %p"),RESET)
    time.sleep(1)
    print(BOLD, ITALIC, YELLOW)
    username = input("Name : ")
    passkey = input("Password : ")
    print(RESET)
    detail_query = "SELECT * FROM taskapptable WHERE user_name = %s AND user_password = %s"
    cursorss.execute(detail_query, (username, passkey))
    result = cursorss.fetchall()
    if result:
        change_pass=input(f"{BOLD}{ITALIC}New Password : ")
        new_date=date.strftime("%Y-%m-%d")
        insert_query="UPDATE taskapptable SET user_date=(%s),user_password=(%s)  WHERE user_name =(%s)"
        cursorss.execute(insert_query,(new_date,change_pass,username))
        db_connect.commit()
        print("")
        print(f"Password Successfully Changed!!! {RED}{username}{RESET}{smile_mouth}")
        time.sleep(2)
    else:
        print(NEGATIVE ,"User_name or Password wrong,Please try again!!!", RESET, WRONG)
        time.sleep(1)
        userpass_change()

def user_removed():

    print(f"\t\t\t{BOLD}{ITALIC}User Details Removed portal")
    date = d.now()
    print("\t\t\tDate & time : ", date.strftime("%d/%m/%Y; %H:%M:%S %p"))
    time.sleep(1)
    try:
        print(BOLD, ITALIC,YELLOW)
        user_id=int(input("Enter User Id : "))
        user_name=input("Enter User Name : ")
        print(RESET)

    except Exception:
        print(RESET,NEGATIVE, "Id (Numeric) & Name (Characters)!!!", RESET,WRONG)
        time.sleep(1)
        user_removed()
    else:
        get_query=("SELECT * FROM taskapptable WHERE user_id = %s AND user_name = %s")
        cursorss.execute(get_query,(user_id,user_name))
        result=cursorss.fetchall()

        if not result:
           print(NEGATIVE, "User_name or Password wrong,Please try again!!!", RESET, WRONG)
           time.sleep(1)
           user_removed()
        else:
            print(f"{BOLD+ITALIC+YELLOW}")
            admin_pass = input("Enter Admin's Password : ")
            print(f"{RESET}")
            if admin_pass == "Welcome@123$":
               delete_query = ("DELETE FROM taskapptable WHERE user_id = %s AND user_name = %s")
               cursorss.execute(delete_query,(user_id,user_name))
               db_connect.commit()
               print(f"\n{BOLD+ITALIC}User {user_name} Deleted Successfully!!!", RIGHT, smile_emoji)
               time.sleep(1)
            else:
                print("\n",NEGATIVE,"Admin Your Password wrong,Please try again!!!", RESET, WRONG)
                time.sleep(1)
                user_removed()


def usertask_change():

    print(f"\t\t\t{BOLD}{ITALIC}User Task's Changes portal")
    date = d.now()
    print("\t\t\tDate & time : ", date.strftime("%d/%m/%Y; %H:%M:%S %p"))
    time.sleep(1)
    while True:
            print(BOLD, ITALIC)
            print(BLUE, "Menu's".center(30, "*"))
            print("1.Task_Insert Table Delete")
            print("2.Task_Update Table Delete")
            print("3.Sign Out")
            try:
                print(PURPLE)
                choose = int(input("Enter the option(1/2/3): "))
                print(RESET)
            except Exception:
                print(f"\n{RESET+NEGATIVE}Numeric Only!!!{RESET+WRONG}")
                time.sleep(1)
            else:
               if choose==1:
                  cursorss.execute("SELECT * FROM taskinsert")
                  result = cursorss.fetchall()
                  if result:
                        cursorss.execute("DELETE FROM taskinsert")
                        db_connect.commit()
                        print(BOLD,ITALIC,"Successfully Deleted Taskinsert Item's!!!",RIGHT)
                        time.sleep(1)
                  else:
                        print(NEGATIVE,"Taskinsert Table already Empty!!!",RESET)
                        time.sleep(1)
               elif choose==2:
                    cursorss.execute("SELECT * FROM taskupdate")
                    result = cursorss.fetchall()
                    if result:
                         cursorss.execute("DELETE FROM taskupdate")
                         db_connect.commit()
                         print(BOLD,ITALIC,"Successfully Deleted Taskupdate Item's!!!",RESET,RIGHT)
                         time.sleep(1)
                    else:
                          print(NEGATIVE,"Taskupdate Table already Empty!!!",RESET)
                          time.sleep(1)
               elif choose == 3:
                   print(BOLD, ITALIC)
                   print("Thanks for coming!!!", smile_emoji)
                   print("---------------Page Re-direct To User Information Changes portal----------------")
                   time.sleep(1)
                   break
               else:
                  print(BOLD, "''If would like to continue this task please choose (1 To 3) numbers!!!''",RESET)
                  time.sleep(2)

