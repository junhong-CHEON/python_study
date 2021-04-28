#-*- coding: utf-8 -*-

# 모듈 및 데이터 참조
from matplotlib import pyplot
from sample import seoul
from sample import label

x = list(range(0, len(seoul)))      # x축의 좌표로 사용할 리스트 만들기
print(x)

# 한글폰트 설정, 가로,세로 크기 (inch단위)
pyplot.rcParams["font.family"] = 'NanumGothic'
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (12, 8)

pyplot.figure()                     # 그래프 설정 시작

# 세로 막대 그래프
# -> 미리 준비한 리스트 x를 X축의 좌표로 사용
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
pyplot.bar(x, seoul, label='교통사고 수', color='#ffff00')  # 막대 그래프 표현

# 선 그래프 덧 그리기
# -> x축의 좌표는 seoul 리스트의 인덱스 값
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
pyplot.plot(seoul, linestyle='--', marker='.', color='#ff0000')

# 그래프 이미지 저장
pyplot.savefig("traffic1.png")

# 그래프의 x좌표에 라벨 적용하기
# -> x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# -> label = ['1월','2월','3월','4월',...,'9월','10월','11월','12월']
pyplot.xticks(x, label)

# 그 외의 기본 옵션들
pyplot.legend()                                 # 범주 표시하기
pyplot.xlabel('월')                             # 기준축(x축) 라벨
pyplot.ylabel('교통사고')                       # 데이터(y축) 라벨
pyplot.ylim(2000, 3600)                         # y축 범위 조절
pyplot.title('2017년 서울의 월별 교통사고')     # 그래프 제목
pyplot.grid()                                   # 격자 선 표시

# 그래프 이미지 저장
pyplot.savefig("traffic2.png")

# 그래프의 데이터 수 만큼 반복하면서 텍스트 표시하기
for i, v in enumerate(seoul):
    # -> 표시할 텍스트
    str_val = "%d건" % v

    # -> x축 좌표, y축 좌표, 표시문구, 글자크기, 색상, 가로/세로 정렬
    pyplot.text(x[i], seoul[i], str_val, fontsize=9, color='#000000',
                horizontalalignment='center', verticalalignment='bottom')

# 그래프 이미지 저장
pyplot.savefig("traffic3.png", dpi=300)

# 그래프 관련 설정 해제
pyplot.close()
