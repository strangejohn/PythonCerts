import re
def arithmetic_arranger(problems, exit=False):
    txt = problems
    #convert string into arrays for processing
    arr1,arr2, arr3, length = [], [], [], []
    for x in txt:
    	first = re.findall("^[0-9]*", x)
    	second = re.findall('\S[0-9]*$', x)
    	opper = re.findall('[-+/%*^]', x)
    	arr1.append(first[0])
    	arr2.append(second[0])
    	arr3.append(opper[0])
    arr_error = '0'
    #check to see if the string was valid to specifications
    def checkElist(eList1, eList2, eList3):
    	if len(eList1)> 5 or len(eList2)> 5 or len(eList3)> 5:
    	    return 2
    	for x in eList1:
    	    if len(x) > 4:
    	        return 3
    	for x in eList2:
    	    if len(x) > 4:
    	        return 3
    	for x in eList3:
    	    if x == '+' :
    	        continue
    	    if x == '-' :
    	        continue
    	    else:
    	        return 4
    	for x in eList1:
    	    if re.search('[a-zA-Z]', x):
    	        return 5
    	for x in eList2:
    	    if re.search('[a-zA-Z]', x):
    	        return 5
    	return 1

    #ends function if error
    if checkElist(arr1, arr2, arr3) == 2:
        arr_error = "Error: Too many problems."
        return arr_error
    if checkElist(arr1, arr2, arr3) == 3:
        arr_error = "Error: Numbers cannot be more than four digits."
        return arr_error
    if checkElist(arr1, arr2, arr3) == 4:
        arr_error = "Error: Operator must be '+' or '-'."
        return arr_error
    if checkElist(arr1, arr2, arr3) == 5:
        arr_error = "Error: Numbers must only contain digits."
        return arr_error

    #find the total for the equations and convert back to string
    arr1_int = []
    arr2_int = []
    arr_total = []
    for i in range(0,len(arr1)):
        arr1_int.append(int(arr1[i]))
        arr2_int.append(int(arr2[i]))
    for i in range(0,len(arr1)):
        if arr3[i] == '+':
            arr_total.append(arr1_int[i] + arr2_int[i])
        if arr3[i] == '-':
            arr_total.append(arr1_int[i] - arr2_int[i])
    for i in range(0,len(arr_total)):
        arr_total[i] = str(arr_total[i])


    #find the total spacing needed per section

    def len_arr(val1,val2):
        x = []
        y = []
        bigger = []
        for i in range(0,len(arr1)):
            x.append(int(val1[i]))
            y.append(int(val2[i]))
            if x[i] > y[i]:
                x[i] = str(x[i])
                bigger.append(x[i])
            else:
                y[i] = str(y[i])
                bigger.append(y[i])
        return bigger

    len_hold = len_arr(arr1,arr2)

    for x in len_hold:
    	length.append(len(x))

    #construct top line
    line1 = []

    for i in range(0,len(arr1)):
        line1.append((length[i] + 2 - len(arr1[i]))*' ')
        line1.append(arr1[i])
        if i != (len(arr1) - 1):
            line1.append('    ')
        else:
            line1.append('\n')
    #construct 2nd line
    for i in range(0,len(arr2)):
        line1.append(arr3[i])
        line1.append(' ')
        line1.append((length[i] - len(arr2[i]))*' ')
        line1.append(arr2[i])
        if i != (len(arr2) - 1):
            line1.append('    ')
        else:
            line1.append('\n')
    #construct equation line
    for i in range(0,len(arr1)):
        line1.append((length[i] + 2)*'-')
        if i != (len(arr1) - 1):
            line1.append('    ')

    #convert total to pre spaced
    for i in range(0,len(arr_total)):
        if int(arr_total[i]) < 0:
            arr_total[i] = int(arr_total[i]) * (-1)
            arr_total[i] = str(arr_total[i])
            arr_total[i] = '- ' + (length[i]-len(arr_total[i]))*' ' + arr_total[i]
        else:
            arr_total[i] = (length[i]-len(arr_total[i])+2)*' ' + arr_total[i]

    #if answer = True:''
    if exit == True:
        line1.append('\n')
        for i in range(0,len(arr_total)):
            line1.append(arr_total[i])
            if i != (len(arr_total) - 1):
                line1.append('    ')

    arranged_problems = ''.join(line1)
    return arranged_problems
