print("asdf")

g = [65, 23.32, 22, 1, 6, 32]

print(g[1])
space = []

i=0
while i < len(g):
    space.append(" ")
    i += 1


final_1 = "how {} many"
print(final_1.format(space))


n = 1
b = 0

for i in g :
    if b < i:
        b = i

c = "{0}, {1}"
print(c.format(b, n,))

print(f"{g[2]:<5}")


