
print(5+5+5)
print(6+6+6)
print (7+7+7)
print (8+8+8)


# Define a class called "Person"
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def greet(self):
    print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object of the Person class
person1 = Person("Alice", 30)

# Access object attributes
print(person1.name)  # Output: "Alice"
print(person1.age)   # Output: 30

# Call object method
person1.greet()  # Output: "Hello, my name is Alice and I am 30 years old."

# Create another object of the Person class
person2 = Person("Bob", 35)
person2.greet()  # Output: "Hello, my name is Bob and I am 35 years old."

