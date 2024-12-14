list_1 = []
list_2 = []

with open('/workspace/A-O-C-2024/1/input.txt', 'r') as cal: 
    for line in cal.readlines():
        id_1, id_2 = line.split()
        list_1.append(int(id_1))
        list_2.append(int(id_2))

list_1.sort()
list_2.sort()

result = sum([x - y if x >= y else y - x for x, y in zip(list_1, list_2)])

print(result)

