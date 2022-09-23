class Category:
    def __init__(self):
        name=""
        ledger=[]
        balance=0.0
        
    def deposit(self, ledger):
        if not ledger["description"]:
            ledger["description"] = ""        
        self.ledger.append(ledger)
        self.balance += ledger["amount"]

    def check_funds(self, amount):
        if amount<self.balance:
            return True

    def withdraw(self, ledger):
        if self.check_funds(ledger["amount"]):
            ledger["amount"] = -ledger["amount"]
            
            if not ledger["description"]:
                ledger["description"] = ""
            self.ledger.append(ledger)
            self.balance+=ledger["amount"]
            return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, another_budget):
        if self.check_funds(amount):
            self.withdraw({"amount":amount, "description":"Transfer to "+another_budget.name})
            another_budget.deposit({"amount":amount, "description":"Transfer from "+self.name})
            return True
    
def create_spend_chart(categories):
    spent_amounts = []
  
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))


    total = round(sum(spent_amounts), 2)
    spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))

    header = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    footer = "    " + "*" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.description, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (header + chart + footer).rstrip("\n")


