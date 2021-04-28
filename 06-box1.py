#-*- coding: utf-8 -*-

# 모듈 및 데이터 참조
from matplotlib import pyplot
from sample import vote
from collections import Counter

# 리스트의 각 원소별 빈도수 측정
cnt = Counter(vote)
print(cnt)

# 결과를 딕셔너리로 변환
cnt_dict = dict(cnt)
print(cnt_dict)

# 변환된 결과에서 value로 구성된 리스트 추출
values = list(cnt_dict.values())
print(values)

# 변환된 결과에서 key로 구성된 리스트 추출
keys = list(cnt_dict.keys())
print(keys)


# 한글폰트 설정 및 그래프 크기 설정
pyplot.rcParams["font.family"] = 'NanumGothic'
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (12, 8)

# 그래프 설정 시작
pyplot.figure()

# 세로 막대 그래프
# -> x축, y축, 그래프의 범주 설정
pyplot.bar(keys, values, label='득표수')    # 막대 그래프 표현
pyplot.legend()                             # 범주 표시하기
pyplot.xlabel('캐릭터')                     # 기준축(x축) 라벨
pyplot.ylabel('득표수')                     # 데이터(y축) 라벨
pyplot.title('어벤져스 인기투표')           # 그래프 제목
pyplot.grid()                               # 격자 선 표시
pyplot.savefig('avengers1.png')             # 그래프 표시하기


# 그래프의 데이터 수 만큼 반복하면서 텍스트 표시하기
for i, v in enumerate(values):
    # -> 표시할 텍스트
    str_val = "%d표" % v

    # -> x축 좌표, y축 좌표, 표시문구, 글자크기, 색상, 가로/세로 정렬
    pyplot.text(keys[i], v, str_val, fontsize=9, color='#ff6600',
                horizontalalignment='center', verticalalignment='bottom')

pyplot.savefig('avengers2.png')             # 그래프 표시하기

pyplot.close()                              # 그래프 관련 설정 해제
