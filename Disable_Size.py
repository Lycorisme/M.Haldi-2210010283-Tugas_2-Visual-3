from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QDesktopWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Label", self)
        self.label.move(200, 0)
        self.button = QPushButton("Button", self)
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Belajar PyQt5")
        cwa = self.frameGeometry() 
        cwc = QDesktopWidget().availableGeometry().center()
        cwa.moveCenter(cwc)
        self.move(cwa.topLeft())
        self.setFixedSize(500, 500)
app = QApplication([])
window = MyWindow()
window.show()
app.exec_()