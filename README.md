# binary_tree_avarage_value_of_each_level
Calculate avarage value of nodes reside in each level of a binary tree

# Problem Statement:
For any given binary tree, calculate avarage value of nodes reside in each level.

Example:
```
Input:
  3         --> level 0, avarage 3
|   | 
9   20      --> level 1, avarage 14.5
   |  |
  15  17    --> level 2, avarage 11

Output: [3, 14.5, 11]
```
# Solution:
- Determine each nodes in each level using bfs algorithm
- Calculate avarage values of each level
- Return result