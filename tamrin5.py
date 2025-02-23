transactions = [
    ["Ali", 1001, 500000],
    ["Zahra", 1002, 200000],
    ["Mohammad", 1003, 0],
    ["Sara", 1004, 750000],
    ["Reza", 1005, 1500000],
    ["Mina", 1006, -1000000],
]
def check():
    transaction = []
    for i in transactions:
        if i[2] <= 0:
            continue
        transaction.append(i)
    return transaction
print(check())

#تعداد تراکنش های رد شده را در انتهای برنامه نمایش دهید
#گر تعداد تراکنش های نامعتبر از 2 مورد بیشتر شد، پیام "خطا: تعداد زیادی تراکنش نامعتبر شناسایی شد!" 
def display():
    invalid_transactions = [transaction for transaction in transactions if transaction[2] <= 0]
    if len(invalid_transactions) >= 2:
        return invalid_transactions, 'A large number of invalid transactions were detected.'
    return invalid_transactions
print(display())
