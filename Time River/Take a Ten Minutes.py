walk = ['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']
walk =['n','s','n','s','n','s','n','s','n','s']
walk = ['n','n','n','s','n','s','n','s','n','s']
# walk = ['w', 'w', 's', 's', 'e', 'e', 'e', 'n', 'n', 'w']
# direct = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
text = "A wise old owl lived in an oak"
result=[]
for item in text.split():
    item.replace(item[0],str(ord(item[0])))

    if len(item)>2:
        tmp = item[-1]
        item.replace(item[-1],item[-2])
        item.replace(item[-2],tmp)
    result.append(item)
    print(item)
print(''.join(item))

    print(True)
else:
    print(False)

# for item in walk:
#     if stack == []:
#         stack.append(item)
#     elif direct[item] != stack[-1]:
#         stack.append(item)
#     else:
#         stack.pop(-1)
# print(stack)
