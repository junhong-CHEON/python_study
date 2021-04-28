#-*- coding: utf-8 -*-

from matplotlib import pyplot

# 데이터 참조
from sample import newborn
from sample import year

# 그래프 설정 시작
pyplot.figure()

# 리스트 데이터를 선 그래프로 표현.
# -> 리스트의 각 값은 y축이 되고, 리스트 값의 인덱스는 x축이 된다.
pyplot.plot(newborn, label='baby count', linestyle='--', marker='.', color='#ff6600')
pyplot.savefig('line1.png')

# plot()함수의 label속성을 그래프에 적용함 -> 범주
pyplot.legend()
pyplot.savefig('line2.png')

# 배경에 그리드 표시하기
pyplot.grid()
pyplot.savefig('line3.png')

# 그래프 제목, x축, y축 라벨 설정
pyplot.title('Newborn baby of year')
pyplot.xlabel('year')
pyplot.ylabel('newborn')
pyplot.savefig('line4.png')

# x축의 각 위치에 year 리스트의 값을 라벨로 적용
# -> 데이터 리스트의 '인덱스를 원소로 갖는 리스트'와
#    그 위치에 표시될 '텍스트를 원소로 갖는 리스트'를 설정
pyplot.xticks([0, 1, 2, 3, 4], year)
pyplot.savefig('line5.png')

# 그래프 관련 설정 해제
pyplot.close()
