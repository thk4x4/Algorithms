def zero(street_length, street_num):
    range_num = 10 ** 9
    result = [range_num] * street_length
    greater = range_num
    for x in range(street_length):
        if not street_num[x]:
            greater = 0
        result[x] = min(result[x], greater)
        greater += 1

    greater = range_num
    for x in range(street_length - 1, -1, -1):
        if not street_num[x]:
            greater = 0
        result[x] = min(result[x], greater)
        greater += 1
    return ' '.join(map(str, result))


def main():
    length = int(input())
    numbers = list(map(int, input().split()))
    print(zero(length, numbers))


if __name__ == "__main__":
    main()
