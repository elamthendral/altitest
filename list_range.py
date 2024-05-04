1)#input: [[1,3],[2,6],[8,10],[11,18]] output:[[1, 6], [8, 10], [11, 18]]
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



2) # x=[7,8,9,10,11,12,13,1,2,3,4,5,6]	 

# output=[[7,8,9,10],[11,12,13,1],[2,3,4,5],[6]]

def split_list(input, range=4):
    output_list = []
    sub_list = []
    final_check_flag=False
    for item in input:
        if len(sub_list)==range:
            output_list.append(sub_list)
            final_check_flag=True
            sub_list=[]
        else:
            final_check_flag = False
            sub_list.append(item)
    
    if not final_check_flag:
        output_list.append(sub_list)
    return output_list

3) out="ggiyvgnhykhh"
output=['gg','hh']

con=''
cstr=""
repeat_flag=False
for i in range(len(out)-1):
    if out[i]==out[i+1]:
        repeat_flag=True
        if not cstr:
           cstr=out[i]+out[i+1]
        else:
            cstr = out[i+1]
    else:
        repeat_flag=False
        if len(cstr)>1:
            print(cstr)
        cstr=""
if repeat_flag:
    print(cstr)
