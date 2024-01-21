def median():
    '''
    The funcation takes three values as input from user and calculates the median of the values. You are supposed to write a white box test for the code checking all paths in the code. Also, test the input and output on console (i.e. use test fixture concepts). 
    '''
    value1 = int(input("Enter 1st number: "))
    value2 = int(input("Enter 2nd number: "))
    value3 = int(input("Enter 3rd number: "))
    median  = -1
    if (value1-value2) * (value3-value1)>0:
        median = value1
    elif (value2-value1) * (value3-value2)>0:
        median = value2
    else: 
        median = value3
    return median

