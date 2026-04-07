N = input()
print(type(N))
even_sum = 0
odd_sum = 0

for index in range(len(N)):
digit = int(N[index])
  if (index + 1) % 2 == 0:
    even_sum += digit
  else:
    odd_sum += digit

diff = even_sum - odd_sum
if diff  == 0 or diff % 11 == 0:
  print("Yes")
else:
 print("No")

