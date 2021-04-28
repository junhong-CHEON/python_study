#-*- coding: utf-8 -*-
"""
    01-line1.py
        선 그래프 : 한가지 지표에 대한 특정 기준(주로 시간)에 따른 변화
"""
# matplotlib라는 모듈에서 pyplot이라는 기능만 골라서 가져오기
# -> pip install matplotlib
from matplotlib import pyplot

# 기본값 f(x) = x
# -> 그래프로 표현할 데이터는 리스트나 배열 등 연속성 데이터 형식으로 준비
# -> 리스트의 각 원소는 y축. 리스트의 index는 x축
data = [ 0, 1, 2, 3, 4 ]

# 그래프 설정 시작 -> 모든 그래프 작업시작시에 호출
pyplot.figure()

# 리스트 데이터를 선 그래프로 표현.
# -> 리스트의 각 값은 y축이 되고, 리스트 값의 인덱스는 x축이 된다.
pyplot.plot(data, linestyle='-', marker='+')

# 그래프 표시하기
pyplot.show()

# 그래프 관련 설정 해제
pyplot.close()
