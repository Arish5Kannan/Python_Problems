s = input()
t = s[0]
i = 1
j = len(s)-1
while(i<=j):
      if ord(s[i]) == 32:
          t += s[i]
      elif ord(s[i])&31 > ord(s[j])&31:
          t += s[j].upper()
      else:
          t += s[i].lower()
      i += 1
      j -= 1

print(t)

