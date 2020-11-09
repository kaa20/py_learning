from week_4.solution_w4_ex2 import Value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission

new_account = Account(0.1)
new_account.amount = 100

print(new_account.amount)