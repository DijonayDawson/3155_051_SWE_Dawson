class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        largeDollars = float(input("how many large dollars?: "))
        halfDollars = float(input("how many half dollars?: "))
        quarters = float(input("how many quarters?: "))
        nickels = float(input("how many nickels?: "))

        total = largeDollars + halfDollars / 2 + quarters / 4 + nickels / 20

        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = coins - cost
            print("Here is $" + str(change) + " in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False