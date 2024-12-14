list_1 = []
list_2 = []

with open('/workspace/A-O-C-2024/1/input.txt', 'r') as cal: 
    for line in cal.readlines():
        id_1, id_2 = line.split()
        list_1.append(int(id_1))
        list_2.append(int(id_2))


result = sum([x * list_2.count(x) for x, y in zip(list_1, list_2) if x in list_2])

print(result)
