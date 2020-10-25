# -----------------Importing dependecies
from tkinter import  *
import  cv2
from PIL import  ImageTk,Image
import  time
import threading
# SOUND \
# from pyQT5.QMultimedia import *
# from pyQT5.QtCore import QUrl
# ----------------  TKINTER APP -------------------
class App:
    def __init__(self,video_source=0):
        self.appName='Camera'
        self.root=Tk()
        self.root.title(self.appName)
        self.root.resizable(0,0)
        # self.root.wm_iconbitmap('cam.ico')
        self.root['bg']='black'
        self.video_source=video_source

        self.vidobj=MyVideoCapture(self.video_source)
        self.label=Label(self.root,text=self.appName,font=15,bg='blue',fg='white').pack(side=TOP,fill=BOTH)
#         CREATE CANVAS TO FIT THE VIDEO SOURCE
        self.canvas=Canvas(self.root,width=self.vidobj.width,height=self.vidobj.height)
        self.canvas.pack()
#         BUTTON TO TAKE THE SNAPSHOT
        self.snapBtn=Button(self.root,text='Take Snap',width=30,bg='white',fg='black',activebackground='green',command=self.snapshot)
        self.snapBtn.pack(anchor=CENTER,expand=TRUE)
        self.imgframe=Frame(self.root,height=100 , bg='gray23').pack(side=BOTTOM,fill=X)
        self.update()
        self.root.mainloop()
    def snapshot(self):
#         GET VIDEO FRAME ON PRESSING TTHE BTN
        check,frame=self.vidobj.getFrame()
        if check:
            t = threading.Thread(target=self.capture('yellow'))
            t.start()
            img='images/IMG-'+time.strftime('%H-%M-%S-%d-%m')+".jpg"
            cv2.imwrite(img,cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
#       --------SHOW SAVE MESSAGE-----------------------
            msg=Label(self.root,text='Image Saved !',bg='black',fg='green').place(x=430,y=510)

    def capture(self,color):
            self.canvas.config(highlightthickness=5, highlightbackground=color)
            t2 = threading.Thread(target=self.redefinedColor)
            t2.start()
    def redefinedColor(self):
        time.sleep(1)
        self.canvas.config(highlightthickness=5, highlightbackground='white')




    #   --------------PLAY SOUND------------
    #         file=Qurl("click.wav")
    #         content=QMediaContent(file)
    #         self.player=QMediaPlayer()
    #         self.player.setMedia(content)
    #         self.player.play()
    def update(self):
        check, frame = self.vidobj.getFrame()
        if check:
            self.photo=ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0,0,image=self.photo,anchor=NW)
        self.root.after(15,self.update)
# -------------------CLASS FOR CAPTURING VIDEO------------------
class MyVideoCapture:
    def __init__(self,video_source=0):
        # Open the video source
        self.vid=cv2.VideoCapture(video_source)
        # if video source is not open
        if not self.vid.isOpened():
            raise ValueError('Enable o open camera \n Select another video source',video_source)
        # Get video source width and height
        self.width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)


    def getFrame(self):
        if self.vid.isOpened():
            ret,frame=self.vid.read()
            # If frame is true convert the frame to RGB and return it
            if ret:
                return (ret,cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
            else:
                return (ret,None)
        else:
            return None

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
# ----------------------- MAIN -----------------------
if __name__=='__main__':
    App()