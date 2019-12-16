#J_mwai
#10/30/2019
#This code defines a class Button that will draw buttons on the graphics window

from graphics import*
class Button:
    def __init__(self,win,center,width,height,label):
        """Here we will define the class by first passing the parameters of drawing
            a button. Here we use the height , width and the center. We will also
            label the button by drawing a message at the center of the button"""
        w=width/2.0
        h=height/2.0
        x=center.getX()
        y=center.getY()
        #we will then get two points that we will use to draw the button.
        #We will just take the center points and and height and width to get the max point and
        #substract the height and width from the center to get the min point
        
        self.xmax=x+w
        self.xmin=x-w
        self.ymax=y+h
        self.ymin=y-h
        p1=Point(self.xmin,self.ymin)
        p2=Point(self.xmax,self.ymax)
        #After getting the points we draw the rectangle
        self.rect=Rectangle(p1,p2)
        #We the set the default color to be light gray
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label=Text(center,label)
        self.label.draw(win)
        self.activate()
    #This function gets the message that will label the button
    def getLabel(self):
        """returns the label string of this button"""
        return self.label.getText()
#The activate button will make a button active.
    #we achieve this by setting the self.active to be True
    def activate(self):
        """sets this button to active"""
        self.label.setFill('black')
        # we also increase the width of the outline width of the button
        #To make it more distinct
        self.rect.setWidth(4)
        self.active = True
#We the create a deactivate function.
        #By setting self.active to false
    def deactivate(self):
        self.label.setFill("gray")
        self.rect.setWidth(1)
        self.active = False
        #We then get a mouse click and check if it it within the button
        #This will help us button actions when either button is clicked
    def isClicked(self,pt):
        """Returns true is a pt is clicked in the button"""
        return (self.active and self.xmin<=pt.getX()<=self.xmax and self.ymin<=pt.getY() <=self.ymax)

def main():
    #Then we will draw the graphics window
    #were we will test our buttons
    win=GraphWin('JohnCode',600,600)
    win.setCoords(0.0,0.0,100.0,100.0)
    #We use the button class parameters to create a button within the graphics  window
    button_a=Button(win,Point(40,40),10,5,'Roll')
    button_b=Button(win,Point(60,60),10,5,'Exit')
    #Then we will get a point from the mouse click
    pt=win.getMouse()
    #We wlll then set conditions in that while not the exit button is clicked
    #and if roll button is clicked , deactivate the display button
    while not button_b.isClicked(pt):
        if button_a.isClicked(pt):
            button_b.activate()
        #we then get a mouse click every time we click a button
        pt=win.getMouse()
    win.close()#This just closes the window
#The function makes sure we don't output the tests in this class once it is calle
    #in another program
if __name__== '__main__':
    main()
        
