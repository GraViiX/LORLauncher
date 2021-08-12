import sys
import os
import http.client, urllib.parse
import requests
import json

from PySide6.QtGui import *
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import *
from PySide6.QtWidgets import *

class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)
    
    isVisible = Signal(bool)

    username = Signal(str)

    @Slot()
    def on_qml_mouse_clicked(self):
        print(self)
        engine.load(os.path.join(os.path.dirname(__file__), "../Qml/Home.qml"))

    @Slot(str, str)
    def checkLogin(self, user, passw):
        url = 'http://192.168.4.231:48935/api/Users/Login'

        headers = {'content-type':'application/json'}

        body = {
            'Username': user,
            'Password': passw
        }

        data=json.dumps(body, separators=(',',':'))

        r=requests.post(url=url, data=data, headers=headers)

        print(r.text)

    @Slot(bool)
    def closewindow(self, isChecked):
        print("Is rectangle visible: ", isChecked)
        self.isVisible.emit(isChecked)


if __name__ == "__main__":

    main = MainWindow() 
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
   
    engine.rootContext().setContextProperty("Con",main)
    engine.load(os.path.join(os.path.dirname(__file__), "../Qml/Main.qml"))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
