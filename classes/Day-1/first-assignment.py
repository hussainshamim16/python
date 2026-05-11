# 1. Ek string variable banayein jisme aapka full name ho, aur usse poora CAPITAL letters mein print karein.
name = "Muhammad Hussain"
print(name.upper())

# 2. User se unka fav fruit poochiye aur uski length (kitne characters hain) print karein.
fruit = input("Enter your favorite fruit: ")
print(len(fruit))

# 3. Ek sentence likhiye 'Python is fun' aur 'fun' ko 'awesome' se replace karke print karein.
sentence = 'Python is fun'
print(sentence.replace('fun', 'awesome'))

# 4. Check karein ke string 'Hello World' mein 'World' kaunse index par start hota hai.
s = 'Hello World'
print(s.find('World'))

# 5. User se unka email address lein aur usse hamesha small letters (lowercase) mein convert karke dikhayein.
email = input("Enter your email: ")
print(email.lower())

# 6. Ek sentence 'Python Programming' banayein aur uske extra spaces (suru aur aakhir ke) remove karein.
s = '  Python Programming  '
print(s.strip())

# 7. Ek string 'Welcome to coding' mein count karein ke 'o' letter kitni baar aaya hai.
s = 'Welcome to coding'
print(s.count('o'))

# 8. User se unki age input lein aur usse integer mein convert karke print karein.
age = input("Enter your age: ")
print(int(age))

# 9. Ek float value '15.99' ko integer mein convert karein. Output kya aaya?
print(int(15.99))  # Output 15

# 10. Do numbers ko input lein, dono ko add karein, lekin dhayan rahe input hamesha string hota hai, isliye unhe cast karein.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)

# 11. Ek integer 100 ko string mein convert karein aur check karein ke uska type ab 'str' hai ya nahi.
num = 100
num_str = str(num)
print(type(num_str) == str)

# 12. User se price lein (99.5) aur usse integer mein badal kar dikhayein.
price = float(input("Enter price: "))
print(int(price))

# 13. Ek string '10' aur doosri string '20' ko add (concatenate) karne ki jagah math wala addition (30) karke dikhayein.
a = '10'
b = '20'
print(int(a) + int(b))

# 14. Ek variable mein '50.5' save karein aur usse float mein cast karne ke baad 10 plus karein.
val = '50.5'
print(float(val) + 10)

# 15. User se uska naam aur shehar (city) ka naam poochiye aur ek sentence print karein: 'Hello [Name], welcome to [City]'.
name = input("Enter your name: ")
city = input("Enter your city: ")
print(f"Hello {name}, welcome to {city}")
print("Hello" ,name, "welcome to" ,city)

# 16. User se do numbers lein aur unka product (multiply) print karein.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a * b)

# 17. User se unka favorite color poochiye aur print karein: 'I also like [color]'.
color = input("Enter your favorite color: ")
print(f"I also like {color}")

# 18. Ek chota program banayein jo user se uska birth year le aur uska current age calculate karein.
birth_year = int(input("Enter your birth year: "))
current_year = 2025
print(f"Your age is: {current_year - birth_year}")

# 19. User se ek word input lein aur usse 5 baar print karein (string multiplication use karke).
word = input("Enter a word: ")
print(word * 5)

# 20. User se unka mobile number lein (as string) aur unhe batayein ke unhone kya number type kiya hai.
mobile = input("Enter your mobile number: ")
print(f"You entered: {mobile}")

# 21. Do variables lein a=10, b=3. Inka remainder (modulo) nikal kar dikhayein.
a, b = 10, 3
print(a % b)

# 22. Check karein ke 15, 10 se bada hai AUR 20 se chota hai (Logical AND operator).
print(15 > 10 and 15 < 20)

# 23. User se ek number lein aur check karein ke wo 100 se bada hai ya nahi (Comparison operator).
num = int(input("Enter a number: "))
print(num > 100)

# 24. 2 ki power 5 (2^5) calculate karke print karein.
print(2 ** 5)

# 25. Check karein ke kya 50, 100 ke barabar hai (Equal to operator).
print(50 == 100)

# 26. Do Boolean values (True, False) lein aur 'OR' operator ka result dikhayein.
print(True or False)

# 27. User se ek number lein aur check karein ke wo Positive hai ya Negative.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 28. Check karein ke user ki age 18 se zyada hai ya nahi, agar hai toh print 'Eligible for Vote'.
age = int(input("Enter your age: "))
if age > 18:
    print("Eligible for Vote")
