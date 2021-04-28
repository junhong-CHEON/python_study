#-*- coding: utf-8 -*-

# 필요한 패키지와 라이브러리를 가져옴
import os
import sys
import matplotlib as mpl
from matplotlib import font_manager

# 폰트매니저 리빌드 --> 시스템 글꼴폴더(C:/Windows/fonts)를 스캔
font_manager._rebuild()

# 설정파일의 위치 조회
conf_file_path = mpl.matplotlib_fname()
print ('설정파일 위치: ' + conf_file_path)

# 설정파일이 들어 있는 폴더
conf_file_dir = os.path.dirname(conf_file_path)
print ('설정폴더 위치: ' + conf_file_dir)

# 설정파일의 폴더 하위에 폰트파일이 위치해야 하는 폴더 경로 조합
font_path =  conf_file_dir + "/fonts/ttf"
print ('폰트폴더 위치: ' + font_path)

# 폰트 폴더를 열기 위한 명령어 수행
command = 'open ' + font_path
os.system(command)

