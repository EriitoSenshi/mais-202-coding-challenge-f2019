from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setGeometry(400, 100, 1200, 800)
        self.setWindowTitle("Plotted graph")


def main():
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
