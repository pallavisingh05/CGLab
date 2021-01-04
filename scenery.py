from graphics import *
win = GraphWin("Draw",900,650,True)

# ================Fish Functions===================== 
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
'''========================fish functions over here==========================='''

#===========================making boat=======================================
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
    #return MakeBoat(Boat[0].getPoints()[0])

#===========================Boat finished=====================================

greenland=Rectangle(Point(0,500),Point(900,650))
greenland.draw(win)
greenland.setFill('green')

Sun=Circle(Point(430,350),50)
Sun.draw(win)
Sun.setFill('yellow')

water=Rectangle(Point(0,350),Point(900,500))
water.draw(win)
water.setFill('blue')

Hill1_endPoints=[Point(0,300),Point(200,150),Point(500,350),Point(0,350)]
Hill1=Polygon(Hill1_endPoints)
Hill1.draw(win)
Hill1.setFill('saddlebrown')

Hill2_endPoints=[Point(350,350),Point(650,175),Point(900,300),Point(900,350)]
Hill2=Polygon(Hill2_endPoints)
Hill2.draw(win)
Hill2.setFill('saddlebrown')

for i in range(30):
    Sun.move(0,-5)
    time.sleep(0.05)
while(True):
    p1=Point(850,410)
    MoveTheFishRight(MoveTheFishLeft(GetTheFish(p1)));

    p2=Point(800,400)
    MoveTheBoatRight(MoveTheBoatLeft(MakeBoat(p2)))


