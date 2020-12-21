a = round(float(input()), 1)
b = round(float(input()), 1)

if 0 <= a <= 10 and 0 <= b <= 10:
    media = ((3.5*a) + (7.5*b))/11
    print(f'MEDIA = {media:.5f}')
