import time
from datetime import datetime as d
import os,time
import mysql.connector
from tabulate import tabulate

db_connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythondb"
)
cur = db_connect.cursor()
def table_tasks():
 insert_task = '''
    CREATE TABLE IF NOT EXISTS taskinsert(
      user_name VARCHAR(20),
      task_name VARCHAR(20),
      task_time TIME

    )'''
 cur.execute(insert_task)
#table_tasks()
def table_update():
    update_tasks='''
    CREATE TABLE IF NOT EXISTS taskupdate(
      user_name VARCHAR(20),
      task_name VARCHAR(20),
      task_time time
    )'''
    cur.execute(update_tasks)
#table_update()


date = d.now()
start=time.time()

BLUE = "\033[0;34m"
RED = '\033[91m'
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
NEGATIVE = "\033[7m"
RESET = '\033[0m'

BOLD = "\033[1m"
ITALIC = "\033[3m"

smile_emoji='\U0001F60A'
verify_emoji ='\U0001F914'
success_emoji='\U0001F60E'
thanks_emoji='\U0001F64F'
hand_emoji='\U0001F44D'
heart_emoji='\U00002764'

cat_art = r'''
 /\_/\  
( o.o ) 
 > ^ <
'''

print(BOLD,ITALIC,f"Task Program{smile_emoji}".center(30,"*"))
print("\rDate & time : ",date.strftime("%d/%m/%Y; %H:%M:%S %p"))

user = ''
passwords = ''

def add_task(user):

   try:
       print(BOLD,ITALIC)
       number = int(input("How many task's will added : "))

   except Exception:
       print(NEGATIVE,"Only Numeric!!!",RESET,verify_emoji)
       add_task()
   else:
       for i in range(1, number + 1):
           task = input(f"Enter the task {i}: ")
           insert_task_query="INSERT INTO taskinsert VALUES (%s,%s,%s)"
           dates = d.now()
           cur_time=dates.strftime("%H:%M:%S")
           cur.execute(insert_task_query,(user,task,cur_time))
           db_connect.commit()
       print("Task's added Successfully!!",smile_emoji)
       task_start=time.time()
       time.sleep(2)

def view_task():
    print(BOLD,ITALIC)
    cur.execute("SELECT user_name,task_name,TIME_FORMAT(task_time,'%h:%i:%s %p') FROM taskinsert")
    result_tasks=cur.fetchall()
    if not result_tasks:
        print(NEGATIVE,"No Task's Found!!!",RESET,hand_emoji)
        time.sleep(2)
    else:
       count=1
       table_format=[]
       for j in result_tasks:
           table_format.append(j)
          #print(f"{count}: {j[0]}  Time is :{j[1]}".title())
          #count+=1
       print(tabulate(table_format,headers=["User_Name","Task_Name","Task_Time"],tablefmt="grid",numalign="center"))
       time.sleep(2)
def update_task(user):

    print(BOLD,ITALIC)
    cur.execute("SELECT task_name FROM taskinsert")
    result_tasks = cur.fetchall()
    if not result_tasks:
        print(NEGATIVE,"No Task's Found!!!",RESET,hand_emoji)
        time.sleep(2)
    else:
        try:
          num= int(input("How many task's updated : "))
        except Exception:
            print("Only Numeric!!!",verify_emoji)
            time.sleep(2)
            update_task()
        else:
            if num<=len(result_tasks):
              for i in range(0, num):

                choose = input("Please Enter task : ")
                for j in result_tasks:
                  if choose in j:
                     delete_query="DELETE FROM taskinsert where task_name=(%s)"
                     cur.execute(delete_query,(choose,))
                     db_connect.commit()
                     print("\n Updated Successfully!!!", smile_emoji)
                     dates = d.now()
                     dates=dates.strftime("%H:%M:%S")
                     insert_table="INSERT INTO taskupdate VALUES(%s,%s,%s)"
                     cur.execute(insert_table,(user,choose,dates))
                     db_connect.commit()
                     time.sleep(2)
                     break

                else:
                     print(f"{NEGATIVE}Enter Correct Task's name",RESET)
                     time.sleep(2)
                     update_task()
            else:
                  print(f"Please Enter {RED}Less_than {len(result_tasks)}{RESET} (OR) {RED}{BOLD}{ITALIC}Equal_To {len(result_tasks)}{RESET}")
                  time.sleep(2)
                  update_task()

def complete_task():
    print(BOLD,ITALIC)
    cur.execute("SELECT user_name,task_name,TIME_FORMAT(task_time,'%h:%i:%s %p') FROM taskupdate")
    result_tasks = cur.fetchall()
    if not result_tasks:
        print(BOLD, ITALIC, NEGATIVE, "No Task's Found!!!", RESET, hand_emoji)
        time.sleep(2)
    else:
        count = 1
        table_complete=[]
        for j in result_tasks:
            #print(f"{count}: {j[0]}  Time is :{j[1]}".title())
            #count += 1
            table_complete.append(j)
        print(tabulate(table_complete, headers=["user_Name","Task_Name", "Task_Time"], tablefmt="grid", numalign="center"))
        time.sleep(2)

def main(user):
    count=0
    print(f"{BOLD}{ITALIC}Hi! welcome '{RED+user+heart_emoji+RESET}'")
    print("\t",cat_art)
    time.sleep(2)
    while True:
     print(BOLD,ITALIC)
     print(BLUE,"Menu's".center(30,"*"))
     print("1.Add Task")
     print("2.View Task")
     print("3.Update Task ")
     print("4.Complete Task ")
     print("5.Sign out",RESET)

     try:
        count += 1
        print(PURPLE)
        task = int(input("Enter the option(1/2/3/4/5): "))
        print(RESET)

     except Exception:
         print(NEGATIVE,"Only Numeric!!!",RESET,verify_emoji)
     else:
        if task == 1:
          add_task(user)
        elif task == 2:
          view_task()
        elif task == 3:
          update_task(user)
        elif task == 4:
          complete_task()
        elif task==5:
          print(BOLD,ITALIC)
          print("Thanks for coming!!!",smile_emoji)
          print("Using of no.of entry's this Portal count : ",count)
          with open("taskapp.py", "r") as a:
              count = 0
              for i in a:
                  count += 1
              print(f"Total lines : {count}")

          if os.path.exists("taskapp.py"):
              end = time.time()
              result_time = end - start
              size = os.path.getsize("taskapp.py") / 1024
              print("File size : {:.2f}KB".format(size))
              print("Execution Time : ",result_time)
              cur.execute("DELETE FROM taskupdate")
              cur.execute("DELETE FROM taskinsert")
              db_connect.commit()
              break

        else:
            print(BOLD,ITALIC,NEGATIVE,"''If would like to continue this task please choose (1 To 4) numbers!!!''",RESET)
            time.sleep(2)

