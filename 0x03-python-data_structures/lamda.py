#!/usr/bin/python3
order = [34587, 98762, 77226, 88112]
quantity = [4, 5, 3, 3]
price = [40.95, 56.80, 32.95, 24.99]

answer = list(map(lambda a, b, c : ((a, b * c) if (b * c) > 100.00 else (a, (b * c + 10))), order, quantity, price))
for i in answer:
    print(i)
