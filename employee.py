class Employee:
    """Models of each Employee."""
    
    def __init__(self, name_account, email_account, position_account):
        self.name_account = name_account
        self.email_account = email_account
        self.position_account = position_account

    def work(self):
        print(self.name_account + " is working")
    
    @classmethod
    def update(cls, account_id, account_number, option_update):
        account_number_updated = 0
        for i in range(account_number):
            if option_update == str(account_id[i].name_account):
                account_number_updated = i
                break
            else:
                pass
        email_account_updated = str(input('Type new email here: ')).strip().lower()
        account_id[account_number_updated].email_account = email_account_updated
    
    @classmethod
    def delete(cls, account_id, account_number, option_delete):
        account_number_deleted = 0
        for i in range(account_number):
            if option_delete == str(account_id[i].name_account):
                account_number_deleted = i
                break
            else:
                pass
        del account_id[account_number_deleted]
    
    @classmethod
    def view_report(cls, account_id, account_number):
        for i in range(account_number):
            print('------------------------------------------------------')
            if account_id[i].position_account == "programmer":
                print(account_id[i].name_account + ' - ' + account_id[i].email_account + ' - ' + account_id[i].position_account + ' - ' + account_id[i].programming_account)
            elif account_id[i].position_account == "designer":
                print(account_id[i].name_account + ' - ' + account_id[i].email_account + ' - ' + account_id[i].position_account + ' - ' + account_id[i].tool_account)
            else:
                print(account_id[i].name_account + ' - ' + account_id[i].email_account + ' - ' + account_id[i].position_account)


class Programmer(Employee):
    """Model of each Programmer"""

    def __init__(self, name_account, email_account, position_account, programming_account):
        super().__init__(name_account, email_account, position_account)
        self.programming_account = programming_account
    
    def work(self):
        print(self.name_account + " is writing a code")


class Designer(Employee):
    """Model of each Designer"""

    def __init__(self, name_account, email_account, position_account, tool_account):
        super().__init__(name_account, email_account, position_account)
        self.tool_account = tool_account
    
    def work(self):
        print(self.name_account + " is creating a design")