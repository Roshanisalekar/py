def print_list(list,idx):

    if (idx== len(list)):
        return
    print(list[idx])
    print_list(list,idx +1)


name =["roshani","savita","ankush","sagar","amol"]    
print_list(name)