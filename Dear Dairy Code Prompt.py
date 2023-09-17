import os

Date = input('Enter Date:')
Diary_Entry = input('Tell me all about your day bestie: ')

file_path = r'C:\Users\KING G\OneDrive\Desktop\git\Python\Dear Diary'

try:
    with open(file_path, 'a') as file:
        file.write (Date + '\n')
        file.write(Diary_Entry + '\n\n')

        print(f'Diary entry filled and saved to {file_path} Succssfully.')

except Exception as e:
    print(f'An error was encountered: {e}')
