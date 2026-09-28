name = input("Enter your name: ")
age = int(input("Enter your age: "))
favorite_number = int(input("Enter your favorite number: "))

user_age_10_years = age + 10
square_of_favorite_number = favorite_number ** 2
favorite_number_format = "odd" if favorite_number % 2 != 0 else "even"

print(user_age_10_years)
print(square_of_favorite_number)
print(favorite_number_format)

print(f"Hi, {name}! In 10 years, you will be {user_age_10_years}. Your favorite number squared is {square_of_favorite_number}, and it is {favorite_number_format}.")

"""

I think because String is safer to has as an input, 
because it can be converted to any other type. 
It takes input as a string and then give programmer the ability to how to use that data.

"""