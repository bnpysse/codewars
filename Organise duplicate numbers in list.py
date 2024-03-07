arr = []

stack = [[arr[0]]]
found=False
for item in arr[1:]:
    found=False
    for val in stack:
        if item in val:
            val.append(item)
            found = True
            break
    if not found:
        stack.append([item])
print(stack)