# Expense Sharing System

A Python-based expense-sharing application that helps groups of friends split costs fairly, track balances, and visualize settlements.

---

## 📌 Methodology

### Expense Splitting
- **Equal Contribution (Implemented)**  
  Each expense is divided equally among all participants.  
  Example: If a bill is ₹120 split among 3 friends, each owes ₹40.  
  - The payer’s balance increases by the full amount paid.  
  - Each participant’s balance decreases by their share.  

- **Weighted Contribution (Future Extension)**  
  Expenses can be split based on custom weights (e.g., 50%-30%-20%).  
  This allows flexibility for unequal contributions.

---

## 📊 Dataset & Preprocessing

### Data Structures
- **`balance_df`**: Pandas DataFrame storing each friend’s net balance.  
- **`expense_log`**: Pandas DataFrame recording each transaction (`Payer`, `Amount`, `Participants`).  

### Preprocessing Steps
- Input parsing: Friend names and participants are split by commas and stripped of whitespace.  
- Balances initialized to zero.  
- Each expense updates balances and logs the transaction.  

---

## 🔑 Key Insights & Special Cases

- **Refunds**: Positive balances indicate reimbursement owed to the payer.  
- **Missed Payments**: Non-participants are excluded from expense splitting.  
- **Edge Cases**:
  - Empty participant list → division by zero (should be handled).  
  - Payer not in friends list → validation required.  
  - `"all"` keyword can simplify participant entry.  

---

## 🧑‍💻 Data Science Implementation

### Libraries Used
- **Pandas**: Tabular data handling (`balance_df`, `expense_log`).  
- **NumPy**: Numerical operations (initializing balances).  
- **Matplotlib**: Visualizations (bar charts, settlement flows).  

### Analytics Features
- Track total expenses per user.  
- Track group-level spending.  
- Settlement algorithm computes minimal transactions to balance debts.  

### Visualizations
- **Balance Overview**: Bar chart showing net balances.  
- **Settlement Flow**: Horizontal bar chart showing “who pays whom.”  

---

## 📈 Results & Insights

### Sample Input
```text
Friends: Alice, Bob, Charlie
Expenses:
- Alice pays 120 for Alice, Bob, Charlie
- Bob pays 60 for Bob, Charlie

OUTPUT :

Settlement Details:
Charlie wants to pay Alice: Rs.70.00
Bob wants to pay Alice: Rs.10.00

Friend   Balance
Alice    80.0
Bob     -10.0
Charlie -70.0

Payer   Amount   Participants
Alice   120.0    Alice, Bob, Charlie
Bob      60.0    Bob, Charlie  
