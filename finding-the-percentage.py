if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split(" ")
        scores = list(line)
        student_marks[name] = scores
    query_name = input()


    result = student_marks.get(query_name)




    sum = 0
    for i in result:
        sum+=float(i)

    print(format(sum/len(result), '.2f'))












