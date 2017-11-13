def ext_min(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) > 1:
        a_min = arr[0]
        for a in arr:
            if a_min > a:
                a_min = a
        return a_min
    else:
        raise ValueError


def ext_mean(arr):
    return sum(arr) / len(arr)

if __name__ == '__main__':
    a = [int(i) for i in input('Stage 1. Searching for minimum element in: ').split(' ')]
    print(f'Minimum element: {ext_min(a)}')
    print(f'Mean value: {ext_mean(a)}')
