def binary_search(arr, x, left, right):
    if right <= left:
        return -1

    mid = (left + right) // 2

    if x == arr[mid]:
        return mid

    if arr[mid] < arr[right - 1]:

        if arr[mid] < x <= arr[right - 1]:
            return binary_search(arr, x, mid + 1, right)
        return binary_search(arr, x, left, mid)

    if arr[left] < arr[mid]:

        if arr[left] <= x < arr[mid]:
            return binary_search(arr, x, left, mid)
        return binary_search(arr, x, mid + 1, right)

    return binary_search(arr, x, mid + 1, right)


def main():
    length = int(input())
    x = int(input())
    arr = list(map(int, input().split()))
    print(binary_search(arr=arr, x=x, left=0, right=length))


if __name__ == '__main__':
    main()
