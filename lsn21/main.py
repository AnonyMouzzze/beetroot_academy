import sys
from userInterface import MainWindow
from controll import CalculatorControll
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    CalculatorControll(view=window)
    window.show()
    sys.exit(app.exec_())
    
main()