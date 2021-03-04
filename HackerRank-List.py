if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        data = []
        data.append(name)
        data.append(score)
        students.append(data)

    sortedStudents = sorted(students)
    print()
    print(max(sortedStudents))

    for i in range(0, len(sortedStudents)):
        print(sortedStudents[i][1]) 
