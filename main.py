accX = 0
accY = 0
x = 2
y = 2

def show():
    global accX, accY, x, y
    led.plot(x, y)
    accX = input.acceleration(Dimension.X)
    accY = input.acceleration(Dimension.Y)
    if accX < -150 and x > 0:
        x = x - 1
    if accX > 150 and x < 4:
        x = x + 1
    if accY < -150 and y > 0:
        y = y - 1
    if accY > 150 and y < 4:
        y = y + 1

basic.forever(show)
