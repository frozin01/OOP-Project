class MenuItem:
    """Models of each Menu Item."""
    
    def __init__(self, coffee_type, cost):
        self.coffee_type = coffee_type
        self.cost = cost

class User:
    """Model of each Users"""

    def __init__(self, name_user, table_number_user):
        self.name_user = name_user
        self.table_number_user = table_number_user
        self.menu_item = [
            MenuItem(coffee_type="Kopi Aceh", cost=10000),
            MenuItem(coffee_type="Kopi Arabica", cost=10000),
            MenuItem(coffee_type="Kopi Cappucino", cost=12000),
            MenuItem(coffee_type="Kopi Espresso", cost=8000),
            MenuItem(coffee_type="Kopi Latte", cost=14000),
        ]
    
    def menu(self, name_user, table_number_user):
        global coffee_order
        global cost_order
        condition_menu = True
        coffee_order = {} 
        cost_order = 0

        while(condition_menu):
            coffee_type = str(input('Coffee\'s type: '))
            amount_of_coffee = int(input('Amount of '+ coffee_type + ' you want to order: '))
            option_menu = str(input('Order again? (Yes/No)')).strip().lower()
            coffee_order[coffee_type] = amount_of_coffee
            if (option_menu == 'no'):
                condition_menu = False

        for key, value in coffee_order.items():
            for item in self.menu_item:
                if key == item.coffee_type:
                    cost_order += value*item.cost

    def order_summary(self):
        self.coffee_order = coffee_order
        self.cost_order = cost_order
        print('\n'+ self.name_user + '\'s Order ' + '(Table Number: ' + self.table_number_user + ')' + ':')
        for key, value in coffee_order.items():
            print(key + ': ' + str(value))
        print('Total cost: ' + str(cost_order))