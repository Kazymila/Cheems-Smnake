'''
[Cheems Smnake]
Description: It's a snake game cheemsificated :D
Autor: Kazy
'''
import turtle
import random
import time
from pyglet import font
from playsound import playsound

# Set Window
window = turtle.Screen()
window.setup(683,600)
window.bgcolor("#2c2a38")
window.title("Cheems Smnake")
turtle.Screen()._root.iconbitmap("Assets/cheemsIcon.ico")

# Load font
font.add_file("Assets/joystix monospace.ttf")
font_src = ("joystix monospace", 15, "normal")
font_h1 = ("joystix monospace", 32, "normal")

# Sounds
PICKUP_SOUND = "Assets/Sounds/pickupFood.wav"
DEATH_SOUND = "Assets/Sounds/wallHit.wav"
BONK_SOUND = "Assets/Sounds/bonk.wav"

# Sprites
SPRITE_CHEEMS = ["Assets/Sprites/cheems_1.gif","Assets/Sprites/cheems_2.gif",
	         	 "Assets/Sprites/bonk_1.gif","Assets/Sprites/bonk_2.gif"]
SPRITE_PORTRAITS = ["Assets/Sprites/Portrait_nice.gif",
					"Assets/Sprites/Portrait_happy.gif",
					"Assets/Sprites/Portrait_anxiety.gif",
					"Assets/Sprites/Portrait_sad.gif",
					"Assets/Sprites/Portrait_dead.gif"]

# ========================= Add cheems ==============================
for i in range(len(SPRITE_CHEEMS)):
	window.addshape(SPRITE_CHEEMS[i])

for i in range(len(SPRITE_PORTRAITS)):
	window.addshape(SPRITE_PORTRAITS[i])

cheems = turtle.Turtle()
cheems.shape(SPRITE_CHEEMS[0])
cheems.speed(0)
cheems.penup()
cheems.setpos(-5,20)

portrait = turtle.Turtle()
portrait.shape(SPRITE_PORTRAITS[0])
portrait.speed(0)
portrait.penup()
portrait.hideturtle()

# ======================== Create Frame =============================
x_leftLimit = -window.window_width()/2.3
x_rightLimit = window.window_width()/2.3
y_topLimit = window.window_height()/2.5
y_floorLimit = -window.window_height()/2.3

frame_line = turtle.Turtle()
frame_line.color("white")
frame_line.hideturtle()
frame_line.speed(0)
frame_line.penup()
frame_line.setpos(x_leftLimit,y_topLimit)
frame_line.pensize(2)
frame_line.pendown()
frame_line.goto(x_rightLimit,y_topLimit)
frame_line.goto(x_rightLimit,y_floorLimit)
frame_line.goto(x_leftLimit,y_floorLimit)
frame_line.goto(x_leftLimit,y_topLimit)

portrait.setpos(x_rightLimit-55, y_topLimit+63)

# ========================= Score Board =============================
score = 0
highscore = 0
score_label = turtle.Turtle()
score_label.hideturtle()
score_label.color("white")
score_label.speed(0)
score_label.penup()
score_label.setpos(x_leftLimit+10,y_topLimit+15)
score_label.write("Score = "+str(score)+" | High Score = "+str(highscore), font=font_src)

def updateScore():
	score_label.clear()
	score_label.write("Score = "+str(score)+" | High Score = "+str(highscore), font=font_src)

# =========================== Labels ================================
by = turtle.Turtle()
by.hideturtle()
by.color("white")
by.speed(0)
by.penup()
by.setpos(x_rightLimit-80,y_floorLimit-27)
by.write("@Kazymila", font=font_src)

Title = turtle.Turtle()
Title.hideturtle()
Title.color("white")
Title.speed(0)
Title.penup()
Title.setpos(x_leftLimit+60,y_topLimit-80)
Title.write("Cheems Smnake", font=font_h1)

gameover = turtle.Turtle()
gameover.hideturtle()
gameover.color("white")
gameover.speed(0)
gameover.penup()
gameover.setpos(x_leftLimit+120,y_topLimit-80)

play_text = turtle.Turtle()
play_text.hideturtle()
play_text.color("white")
play_text.speed(0)
play_text.penup()
play_text.setpos(x_leftLimit+130,y_floorLimit+80)
play_text.write("Press Emnter to play", font=font_src)

# ======================== Snake and food ===========================
## Snake head
head = turtle.Turtle(shape="square")
head.hideturtle()
head.color("#edc558")
head.speed(0)
head.penup()

## Snake body
body_segments = []

def snakeGrow():
	segment = head.clone()
	segment.speed(0)
	body_segments.append(segment)

