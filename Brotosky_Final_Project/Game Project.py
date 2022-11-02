import turtle
import math
import random
import time
from turtle import *


print("Welcome! The object of the game is to guess what image is being drawn.")
print("If you guess incorrectly, the game will restart.")
print("There are 10 images in total. If you guess all 10 correctly, I will draw you a cool picture.")
print("You may have to move the turtle window or shell window to see the images and/or type your response in the shell.")
print("Please wait for the image to finish being drawn to input answer.")
print("Let's go!")





def draw_snowflake():
    print("Hint: This word has 9 letters.")
    
    myPen = turtle.Turtle()
    myPen.shape("turtle")
    myPen.speed(500)
    myPen.width(15)
    myPen.color("#c4e2e2")
    myPen.left(90)

    for i in range (1,7):
        myPen.forward(100)
        myPen.forward(-30)
        myPen.left(60)
        myPen.forward(30)
        myPen.forward(-30)

        myPen.right(120)
        myPen.forward(30)
        myPen.forward(-30)

        myPen.left(60)
        myPen.forward(-70)
        myPen.left(60)
      
def draw_sunflower():
    print("Hint: This word has 9 letters.")
    
    def drawPhyllotacticPattern( t, petalstart, angle = 137.508, size = 2, cspread = 4 ):
        """print a pattern of circles using spiral phyllotactic data"""
        # initialize position
        turtle.pen(outline=1,pencolor="black",fillcolor="orange")
        # turtle.color("orange")
        phi = angle * ( math.pi / 180.0 )
        xcenter = 0.0
        ycenter = 0.0
       
        # for loops iterate in this case from the first value until < 4, so
        for n in range (0,t):
                r = cspread * math.sqrt(n)
                theta = n * phi
                
                x = r * math.cos(theta) + xcenter
                y = r * math.sin(theta) + ycenter
 
                # move the turtle to that position and draw 
                turtle.up()
                turtle.setpos(x,y)
                turtle.down()
                # orient the turtle correctly
                turtle.setheading(n * angle)
                if n > petalstart-1:
                        #turtle.color("yellow")
                        drawPetal(x,y)
                else: turtle.stamp()
                
    def drawPetal( x, y ):
            turtle.up()
            turtle.setpos(x,y)
            turtle.down()
            turtle.begin_fill()
            #turtle.fill(True)
            turtle.pen(outline=1,pencolor="black",fillcolor="yellow")
            turtle.right(20)
            turtle.forward(100)
            turtle.left(40)
            turtle.forward(100)
            turtle.left(140)
            turtle.forward(100)
            turtle.left(40)
            turtle.forward(100)
            turtle.up()
            turtle.end_fill() # this is needed to complete the last petal

    turtle.shape("turtle")
    turtle.speed(0) # make the turtle go as fast as possible
    drawPhyllotacticPattern( 200, 160, 137.508, 4, 10 )





