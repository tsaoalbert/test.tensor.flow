s = input ("Enter strings separated by commas:\n")
#s = "a,b,c"
lines = s.split(",")
with open('text.txt', 'w') as f: 
  f.writelines("%s\n" % l for l in lines)
f.close()
