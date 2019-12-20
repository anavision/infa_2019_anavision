from graph import *


def krug(a, b, c, d, e, f, g, o, p):
    """
    risuem krug
    a,b,c -rgb цвет линии
    d,e,f - цвет заливки
    g,o, - координаты круга, p - радиус
    """
    penColor(a, b, c)
    brushColor(d, e, f)
    circle(g, o, p)
    return ()


krug(160, 60, 60, 56, 102, 70, 250, 200, 150)   # bashka
krug(250, 21, 193, 255, 120, 40, 200, 130, 25)  #glaza
krug(250, 201, 193, 255, 120, 40, 300, 130, 25)  #praviyglaz
krug(250, 21, 193, 0, 0, 0, 200, 130, 10)  #zrachki
krug(250, 21, 193, 0, 0, 0, 300, 130, 10)  #zrachki


rectangle(100, 10, 150, 60)

#hren rervdfvfddfvdfvdfffffffffffffff

#rectangle(300, 100, 120, 100)

run()
