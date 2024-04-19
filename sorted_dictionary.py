def sort_method(value):
    sort_keys=[]
    sort_values=[]
    for k,v in value.items():
        if not sort_keys:
            sort_keys.append(k)
            sort_values.append(v)
        else:
            print(k,v)
            item = sort_values[-1]
            if item > v:
                ind = sort_values.index(item)
                sort_values.insert(ind, v)
                sort_keys.insert(ind, k)
            else:
                sort_values.append(v)
                sort_keys.append(k)
        print(sort_keys, sort_values)
    sort_items={sort_keys[i]:sort_values[i] for i in range(len(sort_keys))}
    print(sort_items)

#input {'a':3, 'b':-2, 'c':1} output: {'b':-2, 'c':1, 'a':3}
