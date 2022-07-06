# 1 Print all integers from 0 to 150.
for i in range(0,151):
  print(i)

# 2 Print all the multiples of 5 from 5 to 1,000
for i in range(5, 1001, 5):
  print(i)

# 3 Print 1 to 100. i/5 - "Coding", i/10 - "Coding Dojo"
for i in range(1, 101):
  if i%10 == 0:
    print("Coding Dojo")
  elif i%5 == 0:
    print("Coding") 
  else:
    print(i)

# 4 Add odd integers from 1 to 500000, print the final sum
sum = 0
for i in range(1, 500001):
  if i%2 != 0:
    sum += i
  print(sum)

# 5 Print positive numbers starting 
for i in range(2018, 0, -4):
    print(i)

# 6 Flexible numbers loop
low_num = 2
high_num = 9
mult = 3
for i in range(low_num, high_num + 1):
  if i%mult == 0:
    print(i)