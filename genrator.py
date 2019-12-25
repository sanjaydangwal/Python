def series(n):
    for i in range(0,n+1):
        yield i


nums = series(10)
for i in nums:
    print(i)

print(nums)