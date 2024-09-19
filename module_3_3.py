from module_2_3 import len_list


def print_params(a = 1, b = '', c = True):
    print(a, b, c)


print_params() #
print_params(c = "Orange") #
print_params(b = 25, c = [1,2,3]) #
print_params(-0.7896, {'a':6, 'b':9, 'c': -987}) #
print()
values_list = [678.9, 'Do you want pizza?', [1,2,3]]
values_list_2 = ['values_list_2', 42]
values_dict = {'a':-987,'b':65.7,'c':"a difficult task"}
print_params(*values_list)
print_params(*values_list_2)
print_params(**values_dict)