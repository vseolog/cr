def F(x, y, w, z):
    return (not (w <= (not (x <= y)))) and ((not x) <= ((not y) == z))

# for x in range(0, 2):
#     for y in range(0, 2):
#         for w in range(0, 2):
#             for z in range(0, 2):
#                 if F(x, y, w, z) == 1:
#                     print(y, w, z, x)

y = int(input())
w = int(input())
z = int(input())
x = int(input())
print(F(x, y, w, z))

# ans = y, w, z, x