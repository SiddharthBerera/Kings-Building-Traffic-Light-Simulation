#import neccessary modules
import turtle
import tkinter as tk
import time 
import random
import threading

#function to start traffic light simulation when start button is pressed
def start_traffic_light_cycles():
    global waiting, mayfield_road, west_mains_road, pedestrian_crossing
    run_traffic_lights(mayfield_road, west_mains_road, pedestrian_crossing)

#function to set waiting variable to true which will alter the timings for
#the different states of the traffic lights
def wait():
    global waiting
    waiting = True

#function that uses turtle to write specfied text at a specified position
def write_text(start, text):
    pen = turtle.Turtle()
    pen.color("black")
    pen.width(3)
    pen.hideturtle()
    pen.penup()
    pen.goto(start[0],start[1])
    pen.pendown()
    pen.write(text)

#function that uses turtle to draw a vehicle traffic light
#at a specified position
def vehicle_light_box(start, width, height):
    pen = turtle.Turtle()
    pen.color("black")
    pen.width(3)
    pen.hideturtle()
    pen.penup()
    pen.goto(start[0],start[1])
    pen.pendown()
    pen.fd(width)
    pen.rt(90)
    pen.fd(height)
    pen.rt(90)
    pen.fd(width)
    pen.rt(90)
    pen.fd(height)

    red_light = turtle.Turtle()
    red_light.shape("circle")
    red_light.color("grey")
    red_light.penup()
    red_light.goto(start[0]+width/2, 40)
    red_light.pendown()

    yellow_light = turtle.Turtle()
    yellow_light.shape("circle")
    yellow_light.color("grey")
    yellow_light.penup()
    yellow_light.goto(start[0]+width/2, 0)
    yellow_light.pendown()

    green_light = turtle.Turtle()
    green_light.shape("circle")
    green_light.color("grey")
    green_light.penup()
    green_light.goto(start[0]+width/2, -40)
    green_light.pendown()

    #stores turtle objects of the different traffic light bulbs
    #so that the colour of these bulbs can be changed
    return [red_light, yellow_light, green_light]

#function that uses turtle to draw a pedestrian traffic light
#at a specified position
def pedestrian_light_box(start, width, height):
    pen = turtle.Turtle()
    pen.color("black")
    pen.width(3)
    pen.hideturtle()
    pen.penup()
    pen.goto(start[0],start[1])
    pen.pendown()
    pen.fd(width)
    pen.rt(90)
    pen.fd(height)
    pen.rt(90)
    pen.fd(width)
    pen.rt(90)
    pen.fd(height)

    red_light = turtle.Turtle()
    red_light.shape("circle")
    red_light.color("grey")
    red_light.penup()
    red_light.goto(start[0]+width/2, 40)
    red_light.pendown()

    green_light = turtle.Turtle()
    green_light.shape("circle")
    green_light.color("grey")
    green_light.penup()
    green_light.goto(start[0]+width/2, 0)
    green_light.pendown()

    #stores turtle objects of the different traffic light bulbs
    #so that the colour of these bulbs can be changed
    return [red_light, green_light]

#procedure that runs the main traffic light program, this takes the turtle traffic light bulbs
#as input and updates them as required
#timings are also dynamic by the fact that pedestrian wait button can affect these timings
def run_traffic_lights(mayfield_road, west_mains_road, pedestrian_crossing):
    global waiting
    #counts which state traffic light is in so that
    #it can be appropriatly updated 
    state = 0
    #loops forever
    while True:
        #loops through the 9 states of the traffic light 
        for n in range(0,9):
            if state == 0:
                #increments state
                state += 1 
                #updates traffic light colour
                west_mains_road[1].color("grey")
                west_mains_road[0].color("grey")
                mayfield_road[0].color("red")
                west_mains_road[2].color("green")
                pedestrian_crossing[0].color("red")
                #keeps traffic lights in this state for
                #the appropriate amount of time
                time.sleep(10)
                #depending on whether or not pedestrian wait button has been
                #pressed allows green light to stay on for longer
                if waiting == False:
                    time.sleep(random.randint(0,30))
            elif state == 1:
                state += 1
                west_mains_road[2].color("grey")
                west_mains_road[1].color("yellow") 
                time.sleep(3)  
            elif state == 2:
                state += 1 
                west_mains_road[1].color("grey")
                west_mains_road[0].color("red")
                mayfield_road[0].color("grey")
                mayfield_road[1].color("yellow")
                time.sleep(2)                 
            elif state == 3:
                state += 1
                mayfield_road[1].color("grey")  
                mayfield_road[2].color("green")
                time.sleep(10)
                #depending on whether or not pedestrian wait button has been
                #pressed allows green light to stay on for longer
                if waiting == False:
                    time.sleep(random.randint(0,30))
            elif state == 4:
                state += 1  
                mayfield_road[2].color("grey")                
                mayfield_road[1].color("yellow") 
                time.sleep(3)
            elif state == 5:
                state += 1  
                mayfield_road[1].color("grey") 
                mayfield_road[0].color("red")
                time.sleep(random.randint(1,3))
            elif state == 6:
                state += 1 
                pedestrian_crossing[0].color("grey")
                pedestrian_crossing[1].color("green") 
                time.sleep(random.randint(4,7)) 
            elif state == 7:
                state += 1 
                pedestrian_crossing[0].color("red") 
                time.sleep(3)
                #depending on whether or not pedestrian wait button has been
                #pressed allows blackout period to last for longer
                if waiting == True:
                    time.sleep(random.randint(0,22))
                    waiting = False
            elif state == 8:
                state += 1 
                pedestrian_crossing[1].color("grey") 
                west_mains_road[1].color("yellow")
                time.sleep(2)
        #resets state to 0, so that the for loop will execute the same way it just did
        #indefinetly 
        state = 0

#creates gui window for turtle drawing to ouput on 
wn = turtle.Screen()
wn.title("Toucan Traffic Lights Simulation")
wn.bgcolor("white")
canvas = wn.getcanvas()
#starts off with the pedestrian light having not been pressed
waiting = False

#creates a quit button to close program when required
quit_button = tk.Button(wn._root, text="QUIT", command = wn._destroy)
quit_button.pack(side=tk.RIGHT)

#adds required static text and drawings
write_text([-205, 70], "Mayfield Road")
mayfield_road = vehicle_light_box([-200,60], 60, 120)
write_text([-10, 70], "West Mains Road")
west_mains_road = vehicle_light_box([0,60], 60, 120)
write_text([190, 70], "Crossing Signal")
pedestrian_crossing = pedestrian_light_box([200,60], 60, 80)

write_text([195, -60], "PEDESTRIANS")
write_text([195, -60], "PEDESTRIANS")
write_text([195, -70], "push button and wait")
write_text([195, -80], "for signal opposite")

#creates a start button which starts the simulation
#since the simulation is running on an infinite loop it starts it in a 
#seperate thread so that the rest of the program can continue executing
start_button = tk.Button(canvas.master, text="START", command = threading.Thread(target=start_traffic_light_cycles).start())
start_button.pack(side=tk.LEFT)

#creates intereactive pedestrian wait button which will allow the timings to be changed
#depening on whether or not a pedestrian wants to cross the road
wait_button = tk.Button(canvas.master, text="WAIT", command = wait)
canvas.create_window(225, 100, window=wait_button)

#creates an infinite loop on a seperate thread that constantly check for interactivity from the user
wn.mainloop()

    
