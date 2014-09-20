from random import randrange

f = open("voitot.txt","r")

lines = f.readlines()
f.close()

print lines.pop(randrange(len(lines)))

f = open("voitot.txt","w")

for line in lines:
  f.write(line)

f.close()

