from guizero import App, Text, TextBox, PushButton
import cv2
from datetime import datetime
cam = cv2.VideoCapture(0)  # set camera
cam.set(cv2.CAP_PROP_FPS, 60)  # set fps
cam.set(3, 1920)  # x axis resolution
cam.set(4, 1080)  # y axis resolution

font = cv2.FONT_HERSHEY_SIMPLEX  # set font

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # set codec

out = cv2.VideoWriter('Output.avi', fourcc, 15, (1280, 720))    # sets video output

def check_user():
    if un_box.value =='Fletcher' and pw_box.value == 'password1':
        message = Text (app, text='Access Granted')
    else:
        message = Text(app, text='Access Denied')
        while True:
            re, img = cam.read()  # set camera read
            img = cv2.flip(img, 1)  # flip image
            cv2.putText(img, "You are being recorded", (300, 400), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

            cv2.putText(img, str(datetime.now()), (1000, 700), font, .5, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.imshow('Security Camera', img)  # display window

            out.write(img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:  # press ESC to quit
                cam.release()
                cv2.destroyAllWindows()
                break

app = App(title='Hello GUI')
message = Text(app, text= ' Hola amigo')
un_box = TextBox(app)
pw_box = TextBox(app)
submit = PushButton(app, command=check_user)
app.display()


