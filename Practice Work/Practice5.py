#1
''' print the below pattern
*****
 ****
  ***
   **
    *
'''
n=int(input("Enter the size: "))
for row in range(n):
    print(' '*row,end='')
    print("*"*(n-row),end='')
    print()

#2
''' print the below pattern 
*
**
***
**
*
'''
n=int(input("Enter the size: "))
for row in range(n):
    if row<=n//2:
        print("*"*(row+1),end='')
    else:
        print("*"*(n-row),end='')
    print()

#3
'''print the below pattern
*****
*   *
*   *
*   *
*****
'''
n=int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()

#4
'''print the below pattern 
*****
* * *
*****
* * *
*****
'''
n=int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1 or row==n//2 or col==n//2:
            print("*",end='')
        else:
            print(" ",end='')
    print()

#5
'''print the below pattern
*      *
 *    *
  *  *
   **
   **
  *  *
 *    *
*      *
'''
n=int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if row==col or row+col==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()

#6
'''print the below pattern
*******   
   *       
   *       
   *       
   *       
   *       
*******
'''
n=int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==n//2:
            print("*",end='')
        else:
            print(" ",end='')
    print()

#7
'''print the below pattern
*     *
*     *
*     *
*******
*     *
*     *
*     *
'''
n=int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==n//2:
            print("*",end='')
        else:
            print(" ",end='')
    print()

#8
'''print the below pattern
 ***** 
*      
*      
*******
      *
      *
*******

'''
n = int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if ((row == 0 and col != 0) or (row == n // 2) or (row == n - 1) or (col == 0 and row <= n // 2) or (col == n - 1 and row >= n // 2)):
            print("*", end="")
        else:
            print(" ", end="")
    print()

#9
'''print the below pattern
*******
*  *  *
*  *  *
*******
*  *  *
*  *  *
*******

'''
n=int(input("Enter the number: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n//2 or col==n//2 or col==0 or col==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()

#10
'''print the below pattern
*                         *
 *                       * 
  *                     *  
   *                   *   
    *                 *    
     *               *     
      *             *      
       *           *       
        *         *        
         *       *         
          *     *          
           *   *           
            * *            
             *             
'''
n=int(input("Enter the Number: "))
for rows in range(n):
    for col in range(n*2):
        if col==rows or col==(n*2-rows-1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
