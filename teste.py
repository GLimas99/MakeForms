self.left.mousePressEvent=self.myfunction
        self.left.mouseMoveEvent = self.myfunc


def myfunction(self, event):
    widget.dragPos = event.globalPosition().toPoint()


def myfunc(self, event):
    widget.move(widget.pos() + event.globalPosition().toPoint() - widget.dragPos)
    widget.dragPos = event.globalPosition().toPoint()
    event.accept()


def max(self):
    global multi
    status = multi
    if status == 0:
        widget.showMaximized()
        self.frame.setStyleSheet("background-color: rgb(40, 40, 40);\n"
                                 "border-radius: 0px;\n"
                                 "color:rgb(200, 200, 255);")
        self.maxwin.setText("❐")
        multi = 1
    else:
        widget.showNormal()
        menu.resize(menu.width() + 1, menu.height() + 1)
        self.frame.setStyleSheet("background-color: rgb(40, 40, 40);\n"
                                 "border-radius: 10px;\n"
                                 "color:rgb(200, 200, 255);")
        self.maxwin.setText("☐")
        multi = 0