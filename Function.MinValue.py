# Author: Ahmad Ershad Hesami
# Author URI: https://www.facebook.com/ershad.hesami/
# Date: 4/2/2020
# Author Email: personal.aeh@outlook.com
# Description: A small python program for finding minimum value of a list or a tuple
def find_min(the_list):
    try:
        if type(the_list) != ["list", "tuple"]:
            min_value = the_list[0]
            for list_item in the_list:
                if float(min_value) > float(list_item):
                    min_value = list_item
            return min_value
        else:
            return "You should pass (list or tuple)."
    except ValueError:
        return "Unsupported value found"

# Test

my_list = [3,2,'1',"12.1",7,2,"300",0]

print(find_min(my_list))