#-*- coding: utf-8 -*-

# 모듈 및 데이터 참조
import numpy
from matplotlib import pyplot
from sample import grade_card

# 중간고사 데이터
grade1 = grade_card["중간고사"]
print(grade1)

# 중간고사의 과목 종류
subject1 = list(grade1.keys())
print(subject1)

# 중간고사의 과목별 점수
result1 = list(grade1.values())
print(result1)

# 중간고사의 과목별 점수에 대한 인덱스(x좌표)를 구성하기 위한 배열
index1 = numpy.arange(len(result1))
print(index1)

print("-" * 30)

# 기말고사 데이터
grade2 = grade_card["기말고사"]
print(grade2)

# 기말고사의 과목 종류
subject2 = list(grade2.keys())
print(subject2)

# 기말고사의 과목별 점수
result2 = list(grade2.values())
print(result2)

# 기말고사의 과목별 점수에 대한 인덱스(x좌표)를 구성하기 위한 배열
index2 = numpy.arange(len(result2))
print(index2)


# 그래프의 한글폰트 및 가로,세로 크기
pyplot.rcParams["font.family"] = 'NanumGothic'
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (12, 8)

# 그래프 설정 시작
pyplot.figure()

# x축의 좌표값을 사용한 그래프 구현
pyplot.bar(index1-0.2, result1, label='중간고사', width=0.4, color='#f2e3f7')
pyplot.bar(index2+0.2, result2, label='기말고사', width=0.4, color='#ecc2f9')
pyplot.savefig("grade1.png")

# x축의 제목 설정 (중간고사와 기말고사 과목이 동일하므로 둘 중 하나만 지정)
pyplot.xticks(index1, subject1)

pyplot.legend()                             # 범주 표시하기
pyplot.grid()                               # 그래프에 격자 표시하기
pyplot.xlabel('과목')                       # x축 라벨
pyplot.ylabel('점수')                       # y축 라벨
pyplot.ylim(0,100)                          # y축 범위
pyplot.title('철수의 이번학기 과목별 성적') # 그래프 제목

pyplot.savefig("grade2.png")                # 그래프 이미지 저장
pyplot.close()                              # 그래프 관련 설정 해제
