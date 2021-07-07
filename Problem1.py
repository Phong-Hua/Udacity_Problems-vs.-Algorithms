"""
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:
"""

def sqrt(number):
   """
   Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
   """
   

   def binary_search(target, start, end):
      """
      Using binary search, and find a number within range(start, from) satisfy number**2 = target.
      """
      if start is None or end is None or start > end:
         return None
      center = (start + end) // 2
      center_square = center**2
      
      if center_square == target:
         return center
      elif center_square < target:  
         center_next_square = (center+1)**2
         if center_next_square > target:
            return center
         else:
            return binary_search(target, center+1, end)
      else:
         return binary_search(target, start, center)
      



   if number == None or type(number) is not int or number < 0:
      return None
   if number < 2:
      return number

   return binary_search(number, 0, number)

print ("Pass" if  (None == sqrt(None)) else "Fail")
print ("Pass" if  (None == sqrt('Hello')) else "Fail")
print ("Pass" if  (None == sqrt(-1)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
