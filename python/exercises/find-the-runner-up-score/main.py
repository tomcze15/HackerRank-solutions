if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    first_place = -99
    second_place = -100

    for score in arr:
        if first_place < score:
            second_place = first_place
            first_place = score

        if second_place < score < first_place:
            second_place = score

    print(second_place)
    