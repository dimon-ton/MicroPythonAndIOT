from tkinter import *
from turtle import Turtle
from PIL import Image, ImageTk
from threading import Thread
import time

GUI = Tk()
GUI.geometry('10000x900')
GUI.title('Dashboard ควบคุมระบบ IOT ควบคุม Smart Farm')
GUI.state('zoomed')

canvas = Canvas(GUI, width=1500, height=900)
canvas.place(x=0, y=0)

background = ImageTk.PhotoImage(Image.open('EP.8_Dashboard/farm.png'))
canvas.create_image(300, 200, anchor=NW, image=background)

canvas.create_polygon([630,426,675,450,675,495,629,470], fill='green', width=1, outline=None, tags='d1')
canvas.create_text(300, 300, text='ประตูฟาร์มกำลังเปิด', fill='green', font=('Angsana New', 30, 'bold'), tags='d1')
canvas.create_line(425, 320, 640, 455, fill='black', width=4, tags='d1')

door_state = True
def DoorOnOff(event):
    global door_state
    door_state = not door_state
    canvas.delete('d1')
    if door_state == True:
        canvas.create_polygon([630,426,675,450,675,495,629,470], fill='green', width=1, outline=None, tags='d1')
        canvas.create_text(300, 300, text='ประตูฟาร์มกำลังเปิด', fill='green', font=('Angsana New', 30, 'bold'), tags='d1')
        canvas.create_line(425, 320, 640, 455, fill='black', width=4, tags='d1')
    else:
        canvas.create_polygon([630,426,675,450,675,495,629,470], fill='red', width=1, outline=None, tags='d1')
        canvas.create_text(300, 300, text='ประตูฟาร์มกำลังปิด', fill='red', font=('Angsana New', 30, 'bold'), tags='d1')
        canvas.create_line(425, 320, 640, 455, fill='black', width=4, tags='d1')

GUI.bind('<Return>', DoorOnOff)

# fan rotating
fan = ImageTk.PhotoImage(Image.open('EP.8_Dashboard/fan.png')) 
canvas.create_image(1063,461,image=fan,tags='img3', anchor=CENTER)



angle = 0

def run_fan(event=None):
	# fan = ImageTk.PhotoImage(resize_image('fan-icon.png',100))
	global angle
	while True:	
		if angle != 0:
			canvas.delete('img3')
			fan = ImageTk.PhotoImage(image = Image.open('EP.8_Dashboard/fan.png').rotate(angle)) 
			canvas.create_image(1063,461,image=fan,tags='img3')
		angle += 20
		if angle >= 360:
			angle = 0
		time.sleep(0.1)

task = Thread(target=run_fan)
task.start()

GUI.mainloop()