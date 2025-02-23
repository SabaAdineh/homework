accounts = [
    ["Ali", "1001", 5000000],
    ["Zahra", "1002", 8200000],
    ["Mohammad", "1003", 2300000],
    ["Sara", "1004", 12500000]
]
#حسابهایی که کمتر از 3 میلیون تومان موجودی دارن نمایش دهد
def find_less_than_3milion(lst):
    for i in accounts:
        if i[2] <= 3000000:
            return i
print(find_less_than_3milion(accounts))

#ر کل موجودی بانک را حساب کنید
def find_money(lst):
    return sum(i[2] for i in lst)  # جمع موجودی تمام حساب‌ها

print(find_money(accounts))

# جستجوی حساب
def find_account(account):
    for i in accounts:
        while account in i[1]:
            return i
print(find_account("1004"))

def takeOut(id, money):
    for i in accounts:
        if id == i[1]: 
            if i[2] >= money:  
                i[2] -= money  
                return f"New balance: {i[2]}"  
            else:
                return "Cannot take out: Insufficient balance"  
    return "ID is not available"  

print(takeOut("1003", 20))  
print(takeOut("1003", 3000000)) 
print(takeOut("1005", 20))  

#وام اگه بیش از 10 میلیون بود
def check_accounts(id):
     found = False
     for account in accounts:
        if account[1] == id:
            found = True
            if account[2] > 10000000:
                print(f"حساب با شماره {id} واجد شرایط دریافت وام است!")
            else:
                print(f"حساب با شماره {id} موجودی کافی برای وام ندارد.")
            break
        
    # اگر حساب پیدا نشد
     if not found:
            print(f"حساب با شماره {id} یافت نشد.")

    # بررسی نهایی اگر هیچ حسابی با موجودی بیش از ۱۰ میلیون نبود
     if not any(account[2] > 10000000 for account in accounts):
        print("حسابی با موجودی بالای ۱۰ میلیون یافت نشد.")

check_accounts(1003)
