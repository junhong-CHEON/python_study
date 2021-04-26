#%%
i = 0
while i < 5:
    print("*" * (i+1))
    i+=1


# %%
dic = {'재석' : 82 , '광수' : 62, '민영' : 91, '승기' : 88, '종민' : 52, '새정' : 90}

value_list = list(dic.values())
key_list = list(dic.keys())

i = 0

while i < len(value_list) - 1:
    j = i + 1
    while j < len(value_list):
        if value_list[i] < value_list[j]:
            key_list[i],key_list[j] = key_list[j], key_list[i]
        j += 1
    i+=1

i = 0
while i < len(key_list):
    print(key_list[i], end = " ")
    i += 1

# %%
total = 0

for i in range(1, 10001):
    tmp = str(i)
    total += tmp.count('8')

print(total)
    
# %%
msg = 'Life is too short, You need Pyhton'
count = 0

for i in range(0, len(msg)):
    if msg[i] == 'e':
        count += 1

print(count)
# %%
height = 100
count = 0

while (height//1) > 0:
    height = (height/5) * 3
    print(height)
    count += 1

print(count - 1)
# %%
genres = ['pop','rock','rock','pop','balad']
plays = [500,600,150,800,1500]

i = 0
while i < len(plays) - 1:
    j = i + 1
    while j < len(plays):
        if plays[i] < plays[j]:
            plays[i],plays[j] = plays[j], plays[i]
            genres[i],genres[j] = genres[j], genres[i]
        j += 1
    i+=1

mydict = {}

for i in range(0, len(genres)):
    if genres[i] not in mydict:
        mydict[genres[i]] = plays[i]
        continue
    mydict[genres[i]] += plays[i]

print(mydict)
print(genres,plays)
# %%
array = [[0] * 8 for i in range(9)]

for i in range(0,8):
    dan = i + 2
    val = dan
    for j in range(0,9):
        array[j][i] = val
        val += dan
    
for i in array:
    print(i)
# %%
