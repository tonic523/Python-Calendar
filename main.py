from my_calendar import *
from prompt import *
from datetime import datetime

print_calendar(datetime.today().year, datetime.today().month)
while True:
    command = instruction()
    if command == 1:    # 1. 일정 등록
        registe_schedule()
    elif command == 2:  # 2. 일정 검색
        search_schedule()
    elif command == 3:  # 3. 등록된 일정
        search_entire_schedule()
    elif command == 4:  # 4. 달력 보기
        year, month = get_year_month()
        print_calendar(year, month)
    else:
        print('bye')
        break
