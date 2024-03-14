if __name__ == '__main__':
    students = {}
    lowest = 100.0
    second_lowest = 100.0

    for _ in range(int(input())):
        name = input()
        score = float(input())

        students[name] = score

        if score < lowest:
            second_lowest = lowest
            lowest = score

        if lowest < score < second_lowest:
            second_lowest = score

    students_name = []

    for name, score in students.items():
        if second_lowest == score:
            students_name.append(name)

    students_name.sort()

    for student in students_name:
        print(student)
