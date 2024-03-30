Name = input("Enter your string - ")
a = 'aeiouAEIOU'
n = []
for i in Name:
    count = 0
    for r in range(len(a)):
       if i == a[r]:
        count += 1
    if i not in a:
        n.append(i)
    if count == 2:
           n.append(i)
    else:
          continue
print("Remove String:",end='')
for h in n:
    print(h,end="")











