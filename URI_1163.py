while True:
    try:
        import math

        h = float(input())
        p1, p2 = map(int, input().split())
        n = int(input())
        g = 9.80665
        pi = 3.14159

        for tentativas in range(n):
            alfa, v = map(float, input().split())
            alfa = (3.14159 * alfa) / 180
            voy = v * math.sin(alfa)
            vox = v * math.cos(alfa)
            tup = voy / g

            Y = ((voy ** 2) / (2 * g)) + h
            tdown = math.sqrt(2 * Y / g)

            t = tup + tdown
            alcance = vox * t

            if p1 <= alcance <= p2:
                print(f'{alcance:.5f} -> DUCK')
            else:
                print(f'{alcance:.5f} -> NUCK')

    except EOFError:
        break
