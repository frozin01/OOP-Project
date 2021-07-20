class Report:
    """Models of User Order Reports."""

    def view_report(self, user_id, report_number):
        for i in range(report_number):
            print('---------------------')
            print('User\'s Name: ' + user_id[i].name_user)
            print('User\'s Table Number: ' + user_id[i].table_number_user)
            print('User\'s Coffee Order: ' + str(user_id[i].coffee_order))
            print('User\'s Cost: ' + str(user_id[i].cost_order))
    
    def delete(self, user_id, report_number, option_delete):
        id_number_delete = 0
        for i in range(report_number):
            print("check1")
            if (option_delete == str(user_id[i].table_number_user)):
                print("check2")
                id_number_delete = i
                break
            else:
                pass
        del user_id[id_number_delete]
        print("check3")