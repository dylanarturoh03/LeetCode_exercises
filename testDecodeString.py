arr = [3, 1, 3]
arr.append(0)
max_area = 0
stack = []

for i in range(len(arr)):
    while stack and arr[stack[-1]] >= arr[i]:
        h = arr[stack.pop()]
        l = stack[-1] if stack else -1
        r = i
        area = h * (r - l - 1)
        max_area = max(max_area, area)
    stack.append(i)

print(stack)
print(max_area)
