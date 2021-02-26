def calc_total_price(weight, price):
    total_price = weight * price 
    return total_price

def calc_money_return(money_given, total_price):
    money_return = money_given - total_price
    return money_return

def calc_money_type(money_given, per100, per50, per20, per10, per5, per2, per1):
    pass


def main():
    APPLE_PRICE = 21 #k vnd
    apple_weight = float(input("Enter weight of apples: "))

    total_price = calc_total_price(apple_weight, APPLE_PRICE)
    print(total_price)

    money_given = int(input("Total money customer give you: "))

    money_return = calc_money_return(money_given, total_price)

    print(money_given)
    print(money_return)

main()