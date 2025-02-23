student = [
    ["ali", 18.5, "computer", 17],
    ["zahra", 19.2, "graphic", 16],
    ["mohammad", 17.8, "mechanic", 18],
    ["sara", 18.0, "hesabdari", 17]
]
# یک هنرجوی جدید به نام "رضا" با سن ،16 رشته "الکترونیک" و معدل 17.5 به لیست اضافه کنید.
def plus(x):
    student.append(x)
    return student
plus(["reza", 17.5, "electronic", 16])

#هنرجویی که معدل او کمتر از 18 است، از لیست حذف کنید.
def minus(x): #نمره شرط را میگیرد که در اینجا 18 است
  for i in student:
      if i[1] < x:
        student.remove(i)
  return(student)
minus(18)    

#لیست را بر اساس معدل از بیشترین به کمترین مرتب کنید
def get_grade(stu):
     return stu[1]
# مرتب کردن لیست تودرتو بر اساس نمره (ایندکس 2)
student.sort(key= get_grade, reverse= True)

#هنرجویی به نام "زهرا" در کدام ایندکس لیست قرار دارد؟ 
def search():
    for i in student:
        if "sara" in i:
            return(student.index(i))
x = search()
print(x)

#چند هنرجو در رشته "کامپیوتر" تحصیل می کنند؟
def SearchComputer():
    x=0
    for i in student:
        if "computer" in i:
            x += 1
    return x
print(SearchComputer())

#یک تابع بنویسید که نام هنرجو را بگیرد و اطالعات او را از لیست نمایش دهد.
def info(name):
    for i in student:
        if i[0] == name:
            return i
print(info("ali"))

#اگر معدل باالترین هنرجو کمتر از 19 بود، به او 0.5نمره تشویقی بدهید. 
def find_add():
    top_student = student[0]  # فرض کنیم اولین دانشجو بالاترین نمره را دارد
    for i in student:
        if i[1] > top_student[1]:
            top_student = i
    if top_student[1] < 19:
        top_student[1] += 0.5
    return top_student
print(find_add())

    
