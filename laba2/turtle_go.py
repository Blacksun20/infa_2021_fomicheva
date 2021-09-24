import turtle as t
t.shape('turtle')

def go(x, y, vx, vy):
    ay = -1
    dt = 0.1
    kx = 0.001
    ky = 0.1
    while vx > 0:
        t.goto(x, y)
        x+=vx*dt
        y+=vy*dt+ay*dt**2/2
        vy+=ay*dt
        vx-=kx*vx
        if y < 0:
            vy = abs(vy)*(1-ky)

go(0, 0, 10, 14)
