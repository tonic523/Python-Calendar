def instruction():
    print('''
    | 1. 일정 등록  |
    | 2. 일정 검색  |
    | 3. 등록된 일정  |
    | 4. 달력 보기  |
    | 5. 프로그램 종료 |
    ''')
    str_command = input('명령을 입력하세요.(1, 2, 3, 4, 5) > ')
    return int(str_command)


def registe_schedule():
    str_day = input('날짜를 입력하세요(yyyy.mm.dd) > ')
    date = input('일정을 입력하세요 > ')
    f = open('schedule.txt', 'a')
    f.write(str_day + '>')
    f.write(date)
    f.write('\n')
    f.close


def search_schedule():
    search = input('날짜를 입력하세요(yyyy.mm.dd) > ')
    f = open('schedule.txt', 'r')
    while True:
        line = f.readline()
        if search == line[:10]:
            print(line[10:])
        if not line:
            break
    f.close()


def search_entire_schedule():
    f = open("schedule.txt", 'r')
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
    f.close()
