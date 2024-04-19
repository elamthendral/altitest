def find_list(input):
    output_list = []
    for item in input:
        if not output_list:
            output_list.append(item)
            continue
        if output_list[-1][-1]>item[0]:
            new_list=[]
            new_list.append(output_list[-1][0])
            if output_list[-1][-1] > item[1]:
                new_list.append(output_list[-1][-1])
            else:
                new_list.append(item[1])
            output_list.pop(-1)
            output_list.append(new_list)
        else:
            output_list.append(item)
    return output_list 

print(find_list([[1,9],[4,6],[8,10],[11,18]]))
#input: [[1,3],[2,6],[8,10],[11,18]] output:[[1, 6], [8, 10], [11, 18]]
