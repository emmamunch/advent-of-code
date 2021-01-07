with open('day1input.txt') as f:
    content = f.readlines()
content = [int(l.strip()) for l in content] 
print(len(content))
# print(content)
p = None
q = None
# for i,n in enumerate(content):
#     rest = content[i+1:].copy()
#     for n2 in rest:
#         if n+n2 == 2020:
#             p = n
#             q = n2
#             print(n*n2)
#             break

# for i,n in enumerate(content):
#     rest = content[i+1:].copy()
#     for j,n2 in enumerate(rest):
#         rest2 = rest[j+1:].copy()
#         for n3 in rest2:
#             if n+n2+n3 == 2020:
#                 print(n*n2*n3)
                # break

seen = set()
for n in content:
    seen.add(n)
    if 2020-n in seen:
        print(n*(2020-n))

seen = set()
seen2 = set()
for i,n in enumerate(content):
    seen.add(n)
    for n2 in content[i+1:]:
        seen.add(n2)
        if 2020-n-n2 in seen:
            print(n*n2*(2020-n-n2))
            break

    
# print(p*q)