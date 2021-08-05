# Yes, I know not to use floats for currency. 
# It's a tip calculator. I'm not concerned with perfect accuracy here. 

bill_amount = 0
tip = 0
tip_rate = 0
total = 0

def get_bill_amount():
    bill_prompt = input("What is the bill amount? ")
    if "$" in bill_prompt:
        bill_prompt = bill_prompt.replace("$", "")
    try: 
        ba = float(bill_prompt)
        return ba
    except:
        print(f"{bill_prompt} is not a valid dollar amount.")
        ba = get_bill_amount()
        return ba

def get_tip_rate():
    tip_rate_prompt = input("What is the tip percentage? ")
    if "%" in tip_rate_prompt:
        tip_rate_prompt = tip_rate_prompt.replace("%", "")
    try:
        tr = float(tip_rate_prompt)
        return tr
    except:
        print(f"{tip_rate_prompt} is not a valid percentage.")
        tr = get_tip_rate()
        return tr

def calculate_bill():
    bill_amount = get_bill_amount()
    if bill_amount < 0:
        bill_amount = bill_amount * -1
    tip_rate = get_tip_rate()/100
    if tip_rate < 0: 
        tip_rate = tip_rate * -1
    tip = (bill_amount * tip_rate).__round__(2)
    total = (bill_amount + tip).__round__(2)
    bill_string = "{:.2f}".format(bill_amount)
    tip_string = "{:.2f}".format(tip)
    total_string = "{:.2f}".format(total)
    print(f"Bill amount: {bill_string}")
    print(f"Tip amount: {tip_string}")
    print(f"Total: {total_string}")

calculate_bill()
