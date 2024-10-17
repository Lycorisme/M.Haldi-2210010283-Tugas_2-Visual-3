from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

app = QApplication([])
window = QMainWindow()
label = QLabel("Labell", window)
label.move(200, 0)
button = QPushButton("Button1", window)
window.show()
app.exec_()
