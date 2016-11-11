Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
def data_type(n):
  if isinstance (n , str):
    return len(n)
  elif n is None:
    return 'no value'
  elif isinstance (n, bool):
    return n
  elif isinstance (n , int):
    if n < 100:
      return 'less than 100'
    elif n > 100:
      return 'more than 100'
    else:
      return 'equal to 100'
  else:
    if len(n) > 2:
      return n[2]
    else:
      return None
