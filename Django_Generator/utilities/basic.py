def reverse_list(lst):
    start = len(lst)
    stop = -1
    step = -1
    newLst = []
    for i in range(len(lst) -1, -1, -1):
        newLst.append(lst[i])
    return newLst


def find_in_list(mylist, str_to_search):
    for i in mylist:
        if i == str_to_search:
            return True
    return False


def replace_in_list(mylist, str_to_repalce, new_str):
    if find_in_list(mylist,str_to_repalce):
        for count, item in enumerate(mylist):
            if str_to_repalce in item:
                mylist[count] = str(item).replace(str_to_repalce,new_str)
    return mylist

