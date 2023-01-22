a = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
split_list = []
upper_bound = []
lower_bound = []
length = ""

for x in a:
    split_list.append(x.split())

print(split_list)


p = ""
d = ""
i = 0
space = " "
difference = " "
lines = ""
line = "-"

while i < (a.__len__()):
    print(split_list[i][0])
    upper_bound.append(split_list[i][0].__len__())
    lower_bound.append(split_list[i][2].__len__())

    if upper_bound[i] < lower_bound[i]:
        difference = upper_bound[i] - lower_bound[i] - 1
        p += lower_bound[i]*space + split_list[i][0] + space*difference + space*4
        d += split_list[i][1] + space + split_list[i][2] + space*4
        lines += line*(lower_bound[i] + 2) + space*4
    elif upper_bound[i] == lower_bound[i]:
        p += 2*space + split_list[i][0] + space + space*4
        d += split_list[i][1] + space + split_list[i][2] + space*4
        lines += line*(upper_bound[i]+2) + space*4
    else:
        difference = lower_bound[i] -  upper_bound[i]
        p += split_list[i][0] + space*4
        d += split_list[i][1] + space + (upper_bound[i]-lower_bound[i]-2)*space + split_list[i][2] + space*4
        lines += line*(upper_bound[i]) + space*4
    i += 1
    

print(p)
print(d)
print(lines)
print(upper_bound)
print(lower_bound)
'''
while split_list.__len__() < 5:
    split_list.append([0,0,0])


print(upper_bound)
print(lower_bound)

if upper_bound < lower_bound:
    print(" "+lower_bound+1)
#print(' sd'*length[1] + "Helo")

upper_print ="{0}{1}    {2}{3}    {4}{5}    {6}{7}"
spaces = " "
print(upper_print.format(split_list[0][0]," "*1, split_list[1][0],spaces, split_list[2][0],spaces, split_list[3][0],spaces))
'''
