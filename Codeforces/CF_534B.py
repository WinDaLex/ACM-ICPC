# CF 534B
# Covered Path

V1, V2 = map(int, raw_input().split())
T, D = map(int, raw_input().split())

l = [V1]
r = [V2]
for i in range(T-1):
    l.append(l[-1] + D)
    r.append(r[-1] + D)

r.reverse()
ans = 0
for i in range(T):
    ans += min(l[i], r[i])

print ans
