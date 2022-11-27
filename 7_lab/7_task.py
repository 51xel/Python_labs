import re 

f = open("./7_lab/TF14_1", 'w')
f.write("kgjhsdkjh132u9-18jfkjfo9.999klsdkf;\n12ekjfnj1d9kda8.1kaj\nkDPKAk1dk0.1dadlk1ok-221")
f.close()

try:
    print("Файл TF14_1:")
    f = open("./7_lab/TF14_1", 'r')
    print(f.read())
    f.seek(0)
except:
    print("Файл не знайдено!")

f2 = open("./7_lab/TF14_2", 'w')

tempStr = []

for line in f:
    tempStr = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', line)
    for i in tempStr:
        f2.write(i + " ")

f.close()
f2.close()
print()
try:
    print("Файл TF14_2:")
    f = open("./7_lab/TF14_2", 'r')
    print(f.read())
    f.seek(0)

except:
    print("Файл не знайдено!")

max = -999999
for i in f.read().split():
    if float(i) > float(max):
        max = i
print()
print("Максимальне число = ",max)
f.close()