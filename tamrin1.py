#_____________question1
stu = [
    ["Saba", 19.99, 15, "computer"],
    ["Parnia", 18, 17, "computer"],
    ["Gojo", 3.5, 28, "computer"],
    ["Eren", 15.25, 18, "computer"],
    ["levi", 20, 39, "computer"]
]
stu.append(["Mike", 5, 17, "computer"])

stu.remove(["Parnia", 18, 17, "computer"])

stu.sort()
stu.reverse()
copy_stu = stu.copy()
# پیدا کردن شاگردی که بیشترین نمره را دارد
top_student = stu[0]  # فرض کنیم اولین دانشجو بالاترین نمره را دارد
for i in stu:
    if i[1] > top_student[1]:
        top_student = i
# حذف شاگرد با بیشترین نمره از لیست
stu.remove(top_student)
# اضافه کردن شاگرد با بیشترین نمره به بالای لیست
stu.insert(0, top_student)


stu = [i for i in stu if i[1] >= 18]   #هنرجو با نمره کمتر از 18 را حذف میکند

index = stu.index(["Saba", 19.99, 15, "computer"])

# تعداد هنرجویانی که در رشته ی "کامپیوتر " تحصیل میکنند
count_of_computer= 0
for i in stu:
    count_of_computer += i.count("computer")

#لیستی از نمرات معدل هنرجویان را ایجاد کنید
scores=[]
for i in stu:
  for j in i:
     scores.append(i[2])
print(stu, index, count_of_computer, scores)
stu.clear()

scores=[] #قرار دادن نمرات در لیستی جداگونه
for i in stu:
     scores.append(i[1])
print(scores)