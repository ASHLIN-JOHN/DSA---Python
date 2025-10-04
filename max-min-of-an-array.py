a = [9,11,23,45,2,54,33,102,54,2,2]
maxe = a[0]
mine = a[0]
for i in range(1, len(a)):
  if a[i]> maxe:
    maxe = a[i]
  if mine > a[i]:
    mine = a[i]
print(maxe,mine)
