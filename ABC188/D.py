N, C = map(int, input().split())
event = []
for i in range(N):
    a, b, c = map(int, input().split())
    a -= 1
    event.append((a, c))
    event.append((b, -c))
#print(event)

event.sort()
ans = 0
fee = 0
t = 0
for x,y in event:
    if x != t:
        ans += min(C,fee)* (x-t)
        t = x
    fee += y
print(ans)


""" 
N,prime= map(int, input().split())
abc = [map(int, input().split()) for _ in range(N)]
a,b,c = [list(i) for i in zip(*abc)]
nedan = 0
end = max(b)
nu = [0 for i in range(end+1)]

for i in range(N):
    if a[i] != b[i]:
        nu[a[i]] += c[i]
        nu[b[i]] += c[i]
    else:
        nu[a[i]] += c[i]

for i in range(1,len(nu)):
    nu[i] = nu[i-1] + nu[i]
print(nu)

for i in range(len(nu)):
    if nu[i] >prime:
        nu[i] = prime

for i in range(len(nu)):
    nedan +=nu[i]
print(nedan) """