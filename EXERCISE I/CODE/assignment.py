# Project 111: Water Quality Tests
from array import array

print("=== Project 111: Water Quality Tests ===\n")

# ---------------- Integers ----------------
# Input integer values related to Water Quality Tests
test_values = [78, 85, 92, 67, 88]  # sample scores or test results

total = sum(test_values)
average = total / len(test_values)
minimum = min(test_values)
maximum = max(test_values)

print("---- Integers ----")
print(f"Values: {test_values}")
print(f"Total = {total}, Average = {average:.2f}, Min = {minimum}, Max = {maximum}\n")

# ---------------- Strings ----------------
print("---- Strings ----")
report = (
    f"Water Quality Test Report\n"
    f"Total Results: {total}\n"
    f"Average Result: {average:.2f}\n"
    f"Highest Score: {maximum}, Lowest Score: {minimum}"
)
print(report, "\n")

# ---------------- Booleans ---------------
print("---- Booleans ----")
threshold = 80
# Compound condition: above threshold AND max above 90
if average > threshold and maximum > 90:
    print("Status: Above Standard \n")
else:
    print("Status: Below Standard \n")

# ---------------- Lists ----------------
print("---- Lists ----")
tests_list = ["pH", "Turbidity", "Nitrate", "Chlorine"]
print("Original list:", tests_list)

# Add a new element
tests_list.append("Fluoride")
# Remove one element if condition is met (remove "Nitrate")
if "Nitrate" in tests_list:
    tests_list.remove("Nitrate")

print("Modified list before sort:", tests_list)
tests_list.sort()
print("Sorted list:", tests_list, "\n")

# ---------------- Arrays ----------------
print("---- Arrays ----")
# Store subset of numeric data
test_array = array('i', [78, 85, 92])  # integers only
array_sum = sum(test_array)
list_sum = sum(test_values)

print("Array values:", test_array.tolist())
print(f"Array Sum = {array_sum}, List Sum = {list_sum}")
print("Comparison:", "Equal" if array_sum == list_sum else "Not Equal", "\n")

# ---------------- Dictionaries ----------------
print("---- Dictionaries ----")
records = [
    {"id": 1, "name": "pH", "value": 78},
    {"id": 2, "name": "Turbidity", "value": 85},
    {"id": 3, "name": "Nitrate", "value": 92},
]

print("Original Records:", records)

# Update one record
records[0]["value"] = 80  # update pH
# Delete one record
records = [rec for rec in records if rec["id"] != 2]

# Compute total value
total_values = sum(rec["value"] for rec in records)

print("Updated Records:", records)
print("Total of values:", total_values)
