
lines = [line.rstrip('\n') for line in open('burek.txt', 'r')]
res_dict = {}

teza, visina = lines[0].split(";")

t = []
v = []

for line in lines[1:]:
    t.append(float(line.split(";")[0]))
    v.append(float(line.split(";")[1]))

res_dict[teza] = t
res_dict[visina] = v

print(res_dict)
