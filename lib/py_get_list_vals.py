#
# PROGRAM: PYTHON CONSOLE DATABASE BROWSER
# MODULE : GET LIST VALUES EXCLUDING NONE
#


def get_list_vals(p_list):
    ret = []
    for i in p_list:
        if i is not None:
            ret.append(len(str(i)))
    return ret
