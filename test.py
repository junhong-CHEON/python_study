# %%
f = open("test.txt", 'w')
f.write("가나다라f")
f.close()
# %%
f = open("test.txt", 'r', encoding = 'EUC-kr')
msg = f.read()
print(msg)
f.close()

# %%
input = [1,14,35,41,4,40]

target = [14,1,15,4,40,41]
bonus = 35

count = 0

for i in input:
    if i in target:
        count += 1

if count == 6:
    print("1등!!!")
elif count == 5 and (bonus in input):
    print("2등!!!")
else:
    print("탈락")
# %%
import locale

locale.getpreferredencoding()
# %%