else:
    print("Ap Vote Nhi sey sakty hen")

# 29. Ek number input lein aur check karein ke wo Even hai ya Odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 30. User se do numbers lein aur batayein dono mein se bada (Greater) kaunsa hai.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(a)
else:
    print(b)

# 31. Ek student ke marks input lein. Agar marks 33 se zyada hain toh 'Pass', warna 'Fail'.
marks = int(input("Enter marks: "))
if marks > 33:
    print("Pass")
else:
    print("Fail")

# 32. Check karein ke user ne jo string input ki hai wo empty toh nahi hai.
s = input("Enter something: ")
if s == "":
    print("Empty string")
else:
    print("Not empty")

# 33. User se ek password input lein. Agar password 'python123' hai toh 'Access Granted', warna 'Wrong Password'.
password = input("Enter password: ")
if password == 'python123':
    print("Access Granted")
else:
    print("Wrong Password")

# 34. Check karein ke user ka input kiya hua number zero hai ya nahi.
num = int(input("Enter a number: "))
if num == 0:
    print("Zero")
else:
    print("Not zero")

# 35. Student Grading System: 90+ (A), 80-89 (B), 70-79 (C), below 70 (D).
marks = int(input("Enter marks: "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("D")

# 36. User se temperature lein. Agar 30 se zyada hai toh 'Hot', 15-30 hai toh 'Warm', 15 se niche hai toh 'Cold'.
temp = int(input("Enter temperature: "))
if temp > 30:
    print("Hot")
elif temp >= 15:
    print("Warm")
else:
    print("Cold")

# 37. Ek number check karein ke wo 3 se divisible hai, 5 se divisible hai, ya dono se (FizzBuzz logic).
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

# 38. User se ek character lein aur check karein ke wo Vowel (a, e, i, o, u) hai ya Consonant.
ch = input("Enter a character: ").lower()
if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

# 39. Bill Calculator: Agar shopping 5000 se upar hai toh 20% discount, 2000-5000 par 10% discount, warna No discount.
amount = float(input("Enter shopping amount: "))
if amount > 5000:
    print(amount * 0.8)
elif amount >= 2000:
    print(amount * 0.9)
else:
    print(amount)

# 40. Ek person ki age check karein: 0-12 (Child), 13-19 (Teenager), 20-59 (Adult), 60+ (Senior Citizen).
age = int(input("Enter age: "))
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")

# 41. Check karein ke ek saal (year) Leap Year hai ya nahi.
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 42. User se week number (1-7) lein aur corresponding day (Monday, Tuesday...) print karein.
day_num = int(input("Enter week number (1-7): "))
if day_num == 1:
    print("Monday")
elif day_num == 2:
    print("Tuesday")
elif day_num == 3:
    print("Wednesday")
elif day_num == 4:
    print("Thursday")
elif day_num == 5:
    print("Friday")
elif day_num == 6:
    print("Saturday")
elif day_num == 7:
    print("Sunday")
else:
    print("Invalid")

    
# 43. Ek simple calculator banayein (+,-, *, /) symbols ke basis par operation perform karein.
a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print("Invalid operator")

# 44. User ka weight aur height le kar BMI category batayein (Underweight, Normal, Overweight).
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
else:
    print("Overweight")

# 45. ATM Machine Logic: Pehle PIN check karein, agar sahi ho toh Amount poochiye, agar account balance se kam amount ho toh 'Withdrawal Success'.
pin = input("Enter PIN: ")
balance = 5000
if pin == "1234":
    amount = float(input("Enter amount: "))
    if amount <= balance:
        print("Withdrawal Success")
    else:
        print("Insufficient balance")
else:
    print("Wrong PIN")

# 46. Login System: Pehle Username check karein, agar match ho tabhi Password check karein.
username = input("Enter username: ")
if username == "admin":
    password = input("Enter password: ")
    if password == "admin123":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# 47. Largest of Three: User se 3 numbers lein aur nested if-else use karke sabse bada number dhoondein.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if b >= c:
        print(b)
    else:
        print(c)

# 48. Ticket Booking: Pehle age check karein. Agar 18+ hai toh check karein 'Do you have ID?'. Agar ID hai toh 'Ticket Issued'.
age = int(input("Enter age: "))
if age >= 18:
    id_proof = input("Do you have ID? (yes/no): ")
    if id_proof == "yes":
        print("Ticket Issued")
    else:
        print("ID required")
else:
    print("Underage")

# 49. Admission System: Agar student ke marks 80+ hain, toh check karein unka interview clear hai ya nahi. Dono clear hone par 'Admission Done'.
marks = int(input("Enter marks: "))
if marks >= 80:
    interview = input("Interview cleared? (yes/no): ")
    if interview == "yes":
        print("Admission Done")
    else:
        print("Interview failed")
else:
    print("Marks insufficient")

# 50. Number Range: Check karein number positive hai ya nahi. Agar positive hai, toh check karein wo 100 se bada hai ya chota.
num = int(input("Enter a number: "))
if num > 0:
    if num > 100:
        print("Greater than 100")
    else:
        print("Less than or equal to 100")
else:
    print("Negative or zero")

# 51. Restaurant Order: Pehle Veg ya Non-Veg poochein. Veg mein Paneer ya Dal, Non-Veg mein Chicken ya Mutton ka option dein.
choice = input("Veg or Non-Veg? ").lower()
if choice == "veg":
    dish = input("Paneer or Dal? ").lower()
    print(f"You ordered {dish}")
elif choice == "non-veg":
    dish = input("Chicken or Mutton? ").lower()
    print(f"You ordered {dish}")
else:
    print("Invalid choice")

# 52. Ek number input lein aur check karein ke wo Single digit hai, Double digit ya Triple digit.
num = int(input("Enter a number: "))
if -9 <= num <= 9:
    print("Single digit")
elif -99 <= num <= 99:
    print("Double digit")
elif -999 <= num <= 999:
    print("Triple digit")
else:
    print("More than triple digit")

# 53. User se salary aur service years lein. Agar service 5 saal se zyada hai toh 5% bonus calculate karke final salary batayein.
salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))
if years > 5:
    bonus = salary * 0.05
    print(f"Final salary: {salary + bonus}")
