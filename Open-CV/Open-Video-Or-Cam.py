import cv2
# the list of reference point
def shape_selection(event, x, y, flags, frame):
    global ref_point
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]
    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x, y))
            
# draw a rectangle around the region of interest
def draw_rectangle(frame):
    global ref_point
    if len(ref_point) == 2:
        cv2.rectangle(frame, ref_point[0], ref_point[1], (0, 255, 0), 2)
    return frame

# creating window and setting mouse callback
def video(path):
    cv2.namedWindow('camera')
    capture = cv2.VideoCapture(path)
    while True:
        flag, frame = capture.read()
        if flag == 0:
            break
        cv2.setMouseCallback("camera", shape_selection, frame)
        cv2.imshow("camera", draw_rectangle(frame))
        # if the 'esc' key is pressed, break from the loop
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # close all open windows
    cv2.destroyAllWindows() 

def main():
    while True:
        choice = input('\n\ndo you want to open a video or quit ?\nenter video or q\n\n'.title()).lower().strip()
        if choice =='video':
            path = input("Enter a path to a video or enter live to open live video\n\n".title()).lower().strip()
            if path == 'live':
                path = 0
            print("Press esc if you want to close the video!".title())
            video(path)
        if choice == 'q':
            break

if __name__ == "__main__":
    ref_point = []

    main()
