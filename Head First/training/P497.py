# # 1
# data = [1, 2, 3, 4, 5, 6, 7, 8]
# evens = []
# for num in data:
#     if not num % 2:
#         evens.append(num)
evens = [num for num in range(1, 9) if num % 2 == 0]

# # 2
# data = [1, "one", 2, "two", 3, "three", 4, "four"]
# word = []
# for num in data:
#     if isinstance(num, str):
#         word.append(num)
word = [num for num in [1, "one", 2, "two", 3, "three", 4, "four"] if isinstance(num, str)]

# # 3
# data = list('So long and thanks fr all the fish'.split())
# title = []
# for word in data:
#     title.append(word.title())
title = [word.title() for word in list('So long and thanks fr all the fish'.split())]