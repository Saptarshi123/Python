n1 = 0
n2 = 1
count = 0
nos=20
if nos <= 0:
   print("Please enter a positive integer")
elif nos == 1:
   print("Fibonacci sequence upto",nos,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nos,":")
   while count < nos:
       print(n1,end=' , ')
       sum = n1 + n2
       n1 = n2
       n2 = sum
       count += 1