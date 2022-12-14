from pygame import *
import sys
import math

def coord(ang, vinicial):
    ang1 = math.radians(ang)
    x1 = 0 
    ycoord = []
    xcoord = []

    while x1 < 1000:
        y1 = (x1*math.tan(ang1))-((9.8*x1*x1))/(2*(vinicial*vinicial)*(math.cos(ang1)*math.cos(ang1)))
        x1 = x1 + 50
        ycoord.append(y1)
        xcoord.append(x1)

    return xcoord, ycoord

def resistencia(ang, vinicial, t):
    ang1 = math.radians(ang)
    vox = vinicial*math.cos(ang1)
    voy =  vinicial*math.sin(ang1)
    av = -2 
    xcoordr = []
    ycoordr = []
    while t < 10:
        xr = vox*t + ((av*t*t)/2)
        yr = voy*t + ((-9.81*t*t)/2)
        t = t + 1
        ycoordr.append(yr)
        xcoordr.append(xr)
    return xcoordr, ycoordr

def animr(xcoordr, ycoordr, color):
    puntos = 0
    while puntos < len(xcoordr):
        draw.rect(screen, color, (xcoordr[puntos], 300-ycoordr[puntos], 10, 10), 3)
        time.delay(300)
        display.update()
        puntos += 1
        

def criticos(ang,vinicial):
    ang1 = math.radians(ang)
    alcance = ((vinicial*vinicial)*math.sin(2*ang1))/9.81
    alturamax = 300 + ((vinicial*vinicial)*(math.sin(ang1)*math.sin(ang1))/(2*9.81))

    return alcance, alturamax

def draw1():
    x1, y1 = coord(30,100)
    animr(x1, y1, (255, 0,0))
    alcance1, alturamaxima1 = criticos(30,100)
    print(alcance1)
    print(alturamaxima1)
    trayectoria = calibri.render("30°, 100m/s", True, (0,0,0))
    alcance = calibri.render("862.79 m", True, (0,0,0))    
    altura = calibri.render("427.42 m", True, (0,0,0))
    screen.blit(trayectoria, (550, 530))
    screen.blit(alcance, (550, 550))
    screen.blit(altura, (550, 570))
    
def draw1r():
    xr1, yr1 = resistencia(30,100,0)
    animr(xr1,yr1, (0, 255,0))

def draw2():
    x2, y2 = coord(41, 175)  
    animr(x2,y2, (255, 0, 0))
    alcance1, alturamaxima1 = criticos(41,175)
    print(alcance1)
    print(alturamaxima1)
    trayectoria = calibri.render("41°, 175m/s", True, (0,0,0))
    alcance = calibri.render("3091.43 m", True, (0,0,0))    
    altura = calibri.render("971.83", True, (0,0,0))
    screen.blit(trayectoria, (550, 530))
    screen.blit(alcance, (550, 550))
    screen.blit(altura, (550, 570))

def draw2r():
    xr2, yr2 = resistencia(41,175,0)
    animr(xr2,yr2, (0, 255,0))

def draw3():
    x3, y3 = coord(44,300)
    animr(x3,y3, (255, 0, 0))
    alcance1, alturamaxima1 = criticos(44,300)
    print(alcance1)
    print(alturamaxima1)
    trayectoria = calibri.render("44°, 300m/s", True, (0,0,0))
    alcance = calibri.render("9168.72 m", True, (0,0,0))    
    altura = calibri.render("2513.53 m", True, (0,0,0))
    screen.blit(trayectoria, (550, 530))
    screen.blit(alcance, (550, 550))
    screen.blit(altura, (550, 570))

def draw3r():
    xr3, yr3 = resistencia(44,300,0)
    animr(xr3,yr3, (0, 255,0))

init()
screen = display.set_mode((800,600))
calibri = font.SysFont('Calibri', 20)
fondo = transform.scale(image.load("fondo.jpg"), (800,600))
volcan = transform.scale(image.load("volcan.png"), (300,300))

while True:
    screen.fill((255,255,255))
    leyenda1 = calibri.render("Trayectoria actual: ", True, (0,0,0))
    leyenda2 = calibri.render("Alcance máximo: ", True, (0,0,0))
    leyenda3 = calibri.render("Altura máxima: ", True, (0,0,0))
    screen.blit(fondo, (0,0))
    screen.blit(volcan, (-120,310))
    screen.blit(leyenda1, (400,530))
    screen.blit(leyenda2, (400,550))
    screen.blit(leyenda3, (400,570))

    for e in event.get():
        if e.type == QUIT: sys.exit()
        if e.type == KEYDOWN and e.key == K_1:
            draw1()
            draw1r()
        elif e.type == KEYDOWN and e.key == K_2:
            draw2()
            draw2r()
        elif e.type == KEYDOWN and e.key == K_3:
            draw3()
            draw3r()
