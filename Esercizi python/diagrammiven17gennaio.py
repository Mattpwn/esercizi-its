
# # define  sum
# sum: int = 0

# # define a counter loop

# i: int = 1
# while i <= 5:

#     # insert a number 
#     n: int = int(input(f"insert number {i}: "))

#     # check positive numbers
#     if n > 0:

#         # update sum 
#         sum += n

#     # update counter 
#     i += 1

# # display result
# print(f"sum: {sum}")


# ex numero 6

n: int = int(input("insert number :"))

m = 1

for i in range (1, n + 1):
    m = m * i

print(m)