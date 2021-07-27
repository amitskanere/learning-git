a='aa ab ac ad ba aa cd ad'
b=a.split()
print(b)
result={}  # result["aa"] = a
# { "aa" : 1 }
for word in b:
   if result.get(word):
        result[word] = result[word] + 1
   else:
       result[word]=1

print(result)
