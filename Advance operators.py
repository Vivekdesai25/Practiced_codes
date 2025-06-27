#ADVANCED OPERATORS
#Identity operator 
a_list = [110, 320]
b_list = a_list
same_ref = (a_list is b_list) //true
new_list = [10, 20]
not_same = (a_list is not new_list)


# Membership operators
colors = ['red', 'green', 'blue']
has_red = 'red' in colors
no_purple = 'purple' not in colors

# Ternary operator
marks = 75
result = " Yes its Pass" if marks >= 35 else "Fail"
