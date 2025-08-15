import os 

Fill = "score.txt"

def chake_resalt():

    if not os.path.exists(Fill):
        print("Your data is not alone")
        return

    student_id = input("Enter Your ID: ")
    name = input("Enter Your Name: ")

    
    with open(Fill, 'r') as f:
        lines = f.readlines()

    found = False
    for line in lines:
        
        record_id, record_name, scores, avg = line.strip().split(':')

        if record_id == student_id and record_name.lower() == name.lower():
            print( f"\n Hello {record_name}")
            print(f"Your Score: {scores}")
            print(f"Your Average: {avg}")
            found = True
            break
    if not found:
        print(" No matching student found. Check your ID and name!")    

def manu():

    while True:
        print("\n 1. Chake resalt")
        print(" 2. Exit")
        choice = input("Enter Your Choice:")
        
        if choice == "1":
            chake_resalt()
        elif choice == "2":
            print("Doodbye")  
            break
        else:
            print("Invalid choice, try again")
manu()            
