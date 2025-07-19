# Through command line arguments, three strings separated by space are given to you. Each string is a series of numbers separated by hyphens (-).
import sys

like = set(map(int, sys.argv[1].split('-')))
dislike = set(map(int, sys.argv[2].split('-')))
nums = list(map(int, sys.argv[3].split('-')))

happiness = 0
for num in nums:
    if num in like:
        happiness += 1
    elif num in dislike:
        happiness -= 1

print(happiness)
