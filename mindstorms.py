import turtle

def draw_square(bradt):

	bradt.shape("turtle")
	bradt.speed(6)
	bradt.color("red", "green")

	for i in range(4):
		bradt.forward(100)
		bradt.right(90)

def draw_circle(angie):
	angie.shape("arrow")
	angie.color("blue")
	angie.circle(100)
def draw_triangle(baby):
	#baby = turtle.Turtle()
	baby.shape("circle")
	baby.color("green")
	for i in range(4):
		if i == 0 or i == 3:
			baby.forward(50)
		else:
			baby.forward(100)
		baby.right(120)

brad = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("yellow")	
for i in range(36):
	brad.right(10)
	#draw_square(brad)
	draw_triangle(brad)
	
#draw_circle()
window.exitonclick()
		
