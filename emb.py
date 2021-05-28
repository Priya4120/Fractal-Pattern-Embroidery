import turtle
from turtle import *

speed(200)

length = float(input("Please enter length of koch pattern, in 0.1mm: "))
depth = float(input("Please enter depth i.e. level of koch pattern: "))

stitches = []


def f(length,depth,stitches):

   

    if depth == 0:

        x1=round(turtle.xcor());
        y1=round(turtle.ycor());
        
        turtle.forward(length)

        x2=round(turtle.xcor());
        y2=round(turtle.ycor());

        if x2-x1<0:
            dx=255 + round((x2-x1))
            dx2=abs(round((x2-x1)))
        else:
            dx=round((x2-x1))
            dx2=255-round((x2-x1))

        if y2-y1<0:
            dy=255 + round((y2-y1))
            dy2=abs(round((y2-y1)))
        else:
            dy=round((y2-y1))
            dy2=255-round((y2-y1))

        
        stitches.append(dx)
        stitches.append(dy)
        stitches.append(dx2)
        stitches.append(dy2)
        stitches.append(dx)
        stitches.append(dy)
        stitches.append(dx2)
        stitches.append(dy2)
        stitches.append(dx)
        stitches.append(dy)
        

    else:
        f(length/3,depth-1,stitches)
        turtle.right(60)
        f(length/3,depth-1,stitches)
        turtle.left(120)
        f(length/3,depth-1,stitches)
        turtle.right(60)
        f(length/3,depth-1,stitches)

    print(stitches)


def getStitches():
    stitches = [128, 2] # 128 = escape_character -> 2 = Move followed by 8 bit displacement X,Y

    stitches += [0,0,0,0,0,0,]
    #for i in range(9):
        #stitches += [0,0,0,0,0,0,]
        #stitches += [128, 0, 225, 50]

    
    for i in range(6):
        f(length,depth,stitches)       
        right(60)

    #for i in range(2):
       # stitches += [128, 0, 120, 30]

    #stitches += [128, 1] # 128 = escape_character -> 1 = Change to next thread in list


    #for i in range(6):
        #f(length,depth,stitches)       
        #right(60)
            
    #for i in range(2):
        #stitches += [128, 0, 120, 30]

    #stitches += [128, 1] # 128 = escape_character -> 1 = Change to next thread in list



    #for i in range(6):
        #f(length,depth,stitches)       
        #right(60)


    stitches += [128, 16]   # 128 = escape_character -> 16 = last_stitch 
    return stitches

def getJeffList(stitches):
    jefBytes = [    128, 0, 0, 0,   # The byte offset of the first stitch
                    10, 0, 0, 0,   # unknown command
                    ord("2"), ord("0"), ord("2"), ord("1"), #YYYY
                    ord("0"), ord("2"), ord("2"), ord("4"), #MMDD
                    ord("1"), ord("5"), ord("2"), ord("1"), #HHMM
                    ord("0"), ord("0"), 99, 0, #SS00
                      3, 0, 0, 0,   # Thread count nr. (nr of thread changes)
                    (len(stitches)//2) & 0xff, (len(stitches)//2) >> 8 & 0xff, 0, 0, # Number of stitches
                      3, 0, 0, 0, # Sewing machine Hoop
                    # Extent 1
                     50, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                    # Extent 2
                     50, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                    # Extent 3
                     50, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                    # Extent 4
                     50, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                    # Extent 5
                     50, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                      9, 0, 0, 0, # Thread Color (white)
                      7, 0, 0, 0, # Thread Color (white)
                      6, 0, 0, 0, # Thread Color (white)
                     13, 0, 0, 0, # Thread type (unknown)
                ] + stitches
    return jefBytes
def main():
    data = bytes(getJeffList(getStitches()))
    with open("snowflake.jef", "wb") as f:
        f.write(data)

if __name__ == '__main__':
    main()
