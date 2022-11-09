first = int(input("Enter first number: "))
last = int(input("Enter last number: "))
num_list = list(range(first, last+1))
prime_list = []
for num in num_list:
  if num > 1 :
    for i in range(2, num):
      if num % i == 0:
        break
    else:
      prime_list.append(num)
print(prime_list)
