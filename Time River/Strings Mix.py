from collections import Counter
from itertools import chain
import string

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
s1="Are they here"
s2="yes, they are here"
s1="A generation must confront the looming "
s2="codewarrs"
s1 = "Lords of the Fallen"
s2 = "gamekult"
c1, c2 = Counter(s1), Counter(s2)

l1 = sorted([(k,v,1) for k,v in c1.items() if k in string.ascii_lowercase and v>1],key=lambda x:(x[1],-ord(x[0])),reverse=True)
l2 = sorted([(k,v,2) for k,v in c2.items() if k in string.ascii_lowercase and v>1],key=lambda x:(x[1],-ord(x[0])),reverse=True)
"""
要针对字符的数量进行第一排序，然后在相同的条件下，进行第二项排序，用的是字符的ord的值，取负值的话，可以按字母的正序排序
s1的处理结果：[('a', 4), ('h', 3), ('e', 2), ('s', 2), ('y', 2)]
s2的处理结果：[('n', 5), ('a', 3), ('m', 3), ('y', 3), ('d', 2), ('e', 2), ('f', 2), ('h', 2), ('i', 2), ('r', 2), ('s', 2)]
形成的正确的处理结果应该是这样的： mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
  分几种不同的情况：1.最长的在第一位，譬如 n*5 要在最前面
                  2.同等长度的按照字母顺序，譬如 3*h,3*m,3*y要按字母顺序排序
                  3.如果在结果已经出现过的字符，在后续当中不能再出现，譬如 3*a 不能再出现了，因为在结果串里面已经有 4*a 
                  4.相同字符、相同长度的要用 =: 表示，譬如 2*e,2s 要排在最后，因为在两者中都有，但是 2*y 不能出现，因为结果里面已经有
                    3*y了
"""
# print(l1,l2)
longest = max(l1[0][1],l2[0][1])
result = []
for p in range(longest,1,-1):
    l1 = sorted([(k,v,1) for k,v in c1.items() if k in string.ascii_lowercase and v==p], key=lambda x:(x[1],-ord(x[0])),reverse=True)
    l2 = sorted([(k,v,2) for k,v in c2.items() if k in string.ascii_lowercase and v==p], key=lambda x:(x[1],-ord(x[0])),reverse=True)
    l = sorted(chain(l1,l2), key=lambda x:(x[1],-ord(x[0])), reverse=True)
    dump = Counter(map(lambda x:x[0][0],l))
    for ch,cnt in dump.items():
        if cnt == 1:
            haved = False
            for item in result:
                if ch in item:
                    haved = True
                    break
            if (ch,p,1) in l and not haved:
                result.append(f'1:{ch*p}')

    for ch, cnt in dump.items():
        if cnt == 1:
            haved = False
            for item in result:
                if ch in item:
                    haved = True
                    break
            if (ch,p,2) in l and not haved:
                result.append(f'2:{ch*p}')

    for ch, cnt in dump.items():
        if cnt == 2:
            result.append(f'=:{ch * p}')
    print(list(l))
print(result)
    # result += f'2:{l2[p2][0]*l2[p2][1]}'
"""
DESCRIPTION: 描述：
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.
给定两个字符串 s1 和 s2，我们想要可视化这两个字符串的不同之处。我们只会考虑小写字母（a 到 z）。首先让我们统计一下 s1 和 s2 中每个小写字母出现的频率。

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.
所以 s1 和 s2 中 'a' 的最大值是来自 s1 的 4； 'b' 的最大值是来自 s2 的 3。在下文中，我们将不考虑出现次数的最大值小于或等于 1 的字母。

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.
我们可以在以下字符串中恢复 s1 和 s2 之间的差异： "1:aaaa/2:bbb" 其中 1:aaaa 中的 1 代表字符串 s1 和 aaaa 因为 a 的最大值为 4。以同样的方式 2:bbb 代表字符串 s2 和 bbb 因为 b 的最大值是 3。

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.
任务是生成一个字符串，其中 s1 或 s2 的每个小写字母出现的次数与其最大值相同（如果最大值严格大于 1）；这些字母将以它们出现的字符串编号及其最大值和 : 作为前缀。如果最大值在 s1 和 s2 中，则前缀为 =: 。

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".
结果，子字符串（子字符串例如 2:nnnnn 或 1:hhh；它包含前缀）将按其长度的降序排列，当它们具有相同的长度时，则按字典顺序升序排列（字母和数字 - 更多按代码点精确排序）；不同的组将以“/”分隔。请参阅示例和“示例测试”。

Hopefully other examples can make this clearer.
希望其他示例可以使这一点更清楚。

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
Note for Swift, R, PowerShell Swift、R、PowerShell 的注意事项
The prefix =: is replaced by E:
前缀 =: 替换为 E:

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/E:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/E:ee/E:ss"
"""