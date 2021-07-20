# Import library
from user import User
from report import Report

def welcome():
    print('\nWELCOME TO THE ROZIN\'S COFFEE!\n\n'
          '---------- MENU ---------\n'
          'Kopi Aceh (Rp. 10.000)\n'
          'Kopi Arabica (Rp. 10.000)\n'
          'Kopi Cappuccino (Rp. 12.000)\n'
          'Kopi Espresso (Rp. 8.000)\n'
          'Kopi Latte (Rp. 14.000)\n'
          '-------------------------\n\n'
          'Option:\n'
          '"order": order the menu\n'
          '"report": report of user\'s orders\n'
          '"off": close the program\n')

condition_main = True
id_number = 0
report_number = 0
user_id = []
report = Report()

while condition_main:
    welcome()
    option_main = str(input('Type your option here: ')).strip().lower()

    if option_main == 'order':
        user_id_name = "User" + str(id_number)
        user_id.append(user_id_name)
        name_user = str(input('User\'s name: '))
        table_number_user = str(input('User\'s table number: '))
        user_id[id_number] = User(name_user,table_number_user)
        user_id[id_number].menu(name_user,table_number_user)
        user_id[id_number].order_summary()
        id_number += 1
        report_number += 1

    elif option_main == 'report':
        report.view_report(user_id, report_number)
        option_report = str(input('Type your option here (Delete or Back): ')).strip().lower()
        if option_report == 'delete':
            condition_delete = True
            while(condition_delete):
                option_delete = str(input('Type the table number user here: ')).strip().lower()
                report.delete(user_id, report_number, option_delete)
                report_number -=1
                id_number -= 1
                report.view_report(user_id, report_number)
                option_delete_again = str(input('Delete again? (Yes/No)')).strip().lower()
                if (option_delete_again == 'no'):
                    condition_delete = False
        else:
            pass

    elif option_main == 'off':
        print('\nSEE YOU NEXT TIME')
        condition_main = False

    else:
        print('Sorry your option is not valid, please retype yout option!')

    