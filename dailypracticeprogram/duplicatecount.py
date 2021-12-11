a='aa ab ac ad ba aa cd ad'
# b=a.split()
# print(b)
result={}  # result["aa"] = a
# { "aa" : 1 }
# for word in b:
#
#    if result.get(word):
#        result[word] = result[word] + 1
#    else:
#        result[word]=1
#
# print(result)


b = a.split()
for word in b:
    result[word] = result.get(word, 0) + 1

print(result)



#
# def get(dict_variable ,key,default_value=None):
#     try:
#         value = dict_variable[key]
#         return value
#     except Exception:
#         return default_value
#
# a = {"h":56}
#
# value = get(a,"h")
# valuew = a.get("h")
# # print(value)
# print(valuew)