else:
    print(f"Salary: {salary}")

# 54. Ek triangle ki teen sides input lein aur batayein ke wo Equilateral, Isosceles ya Scalene hai.
a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

# 55. Month name check karke batayein ke us month mein kitne days hote hain (Jan, Feb…).
month = input("Enter month name: ").lower()
if month in ["jan", "mar", "may", "jul", "aug", "oct", "dec"]:
    print("31 days")
elif month in ["apr", "jun", "sep", "nov"]:
    print("30 days")
elif month == "feb":
    print("28 or 29 days")
else:
    print("Invalid month")

# 56. Nested If-Else se check karein ke ek number Even hai aur 50 se bada hai, ya Even hai aur 50 se chota hai.
num = int(input("Enter a number: "))
if num % 2 == 0:
    if num > 50:
        print("Even and greater than 50")
    else:
        print("Even and less than or equal to 50")
else:
    print("Odd")

# 57. Student Result: Maths aur Science dono mein 40+ hone chahiye pass hone ke liye. Agar ek mein kam hain toh batayein kaunsa subject weak hai.
maths = int(input("Maths marks: "))
science = int(input("Science marks: "))
if maths >= 40 and science >= 40:
    print("Pass")
elif maths < 40 and science < 40:
    print("Weak in both subjects")
elif maths < 40:
    print("Weak in Maths")
else:
    print("Weak in Science")

# 58. Electricity Bill: Pehle 100 units free, next 100 units Rs 5/unit, uske baad Rs 10/unit.
units = int(input("Enter units consumed: "))
if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 5
else:
    bill = (100 * 5) + (units - 200) * 10
print(f"Bill: Rs {bill}")

# 59. Game Level: Score 0-50 (Beginner), 51-100 (Intermediate). Agar Intermediate hai toh check karein user ne boss level par kiya hai ya nahi.
score = int(input("Enter score: "))
if 0 <= score <= 50:
    print("Beginner")
elif 51 <= score <= 100:
    print("Intermediate")
    boss = input("Did you complete boss level? (yes/no): ")
    if boss == "yes":
        print("Proceed to next level")
    else:
        print("Defeat boss to proceed")
else:
    print("Invalid score")

# 60. Final Challenge: Ek mini-project logic banayein jisme user se Username, Password, aur ek Security Question poochein nested loops aur if-else ke saath.
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "pass123":
    sq = input("What is your pet's name? ")
    if sq.lower() == "tommy":
        print("Access Granted")
    else:
        print("Security answer wrong")
else:
    print("Invalid credentials")
