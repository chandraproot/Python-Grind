# # Enter your code here. Read input from STDIN. Print output to STDOUT
# n = int(input())
# str_1 = []
# for i in range(n):
#   str_input = input()
#   str_1.append(str_input)

# k = int(input())
# ks = 1


# for i in str_1:
#   for j in str_1:
#     if i == j:
#       continue
#     else:
#       ks = ks +1
#       if ks == k:
#         print(i)


n = int(input())
strings = [input() for _ in range(n)]
k = int(input())

sorted_strings = [''.join(sorted(s)) for s in strings]
unique_strings = set()
kth_unique_string = ""

for s in sorted_strings:
    if s not in unique_strings:
        unique_strings.add(s)

for s in strings:
    sorted_s = ''.join(sorted(s))
    if sorted_s not in unique_strings:
        k -= 1
    if k == 0:
        kth_unique_string = s
        break

if kth_unique_string:
    print(kth_unique_string)
else:
    print("")





