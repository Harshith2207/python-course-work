'''1. Right-Angled Triangle Using Nested Loop
*
**
***
****
*****
'''
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

'''2. Right-Angled Triangle (Decreasing Stars)
*****
****
***
**
*
'''
rows = 5
for i in range(rows, 0, -1):
    print("*" * i)

'''3. Square Pattern
****
****
****
****
'''
rows = 4
for i in range(rows):
    print("*" * rows)

'''4. Rectangle Pattern
******
******
******
'''
rows = 3
cols = 6
for i in range(rows):
    print("*" * cols)

'''5. Pyramid Pattern
    *
   ***
  *****
 *******
*********
'''
rows = 5
for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

'''6. Inverted Pyramid Pattern
*********
 *******
  *****
   ***
    *
'''
rows = 5
for i in range(rows, 0, -1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

'''7. Right-Aligned Triangle
    *
   **
  ***
 ****
*****
'''
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)

'''8. Left-Aligned Inverted Triangle
*****
****
***
**
*
'''
rows = 5
for i in range(rows, 0, -1):
    print("*" * i)

'''9. Diamond Pattern
   *
  ***
 *****
*******
 *****
  ***
   *
'''
rows = 4
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
