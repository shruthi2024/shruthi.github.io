# n = int(input())
# s = set(map(int, input().split()))
# #print(s)
# N = int(input())
#
# for i in range(N):
#     op= input().split()
#
#     if op[0] =="pop":
#         s.pop()
#     elif op[0] == "discard":
#         s.discard(op[1])
#     else:
#         try:
#             s.remove(op[1])
#         except KeyError as e:
#             print("ERror")
#
# # print(s.pop())
# # print(s.remove(9))
# # print(s.discard(9))
# # print(s.discard(8))
# # print(s.remove(7))
# # print(s.pop())
# # print(s.discard(6))
# # print(s.remove(5))
# # print(s.pop())
# # print(s.discard(5))
#
#
# print("s",s)
# """
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# print(s.pop())
# print(s.remove(9))
# print(s.discard(9))
# print(s.discard(8))
# print(s.remove(7))
# print(s.pop())
# print(s.discard(6))
# print(s.remove(5))
# print(s.pop())
# print(s.discard(5))
# """
n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())

# Process commands
for _ in range(num_commands):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

# Print the sum of the elements in the set
print(sum(s))
