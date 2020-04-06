'''
Created on Mon 04/06/2020 03:06:48 PM
easy_link_menu
@author: MarsCandyBars
'''
import webbrowser

#Creates two lists. name_menu will store the menu entry
#and name_link will store the associated link.
name_menu = []
name_link = []

#Prompts users for menu selection and appends 'Add' functionality by default.
print('If no menu options are available, please select Add.')
name_menu.append('Add')
count = 1

#Loop is currently infinite. Only able to add 9 menu options currently.
while count < 100:
    
    for i in name_menu:
        choice = input('Please enter menu item choice: ')

        if choice == 'Add':
            print(name_menu)
            name_list = input('Please enter friendly name: ')
            link_list = input('Please enter link: ')

            name_menu.append(name_list)
            name_link.append(link_list)
        #In all choices below, the menu is printed and the webbrowser function
        #opens the name_link increment.
        elif choice == '1':
            print(name_menu)
            webbrowser.open(name_link[0])
        elif choice == '2':
            print(name_menu)
            webbrowser.open(name_link[1])
        elif choice == '3':
            print(name_menu)
            webbrowser.open(name_link[2])
        elif choice == '4':
            print(name_menu)
            webbrowser.open(name_link[3])
        elif choice == '5':
            print(name_menu)
            webbrowser.open(name_link[4])
        elif choice == '6':
            print(name_menu)
            webbrowser.open(name_link[5])
        elif choice == '7':
            print(name_menu)
            webbrowser.open(name_link[6])
        elif choice == '8':
            print(name_menu)
            webbrowser.open(name_link[7])
        elif choice == '9':
            print(name_menu)
            webbrowser.open(name_link[8])
        elif choice == '10':
            print(name_menu)
            webbrowser.open(name_link[9])

    count += 1

