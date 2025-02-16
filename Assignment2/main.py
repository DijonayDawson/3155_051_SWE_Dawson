import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
SandwichMachine = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    while 1==1:
        intro = input("What would you like? (small/ medium/ large/ off/ report):")

        if intro == "off":
            exit()
        elif intro == "report":
            print("Bread: " + str(SandwichMachine.machine_resources["bread"]) + " slice(s)")
            print("Ham: " + str(SandwichMachine.machine_resources["ham"]) + " slice(s)")
            print("Cheese: " + str(SandwichMachine.machine_resources["cheese"]) + " pound(s)")

        elif intro == "small" or "medium" or "large":
            if SandwichMachine.check_resources(recipes[intro]['ingredients']) == True:
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, recipes[intro]['cost']) == True:
                    SandwichMachine.make_sandwich(intro, recipes[intro]['ingredients'])
            else:
                print('Sorry, there is not enough bread')

if __name__=="__main__":
    main()