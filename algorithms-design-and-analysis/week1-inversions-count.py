# python3
import sys

def parse_array(file_name):
    with open(file_name, 'r') as f:
        content = f.readlines()
    arr = [int(x) for x in content]
    return arr

def count_inversions(i, j, arr):
    if i >= j:
        return 0
    c = (i + j) // 2
    res = count_inversions(i, c, arr) + count_inversions(c + 1, j, arr)
    a, b = 0, 0
    arr_a = arr[i:c + 1]
    arr_b = arr[c + 1:j + 1]
    for k in range(i, j + 1):
        if b >= len(arr_b):
            arr[k:j + 1] = arr_a[a:]
            break
        elif a >=len(arr_a):
            arr[k:j + 1] = arr_b[b:]
            break
        elif arr_a[a] <= arr_b[b]:
            arr[k] = arr_a[a]
            a += 1
        elif arr_a[a] > arr_b[b]:
            arr[k] = arr_b[b]
            b += 1
            res += len(arr_a) - a
    return res

def is_sorted(arr):
    arr_b = sorted(arr)
    return arr_b == arr
    p = None
    for x in arr:
        if p != None and p > x:
            return False
        p = x
    return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('file name is not provided')
        sys.exit(2)
    arr = parse_array(sys.argv[1])
    #arr = [1, 3, 5, 2, 4, 6]
    print(count_inversions(0, len(arr) - 1, arr))
    print(is_sorted(arr))

