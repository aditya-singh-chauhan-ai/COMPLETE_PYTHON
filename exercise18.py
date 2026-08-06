def common(l1, l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(common([1,2,3,4], [1,2,8,9]))