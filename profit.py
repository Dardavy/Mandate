
import time
import schedule

Amount_investment = float(input("Enter your Amount investment: "))
profit = Amount_investment * 0.1


def geT_Profit(Amount_investment, profit):
        geT_Profit = Amount_investment + profit
        return geT_Profit


def calc():
        if __name__ == "__main__" :
                Amount_investment,profit

        if Amount_investment < 0 :
                print("no profit gain")

        elif Amount_investment > 0: 
                print(geT_Profit(Amount_investment,profit), "profit") 
                  
calc()               
schedule.every().day.at("00:00").do(calc)

while True:
        schedule.run_pending()
        time.sleep
                



































# import time
# import schedule

# Amount_investment = float(input("Enter your Amount investment: "))
# profit = Amount_investment * 0.1

# def gain_profit(Amount_investment, profit):
#         gain_profit =( Amount_investment + profit)
#         return gain_profit

# def profit_Gain(Amount_investment, profit):
#         profit_Credited = gain_profit
#         return profit_Credited


# def calc():
#         if __name__ == "__main__" :

#                 Amount_investment,profit

#         if Amount_investment < 0 :
#                 print("no profit gain")
#         elif Amount_investment > 0:
#                 gain_profit
#                 print(gain_profit(Amount_investment,profit), "profit")
 
# calc()               
# schedule.every(10).seconds.do(calc)

# while True:
#         schedule.run_pending()
#         time.sleep
                



       
       
# while True:
#     time.sleep(86400) # 86400 seconds = 24 hours

#     profit = gain_profit(Amount_investment)
#     Amount_investment = compound_profit(Amount_investment, profit)

#     print("Your profit is now $", Amount_investment)

# if _name_ == "_main_":
#     main()






#     import math

# # Take user inputs
# principal = float(input("Enter the initial investment amount: "))
# rate = float(input("Enter the annual interest rate (%): "))
# time_period = float(input("Enter the investment period in days per year: "))

# # Calculate the profit
# profit = principal * (math.pow((1 + rate / 100), time_period)) - principal

# # Print the result
# print("The profit earned after", time_period, "years is: $", round(profit, 2))