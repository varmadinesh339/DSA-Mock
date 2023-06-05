from collections import Counter
def process(array):
  count = Counter(array)
  c =0
  for i,j in count.items():
    
    if j == 1:
      for k in range(len(array)):
        if array[k] == i :
            return k
     

  return -1

s = "leetcode"
print(process(s))