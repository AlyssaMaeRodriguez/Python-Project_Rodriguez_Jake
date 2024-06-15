import turtle


turtle.pensize(8)

def body():
	
	turtle.penup()
	turtle.goto(200,-150)
	turtle.pendown()
	turtle.color("black","#F9BB12")

	turtle.begin_fill()
	turtle.setheading(90)
	turtle.forward(250)
	turtle.circle(220,180)
	
	turtle.setheading(270)
	turtle.forward(250)
	turtle.circle(220,180)
	turtle.end_fill()
	
	turtle.penup()
	turtle.goto(0,350)
	turtle.pendown()

	turtle.begin_fill()
	turtle.setheading(354)
	turtle.circle(-260,80)
	turtle.setheading(267)
	turtle.circle(-30,87)
	
	turtle.pensize(3)
	turtle.setheading(85)
	turtle.circle(220,12)
	
	turtle.pensize(8)
	turtle.penup()
	turtle.goto(0,350)
	turtle.pendown()

	turtle.setheading(177)
	turtle.circle(260, 94)
	turtle.setheading(270)
	turtle.circle(20, 120)
	
	turtle.pensize(3)
	turtle.setheading(90)
	turtle.circle(-220,12)
	
	turtle.color("#F9BB12")
	turtle.goto(201,127)
	turtle.end_fill()

def rightarm():

	turtle.pensize(8)
	turtle.penup()
	turtle.goto(-225,60)
	turtle.pendown()
	turtle.color("black","#F9BB12")
	
	turtle.begin_fill()
	turtle.setheading(220)
	turtle.circle(800, 21)
	
	turtle.setheading(250)
	turtle.circle(40, 100)
	
	turtle.setheading(343)
	turtle.circle(400, 20)

	turtle.setheading(240)
	turtle.circle(10,180)
	
	turtle.setheading(40)
	turtle.circle(15,180)
	
	turtle.penup()
	turtle.goto(-220,-219)
	turtle.pendown()
	
	turtle.setheading(80)
	turtle.circle(15,140)
	turtle.penup()
	turtle.goto(-225,-200)
	turtle.pendown()
	turtle.setheading(90)
	turtle.circle(15,155)
	turtle.setheading(225)
	turtle.forward(12)
	
	turtle.setheading(178)
	turtle.circle(-400, 14)
	
	turtle.setheading(180)
	turtle.circle(-15, 120)
	
	turtle.setheading(59)
	turtle.circle(-800, 17)
	
	turtle.color("#F9BB12")
	turtle.goto(-225,60)
	turtle.end_fill()

def leftarm():
	
	turtle.pensize(8)
	turtle.penup()
	turtle.goto(201.3,50)
	turtle.pendown()
	turtle.color("black","#F9BB12")

	turtle.begin_fill()
	turtle.setheading(300)
	turtle.circle(500,17)

	turtle.setheading(320)
	turtle.circle(40,120)
	
	turtle.setheading(80)
	turtle.circle(600,31)
	
	turtle.circle(-7,180)
	turtle.forward(15)
	
	turtle.penup()
	turtle.goto(341,282)
	turtle.pendown()
	
	turtle.setheading(90)
	turtle.circle(-7,180)
	turtle.setheading(285)
	turtle.forward(14)
	
	turtle.penup()
	turtle.goto(355,280)
	turtle.pendown()
	
	turtle.setheading(90)
	turtle.circle(-7,180)
	turtle.setheading(287)
	turtle.forward(14)
	
	turtle.setheading(290)
	turtle.circle(-600,33)
	
	turtle.setheading(260)
	turtle.circle(-60,100)
	
	turtle.setheading(175)
	turtle.forward(14)
	
	turtle.setheading(150)
	turtle.circle(-300, 26)
	turtle.pensize(1)
	turtle.goto(201.3,50)
	turtle.end_fill()

def legs():
	
	turtle.pensize(8)
	turtle.penup()
	turtle.goto(-150,-320)
	turtle.pendown()
	turtle.color("black","#F9BB12")
	
	turtle.begin_fill()
	turtle.setheading(260)
	turtle.circle(900,20)
	
	turtle.setheading(210)
	turtle.circle(200,15)
	turtle.setheading(220)
	turtle.circle(19,180)
	turtle.setheading(35)
	turtle.forward(60)
	turtle.setheading(40)
	turtle.circle(20,70)
	turtle.setheading(100)
	turtle.circle(-900,19)
	turtle.end_fill()
	
	turtle.penup()
	turtle.goto(120,-315)
	turtle.pendown()
	
	turtle.begin_fill()
	turtle.setheading(283)
	turtle.circle(-900, 21)
	turtle.setheading(320)
	turtle.circle(-200, 15)
	turtle.setheading(285)
	turtle.circle(-19, 170)
	turtle.setheading(130)
	turtle.forward(60)
	turtle.setheading(120)
	turtle.circle(-20, 70)
	turtle.setheading(83)
	turtle.circle(900, 19)
	turtle.end_fill()
	
