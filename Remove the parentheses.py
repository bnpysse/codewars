s = "hello example (words(more words) here) something"
stack = [[]]
for ch in s:
    if ch == '(':
        stack.append([])
    elif ch == ')':
        stack.pop(-1)
    else:
        stack[-1].append(ch);
print(stack)
