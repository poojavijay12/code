# def add(a,b):
#     print(f'Addition of {a} and {b} is {a + b}')
# add(5, 3)
# def subtract(a,b):
#     print(f'Subtraction of {a} and {b} is {a - b}')
# subtract(10, 4)
# def multiply(a,b):
#     print(f'Multiplication of {a} and {b} is {a * b}')  
# multiply(6, 7)

# def divide(a,b):
#     print(f'Division of {a} and {b} is {a / b}')
# divide(20, 4)

# def modulus(a,b):
#     print(f'Modulus of {a} and {b} is {a % b}')
# modulus(10, 3)


# def grade_marks(marks):
#     if marks >= 90:
#         print('A')
#     elif marks >= 80:
#         print('B')
#     elif marks >= 70:
#         print('C')
#     elif marks >= 60:
#         print('D')
#     else:
#         print('F')

# grade_marks(85)
# grade_marks(72)
# grade_marks(95)


# def even(num):
#     if num % 2 == 0:
#         print(f"{num} is even.")
#     else:
#         print(f"{num} is odd.")
# even(4)
# even(7)


# def check(x, y):
#     if x > 0 and y > 0:
#         print("Both numbers are positive.")
#     elif x < 0 or y < 0:
#         print("At least one number is negative.")
#     else:
#         print("Numbers include zero ")

# check(5, 10)
# # check(-3, 7)
# # check(0, 4)
# my_int1=10
# my_int2=0
# my_list1=[]
# my_list2=[1,2,3]
# my_set1=set()
# my_set2={10,20,30}
# my_dict1={}
# my_dict2={1:2,3:4}
# my_tuple1=(3,4,5,6)
# my_tuple2=()
# print(bool(my_int1))
# print(bool(my_int2))
# print(bool(my_list1))
# print(bool(my_list2))
# print(bool(my_set1))
# print(bool(my_set2))
# print(bool(my_dict1))
# print(bool(my_dict2))
# print(bool(my_tuple1))
# print(bool(my_tuple2))

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def print_details(self):
#         print(f"Car Details: {self.brand} {self.model}, Year: {self.year}")
# car1 = Car("THAR", "MS", 2022)
# car2 = Car("FORTUNER", "S", 2024)
# car1.print_details()
# car2.print_details()
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Fake in-memory database
fake_db = []

# Schema for user
class User(BaseModel):
    id: int
    name: str
    email: str

# Get all users
@app.get("/users")
def get_users():
    return {"name":"John Doe", "email":"abc@gmail.com","sal":"1000"}

