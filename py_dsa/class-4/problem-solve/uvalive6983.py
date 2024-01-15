def can_nest_dolls(doll_sizes):
    sorted_sizes = sorted(doll_sizes)
    return sorted_sizes == doll_sizes[::-1]
    # The [::-1] is a slicing notation in Python used to reverse a sequence. In this case, it is used to reverse the list.
    # list[start:stop:step] is the general syntax for slicing a list.
    # doll_sizes = [1, 2, 3, 4] reversed_sizes = doll_sizes[::-1] print(reversed_sizes)
    #  output [4, 3, 2, 1]


def uva_problem():
    # Input the number of test cases
    T = int(input("Enter the number of test cases: "))

    for _ in range(T):
        # Input the number of dolls
        N = int(input())

        # Input the sizes of dolls
        doll_sizes = list(map(int, input().split()))

        # Check if dolls can be nested and print the result
        result = "YES" if can_nest_dolls(doll_sizes) else "NO"
        print(result)


uva_problem()
