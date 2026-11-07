import operator

# Q11. Tuple Indexing

colors = ("red", "green", "blue", "yellow", "purple")

second = colors[1]
last = colors[-1]
middle_three = colors[1:4]

print("Q11:", second, last, middle_three)


# Q12. Tuple Unpacking

employee = ("Ali", 28, "Data Engineer", 150000)

name, age, job, salary = employee

print("Q12 Name:", name)
print("Q12 Salary:", salary)


# Q13. Tuple Concatenation

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

combined = tuple1 + tuple2
reversed_tuple = combined[::-1]

print("Q13 Combined:", combined)
print("Q13 Reversed:", reversed_tuple)


# Q14. Count and Locate

numbers = (10, 20, 30, 20, 40, 20, 50)

count = numbers.count(20)
first_index = numbers.index(20)

print("Q14 Count:", count)
print("Q14 First Index:", first_index)


# Q15. Extended Tuple Unpacking

data = (100, 200, 300, 400, 500, 600)

first, second, *remaining, last = data

print("Q15 First:", first)
print("Q15 Second:", second)
print("Q15 Remaining:", list(remaining))
print("Q15 Last:", last)


# Q16. Modify an Immutable Tuple

numbers = (10, 20, 30, 40, 50)

new_numbers = numbers[:2] + (300,) + numbers[3:]

print("Q16:", new_numbers)


# Q17. Nested Tuple Access

students = (
    ("Ali", (85, 90, 88)),
    ("Sara", (92, 87, 95)),
    ("Ahmed", (78, 84, 80))
)

sara_second_score = students[1][1][1]

ali_average = sum(students[0][1]) / len(students[0][1])

ahmed_highest = max(students[2][1])

print("Q17 Sara Second Score:", sara_second_score)
print("Q17 Ali Average:", ali_average)
print("Q17 Ahmed Highest Score:", ahmed_highest)


# Q18. Tuple Sorting

employees = (
    ("Ali", 80000),
    ("Sara", 120000),
    ("Ahmed", 95000)
)

sorted_employees = tuple(
    sorted(employees, key=operator.itemgetter(1), reverse=True)
)

print("Q18:", sorted_employees)


# Q19. Tuple Matrix

matrix = (
    (2, 4, 6),
    (8, 10, 12),
    (14, 16, 18)
)

diagonal = (
    matrix[0][0],
    matrix[1][1],
    matrix[2][2]
)

diagonal_product = diagonal[0] * diagonal[1] * diagonal[2]

row_sums = (
    sum(matrix[0]),
    sum(matrix[1]),
    sum(matrix[2])
)

print("Q19 Diagonal:", diagonal)
print("Q19 Diagonal Product:", diagonal_product)
print("Q19 Row Sums:", row_sums)


# Q20. Inventory Tuple Challenge

records = (
    ("Laptop", 120000, 5),
    ("Mouse", 1500, 20),
    ("Keyboard", 3500, 10)
)

inventory_value = (
    records[0][1] * records[0][2]
    + records[1][1] * records[1][2]
    + records[2][1] * records[2][2]
)

most_expensive = max(records, key=operator.itemgetter(1))

product_names = (
    records[0][0],
    records[1][0],
    records[2][0]
)

reversed_names = product_names[::-1]

print("Q20 Inventory Value:", inventory_value)
print("Q20 Most Expensive:", most_expensive)
print("Q20 Reversed Names:", reversed_names)
