import random
import time


def count_sort(A_list):
    """计数排序

    :param :A_list:无序列表
    :return :B_list;有序列表
    """
    # A_list = unsorted_list
    C_list = [0] * (max(A_list) + 2)

    for x in A_list:
        C_list[x + 1] += 1
    for i in range(1, len(C_list)):
        C_list[i] += C_list[i - 1]

    B_list = [0] * len(A_list)

    for x in A_list:
        B_list[C_list[x]] = x
        C_list[x] += 1

    return B_list


def main():

    n = 10000000 # 样本数
    m = 100000 # 随机数的取值范围
    A_list = [random.randrange(m) for i in range(n)]
    tic = time.time()
    B_list = count_sort(A_list)
    toc = time.time()
    print("%d个样本，计数排序耗时 %.5f s" % (n,toc-tic))

if __name__ == '__main__':
    main()
