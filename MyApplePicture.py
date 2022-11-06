import turtle
import threading

turtle.speed(200)
turtle.fillcolor("#E50000")
turtle.begin_fill()

sideAngle = 180  # в градусах 100, два бока
topAngle = -180  # в градусах 100, две верхушки
topSideAngle = 90  # в градусах 90, четыре штуки

topRadius = 10
topSideRadius = 20
sideRadius = 100

turtle.circle(sideRadius, sideAngle)
turtle.circle(topSideRadius, topSideAngle)

turtle.left(180)
turtle.circle(topRadius, topAngle)  # середина верхушки, зелёный лист
## print(turtle.position())
turtle.left(180)
turtle.circle(topSideRadius, topSideAngle)
turtle.circle(sideRadius, sideAngle)

turtle.circle(topSideRadius, topSideAngle)
turtle.left(180)
turtle.circle(topRadius, topAngle)

turtle.left(180)
turtle.circle(topSideRadius, topSideAngle)

turtle.end_fill()

###################################### листок

turtle.fillcolor("#32CD32")
turtle.begin_fill()

turtle.up()
turtle.goto(-30.00, 170.00)
turtle.down()

turtle.left(270)  # 270
turtle.circle(102, -40)  # правая сторона

turtle.left(320) # 320
turtle.circle(40, 120)  # 40 120 левая сторона

turtle.end_fill()

###################################### тёмно-красное пятно справа
## turtle.speed(10)
turtle.fillcolor("#FF0000")
turtle.begin_fill()

turtle.up()
turtle.goto(20.00, 40.00) # 20 40

turtle.left(400)  # 360
turtle.circle(40, 120)  # 40 120 левая сторона

turtle.left(320) # 320
turtle.circle(102, -40)  # правая сторона

turtle.end_fill()

###################################### белое пятно слева
## turtle.speed(10)
turtle.fillcolor("#FFFFFF")
turtle.begin_fill()

turtle.goto(-120.00, 100.00)

turtle.left(230)  # 270
turtle.circle(102, -40)  # правая сторона

turtle.left(320) # 320
turtle.circle(40, 120)  # 40 120 левая сторона

turtle.end_fill()


def drawMyName(X=-320):
    turtle.goto(X, -50.00)  # -320.00  -50.00  >>>>>>>  -20.00  -50.00
    turtle.color('#0000FF')
    turtle.write("Қайрулла Руслан Ербулатұлы (ВТиП-402)", move=True, align='left', font=('Arial', 14, 'bold'))
    # time.sleep(1)
    turtle.undo()

def tudaSuda():
    while(True):
        for i in range(-320, -20, 20):
            drawMyName(i)
        for i in range(-20, -320, -20):
            drawMyName(i)

threading.Thread(target=tudaSuda(), args=()).start()



turtle.done()
