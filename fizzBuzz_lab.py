Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
ef fizz_buzz(n):
  """
  Return fizz when n is divisible by 3
  Return buzz when n is divisible by 5
  Return fizzbuzz when n is divisible by both 3 and 5
  """
  
  if not isinstance(n, int):
    return 'Enter an integer'
    
  elif n % 3 == 0 and n % 5 == 0:
    return 'FizzBuzz'
  
  elif n % 3 == 0:
    return 'Fizz'
    
  elif n % 5 == 0:
    return 'Buzz'
  
  else:
    return n
