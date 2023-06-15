def greet():
    print("hello")
    print("How are you doing?")
    print("Hope you are good?")

#creating a function with on input
def greet_with_name(name):
    print(f"hello {name}")
    print(f"How are you {name}?")

#creating a function with two inputs
def greet_with_name_and_location(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with_name_and_location("Albert","Kumasi")

greet_with_name_and_location(name="rise", location ="earth")