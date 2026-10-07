# NUMPY GROUP CHALLENGE — ANSWERS

import numpy as np

scores = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 88, 95],
    [55, 65, 70]
])


# 1. What does this array represent?
# ANSWER:
# It represents the scores of 4 students in 3 subjects.

print(scores)


# 2. How many students are represented?
# ANSWER:
# There are 4 students.
# The first dimension (rows) represents the students.

print(len(scores))


# 3. How many subjects/scores does each student have?
# ANSWER:
# Each student has 3 scores.

print(scores.shape[1])


# 4. What is the shape of this array?
# ANSWER:
# The shape is (4, 3).
# 4 = number of rows/students
# 3 = number of columns/subjects

print(scores.shape)


# 5. How can we get the first student's scores?
# ANSWER:
# Index 0 represents the first row.

print(scores[0])


# 6. How can we get the first score of the first student?
# ANSWER:
# [0, 0] means:
# first row = index 0
# first column = index 0

print(scores[0, 0])


# 7. How can we get all students' first scores?
# ANSWER:
# [:, 0] means:
# : = all rows
# 0 = first column

print(scores[:, 0])


# 8. How can we get the scores of the first two students?
# ANSWER:
# :2 selects rows from index 0 up to, but not including, index 2.

print(scores[:2])


# 9. How can we calculate the average of all the scores?
# ANSWER:
# np.mean() calculates the average of all values.

print(np.mean(scores))


# 10. How can we find the highest score?
# ANSWER:
# np.max() returns the largest value in the array.

print(np.max(scores))


# 11. How can we find the lowest score?
# ANSWER:
# np.min() returns the smallest value in the array.

print(np.min(scores))


# 12. Which questions require INDEXING?
# ANSWER:
# Question 5 and Question 6.
#
# Question 5:
print(scores[0])
#
# Question 6:
print(scores[0, 0])


# 13. Which questions require SLICING?
# ANSWER:
# Question 7 and Question 8.
#
# Question 7:
print(scores[:, 0])
#
# Question 8:
print(scores[:2])


# 14. Which questions require ARRAY OPERATIONS?
# ANSWER:
# Question 9, Question 10 and Question 11.
#
# Average:
print(np.mean(scores))
#
# Highest:
print(np.max(scores))
#
# Lowest:
print(np.min(scores))


# 15. Why is understanding the shape important?
# ANSWER:
# Shape tells us how the data is organized.
#
# For this example:
# (4, 3)
#
# 4 = rows/students
# 3 = columns/subjects
#
# Understanding the shape helps us know how to correctly
# access, slice and perform operations on the data.


# ============================================================
# FINAL UNDERSTANDING
# ============================================================

# NumPy concepts are connected:
#
# ARRAY
#   ↓
# Stores numerical data
#
# SHAPE
#   ↓
# Tells us how the data is organized
#
# INDEXING
#   ↓
# Allows us to access specific data
#
# SLICING
#   ↓
# Allows us to select a section of data
#
# OPERATIONS
#   ↓
# Allows us to calculate and analyze data
#
# MATRIX
#   ↓
# Allows us to work with data arranged in rows and columns
#
# PRACTICAL PROBLEM
#   ↓
# Combines all these concepts to solve a real problem


# IMPORTANT QUESTION FOR THE GROUP:
#
# "If I give you a NumPy array, can you explain its structure,
# access the data you need, select a section of the data,
# and perform calculations without memorizing commands?"
#
# If YES, then you are beginning to understand NumPy,
# not just memorize NumPy syntax.