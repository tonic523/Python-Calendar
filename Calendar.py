# 월별 일수
days_of_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
                 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# 월 입력
month = input('월을 입력하세요 > ')
print(month, '월의 최대 일수는 ', days_of_month[int(month)], '입니다')
# 입력된 월로 달력 출력
print('\t\t< 2021 ', month, ' >')
print('Mo\tTu\tWe\tTh\tFr\tSa\tSu')
for days in range(1, days_of_month[int(month)] + 1):
    if days % 7 == 0:
        print(days, '\t')
    else:
        print(days, '\t', end='')
