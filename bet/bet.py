MAX_LINES = 4
MIN_BET = 0
MAX_BET = 100

def get_number_of_lines():
     while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) +"):")
        if lines.isdigit():
            lines = int(lines) 
            if 0 <= lines <= MAX_LINES :
                break
            else:            
             print("Enter the valid number of lines")
        else:
             print("Please Enter a number")
     return lines


def get_bet():
     while True:
        betamount=input("How much amount do you want to bet on each line: $")
        if betamount.isdigit():
            betamount = int(betamount) 
            if MIN_BET <= betamount <=MAX_BET :
                break
            else:            
             print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
             print("Please Enter a number")
     return betamount

def main():
    lines = get_number_of_lines()
    bet = get_bet()
    print(f"Script lines : {lines}")
    print(f"Bet amount is : {bet}")

main()
       


             
             



           