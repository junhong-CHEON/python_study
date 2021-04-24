#%%
import datetime as dt

while True:
    myage = int(input("나이를 입력하세요. :"))
    age = 23
    
    if age == myage:
        print("정답")
        break
    else:
        print("다시")

nowyear = dt.datetime.now().year

print("너는 %d 년생 이구나" %(nowyear - age + 1))

# %%
