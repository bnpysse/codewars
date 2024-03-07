# 题目还是有些特点的，我想用 lambda 来实现。
# 细一看，其实里面还是一个分数的约分问题，实际上是求了一个分数的表达式而已。
# 2023-05-11 16:47:09
# 尤其是第二个 Lambda 公式，是用 lambda 来递归实现的求最大公约数，还是很有一些借鉴意义的。


hms = lambda time: int(time.split(':')[0]) * 3600 + int(time.split(':')[1]) * 60 + int(time.split(':')[2])
gcd = lambda x, y: x if y == 0 else gcd(y, x % y)

part = "02:20:00"
total = "07:00:00"

# 实际上就是求出总的时间来，然后约分做分数就可以了。

print(hms(part) // gcd(hms(part), hms(total)))
print(hms(total) // gcd(hms(part), hms(total)))

"""
You have been watching a video for some time. Knowing the total video duration find out what portion of the video you have already watched.

Example

For part = "02:20:00" and total = "07:00:00", the output should be
solution(part, total) = [1, 3].

You have watched 1 / 3 of the whole video.
"""
