# Import library
from employee import Employee, Programmer, Designer

def welcome():
    print('\nWELCOME TO THE ROZIN\'S OFFICE!\n'
          '-----------------------------------\n'
          'Option:\n'
          '"create": create an account\n'
          '"update": update an account\n'
          '"delete": delete an account\n'
          '"monitor": monitor all works in database\n'
          '"report": report all accounts in database\n'
          '"off": close the program\n')

def working(system):
    if (system.work() != None):
        print(system.work())
    else:
        pass

condition_main = True
account_number = 0
account_id = []

while condition_main:
    welcome()
    option_main = str(input('Type your option here: ')).strip().lower()

    if option_main == 'create':
        account_id_name = "Account " + str(account_number)
        account_id.append(account_id_name)
        name_account = str(input('Account\'s name: '))
        email_account = str(input('Account\'s email: '))
        position_account = str(input('Account\'s position: '))
        if position_account == 'programmer':
            programming_account = str(input('Programmer\'s best programming skill: '))
            account_id[account_number] = Programmer(name_account, email_account, position_account, programming_account)
        elif position_account == 'designer':
            tool_account = str(input('Designer\'s best tool skill: '))
            account_id[account_number] = Designer(name_account, email_account, position_account, tool_account)
        else:
            account_id[account_number] = Employee(name_account, email_account, position_account)
        account_number += 1

    elif option_main == 'update':
        option_update = str(input('Type account\'s name here: ')).strip().lower()
        Employee.update(account_id, account_number, option_update)

    elif option_main == 'delete':
        option_delete = str(input('Type the account\'s name here: ')).strip().lower()
        Employee.delete(account_id, account_number, option_delete)
        account_number -=1
    
    elif option_main == 'monitor':
        for i in range(account_number):
            working(account_id[i])

    elif option_main == 'report':
        Employee.view_report(account_id, account_number)

    elif option_main == 'off':
        print('\nSEE YOU NEXT TIME')
        condition_main = False

    else:
        print('Sorry your option is not valid, please retype your option!')

    