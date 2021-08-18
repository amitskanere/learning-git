
file1 = open('geek1.txt','r')
file2 = open('geek2.text','w')
print(file2.tell())
for lines in file1:
    for words in lines.split():
        file2.write(words + "\t")


file1.close()
file2.close()



