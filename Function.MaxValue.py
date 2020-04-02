# Author: Ahmad Ershad Hesami
# Author URI: https://www.facebook.com/ershad.hesami/
# Author Email: personal.aeh@outlook.com
# Date: 4/2/2020
# Description: A small python program for finding maximum value of a list or a tuple
def find_max(the_list):
    try:
        if type(the_list) != ["list", "tuple"]:
            max_value = the_list[0]
            for list_item in the_list:
                if float(max_value) < float(list_item):
                    max_value = list_item
            return max_value
        else:
            return "You should pass (list or tuple)."
    except ValueError:
        return "Unsupported value found"

# Test

my_list = [3,2,'1',"12.1",7,2,"300"]

print(find_max(my_list))