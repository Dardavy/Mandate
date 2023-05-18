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
                
