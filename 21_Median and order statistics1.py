

def min_e(lyst):
    """ 空列表返回 0

    :param lyst: 需要找最小元的列表
    :return: 最小元的坐标
    """
    if len(lyst) == 0:
        print('列表为空，不符合条件')
        return 0
    min_element = lyst[0]
    min_element_idx = 0
    for i in range(1,len(lyst)):
        if lyst[i] < min_element:
            min_element = lyst[i]
            min_element_idx = i
    return min_element_idx


def min_max_e(lyst):
    """

    :param lyst: 列表
    :return: 元组(最小元与最大元）
    """
    if len(lyst) % 2 == 1:
        min_element = lyst[0]
        max_element = lyst[0]
        for i in range(1,len(lyst),2):
            x = lyst[i]
            y = lyst[i+1]
            if x < y:
                min_element = x if x<min_element else min_element
                max_element = y if max_element<y else max_element
            else:
                min_element = y if y<min_element else min_element
                max_element = x if max_element<x else max_element
    else:
        min_element = lyst[0] if lyst[0] < lyst[1] else lyst[1]
        max_element = lyst[0] if lyst[1] < lyst[0] else lyst[1]
        for i in range(2,len(lyst),2):
            x = lyst[i]
            y = lyst[i+1]
            if x < y:
                min_element = x if x<min_element else min_element
                max_element = y if max_element<y else max_element
            else:
                min_element = y if y<min_element else min_element
                max_element = x if max_element<x else max_element
    return min_element,max_element



def main():
    A_list = [10,2,100000,4,5]
    print(min_e(A_list))
    print(min_max_e(A_list))

if __name__ == "__main__":
    main()