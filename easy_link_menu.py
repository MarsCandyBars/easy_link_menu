'''
Created on Mon 04/06/2020 03:06:48 PM
easy_link_menu
@author: MarsCandyBars
'''
import webbrowser

menu_name = []
link = []


def prompt():
    '''
    Description:
        This function prints the running list and prompts
        for item choice.
    Args:
        None.
    Returns:
        user_choice
    '''
    count = 1
    for i in menu_name:
        print(str(count) + '. ', i)
        count += 1
    user_choice = input('\n' + 'Please enter menu item choice: ')
    return user_choice

def add():
    '''
    Description:
        This function adds new items to the list.
    Args:
        None.
    Returns:
        name_list, link_list
    '''
    name_list = input('Please enter friendly name: ')
    link_list = input('Please enter link: ')

    menu_name.append(name_list)
    link.append(link_list)

    return [name_list, link_list]

def menu():
    '''
    Description:
        This function prints menu tag line.
    Args:
        None.
    Returns:
        None.
    '''
    print('EASY_LINKS_MENU')

menu_name.append('Add')

menu()
count = 1


while True:
    
    choice = prompt()

    if choice == '1':
        add_list = add()
    elif choice == '2':
        webbrowser.open(link[0])
    elif choice == '3':
        webbrowser.open(link[1])
    elif choice == '4':
        webbrowser.open(link[2])
    elif choice == '5':
        webbrowser.open(link[3])
    elif choice == '6':
        webbrowser.open(link[4])
    elif choice == '7':
        webbrowser.open(link[5])
    elif choice == '8':
        webbrowser.open(link[6])
    elif choice == '9':
        webbrowser.open(link[7])
    elif choice == '10':
        webbrowser.open(link[8])
    elif choice == '11':
        webbrowser.open(link[9])

