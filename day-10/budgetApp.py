class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = f"{item['description'][:23]:23}"
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    total_spent = 0
    category_spending = []

    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        category_spending.append(spent)
        total_spent += spent

    percentages = [(spend / total_spent) * 100 for spend in category_spending]

    chart = ""
    for i in range(100, -1, -10):
        chart += f"{i:>3}| " + "  ".join("o" if percent >= i else " " for percent in percentages) + "  \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_len) for category in categories]

    for i in range(max_len):
        chart += "     " + "  ".join(name[i] for name in names) + "  \n"

    return title + chart.rstrip("\n")
