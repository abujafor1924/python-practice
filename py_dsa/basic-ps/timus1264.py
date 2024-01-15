def petechkin_time(N, M):
    time = N * (M + 1)
    return time


N, M = map(int, input("Enter Your Two Number : ").split())
petechk = petechkin_time(N, M)
print("Result of Petechk Time is  = ", petechk)

# ========================== Looping Method ==========================
# def petechkin_time(N, M):
#     # Initialize time to 0
#     time = 0
#
#     # Loop through each element and count for each unique element
#     for i in range(N):
#         for j in range(M + 1):
#             # Increment the count for each unique element
#             time += 1
#
#     return time
#
#
# # Input reading
# N, M = map(int, input().split())
#
# # Output the result
# print(petechkin_time(N, M))
