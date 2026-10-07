# NUMPY FOUNDATION LEVEL — GROUP QUESTIONS

# 1. What is NumPy?
# - What is NumPy in your own words?
# - Is NumPy a programming language or a Python library?
# - What problem was NumPy designed to solve?

# 2. Why is NumPy used?
# - Why would we use NumPy instead of normal Python lists?
# - What makes NumPy useful when working with large amounts of numerical data?
# - Give one real-world situation where NumPy would be useful.

# 3. Creating Arrays
# - What is an array?
# - How do we create a NumPy array?
# - What is the difference between a Python list and a NumPy array?
# - Why would we convert a list into a NumPy array?

# 4. Shape
# - What does the shape of an array mean?
# - What is the difference between a 1D and 2D array?
# - If an array has shape (4, 3), what do the 4 and 3 represent?
# - How can we find the shape of an array?

# 5. Indexing
# - What is indexing?
# - How do we access one specific element of an array?
# - Why does Python start counting indexes from 0?
# - What would happen if we tried to access an index that does not exist?

# 6. Slicing
# - What is the difference between indexing and slicing?
# - How can we select several elements from an array?
# - What does array[1:4] mean?
# - How can slicing be useful when working with real-world data?

# 7. Basic Operations
# - Can we perform mathematical operations directly on NumPy arrays?
# - What happens when we add, subtract, multiply or divide arrays?
# - How can we calculate the mean, maximum and minimum of an array?
# - Why is performing operations on an entire array useful?

# 8. Basic Matrix Concepts
# - What is a matrix?
# - How is a matrix different from a normal 1D array?
# - What are rows and columns?
# - If a matrix has shape (4, 3), how many rows and columns does it have?
# - Where are matrices used in real-world technology?

# 9. CONNECTING EVERYTHING
# - How are arrays, shape, indexing, slicing, operations and matrices connected?
# - If we understand only the commands but do not understand the structure of the data,
#   can we really say that we understand NumPy?
# - What problem does each NumPy concept solve?

# 10. GROUP CHALLENGE

import numpy as np

scores = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 88, 95],
    [55, 65, 70]
])

# Discuss these questions as a group:

# 1. What does this array represent?
# 2. How many students are represented?
# 3. How many subjects/scores does each student have?
# 4. What is the shape of this array?
# 5. How can we get the first student's scores?
# 6. How can we get the first score of the first student?
# 7. How can we get all students' first scores?
# 8. How can we get the scores of the first two students?
# 9. How can we calculate the average of all the scores?
# 10. How can we find the highest score?
# 11. How can we find the lowest score?
# 12. Which questions above require indexing?
# 13. Which require slicing?
# 14. Which require array operations?
# 15. Why is understanding the shape important before working with this data?

# FINAL DISCUSSION QUESTION:
#
# "Don't just tell us what each NumPy command does.
# Explain WHAT PROBLEM each concept solves and HOW the concepts
# connect to one another."