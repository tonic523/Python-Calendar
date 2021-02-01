from my_calendar import get_year_month, print_calendar

while True:
    print('''
    | 1. 일정 등록  |
    | 2. 일정 검색  |
    | 3. 일정 삭제  |
    | 4. 달력 보기  |
    | 5. 프로그램 종료 |
    ''')
    str_command = input('명령을 입력하세요.(1, 2, 3, 4, 5) > ')
    command = int(str_command)
    if command == 1:
        # 1. 일정 등록
        str_day = input('날짜를 입력하세요(yyyy.mm.dd) > ')
        date = input('일정을 입력하세요 > ')
        f = open('schedule.txt', 'a')
        f.write(str_day + '>')
        f.write(date)
        f.write('\n')
        f.close
    elif command == 2:
        # 2. 일정 검색
        search = input('날짜를 입력하세요(yyyy.mm.dd) > ')
        f = open('schedule.txt', 'r')
        while True:
            line = f.readline()
            if search == line[:10]:
                print(line[10:])
            if not line:
                break
        f.close()
    elif command == 3:
        # 3. 일정 삭제
        print(command)
    elif command == 4:
        # 4. 달력 보기
        year, month = get_year_month()
        print_calendar(year, month)
    else:
        break
