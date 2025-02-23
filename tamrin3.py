menu = ["smoti", "moka", "hot chocolate", "tea", "coffee"]
orders = []

#هنگام دریافت سفارش، بررسی کند که آیا نوشیدنی موردنظر در منو هست یا نه.
# تابع برای افزودن سفارش
def add_order(order):
    if order in menu:
        orders.append(order)
    else:
        return("order not in menu.")
    return order
    
add_order("smoti")
add_order("coffee")
add_order("coffee")
add_order("pizza")
add_order("tea")
add_order("hot chocolate")
add_order("hot chocolate")
add_order("hot chocolate")
add_order("hot chocolate")
add_order("hot chocolate")
add_order("hot chocolate")
print(orders)


#یک هنرجو سفارش خود را لغو میکند
def minus(order):
    if order in orders:
        orders.remove(order)
    return orders

#کافه قصد دارد پرفروشترین نوشیدنی را شناسایی کند.

#یک مشتری میخواهد بداند که سفارش او در چه موقعیتی قرار دارد .
def find_index(lst, order):
    if order in lst:
        x = lst.index(order)        
        return x
    else:
        return("order is not in list.")
print(find_index(orders, "coffee"))

#لیست سفارشات را به ترتیب حروف الفبا مرتب کنید.
def sorting(lst):
    lst.sort()
    return lst
print(sorting(orders))

#همهی سفارشات روز را پاک کنید تا برای روز بعد آماده شوید
def clearAll():
    orders.clear()
    return orders
print(clearAll())

#"اگر نوشیدنی "هات چاکلت" بیش از 5 بار سفارش داده شد، پیام ارسال شود "هات چاکلت پرفروشترین آیتم امروز 
def find(lst, item):# کد من درست کار نمیکنه اگه مشکلو متوجه شدن حتما بگید
    count = 0
    for i in lst:
        if i == item:
            count += 1
    if count > 5:
        return f"best selling item is {item}"
print(find(orders, 'hot chocolate'))