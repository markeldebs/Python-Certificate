a = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
split_list = []
upper_bound = []
lower_bound = []
length = ""
p = ""
d = ""
space = " "
difference = " "
lines = ""
line = "-"
show_results= False
results = []
results_print = ""
results_length = []

for x in a:
    split_list.append(x.split())

# Create results list
n = 0
#if show_results is True:
while n < (a.__len__()):
    if split_list[n][1] == "+":
        results.append(int(split_list[n][0]) + int(split_list[n][2]))
    elif split_list[n][1] == "-":
        results.append(int(split_list[n][0]) - int(split_list[n][2]))
    else:
        throw("Invalid argument")
    n += 1


# Create operand strings
i = 0
while i < (a.__len__()):
    #determine length of both operands
    upper_bound.append(split_list[i][0].__len__())
    lower_bound.append(split_list[i][2].__len__())

    #formating number of spaces by concatanating based on length of operands
    if upper_bound[i] < lower_bound[i]:
        difference = upper_bound[i] - lower_bound[i] - 1
        p += lower_bound[i]*space + split_list[i][0] + space*difference + space*4
        d += split_list[i][1] + space + split_list[i][2] + space*4
        lines += line*(lower_bound[i] + 2) + space*4
        results_print += space*2 + str(results[i]) + space*4

    elif upper_bound[i] == lower_bound[i]:
        p += 2*space + split_list[i][0] + space + space*4
        d += split_list[i][1] + space + split_list[i][2] + space*4
        lines += line*(upper_bound[i]+2) + space*4
        results_print += space*2 + str(results[i]) + space*4

    else:
        difference = upper_bound[i]-lower_bound[i]
        p += split_list[i][0] + space*4
        d += split_list[i][1] + space + (difference-2)*space + split_list[i][2] + space*4

        if difference > 2:
            lines += line*(lower_bound[i]+ difference) + space*4
            results_print += str(results[i]) + space*4

        else:
            lines += line*(lower_bound[i]+ difference + 1) + space*4
            results_print += space  + str(results[i]) + space*4

    i += 1

# Results string cration
l = 0

'''
while l < results.__len__():
    difference = maxupper_bound[l] - lower_bound[l]
    if difference == 0:
        results_print += space*2 + str(results[l]) + space*4
    elif difference >= 3:
        results_print += str(results[l]) + space*4
    else:
        results_print += space*2 + str(results[l]) + space*4
    print(difference)
    l += 1
'''

if show_results == True:
    print(p)
    print(d)
    print(lines)
    print(results_print)
else:
    print(p)
    print(d)
    print(lines)
