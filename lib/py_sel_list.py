#
# PROGRAM: PYTHON CONSOLE DATABASE BROWSER
# MODULE : LIST TO STRING
#


def list_to_str(p_list):
    res = ""
    row = ""
    list_keys = list(p_list.keys())
    for k in list_keys:
        res += "|" + k
    res = res[1:]
    res += "\n"
    # print('HELE'+str(p_list[list_keys[0]]))
    if len(p_list) == 0:
        imax = 0
    else:
        imax = len(p_list[list_keys[0]])
    for i in range(0, imax):
        for k in list_keys:
            if len(p_list[k]) > 0:
                row += "|" + str(p_list[k][i]).replace("|", ",")
            # print(str(p_list[k][i]),end="|")
        row = row[1:] + "\n"
        # if res is not None:
        res += row
        row = ""
    res = res[:-1]
    # print(res)
    return res
