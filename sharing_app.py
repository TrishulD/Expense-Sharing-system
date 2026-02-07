import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class ExpenseSharing:
    def __init__(self, friends):
        self.friends = friends

        self.balance_df = pd.DataFrame({
            "Friend": friends,
            "Balance": np.zeros(len(friends))
        }).set_index("Friend")

        self.expense_log = pd.DataFrame(
            columns=["Payer", "Amount", "Participants"]
        )

    def add_expense(self, payer, amount, participants):
        split_amount = amount / len(participants)

        self.expense_log.loc[len(self.expense_log)] = [
            payer, amount, ", ".join(participants)
        ]

        for participant in participants:
            self.balance_df.loc[participant, "Balance"] -= split_amount

        self.balance_df.loc[payer, "Balance"] += amount

    # ---------------- SETTLEMENT LOGIC ----------------

    def get_settlement_transactions(self):
        creditors = []
        debtors = []
        transactions = []

        for friend, row in self.balance_df.iterrows():
            bal = row["Balance"]
            if bal > 0:
                creditors.append([friend, bal])
            elif bal < 0:
                debtors.append([friend, bal])

        while debtors and creditors:
            d, d_amt = debtors.pop()
            c, c_amt = creditors.pop()

            pay = min(abs(d_amt), c_amt)
            transactions.append((d, c, pay))

            if abs(d_amt) > pay:
                debtors.append([d, d_amt + pay])
            if c_amt > pay:
                creditors.append([c, c_amt - pay])

        return transactions

    def calculate_settlement(self):
        print("\nSettlement Details:")
        for d, c, amt in self.get_settlement_transactions():
            print(f"{d} wants to pay {c}: Rs.{amt:.2f}")

    # ---------------- VISUALIZATIONS ----------------

    def plot_balances(self):
        balances = self.balance_df["Balance"]

        plt.figure(figsize=(8, 5))
        bars = plt.bar(balances.index, balances.values)
        plt.axhline(0)

        plt.title("Final Balance Overview")
        plt.xlabel("Friends")
        plt.ylabel("Amount (Rs)")
        plt.grid(axis="y", linestyle="--", alpha=0.6)

        for bar in bars:
            h = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                h,
                f"{h:.2f}",
                ha="center",
                va="bottom" if h >= 0 else "top"
            )

        plt.tight_layout()
        plt.show()

    def plot_who_pays_whom(self):
        transactions = self.get_settlement_transactions()

        if not transactions:
            print("No settlements required.")
            return

        df = pd.DataFrame(
            transactions,
            columns=["Debtor", "Creditor", "Amount"]
        )

        labels = df["Debtor"] + " → " + df["Creditor"]

        plt.figure(figsize=(9, 5))
        bars = plt.barh(labels, df["Amount"])

        plt.title("Who Pays Whom (Settlement Flow)")
        plt.xlabel("Amount (Rs)")
        plt.ylabel("Transaction")
        plt.grid(axis="x", linestyle="--", alpha=0.6)

        for bar in bars:
            w = bar.get_width()
            plt.text(
                w,
                bar.get_y() + bar.get_height() / 2,
                f" Rs.{w:.2f}",
                va="center"
            )

        plt.tight_layout()
        plt.show()


# ---------------- MAIN ----------------

if __name__ == "__main__":
    friends = input("Enter friend names (comma separated): ").split(",")
    friends = [f.strip() for f in friends]

    expense_sharing = ExpenseSharing(friends)

    while True:
        payer = input("\nEnter payer name (or 'done'): ")
        if payer.lower() == "done":
            break

        amount = float(input("Enter amount paid: "))

        participants = input(
            "Enter participants (comma separated): "
        ).split(",")
        participants = [p.strip() for p in participants]

        expense_sharing.add_expense(payer, amount, participants)

    expense_sharing.calculate_settlement()
    expense_sharing.plot_balances()
    expense_sharing.plot_who_pays_whom()