## Set food
food = turtle.Turtle(shape="square")
food.hideturtle()
food.color("#f54242")
food.speed(0)
food.penup()

def setFood():
	x_pos = random.randint(int(x_leftLimit)+50, int(x_rightLimit)-25)
	y_pos = random.randint(int(y_floorLimit)+50, int(y_topLimit)-25)
	if(head.position() == (x_pos,y_pos)): setFood()
	else: food.setpos(x_pos,y_pos)

# =========================== Game Over =============================
def gameOver():
	playsound(DEATH_SOUND)
	updateScore()
	portrait.shape(SPRITE_PORTRAITS[-1])

	# Reset the snake
	head.hideturtle()
	head.goto(0,0)

	for i in range(0,len(body_segments)):
		body_segments[i].clear()
		body_segments[i].hideturtle()

	body_segments.clear()
	food.hideturtle()
	portrait.hideturtle()

	gameover.write("Game Omver", font=font_h1)
	play_text.write("Press Emnter to play", font=font_src)

	# Bonk animation:
	cheems.shape(SPRITE_CHEEMS[2])
	cheems.setpos(0,20)
	cheems.showturtle()

	while(running):
		time.sleep(0.2)
		cheems.shape(SPRITE_CHEEMS[3])
		playsound(BONK_SOUND)
		play_text.clear()
		time.sleep(0.2)
		cheems.shape(SPRITE_CHEEMS[2])
		play_text.write("Press Emnter to play", font=font_src)
	
	window.onkey(playGame, "Return")

# ============================ Run Game =============================
def playGame():
	global score
	global highscore
	global start

	cheems.hideturtle()
	Title.clear()
	gameover.clear()
	play_text.clear()

	portrait.showturtle()
	head.showturtle()
	food.showturtle()

	setFood() 

	### Main loop 
	while(running):
		# Listen the player input
		window.listen()

		# When snake eat food
		if(head.distance(food.position()) < 20):
			portrait.shape(SPRITE_PORTRAITS[1])
			setFood()
			snakeGrow()
			score += 1
			if(score > highscore):
				highscore = score
			updateScore()
			playsound(PICKUP_SOUND)

		# Move snake body with the head
		for i in range(len(body_segments)-1,0,-1):
			x = body_segments[i-1].xcor()
			y = body_segments[i-1].ycor()
			body_segments[i].goto(x,y)

		if (len(body_segments)>0):
			x = head.xcor()
			y = head.ycor()
			body_segments[0].goto(x,y)

		# Move snake head
		if (len(body_segments) < 1):
			head.forward(15)
		else:
			head.forward(25)

		# Collision with the walls
		if(head.ycor() > y_topLimit-20 or head.ycor() < y_floorLimit+20 or 
     	   head.xcor() > x_rightLimit-25 or head.xcor() < x_leftLimit+25): 
			score = 0
			gameOver()
			break

		# Cheems with anxiety for posible collision
		if(head.ycor() > y_topLimit-50 or head.ycor() < y_floorLimit+50 or 
     	   head.xcor() > x_rightLimit-50 or head.xcor() < x_leftLimit+50): 
			portrait.shape(SPRITE_PORTRAITS[2])
		else:
			portrait.shape(SPRITE_PORTRAITS[0])

		# Collision with the body
		for segment in body_segments:
			if(segment.distance(head) < 9):
				score = 0
				gameOver()
				break

# ======================= Set controllers ===========================
def moveUp():
	if(len(body_segments) > 0 and head.heading() == 270): return
	else: head.setheading(90)

def moveLeft():
	if(len(body_segments) > 0 and head.heading() == 0): return
	else: head.setheading(180)

def moveRight():
	if(len(body_segments) > 0 and head.heading() == 180): return
	else: head.setheading(0)

def moveDown():
	if(len(body_segments) > 0 and head.heading() == 90): return
	else: head.setheading(270)

def quit():
	global running
	running = False

window.onkey(moveUp, "Up")
window.onkey(moveLeft, "Left")
window.onkey(moveRight, "Right")
window.onkey(moveDown, "Down")

window.onkey(moveUp, "w")
window.onkey(moveLeft, "a")
window.onkey(moveRight, "d")
window.onkey(moveDown, "s")

window.onkey(playGame, "Return")
turtle.TK._default_root.protocol("WM_DELETE_WINDOW", quit)

# ============================ Start Game ===========================
window.listen()
running = True

# Cheems intro animation:
while(running):
	time.sleep(0.4)
	cheems.shape(SPRITE_CHEEMS[1])
	play_text.clear()
	time.sleep(0.4)
	cheems.shape(SPRITE_CHEEMS[0])
	play_text.write("Press Emnter to play", font=font_src)