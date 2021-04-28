#-*- coding: utf-8 -*-

from matplotlib import pyplot

# 데이터 참조
from sample import grade

# 딕셔너리의 key를 리스트로 추출
keys = list(grade.keys())
print(keys)

# 딕셔너리의 value를 리스트로 추출
values = list(grade.values())
print(values)


pyplot.figure()                # 그래프 설정 시작

# 리스트 데이터를 선 그래프로 표현.
# -> 리스트의 각 값은 y축이 되고, 리스트 값의 인덱스는 x축이 된다.
pyplot.plot(values, label='grade', color='#ff00ff')

pyplot.legend()                # plot()함수의 label속성을 그래프에 적용
pyplot.grid()                  # 배경에 그리드 표시하기
pyplot.title('Level Grade')    # 그래프 제목
pyplot.xlabel('level')         # x축 라벨
pyplot.ylabel('point')         # 점수
pyplot.show()  # 그래프 저장(중간확인)


# x축의 좌표에 대한 리스트 생성
xpos = list(range(0, len(values)))
print(xpos)

# x축의 각 위치에 year 리스트의 값을 라벨로 적용
# -> 데이터 리스트의 '인덱스를 원소로 갖는 리스트'와
#    그 위치에 표시될 '텍스트를 원소로 갖는 리스트'를 설정
pyplot.xticks(xpos, keys)

pyplot.ylim(0, 100)            # y축의 범위 설정
pyplot.xlim(0, 3)              # x축의 범위 설정

pyplot.show()
pyplot.close()                 # 그래프 설정 해제
