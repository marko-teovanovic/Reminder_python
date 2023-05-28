import json
from datetime import datetime

current_time = datetime.now()
time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

with open('reminder_storage.json', 'r') as f:
    storage = json.load(f)

menu = ("""======REMINDER======
[1] Add a reminder
[2] Change reminder
[3] See all reminders
[4] Delete reminder
[5] Search
[0] Exit
====================""")
print(menu)

while True:
    message = input("Please choose an option:")
    if message == '0':
        break
    elif message == '1':
        reminder_title = input("Title:")
        body = input("Write something here:")
        priority = int(input("Enter priority:"))
        new_reminder = {
            "Name of reminder": reminder_title,
            "Text of reminder": body,
            "priority": priority,
            "Time": current_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        storage.append(new_reminder)

        with open('reminder_storage.json', 'w') as f:
            json.dump(storage, f, indent=4)

        print(menu)

    elif message == '2':
        print('All reminders:')
        for i, reminder in enumerate(storage):
            print(f"{i}: {reminder['Name of reminder']}")

        sub_options = int(input("Choose the index of the reminder you want to change: "))
        changing_options = input("""1) Name of reminder
2) Text of reminder
3) Priority
Choose the option you want to change: """)
        if changing_options == '1':
            reminder_title = input("Enter name: ")
            storage[sub_options]["Name of reminder"] = reminder_title
        elif changing_options == '2':
            reminder_text = input("Enter new text for reminder: ")
            storage[sub_options]["Text of reminder"] = reminder_text
        elif changing_options == '3':
            new_priority = int(input("Enter new priority: "))
            storage[sub_options]["priority"] = new_priority

        with open('reminder_storage.json', 'w') as f:
            json.dump(storage, f, indent=4)

    elif message == '3':
        print('All reminders:')
        for i, reminder in enumerate(storage):
            print(f""""{i}: {reminder['Name of reminder']}, 
                  {reminder['Text of reminder']}, 
                  {reminder['priority']}, 
                  {reminder['Time']}""")
    elif message == '4':
        print('All reminders:')
        for i, reminder in enumerate(storage):
            print(f"{i}: {reminder['Name of reminder']}")

        reminder_delete = int(input("Choose the index of the reminder you want to delete: "))

        if reminder_delete < len(storage):
            del storage[reminder_delete]
            print("You successfully deleted your reminder!")

            with open('reminder_storage.json', 'w') as f:
                json.dump(storage, f, indent=4)
        else:
            print("Reminder doesn't exist!")
    elif message == '5':
        option = input(""""\n1) Search by priority.
                      \n2) Search by time of adding.
                      \nChoose search option:""")
        if option == '1':
            priority = int(input("Enter priority of a reminder: "))
            filtered_list = list(filter(lambda x: x['priority'] == priority, storage))
            for reminder in filtered_list:
                print(f"{reminder['Name of reminder']}, {reminder['Text of reminder']}, {reminder['priority']}")
        elif option == '2':
            time_to_search = input("Enter the time of adding (format: YYYY-MM-DD HH:MM:SS): ")
            filtered_list = list(filter(lambda x: x['Time'] == time_to_search, storage))
            if filtered_list:
                for reminder in filtered_list:
                    print(
                        f""""{reminder['Name of reminder']}, 
                        {reminder['Text of reminder']},    
                        {reminder['priority']}, 
                        {reminder['Time']}""")
            else:
                print("No reminders found for the given time.")
