a = round(float(input()), 1)
b = round(float(input()), 1)
c = round(float(input()), 1)

if 0 <= a <= 10 and 0 <= b <= 10 and 0 <= c <= 10:
    media = ((2*a) + (3*b) + (5*c))/10
    print(f'MEDIA = {media:.1f}')

