def calc_total_price(weight, price):
    total_price = weight * price 
    return total_price

def calc_money_return(money_given, total_price):
    money_return = money_given - total_price
    return money_return

def calc_money_type(total): #assumption: giả sử
    #500 200 100 50 20 10 1
    count_500 = int(total/500)
    total = total - 500*count_500
    if count_500 != 0:
        print("500: "+ str(count_500))

    count_200 = int(total/200)
    total = total - count_200*200
    print("200:"+ str(count_200))

    count_100 = int(total/100)
    total = total - count_100*100
    print("100:"+ str(count_100))

    count_50 = int(total/50)
    total = total - count_50*50
    print("50:"+ str(count_50))

    count_10 = int(total/10)
    total = total - count_10*10
    print("10:"+ str(count_10))

    count_1 = total
    print("1:"+ str(count_1))


        
def main():
    APPLE_PRICE = 21 #k vnd
    apple_weight = float(input("Enter weight of apples: "))

    total_price = calc_total_price(apple_weight, APPLE_PRICE)
    print(total_price)

    money_given = int(input("Total money customer give you: "))

    money_return = calc_money_return(money_given, total_price)

    print(money_given)
    print(money_return)
    print(calc_money_type(money_return))
# decoupling # decouple # chia chương trình thành nhiều module nhỏ.
main()