temp = int(input())

h = temp // 3600
temp = temp - h * 3600

m = temp // 60
temp = temp - m * 60

s = temp

print(f'{int(h)}:{int(m)}:{int(s)}')