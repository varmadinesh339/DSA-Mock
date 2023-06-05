def process(array):
  a = [x for x in array if x == 0]
  b = [y for y in array if y != 0]
  c = []
  c = b + a
  return c

nums = [ 0,1,0,3,12]
print(process(nums))