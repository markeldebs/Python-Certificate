def arithmetic_arranger(problems, results = False):

    #a = ["32 + 698", "9999 + 9", "45 + 43", "1233 - 49", "1 - 12"]
    #if ((a.__len__() > 0 & a.__len__() <= 5)

    b = []
    c = []
    n = 0
    upper_bound = []
    lower_bound = []
    max_width = []
    results = []
    results_width = []
    lower_bound_comp = []
    first_line = ''
    second_line = ''
    third_line = ''
    results_line = ''
    space = ' '
    return_ans = ''
    


    # Condition for 5 arguments
    if (problems.__len__() > 5):
        print("Error: Too many arguments.")
        exit()


    for i in problems:
        # Splits function into 2d_array 
        b.append(i.split())
                
        # Adds length of operands into array list
        upper_bound.append(b[n][0].__len__())
        lower_bound.append(b[n][2].__len__())
        
        # Checks for max argument length
        if upper_bound[n] > 4 or lower_bound[n] > 4:
            print("Error: Numbers cannot be more than four digits.")
            quit()
        
        # Checks if all numbers only contain digits
        if (b[n][0]).isdigit() == False or (b[n][2]).isdigit() == False:
            print("Error: Numbers must only contain digits.")
            quit()

        # Calculates Results while checking input conditions
        if b[n][1] == "+":
            results.append(int(b[n][0]) + int(b[n][2]))
        elif b[n][1] == "-":
            results.append(int(b[n][0]) - int(b[n][2]))
        else:
            print("Error: please make sure you are usng addition or subraction.")
            quit()
        
        # Adds length of result into array
        results_width.append(str(results[n]).__len__())
        max_width.append(max(upper_bound[n], lower_bound[n], results_width[n]))

        if int(max_width[n]) > (int(lower_bound[n])+ 2):
            lower_bound_comp.append(max_width[n])
        else:
            lower_bound_comp.append(b[n][2].__len__()+2)
            
        n += 1

    # print(max_width)
    # print(upper_bound)
    # print(lower_bound)
    # print(lower_bound_comp)


    # Concatanating strings for completed statement
    for i in range(problems.__len__()):

        first_line += space*(lower_bound_comp[i] - upper_bound[i]) + b[i][0] + space*4
        second_line += b[i][1] + space*(lower_bound_comp[i]-lower_bound[i]- 1) + b[i][2] + space*4
        third_line += '-'*lower_bound_comp[i] + space*4
        results_line += space*(lower_bound_comp[i] - results_width[i]) + str(results[i]) + space*4

    if results:
        results_print = first_line + '\n' + second_line + '\n' + third_line + '\n' + results_line
        return(results_print)
    else:
        results_print = first_line + '\n' + second_line + '\n' + third_line
        return(results_print)

print(arithmetic_arranger(["12 + 12"]))