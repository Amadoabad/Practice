import cv2
import numpy as np
import pandas as pd

# Reading csv file which contains colors' names
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names = index, header = None)

# Function to simply calssify which color name should appear
def GetColorName(R,G,B):
    min = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"])) + abs(B- int(csv.loc[i,"B"]))
        if(d<min):
            min = d
            color_name = csv.loc[i, "color_name"]
    return color_name

# Function to get rgb from frame
def GetBGR(event, x, y, flags, frame):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = frame[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

# Function to edit the frame to type color name
def TypeColor(frame):
    global clicked
    if clicked:
        cv2.rectangle(frame, (20,20), (550,60), (b,g,r), -1)
        text = GetColorName(r,g,b) + ' R='+ str(r)+ ' G='+ str(g) + ' B='+ str(b)
        cv2.putText(frame,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if(r+g+b) >=550:
            cv2.putText(frame,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
    else:
        cv2.rectangle(frame, (20,20), (550,60), (125,125,125), -1)
        text = 'Douple Click the color you want ^^'
        cv2.putText(frame,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
    return frame

# Function to open a video 
def Video(path):
    global clicked
    clicked = False
    cv2.namedWindow('camera')
    while True:
        capture = cv2.VideoCapture(path)
        while True:
            flag, frame = capture.read()
            cv2.setMouseCallback('camera', GetBGR, frame)

            if flag == 0:
                break        
            
            cv2.imshow("camera", TypeColor(frame))
            if cv2.waitKey(20) & 0xFF == 27:
                break
        break
    cv2.destroyAllWindows()    

# Function to open a picture
def Picture(path):
    global clicked
    clicked = False
    cv2.namedWindow('Image')
    img = cv2.imread(path)
    cv2.setMouseCallback('Image', GetBGR, img)
    while True:
        cv2.imshow('Image',TypeColor(img))
        if cv2.waitKey(20) & 0xFF ==27:
            break
    cv2.destroyAllWindows() 

def main():
    while True:
        global clicked
        clicked = False
        choice = input('\n\ndo you want to search in a video or a picture ?\ntype video or pic\n type q to quit\n\n'.title()).lower().strip()
        if choice == 'video':
            path = input("\n\nEnter the path with the video name and extention, please\n if you want live video type live\n\n".title()).lower().strip()
            if path == 'live':
                path = 0
            print("press esc if you want to close the video!".title())
            Video(path)
            
        elif choice == 'pic':
            path = input("\n\nEnter the path with the picture name, plese\n\n".title()).lower().strip()
            Picture(path)
        elif choice == 'q':
            break
        else:
            print("\n\nmake sure to type either video or pic\n\n".title())


if __name__  == "__main__":
    # Declaring global variables
    clicked = False
    r = g = b = xpos = ypos = 0
    main()