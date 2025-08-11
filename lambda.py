# A simple lambda function to add two numbers
add = lambda x, y: x + y
print(f"Lambda sum: {add(5, 7)}")

# Lambda used with sorted() to sort a list of tuples by the second element
students = [('Alice', 25), ('Bob', 20), ('Charlie', 30)]
sorted_students = sorted(students, key=lambda student: student[1])
print(f"Sorted students by age: {sorted_students}")

# Lambda used with filter() to get even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda num: num % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")
