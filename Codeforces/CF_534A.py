# CF_534A
# Exam

N = int(raw_input())

ans = {1: '1\n1', 2: '1\n1', 3: '2\n1 3'};
if N in ans.keys():
    print ans[N]
else:
    print N
    for i in range(2, N+1, 2):
        print i,
    for i in range(1, N+1, 2):
        print i,
    print

