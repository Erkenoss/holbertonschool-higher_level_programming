#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if my_list_1 is not None or my_list_2 is not None:
        my_list_3 = []
        for i in range(0, list_length):
            result = 0
            try:
                result = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
            except TypeError:
                print("wrong type")
            except IndexError:
                print("out of range")
            finally:
                my_list_3.append(result)
        return my_list_3
