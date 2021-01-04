from graphics import *

win = GraphWin("Draw",900,600,True)

pt = Point(100, 50)
pt.draw(win)

win.plotPixel(150,150,'red')


cir = Circle(pt, 25)
cir.draw(win)
cir.setOutline('red')
cir.setFill('blue')

oval=Oval(Point(300,500),Point(400,550))
oval.draw(win)

line = Line(pt, Point(150, 100))
line.draw(win)

line2=Line(Point(150,100),Point(100,150))
line3=Line(Point(100,150),Point(100,50))

line2.draw(win)
line3.draw(win)

#win.setBackground('red')

rect = Rectangle(Point(20, 10), Point(80,70))
rect.draw(win)

print(pt.getX())
print(pt.getY())

win.plotPixel(line2.getCenter().getX(),line2.getCenter().getY(),'white');

win.plotPixel(cir.getCenter().getX(),cir.getCenter().getY(),'white');

'''
message = Text(Point(win.getWidth()/2, 20), 'That's text')
message.setTextColor('black')
message.setStyle('italic')
message.setSize(10)
message.draw(win)


vertices=[win.getMouse(),win.getMouse(),win.getMouse(),win.getMouse()]
poly=Polygon(vertices)
poly.draw(win)
vertice2=poly.getPoints()


for x in vertice2:
    print(str(x.getX())+","+str(x.getY()))
'''
for i in range(45):
    cir.move(5,0)
    time.sleep(0.05)





def GetTheFish(p1):
    p2=Point(p1.getX()+100,p1.getY()+50)
    fish_body=Oval(p1,p2)
    fish_body.draw(win)
    fish_body.setFill('pink')

    eye=Circle(Point(p1.getX()+10,p1.getY()+20),2)
    eye.draw(win)
    eye.setFill('black')

    fish_tail=Polygon(Point(p2.getX()-20,p2.getY()-25),Point(p2.getX()+10,p1.getY()-10),Point(p2.getX()+10,p2.getY()+10))
    fish_tail.draw(win)
    fish_tail.setFill('darkblue')

    fish_wings=Polygon(Point(p1.getX()+35,p1.getY()+10),Point(p1.getX()+50,p1.getY()+10),Point(p1.getX()+65,p1.getY()-10))
    fish_wings.draw(win)
    fish_wings.setFill('darkblue')
    Fish=[eye,fish_body,fish_tail,fish_wings]
    return Fish



def MoveTheFishLeft(Fish):
    for i in range(105):
        for x in Fish:
            x.move(-5,0)
        time.sleep(0.07)

    eye=Fish[0]
    fish_body=Fish[1]
    fish_tail=Fish[2]
    fish_wings=Fish[3]
    for x in Fish:
        x.undraw()

    p1=fish_body.getP1()
    p2=fish_body.getP2()
    fish_body.draw(win)

    fish_tail=Polygon(Point(p1.getX()+20,p1.getY()+25),Point(p1.getX()-10,p1.getY()-10),Point(p1.getX()-10,p2.getY()+10))
    fish_tail.draw(win)
    fish_tail.setFill('darkblue')

    eye=Circle(Point(p2.getX()-10,p1.getY()+20),2)
    eye.draw(win)
    eye.setFill('black')

    fish_wings=Polygon(Point(p2.getX()-35,p1.getY()+10),Point(p2.getX()-50,p1.getY()+10),Point(p2.getX()-65,p1.getY()-10))
    fish_wings.draw(win)
    fish_wings.setFill('darkblue')
    
    FishTurn=[eye,fish_body,fish_tail,fish_wings];
    
    return FishTurn

def MoveTheFishRight(Fish):
    for i in range(105):
        for x in Fish:
            x.move(5,0)
        time.sleep(0.07)
    for x in Fish:
        x.undraw()

'''
for i in range(75):
    for x in Fish:
        x.move(-5,0)
    time.sleep(0.07)

fish_body.undraw()
fish_tail.undraw()
eye.undraw()

p1=fish_body.getP1()
p2=fish_body.getP2()
fish_body.draw(win)
fish_tail=Polygon(Point(p1.getX()+20,p1.getY()+25),Point(p1.getX()-10,p1.getY()-10),Point(p1.getX()-10,p2.getY()+10))
fish_tail.draw(win)
fish_tail.setFill('darkblue')

eye=Circle(Point(p2.getX()-10,p1.getY()+20),2)
eye.draw(win)
eye.setFill('black')


Fish=[eye,fish_body,fish_tail]
for i in range(75):
    for x in Fish:
        x.move(5,0)
    time.sleep(0.07)
'''

p1=Point(500,400)
#while(True):
Fish=GetTheFish(p1)
MoveTheFishRight(MoveTheFishLeft(Fish));



#fish_tail.draw(win)

#making boat
def MakeBoat(p2):
    Boat_base=[p2,Point(p2.getX()+150,p2.getY()),Point(p2.getX()+130,p2.getY()+40),Point(p2.getX()+20,p2.getY()+40)]
    Boat_base_shape=Polygon(Boat_base)
    Boat_upper=[Point(p2.getX()+110,p2.getY()),Point(p2.getX()+110,p2.getY()-60),Point(p2.getX()+150,p2.getY())]
    Boat_upper_shape=Polygon(Boat_upper)
    Boat_base_shape.draw(win)
    Boat_upper_shape.draw(win)
    Boat_upper_shape.setFill('brown')
    Boat_base_shape.setFill('brown')

    Boat=[Boat_base_shape,Boat_upper_shape]
    return Boat


def MoveTheBoatLeft(Boat):
    for i in range(125):
        for boatpart in Boat:
            boatpart.move(-5,0)
        time.sleep(0.05)
    vertices=Boat[0].getPoints()
    p2=Boat[0].getPoints()[0]
    for x in Boat:
        x.undraw()
    Boat_upper_shape=Polygon(Point(p2.getX(),p2.getY()),Point(p2.getX()+40,p2.getY()),Point(p2.getX()+40,p2.getY()-60))
    Boat=[Boat[0],Boat_upper_shape]
    for x in Boat:
        x.draw(win)
        x.setFill('brown')
    return Boat

def MoveTheBoatRight(Boat):
    for i in range(125):
        for boatpart in Boat:
            boatpart.move(5,0)
        time.sleep(0.05)
    for x in Boat:
        x.undraw()
    return MakeBoat(Boat[0].getPoints()[0])

p2=Point(500,400)
MoveTheBoatRight(MoveTheBoatLeft(MakeBoat(p2)))




