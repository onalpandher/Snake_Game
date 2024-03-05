from turtle import Turtle

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]   #Tupple for snake body containing its cordinate values
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.segments=[]     #each segmnet have an indvidual turtle in it that are our 3 snakes(boxes)
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):#Snake Body(Can be created without loop as well by simply taking diff snakes and poistioning them at diff cordinates)
         for position in STARTING_POSITION:
             self.add_segment(position)


    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):            #so that on over snake recreated itself again to keep game on
        for seg in self.segments:
            seg.goto(1000,1000)   #so that snake is gone out of our screen and only new snake would be visible there
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # we are creating a loop to move are snake in different drxns
            new_x = self.segments[seg_num - 1].xcor()  # in which we r adding range
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!= DOWN:  #To not allow snake to move in backward drxn
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)