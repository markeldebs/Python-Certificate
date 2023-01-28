a = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
#if ((a.__len__() > 0 & a.__len__() <= 5)

b = []
c = []
n = 0
upper_bound = []
lower_bound = []
max_width = []
results = []
results_width = []

for i in a:
    
    # Splits function into 2d_array 
    b.append(i.split())
    
    # Adds length of operands into array list
    upper_bound.append(b[n][0].__len__())
    lower_bound.append(b[n][2].__len__())

    # Calculates Results
    if b[n][1] == "+":
        results.append(int(b[n][0]) + int(b[n][2]))
    elif b[n][1] == "-":
        results.append(int(b[n][0]) - int(b[n][2]))
    else:
        assert ("Error please make sure you are usng addition or subraction")
    
    # Adds length of result into array
    results_width.append(str(results[n]).__len__())
    max_width.append(max(upper_bound[n], lower_bound[n], results_width[n]))

    print(max_width)



        
    n += 1

for i in range(a.__len__()):
    print(i)


'''
for i in range(b.__len__()) :
    
    print(i)
    
    if upper_bound >= 
    




    if  upper_bound[n] > (max_width[n]+1):


    print(b)
    print(b[0][0])
    print(upper_bound)
    print(lower_bound)
    print(max_width)

    n += 1

width = []

'''