class ExpenseSharing:
    def __init__(self, friends):
        self.friends = friends
        self.balance = {friend: 0 for friend in friends}

    def add_expense(self, payer, amount, participants):
        split_amount = amount / len(participants)
        for participant in participants:
            self.balance[participant] -= split_amount
        self.balance[payer] += amount

    def calculate_settlement(self):
        creditors = []
        debtors = []

        for friend, balance in self.balance.items():
            if balance > 0:
                creditors.append((friend, balance))
            elif balance < 0:
                debtors.append((friend, balance))

        while debtors and creditors:
            debitor, debt_amount = debtors.pop()
            creditor, credit_amount = creditors.pop()

            payment = min(abs(debt_amount), credit_amount)
            print(f"{debitor} wants to paid {creditor}: Rs.{payment:.2f}")

            if abs(debt_amount) > payment:
                debtors.append((debitor, debt_amount + payment))  # debt_amount is negative
            if credit_amount > payment:
                creditors.append((creditor, credit_amount - payment))


if __name__ == "__main__":
    friends = input("Enter the names of friends, separated by commas: ").split(",")
    friends = [friend.strip() for friend in friends]

    expense_sharing = ExpenseSharing(friends)

    while True:
        payer = input("Enter the name of the person who paid (or type 'done' to finish): ")
        if payer.lower() == 'done':
            break

        amount = float(input("Enter the amount paid: "))

        participants = input("Enter the names of the participants, separated by commas: ").split(",")
        participants = [participant.strip() for participant in participants]

        expense_sharing.add_expense(payer, amount, participants)

    print("\nFinal Settlement")
    expense_sharing.calculate_settlement()