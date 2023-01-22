a = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
#if ((a.__len__() > 0 & a.__len__() <= 5)

b = []
c = []

for i in a:
    b.append(i.split())

    print(b)
    print(b[0][0])

while b.__len__() < 5:
    b.append(['','',''])


s = 0
while s < 5:
    
    print(f"{b[s][0]:<5}")
    print(f"{b[s][1]:<5}")
    print(f"{b[s][2]:<5}")
    print("--------")
    s = s+1

#print(a)
#print(f"{b[0][0]:<10}{b[1][0]:<10}{b[2][0]:<10}{b[3][0]:<10}{b[4][0]:<10}")
#print(f"{b[0][1]:>1}{b[0][2]:<10}{b[1][1]:>1}{b[1][2]:>1}{b[2][1]:>1}{b[1][2]:>1}{b[2][1]:>1}{b[1][2]:>1}{b[2][1]:>1}{b[1][2]:>1}{b[2][1]:>1}")

'''
b_first = a[0].split()
b_secod = a[1].split()
b_third = a[2].split()
b_forth = a[3].split()
b_fifth = a[4].split()

print(b_first[0])

print(f"{b_first[0]:>10}{b_secod[0]:>10}")
print(f"{b_first[0]:>10}{b[0][2]:>10}")
print("---------")
'''
"""
for i in a:
b = [{},{},{},{},{}]

b[0] = a[0].split()
b[1] = a[1].split()
b[2] = a[2].split()
b[3] = a[3].split()
#b[4] = a[4].split()

print(b)
print(f"{b[0]:>10}{b[3]:>10}")
print(f"{b[1]:<1}{b[2]:>9}")
print("----------")
print()



print(a[x].split(","))
b = a[x].split(",")

print(b)

c = a[1].split(",")
print(c)



print(b[0])



def arithmetic_arranger(num_string, solve_bool):
    
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
"""