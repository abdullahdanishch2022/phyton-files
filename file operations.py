file= open("class-notes.txt","r")
#file.write("")

n=int(input("how many characters to preview"))
print(file.read(n))
file.close()
print()


file=open("class-notes.txt","r")
lines=file.readlines()
file.close()
print("total lines ",len(lines))

for i in range(len(lines)):
    print("-->",lines[i].strip())
print()


#filter lines
words=input("skip lines starting with")
file=open("class-notes.txt","r")
for line in file:
    if line.startswith(words):
        print("skip: ",line.strip())
    else:
        print("keep: ",line.strip())
file.close()


file=open("class-notes.txt","r")
lines=file.readlines()
file.close()
out=open("odd-lines.txt","w")
for i in range(0,len(lines),2):
    out.write(lines[i])
out.close()
print("class notes saved to odd lines")