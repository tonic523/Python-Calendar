# 월별 일수
days_of_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
                 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
while True:
    # 월, 연도 입력
    str_year = input('연도를 입력하세요(-1 입력시 종료) > ')
    year = int(str_year)
    str_month = input('월을 입력하세요 > ')
    month = int(str_month)
    # 반복 탈출
    if year == -1:
        print('bye')
        break
    # 윤년 구하기
    if year % 4 == 0:
        days_of_month[2] = 29
        if year % 100 == 0:
            days_of_month[2] = 28
            if year % 400 == 0:
                days_of_month[2] = 29
    # 1일의 요일 받기
    year -= 1
    weekday = 1 + \
        ((year + year // 4 - year // 100 + year // 400) % 7)
    if month != 1:
        for i in range(1, month):
            weekday = (weekday + (days_of_month[i] % 7)) % 7
    print(weekday)
    # 입력된 년,월로 달력 출력
    print('\t\t< ', year, ' ', month, ' >')
    print('Mo\tTu\tWe\tTh\tFr\tSa\tSu')
    for i in range(weekday):
        print('\t', end='')
    for days in range(1, days_of_month[int(month)] + 1):
        if (days + weekday) % 7 == 0:
            print(days, '\t')
        else:
            print(days, '\t', end='')
    print()
