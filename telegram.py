from PyQt5 import QtCore, QtGui, QtWidgets

MESSAGES = [
    {
        'username': 'Eshmat',
        'text': 'Salom'
    },
    {
        'username': 'Eshmat',
        'text': 'Oshna'
    },
    {
        'username': 'Eshmat',
        'text': 'Alo'
    },
    {
        'username': 'Toshmat',
        'text': 'Salom'
    },
    {
        'username': 'Eshmat',
        'text': 'Axvollar qaley?'
    },
    {
        'username': 'Toshmat',
        'text': 'Uxlavoman'
    },
    {
        'username': 'Eshmat',
        'text': 'Futbol o\'ynaylik'
    },
    {
        'username': 'Toshmat',
        'text': 'Ertalab sigir sog\'shim kerak'
    },
    {
        'username': 'Eshmat',
        'text': 'G\'ishmatnikiga borib ko\'raman'
    },
    {
        'username': 'Toshmat',
        'text': 'Xop'
    },
]

class TelegramUI(object):
    def __init__(self, name: str, Form, x: int, y: int):
        self.username = name
        
        Form.setObjectName("Form")
        Form.resize(650, 600)
        Form.move(x, y)
        self.friendName = QtWidgets.QLabel(Form)
        self.friendName.setGeometry(QtCore.QRect(60, 50, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.friendName.setFont(font)
        self.friendName.setObjectName("friendName")
        self.messageBox = QtWidgets.QListWidget(Form)
        self.messageBox.setGeometry(QtCore.QRect(60, 110, 421, 371))
        self.messageBox.setObjectName("messageBox")
        self.input = QtWidgets.QLineEdit(Form)
        self.input.setGeometry(QtCore.QRect(60, 500, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input.setFont(font)
        self.input.setText("")
        self.input.setObjectName("input")
        self.sendBtn = QtWidgets.QPushButton(Form)
        self.sendBtn.setGeometry(QtCore.QRect(390, 500, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sendBtn.setFont(font)
        self.sendBtn.setStyleSheet("background-color: lightblue;")
        self.sendBtn.setObjectName("sendBtn")
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setGeometry(QtCore.QRect(500, 110, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clearBtn.setFont(font)
        self.clearBtn.setStyleSheet("background-color: red;")
        self.clearBtn.setObjectName("clearBtn")
        self.deleteBtn = QtWidgets.QPushButton(Form)
        self.deleteBtn.setGeometry(QtCore.QRect(500, 160, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deleteBtn.setFont(font)
        self.deleteBtn.setObjectName("deleteBtn")
        self.editBtn = QtWidgets.QPushButton(Form)
        self.editBtn.setGeometry(QtCore.QRect(500, 210, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editBtn.setFont(font)
        self.editBtn.setObjectName("editBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        Form.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", self.username))
        self.friendName.setText(_translate("Form", "Foydalanuvchi"))
        self.sendBtn.setText(_translate("Form", "Send"))
        self.clearBtn.setText(_translate("Form", "Clear"))
        self.deleteBtn.setText(_translate("Form", "Delete"))
        self.editBtn.setText(_translate("Form", "Edit"))


class Chat:
    def __init__(self, user_1: TelegramUI, user_2: TelegramUI):
        self.user_1 = user_1
        self.user_2 = user_2

        for message in MESSAGES:
            item1 = QtWidgets.QListWidgetItem(message["text"])
            item2 = QtWidgets.QListWidgetItem(message["text"])
            item2.setTextAlignment(QtCore.Qt.AlignRight)
            
            if message["username"] == user_1.username:
                user_1.messageBox.addItem(item2)
                user_2.messageBox.addItem(item1)
            else:
                user_1.messageBox.addItem(item1)
                user_2.messageBox.addItem(item2)




        user_1.friendName.setText(user_2.username)
        user_2.friendName.setText(user_1.username)

        user_1.sendBtn.clicked.connect(lambda: self.sendMessage(user_1, user_2))
        user_2.sendBtn.clicked.connect(lambda: self.sendMessage(user_2, user_1))

        user_1.deleteBtn.clicked.connect(lambda: self.deleteMessage(user_1, user_2))


    def sendMessage(self, fromUser: TelegramUI, toUser: TelegramUI):
        message = fromUser.input.text()
        messageItem = QtWidgets.QListWidgetItem(message)
        messageItem.setTextAlignment(QtCore.Qt.AlignRight)

        fromUser.messageBox.addItem(messageItem)
        toUser.messageBox.addItem(QtWidgets.QListWidgetItem(message))

        fromUser.input.clear()


    def deleteMessage(self, fromUser: TelegramUI, toUser: TelegramUI):
        index = fromUser.messageBox.currentIndex().row()
        fromUser.messageBox.takeItem(index)
        toUser.messageBox.takeItem(index)



app = QtWidgets.QApplication([])

oyna_1 = QtWidgets.QWidget()
oyna_2 = QtWidgets.QWidget()

user_1 = TelegramUI("Eshmat", oyna_1, 200, 200)
user_2 = TelegramUI("Toshmat", oyna_2, 1000, 200)

chat = Chat(user_1, user_2)

app.exec_()