def draw_cloud():
    print("Hint: This word has 5 letters.")
    
    screen = turtle.Screen()
    screen.setup(1000,1000)
    screen.title("Random Cloud - PythonTurtle.Academy")

    turtle.speed(0)
    turtle.hideturtle()
    turtle.up()
    turtle.bgcolor('dodger blue')
    turtle.pencolor('white')
    turtle.pensize(2)

    n = 500 # number of points on each ellipse
    # X,Y is the center of ellipse, a is radius on x-axis, b is radius on y-axis
    # ts is the starting angle of the ellipse, te is the ending angle of the ellipse
    # P is the list of coordinates of the points on the ellipse
    def ellipse(X,Y,a,b,ts,te,P):
        t = ts
        for i in range(n):
            x = a*math.cos(t)
            y = b*math.sin(t)
            P.append((x+X,y+Y))
            t += (te-ts)/(n-1)

    # computes Euclidean distance between p1 and p2
    def dist(p1,p2):
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

    # draws an arc from p1 to p2 with extent value ext
    def draw_arc(p1,p2,ext):
        turtle.up()
        turtle.goto(p1)
        turtle.seth(turtle.towards(p2))
        a = turtle.heading() 
        b = 360-ext 
        c = (180-b)/2
        d = a-c
        e = d-90
        r = dist(p1,p2)/2/math.sin(math.radians(b/2)) # r is the radius of the arc
        turtle.seth(e) # e is initial heading of the circle
        turtle.down()
        turtle.circle(r,ext,100)
        return (turtle.xcor(),turtle.ycor()) # returns the landing position of the circle
                                             # this position should be extremely close to p2 but may not be exactly the same
                                             # return this for continuous drawing to the next point


    def cloud(P):
        step = n//10 # draw about 10 arcs on top and bottom part of cloud
        a = 0 # a is index of first point
        b = a + random.randint(step//2,step*2) # b is index of second point
        p1 = P[a] # p1 is the position of the first point
        p2 = P[b] # p2 is the position of the second point
        turtle.fillcolor('white')
        turtle.begin_fill()
        p3 = draw_arc(p1,p2,random.uniform(70,180)) # draws the arc with random extention
        while b < len(P)-1:
            p1 = p3 # start from the end of the last arc 
            if b < len(P)/2: # first half is top, more ragged
                ext = random.uniform(70,180)
                b += random.randint(step//2,step*2)
            else: # second half is bottom, more smooth
                ext = random.uniform(30,70)
                b += random.randint(step,step*2)
            b = min(b,len(P)-1) # make sure to not skip past the last point
            p2 = P[b] # second point
            p3 = draw_arc(p1,p2,ext) # draws an arc and return the end position
        turtle.end_fill()

    P = [] # starting from empty list
    ellipse(0,0,300,200,0,math.pi,P)
    ellipse(0,0,300,50,math.pi,math.pi*2,P) 
    cloud(P)





def draw_olympics():
    print("Hint: This word has 8 letters.")
    
    t = turtle.Turtle()
    t.pensize(6) #Set the thickness of the pen to 6
    firstRowColors = ["blue", "black", "red"] #firstRowColors is a list of colors that are present in the first row of logo
    for i in range(3):
      t.penup()
      t.pencolor(firstRowColors[i])
      t.goto(i*110, 0)
      t.pendown()
      t.circle(50)
     
    secondRowColors = ["", "yellow", "", "green"]
    for i in range(1, 4, 2):
      t.penup()
      t.pencolor(secondRowColors[i])
      t.goto(i*55, -50)
      t.pendown()
      t.circle(50)




def draw_batman():
    print("Hint: This word has 6 letters.")
    
    myPen = turtle.Turtle()
    myPen.speed(500)

    window = turtle.Screen()
    window.bgcolor("#000000")
    myPen.color("yellow")

    zoom=20

    myPen.left(90)
    myPen.penup()
    myPen.goto(-7*zoom,0)
    myPen.pendown()

    for xz in range(-7*zoom,-3*zoom,1):
      x=xz/zoom
      absx=math.fabs(x)
      y=1.5*math.sqrt((-math.fabs(absx-1))*math.fabs(3-absx)/((absx-1)*(3-absx)))*(1+math.fabs(absx-3)/(absx-3))*math.sqrt(1-(x/7)**2)+(4.5+0.75*(math.fabs(x-0.5)+math.fabs(x+0.5))-2.75*(math.fabs(x-0.75)+math.fabs(x+0.75)))*(1+math.fabs(1-absx)/(1-absx))
      myPen.goto(xz,y*zoom)

    for xz in range(-3*zoom,-1*zoom-1,1):
      x=xz/zoom
      absx=math.fabs(x)
      y=(2.71052+1.5-0.5*absx-1.35526*math.sqrt(4-(absx-1)**2))*math.sqrt(math.fabs(absx-1)/(absx-1))
      myPen.goto(xz,y*zoom)
      
    myPen.goto(-1*zoom,3*zoom)
    myPen.goto(int(-0.5*zoom),int(2.2*zoom))
    myPen.goto(int(0.5*zoom),int(2.2*zoom))
    myPen.goto(1*zoom,3*zoom)

    for xz in range(1*zoom+1,3*zoom+1,1):
      x=xz/zoom
      absx=math.fabs(x)
      y=(2.71052+1.5-0.5*absx-1.35526*math.sqrt(4-(absx-1)**2))*math.sqrt(math.fabs(absx-1)/(absx-1))
      myPen.goto(xz,y*zoom)

    for xz in range(3*zoom+1,7*zoom+1,1):
      x=xz/zoom
      absx=math.fabs(x)
      y = 1.5*math.sqrt((-math.fabs(absx-1))*math.fabs(3-absx)/((absx-1)*(3-absx)))*(1+math.fabs(absx-3)/(absx-3))*math.sqrt(1-(x/7)**2)+(4.5+0.75*(math.fabs(x-0.5)+math.fabs(x+0.5))-2.75*(math.fabs(x-0.75)+math.fabs(x+0.75)))*(1+math.fabs(1-absx)/(1-absx))
      myPen.goto(xz,y*zoom)

    for xz in range(7*zoom,4*zoom,-1):
      x=xz/zoom
      absx=math.fabs(x)
      y=(-3)*math.sqrt(1-(x/7)**2) * math.sqrt(math.fabs(absx-4)/(absx-4))
      myPen.goto(xz,y*zoom)

    for xz in range(4*zoom,-4*zoom,-1):
      x=xz/zoom
      absx=math.fabs(x)
      y=math.fabs(x/2)-0.0913722*x**2-3+math.sqrt(1-(math.fabs(absx-2)-1)**2)
      myPen.goto(xz,y*zoom)

    for xz in range(-4*zoom-1,-7*zoom-1,-1):
      x=xz/zoom
      absx=math.fabs(x)
      y =(-3)*math.sqrt(1-(x/7)**2) * math.sqrt(math.fabs(absx-4)/(absx-4))
      myPen.goto(xz,y*zoom)
      
    myPen.penup()
    myPen.goto(300,300)




def draw_vw():
    print("Hint: This word has 10 letters.")
    
    #////////////////////////////////////////#0d4671 
    ts =turtle.Screen()
    player = turtle.Turtle()
    player.color("white")
    player.shape("turtle")
    player.speed(0)################speed
    turtle1= turtle.Turtle()
    turtle1.shape("turtle")
    turtle1.speed(0)############speed
    turtle1.penup()
    turtle1.rt(90)
    turtle1.fd(316)
    turtle1.lt(90)
    turtle1.pendown()
    turtle1.width(13)
    turtle1.color("grey")

    turtle1.circle(312,360)
    turtle1.color("#0d4671")
    turtle1.begin_fill()

    turtle1.lt(90)
    turtle1.penup()
    turtle1.fd(25)
    turtle1.rt(90)
    turtle1.pendown()
    turtle1.width(38)

    turtle1.color("#0d4671")
    turtle1.circle(290,360)

    turtle1.lt(90)
    turtle1.penup()
    turtle1.fd(38)
    turtle1.rt(90)
    turtle1.pendown()
    turtle1.width(38)

    turtle1.color("white")
    turtle1.circle(252,360)
    turtle1.penup()
    turtle1.lt(90)


    turtle1.fd(38)
    turtle1.rt(90)
    turtle1.pendown()
    turtle1.width(38)
    turtle1.color("#0d4671")
    turtle1.circle(214,360)
    turtle1.end_fill()


    turtle1.penup()
    turtle1.lt(45)
    turtle1.fd(65)
    turtle1.lt(70)
    turtle1.width(6)
    turtle1.pendown()
    turtle1.color("white")#######color
    turtle1.fd(130)
    turtle1.bk(200)
    turtle1.rt(90)
    turtle1.fd(15)
    turtle1.lt(41)
    turtle1.fd(370)
    turtle1.lt(90)
    turtle1.fd(54)
    turtle1.lt(90)
    turtle1.fd(273)
    turtle1.rt(132)
    turtle1.fd(115)
    turtle1.lt(65)
    turtle1.fd(70)
    turtle1.lt(67)
    turtle1.fd(110)
    turtle1.rt(132)
    turtle1.fd(269)
    turtle1.lt(87)
    turtle1.fd(51)
    turtle1.lt(93)
    turtle1.fd(375)
    turtle1.lt(45)
    turtle1.fd(15)
    turtle1.lt(87)
    turtle1.fd(230)
    turtle1.penup()
    turtle1.fd(30)
    turtle1.pendown()
    turtle1.fd(230)
    turtle1.lt(90)
    turtle1.fd(54)
    turtle1.lt(90)
    turtle1.fd(186)
    turtle1.rt(130)
    turtle1.fd(190)
    turtle1.lt(90)
    turtle1.fd(48)
    turtle1.lt(87)
    turtle1.fd(225)
    turtle1.lt(65)
    turtle1.fd(53)
    turtle1.lt(67)
    turtle1.fd(13)
    turtle1.width(30)
    turtle1.fd(215)
    turtle1.lt(90)
    turtle1.fd(25)
    turtle1.lt(91)
    turtle1.fd(216)
    turtle1.rt(130)
    turtle1.fd(218)
    turtle1.lt(85)
    turtle1.fd(26)
    turtle1.lt(95)

    turtle1.fd(215)

    turtle1.lt(64)
    turtle1.fd(51)
    turtle1.penup()
    turtle1.fd(155)
    turtle1.lt(66)
    turtle1.pendown()
    turtle1.fd(107)
    turtle1.lt(90)
    turtle1.fd(30)
    turtle1.lt(90)
    turtle1.fd(295)
    turtle1.rt(131)
    turtle1.fd(126)
    turtle1.lt(67)
    turtle1.fd(52)
    turtle1.lt(64)
    turtle1.fd(134)
    turtle1.rt(133)
    turtle1.fd(295)
    turtle1.lt(90)
    turtle1.fd(25)
    turtle1.lt(90)
    turtle1.fd(356)
    turtle1.lt(133)
    turtle1.fd(200)
    #turtle1.color("red")
    turtle1.lt(175)
    turtle1.fd(180)
    turtle1.bk(180)
    turtle1.lt(54)
    turtle1.fd(190)
    turtle1.lt(131)
    turtle1.fd(320)
    turtle1.bk(328)
    turtle1.lt(25)
    turtle1.fd(65)

    ###############################
    player.color("#0d4671")
    player.width(20)
    player.fd(63)
    player.bk(102)
    player.penup()
    player.bk(600)
    player.pendown()
    player.penup()
    player.fd(980)
    player.width(5)
    player.pendown()




def draw_rainbow():
    print("Hint: This word has 7 letters.")

    width = 30
    radius = 330
    y_start = -radius/2
    pensize(width+1)
    # Draw red half-circle
    penup()
    setposition(radius, y_start)
    setheading(90)
    pendown()
    pencolor('red')
    circle(radius,180)
    # Draw orange half-circle
    radius -= width
    penup()
    setposition(radius, y_start)
    setheading(90)
    pendown()
    pencolor('orange')
    circle(radius,180)
    # Draw yellow half-circle
    radius -= width
    penup()
    setposition(radius, y_start)
    setheading(90)
    pendown()
    pencolor('yellow')
    circle(radius,180)
    # Draw green half-circle
    radius -= width
    penup()
    setposition(radius, y_start)
    setheading(90)
    pendown()
    pencolor('green')
    circle(radius,180)
    # Draw blue half-circle
    radius -= width
    penup()
    setposition(radius, y_start)
    setheading(90)
    pendown()
    pencolor('blue')
    circle(radius,180)
    # Draw indigo half-circle
    radius -= width
    penup()
    setposition(radius, y_start)
    setheading(90)
    pendown()
    pencolor('indigo')
    circle(radius,180)
    # Draw violet half-circle
    radius -= width
    penup()
    setposition(radius, y_start)
    setheading(90)
    pendown()
    pencolor('violet')
    circle(radius,180)
    # Finish
    hideturtle()





def draw_flag(): 
    print("Hint: This has two words with 16 letters total.")

    turtle.speed(0)
    # create a screen
    screen = turtle.getscreen()
    # set background color of screen
    screen.bgcolor("white")
    # set tile of screen
    screen.title("USA Flag - https://www.pythoncircle.com")
    # "Yesterday is history, tomorrow is a mystery, 
    # but today is a gift. That is why it is called the present.”
    # — Oogway to Po, under the peach tree, Kung Fu Panda Movie
    oogway = turtle.Turtle()
    # set the cursor/turtle speed. Higher value, faster is the turtle
    oogway.speed(100)
    oogway.penup()
    # decide the shape of cursor/turtle
    oogway.shape("turtle")

    # flag height to width ratio is 1:1.9
    flag_height = 250
    flag_width = 475

    # starting points
    # start from the first quardant, half of flag width and half of flag height
    start_x = -237
    start_y = 125

    # For red and white stripes (total 13 stripes in flag), each strip width will be flag_height/13 = 19.2 approx
    stripe_height = flag_height/13
    stripe_width = flag_width

    # length of one arm of star
    star_size = 10


    def draw_fill_rectangle(x, y, height, width, color):
        oogway.goto(x,y)
        oogway.pendown()
        oogway.color(color)
        oogway.begin_fill()
        oogway.forward(width)
        oogway.right(90)
        oogway.forward(height)
        oogway.right(90)
        oogway.forward(width)
        oogway.right(90)
        oogway.forward(height)
        oogway.right(90)
        oogway.end_fill()
        oogway.penup()

    def draw_star(x,y,color,length) :
        oogway.goto(x,y)
        oogway.setheading(0)
        oogway.pendown()
        oogway.begin_fill()
        oogway.color(color)
        for turn in range(0,5) :
            oogway.forward(length)
            oogway.right(144)
            oogway.forward(length)
            oogway.right(144)
        oogway.end_fill()
        oogway.penup()


    # this function is used to create 13 red and white stripes of flag
    def draw_stripes():
        x = start_x
        y = start_y
        # we need to draw total 13 stripes, 7 red and 6 white
        # so we first create, 6 red and 6 white stripes alternatively    
        for stripe in range(0,6):
            for color in ["red", "white"]:
                draw_fill_rectangle(x, y, stripe_height, stripe_width, color)
                # decrease value of y by stripe_height
                y = y - stripe_height            

        # create last red stripe
        draw_fill_rectangle(x, y, stripe_height, stripe_width, 'red')
        y = y - stripe_height


    # this function create navy color square
    # height = 7/13 of flag_height
    # width = 0.76 * flag_height
    # check references section for these values
    def draw_square():
        square_height = (7/13) * flag_height
        square_width = (0.76) * flag_height
        draw_fill_rectangle(start_x, start_y, square_height, square_width, 'navy')


    def draw_six_stars_rows():
        gap_between_stars = 30
        gap_between_lines = stripe_height + 6
        y = 112
        # create 5 rows of stars
        for row in range(0,5) :
            x = -222
            # create 6 stars in each row
            for star in range (0,6) :
                draw_star(x, y, 'white', star_size)
                x = x + gap_between_stars
            y = y - gap_between_lines


    def draw_five_stars_rows():
        gap_between_stars = 30
        gap_between_lines = stripe_height + 6
        y = 100
        # create 4 rows of stars
        for row in range(0,4) :
            x = -206
            # create 5 stars in each row
            for star in range (0,5) :
                draw_star(x, y, 'white', star_size)
                x = x + gap_between_stars
            y = y - gap_between_lines

    # start after 5 seconds.
    time.sleep(5)
    # draw 13 stripes
    draw_stripes()
    # draw squares to hold stars
    draw_square()
    # draw 30 stars, 6 * 5
    draw_six_stars_rows()
    # draw 20 stars, 5 * 4. total 50 stars representing 50 states of USA
    draw_five_stars_rows()
    # hide the cursor/turtle
    oogway.hideturtle()
    





def draw_moon():
    print("Hint: This word has 4 letters.")
    
    turtle.bgcolor('dark blue')
    turtle.up()
    turtle.goto(0,-200)
    turtle.color('orange')
    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()
    turtle.up()
    turtle.goto(50,-150)
    turtle.color('dark blue')
    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()





def draw_panda():
    print("Hint: This word has 5 letters.")
    
    painter = turtle.Turtle()

    painter.pensize(3)
    painter.speed(0)


    #Draw face

    painter.color('black', 'black')
    painter.pendown()
    painter.circle(100)


    #Draw right ear

    painter.penup()
    painter.setx(50)
    painter.sety(185)
    painter.pendown()

    painter.begin_fill()
    painter.right(90)
    painter.circle(30, -260)
    painter.end_fill()


    #Draw left ear

    painter.penup()
    painter.setx(-50)
    painter.sety(185)
    painter.pendown()

    painter.left(170)
    painter.begin_fill()
    painter.right(90)
    painter.circle(30, 260)
    painter.end_fill()


    #Draw left eye

    painter.penup()
    painter.setx(-40)
    painter.sety(90)
    painter.pendown()

    painter.begin_fill()
    painter.circle(30)
    painter.end_fill()

    painter.left(10)
    painter.penup()
    painter.setx(-30)
    painter.sety(110)
    painter.pendown()

    painter.color('white', 'white')
    painter.begin_fill()
    painter.circle(15)
    painter.end_fill()

    painter.penup()
    painter.setx(-30)
    painter.sety(115)
    painter.pendown()

    painter.color('black', 'black')
    painter.begin_fill()
    painter.circle(5)
    painter.end_fill()


    #Draw right eye

    painter.penup()
    painter.setx(40)
    painter.sety(90)
    painter.pendown()

    painter.color('black', 'black')
    painter.begin_fill()
    painter.circle(30)
    painter.end_fill()

    painter.penup()
    painter.setx(30)
    painter.sety(110)
    painter.pendown()

    painter.color('white', 'white')
    painter.begin_fill()
    painter.circle(15)
    painter.end_fill()

    painter.penup()
    painter.setx(30)
    painter.sety(115)
    painter.pendown()

    painter.color('black', 'black')
    painter.begin_fill()
    painter.circle(5)
    painter.end_fill()


    #Draw mouth and nose

    painter.color('black', 'black')
    painter.penup()
    painter.setx(0)
    painter.sety(50)
    painter.pendown()

    painter.begin_fill()
    painter.circle(10)
    painter.end_fill()

    painter.right(90)
    painter.circle(20, 180)

    painter.penup()
    painter.setx(0)
    painter.sety(50)
    painter.pendown()

    painter.circle(20, -180)




def coolpic():
    bob = turtle.Turtle()
    bob.width(10)

    bob.penup()
    bob.goto(-200,150)
    bob.pendown()
    bob.fd(400)
    bob.rt(90)
    bob.fd(250)
    bob.rt(90)
    bob.fd(400)
    bob.rt(90)
    bob.fd(250)

    bob.penup()
    bob.rt(90)
    bob.fd(200)
    bob.lt(90)
    bob.fd(125)
    bob.lt(135)
    bob.pendown()
    bob.fd(175)
    bob.rt(180)
    bob.fd(175)
    bob.rt(90)
    bob.fd(175)
    bob.rt(180)
    bob.fd(175)
    bob.rt(135)
    bob.begin_fill()
    bob.circle(7)

    bob.penup()
    bob.goto(0,0)
    bob.write("COOL", True, align="center", font=("Arial", 74, "normal"))



def main():
    draw_snowflake()
    answer=input("What is your guess?")
    answer=answer.lower()
    if answer != "snowflake":
        main()
    turtle.clearscreen()
    
    draw_sunflower()
    answer=input("What is your guess?")
    answer=answer.lower()
    if answer != "sunflower":
        main()

    turtle.clearscreen()
    draw_olympics()
    answer=input("What is your guess?")
    answer=answer.lower()
    if answer != "olympics":
        main()

    turtle.clearscreen()
    draw_batman()
    answer=input("What is your guess?")
    answer=answer.lower()
    if answer != "batman":
        main()

    turtle.clearscreen()
    draw_vw()
    answer=input("What is your guess?")
    answer=answer.lower()
    if answer != "volkswagen":
        main()

    turtle.clearscreen()
    draw_rainbow()
    answer=input("What is your guess?")
    answer=answer.lower()
    if answer != "rainbow":
        main()

    turtle.clearscreen()
    draw_flag()
    answer=input("What is your guess?")
    answer=answer.lower()
    if answer != "american flag":
        main()

    turtle.clearscreen()
    draw_moon()
    answer=input("What is your guess?")
    answer=answer.lower()
    if answer != "moon":
        main()

    turtle.clearscreen()
    draw_panda()
    answer=input("What is your guess?")
    answer=answer.lower()
    if answer != "panda":
        main()

    turtle.clearscreen()
    draw_cloud()
    answer=input("What is your guess?")
    answer=answer.lower()
    if answer != "cloud":
        main()
        
    print("Congratulations! You got them all right! Here is your cool picture I promised ;D")
    turtle.clearscreen()
    coolpic()


main()

"""
Credits for all the images found for the game(some modifications were made for the purpose of this program):
Snowflake:
https://www.trinket.io/python/e9b4757389
Sunflower:
http://www.deborahrfowler.com/PythonResources/PythonTurtle.html
Olympics Logo:
https://www.tutorialsandyou.com/python/how-to-draw-olympics-logo-in-python-turtle-10.html
Batman Logo:
https://www.101computing.net/batman-equation/
Volkswagen Logo:
https://www.youtube.com/watch?v=eG0JS083LUo
Rainbow:
https://codewithsara.com/python-with-sara/python-101/u2-python-turtle-graphics/u2s5-turtle-circles-and-arcs/
American Flag:
https://www.pythoncircle.com/post/661/python-script-11-drawing-flag-of-united-states-of-america-using-python-turtle/
Moon:
https://pythonturtle.academy/tutorial-drawing-crescent-moon-with-python-turtle/
Panda:
https://drive.google.com/file/d/1QUESnpJss79d4LGKDzSsTXY-wYbn40NZ/view
Cloud:
https://pythonturtle.academy/tutorial-drawing-clouds-with-python-turtle/"""
