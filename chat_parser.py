import datetime
import re

def parse_chat(filename):
    # Open the file with the given filename
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression pattern to match chat entries
    pattern = re.compile(r"\[(\d{2}\.\d{2}\.\d{2}), (\d{2}:\d{2}:\d{2})\] (.*?): (.*?)(?=\[\d{2}\.\d{2}\.\d{2}, \d{2}:\d{2}:\d{2}\]|$)", re.DOTALL)
    chats = []
    matches = pattern.finditer(content)

    # Initialize variable to store the name of the first user
    my_name = None
    for match in matches:
        date_str, time_str, sender, message = match.groups()
        # Set the first sender name as 'my_name'
        if my_name is None:
            my_name = sender
        # Convert string date and time to datetime object
        date_time = datetime.datetime.strptime(f'{date_str}, {time_str}', '%d.%m.%y, %H:%M:%S')
        # Check if the message was sent by 'my_name'
        mine = sender == my_name
        # Append the parsed chat entry to the list
        chats.append({'datetime': date_time, 'sender': sender, 'message': message.strip(), 'mine': mine})

    return chats