#5. `sys` → Sum from Command Line
import sys
nums = list(map(int, sys.argv[1:4]))
print("Sum =", sum(nums))

# in terminal python add.py 15 20 5