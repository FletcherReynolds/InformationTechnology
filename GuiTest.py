from guizero import App, Text, TextBox, PushButton, Picture


def check_user():
    if un_box.value =='Fletcher' and pw_box.value == 'password1':
        message = Text (app, text='Access Granted')
    else:
        message = Text(app, text='Access Denied')


app = App(title='login', bg = "snow3")
message = Text(app, text= 'Username', color='green')
un_box = TextBox(app)
message1 = Text(app, text= 'password', color='green')
pw_box = TextBox(app)
Submit = PushButton (app, command=check_user)
picture = Picture(app, image="D:\\Semester 2\\Term 4\\ICT\\elon.PNG", )

app.display()