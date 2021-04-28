# -*- coding: utf-8 -*-

# 모듈 참조
from matplotlib import pyplot

# 2013~2017년도 신생아 수
# -> [436455, 435435, 438420, 406243, 357771]
from sample import newborn

# x축의 좌표로 사용하기 위해 0부터 시작하는 리스트 생성
x = list(range(0, len(newborn)))
print(x)

# 한글폰트 설정 및 그래프 크기 설정
pyplot.rcParams["font.family"] = 'NanumGothic'
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (12, 8)

# 그래프 설정 시작
pyplot.figure()

# 세로 막대 그래프
# -> x축, y축, 그래프의 범주, 그래프의 색상 일괄 설정
pyplot.bar(x, newborn, label='신생아 수', color='#ecc2f9')  # 막대 그래프 표현
pyplot.legend()                                             # 범주 표시하기
pyplot.xlabel('년도')                                       # 기준축(x축) 라벨
pyplot.ylabel('신생아 수')                                  # 데이터(y축) 라벨
pyplot.title('2013~2017년도 신생아 수')                     # 그래프 제목
pyplot.grid()  # 격자 선 표시

# 그래프 이미지 저장하기
# -> dpi값은 이미지의 해상도. (기본값=100)
# -> 200은 해상도를 두 배로 설정하겠다는 의미
pyplot.savefig('newborn1.png', dpi=200)

# 그래프의 x좌표에 표시될 텍스트 설정
# -> x축의 좌표를 의미하는 [0, 1, 2, 3, 4] 리스트 x에 1:1로 대응될 리스트 지정
pyplot.xticks(x, ['2013년', '2014년', '2015년', '2016년', '2017년'])
pyplot.savefig('newborn2.png', dpi=200)     # 그래프 표시하기

# 그래프의 데이터 수 만큼 반복하면서 텍스트 표시하기
for i, v in enumerate(newborn):
    # -> 표시할 텍스트
    str_val = "%d명" % v

    # -> x축 좌표, y축 좌표, 표시문구, 글자크기, 색상, 가로/세로 정렬
    pyplot.text(x[i], v, str_val, fontsize=9, color='#ff0000',
                horizontalalignment='center', verticalalignment='bottom')

pyplot.savefig('newborn3.png', dpi=200)  # 그래프 표시하기

# y축의 범위를 조절하여 전달하고자 하는 스토리를 극대화 하기
pyplot.ylim(300000, 450000)
pyplot.savefig('newborn4.png', dpi=200)  # 그래프 표시하기

pyplot.close()                  # 그래프 관련 설정 해제