def eyes():
	
	turtle.penup()
	turtle.goto(-70,200)
	turtle.pendown()
	turtle.color("black", "black")
	
	turtle.begin_fill()
	turtle.circle(72)
	turtle.end_fill()
	
	turtle.penup()
	turtle.goto(160,200)
	turtle.pendown()
	
	turtle.begin_fill()
	turtle.circle(72)
	turtle.end_fill()
	
	turtle.color("white","white")
	turtle.penup()
	turtle.goto(-160,250)
	turtle.pendown()
	
	turtle.begin_fill()
	turtle.setheading(220)
	turtle.circle(65,175)
	
	turtle.setheading(58)
	turtle.circle(72,134)
	turtle.end_fill()
	
	turtle.penup()
	turtle.goto(-155,255)
	turtle.pendown()
	turtle.color("black")
	turtle.circle(72)
	
	turtle.color("white","white")
	turtle.penup()
	turtle.goto(70,250)
	turtle.pendown()
	
	turtle.begin_fill()
	turtle.setheading(220)
	turtle.circle(65,175)
	
	turtle.setheading(58)
	turtle.circle(72,134)
	turtle.end_fill()
	
	turtle.penup()
	turtle.goto(75,255)
	turtle.pendown()
	turtle.color("black")

	turtle.circle(72)
	
def nose():

	turtle.pensize(8)
	turtle.penup()
	turtle.goto(75,80)
	turtle.pendown()
	turtle.color("black","#F9BB12")
	
	turtle.begin_fill()
	turtle.setheading(90)
	turtle.circle(100,180)
	turtle.setheading(265)
	turtle.forward(50)
	turtle.setheading(265)
	turtle.circle(35,180)
	turtle.setheading(83)
	turtle.forward(60)
	turtle.setheading(83)
	turtle.circle(-30,165)
	turtle.setheading(279)
	turtle.forward(60)
	turtle.setheading(281)
	turtle.circle(34,180)
	turtle.setheading(99)
	turtle.forward(55)
	turtle.end_fill()
	
	turtle.penup()
	turtle.goto(9,105)
	turtle.pendown()
	turtle.fillcolor("black")
	
	turtle.begin_fill()
	turtle.setheading(135)
	for _ in range(2):
	    turtle.circle(40,90)
	    turtle.circle(10,90)
	
	turtle.end_fill()
	
def mouth():
	
	turtle.penup()
	turtle.goto(-50,60)
	turtle.pendown()
	turtle.fillcolor("#69260C")

	turtle.begin_fill()
	turtle.setheading(315)
	turtle.circle(40,100)
	turtle.setheading(290)
	turtle.forward(35)
	turtle.setheading(240)
	turtle.circle(-50,120)
	turtle.goto(-50,60)
	turtle.end_fill()

	turtle.penup()
	turtle.goto(-60,50)
	turtle.pendown()
	turtle.fillcolor("white")
	
	turtle.begin_fill()
	turtle.setheading(260)
	turtle.circle(12,160)
	
	turtle.setheading(280)
	turtle.circle(12,170)
	
	turtle.setheading(300)
	turtle.circle(12,190)
	
	turtle.pensize(2)
	turtle.setheading(220)
	turtle.circle(-40,100)
	
	turtle.goto(-60,50)
	turtle.end_fill()
	
	turtle.pensize(8)
	turtle.penup()
	turtle.goto(-50,60)
	turtle.pendown()
	
	turtle.setheading(315)
	turtle.circle(40,100)

	turtle.penup()
	turtle.goto(-20,10)
	turtle.pendown()
	turtle.fillcolor("#E9677D")
	
	turtle.begin_fill()
	turtle.setheading(90)
	turtle.circle(23,130)
	
	turtle.pensize(3)
	turtle.setheading(310)
	turtle.circle(50,50)
	turtle.end_fill()
	
	
body()
rightarm()
leftarm()
legs()
eyes()
mouth()
nose()

turtle.hideturtle()
turtle.done()