#Ramu Vallapurapu
#Practice Sorter

n = open("locationresult.txt","r")  # open file, read-only
s = open("sort.txt", "w") # open file, write
lines = n.readlines()
lines.sort()

for line in lines:
 s.write(line)

n.close()
s.close()