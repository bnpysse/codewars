"""
You are given an array of strings names representing filenames. The array is sorted in order of file creation, such that names[i] represents the name of a file created before names[i+1] and after names[i-1] (assume 0-based indexing). Because all files must have unique names, files created later with the same name as a file created earlier should have an additional (k) suffix in their names, where k is the smallest positive integer (starting from 1) that does not appear in previous file names.

Your task is to iterate through all elements of names (from left to right) and update all filenames based on the above. Return an array of proper filenames.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be solution(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].

Since names[0] = "doc" and names[1] = "doc", update names[1] = "doc(1)"
Since names[1] = "doc(1)" and names[3] = "doc(1)", update names[3] = "doc(1)(1)"
Since names[0] = "doc", names[1] = "doc(1)", and names[4] = "doc", update names[4] = "doc(2)"
"""
names = ["doc", "doc", "image", "doc(1)", "doc"]
names = ["a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
names= ["dd", "dd(1)", "dd(2)", "dd", "dd(1)", "dd(1)(2)", "dd(1)(1)", "dd", "dd(1)"]
stack, origin = list(), dict()
stack.append(names[0])
origin[names[0]] = 0
for item in names[1:]:
    if item in stack:
        if item in origin:
            origin[item] += 1
            while '{0}({1})'.format(item, origin[item]) in origin:
                origin[item] += 1
            stack.append('{0}({1})'.format(item, origin[item]))
        else:
            stack.append('{0}(1)'.format(item))
            origin[item] = 0
        # origin.setdefault(item,k)
    else:
        stack.append(item)
        origin[item] = 0
print(stack)
print(origin)

