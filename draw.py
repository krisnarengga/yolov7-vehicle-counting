import cv2
import sys
import pyautogui
path = sys.argv[1]
if 'youtube.com/' in str(path) or 'youtu.be/' in str(path):  # if source is YouTube video
    import pafy
    path = pafy.new(path).getbest(preftype="mp4").url
elif path == '1':
    path = 1
cap = cv2.VideoCapture(path)

area = []
cont = 0
def cap_cursor(event,x,y,flags,param):
    global area,cont
    if event == cv2.EVENT_LBUTTONDOWN and len(area) < 4:
        area.append((x,y))
        print(area)
        pyautogui.press('space')
        
minute = eval(sys.argv[2])

cap.set(cv2.CAP_PROP_POS_MSEC,minute*60*1000)

while 1:
    ret,frame = cap.read()
    if len(area) >= 4:
        with open(sys.argv[3],"w") as f :
            f.write(str(area))
        break
    for i in area:
        cv2.circle(frame,i,2,(0,0,255),-1)
    try:
        cv2.line(frame,area[0],area[1],(0,255,0),2)
        cv2.line(frame,area[2],area[3],(0,255,0),2)
    except:
        pass
    cv2.imshow('Window',frame)
    cv2.setMouseCallback('Window',cap_cursor)
    
    cv2.waitKey(0)
    print("continue")
cap.set(cv2.CAP_PROP_POS_MSEC,0)

ret,frame = cap.read()
cv2.line(frame,area[0],area[1],(0,255,0),2)
cv2.line(frame,area[2],area[3],(0,255,0),2)
cv2.imshow('Window',frame)
cv2.waitKey(0)