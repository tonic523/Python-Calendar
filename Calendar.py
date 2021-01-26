days_of_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
                 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
month = input('월을 입력하세요 > ')
print(month, '월의 최대 일수는 ', days_of_month[int(month)], '입니다')
