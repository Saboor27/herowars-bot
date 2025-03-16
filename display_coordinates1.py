import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt

class TransparentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setGeometry(100, 100, 800, 600)  # Not needed if maximizing
        self.setWindowOpacity(0.5)  # Set the opacity of the window (changeable)

    def mousePressEvent(self, event):
        # This function is called when the mouse is clicked in the window
        x = event.x()
        y = event.y()
        print(f"Click at: ({x}, {y})")
        # Optionally, write to a file
        with open('click_coordinates.txt', 'a') as f:
            f.write(f'{x}, {y}\n')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TransparentWindow()
    w.showMaximized()  # Maximize the window
    sys.exit(app.exec_())
