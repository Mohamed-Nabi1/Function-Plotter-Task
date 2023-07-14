import re
from PySide2.QtWidgets import QApplication ,QWidget,QDesktopWidget,QLabel,QMessageBox,QPushButton,QDoubleSpinBox,QVBoxLayout,QHBoxLayout,QLineEdit
from PySide2.QtGui import QFont
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import numpy as np

# our default font for all text
font=QFont("Times",20)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Plotter")
        self.setGeometry(100,100,800,800)
        self.center()

        #create widgets and layout of function
        self.function = QLineEdit()
        self.function.setFont(font) 
        self.function.setText("x")
        self.func_label = QLabel(text="Function: ")
        self.func_label.setFont(font) 

        input_layout1 = QHBoxLayout()
        input_layout1.addWidget(self.func_label)
        input_layout1.addWidget(self.function)


        #create widgets and layout of max min for x value
        self.mn=QDoubleSpinBox()
        self.mn_label = QLabel(text="Minimum x: ")
        self.mn_label.setFont(font)
        self.mn.setRange(-1000,1000)
        self.mn.setValue(-1)
        self.mn.setFont(font)
        self.mx=QDoubleSpinBox()
        self.mx_label = QLabel(text="Maximum x: ")
        self.mx_label.setFont(font)
        self.mx.setRange(-1000,1000)
        self.mx.setValue(1)
        self.mx.setFont(font)

        input_layout2 = QHBoxLayout()
        input_layout2.addWidget(self.mn_label)
        input_layout2.addWidget(self.mn)
        input_layout2.addWidget(self.mx_label)
        input_layout2.addWidget(self.mx)
        

        #create widgets and layout of plot (submit) button
        self.plot = QPushButton(text="Plot")
        self.plot.setFont(font)
        self.plot.setFixedSize(200,70)

        input_layout3 = QHBoxLayout()
        input_layout3.addWidget(self.plot)


        #create widgets and layout of 2D matplot figure
        self.fig = FigureCanvas(Figure(figsize=(8, 8)))
        self.axes = self.fig.figure.subplots()

        input_layout4 = QHBoxLayout()
        input_layout4.addWidget(self.fig)


        #create vertical layout to group all horizontal layout
        all_layout = QVBoxLayout()
        all_layout.addLayout(input_layout1)
        all_layout.addLayout(input_layout2)
        all_layout.addLayout(input_layout3)
        all_layout.addLayout(input_layout4)
        self.setLayout(all_layout)

        # create messageBox to show all error messages on it
        self.error_message = QMessageBox()
        self.error_message.setFont(QFont("Times",12))
        self.error_message.setWindowTitle("Error!")

        # when x value or click on plot button , call change_value() function
        self.mn.valueChanged.connect(lambda _: self.change_value())
        self.mx.valueChanged.connect(lambda _: self.change_value())
        self.plot.clicked.connect(lambda _: self.change_value())
        self.change_value()

    def change_value(self):
        mn = self.mn.value()
        mx = self.mx.value()

        # error Minimum x must be less than or equal to Maximum x
        if mn >= mx:
            self.mn.setValue(mx-1)          
            self.error_message.setText("'Minimum x' should be less than 'Maximum x'")
            self.error_message.show()
            return
        
        equation=self.function.text()
        allowed_words=['x','/','*','^','-','+']

        #all letter in equation
        all_letters=re.findall('[a-zA-Z]+', equation)
        #check for allowed letter in equation 'x' only 
        for letter in all_letters:
            if letter not in allowed_words:
                self.error_message.setText(f"'{letter}' is not allowed to use in math equation.\nOnly equations of 'x' are allowed.\ne.g., x^2+2*x-1\n")
                self.error_message.show()

        #all symbols in equation
        all_symbols=re.findall('[^0-9A-Za-z]+',equation)
        #check for allowed symbols ('*','/','-','+','^')
        for letter in all_symbols:
            if letter not in allowed_words:
                self.error_message.setText(f"'{letter}' is not allowed to use in math equation.\nOnly these symbols '*','/','-','+','^' are allowed.\ne.g., 3*x^2+x/2-1\n")
                self.error_message.show()

        #replace '^' to '**' for math equation
        equation = equation.replace('^', '**')

        # make interval array from mn to mx
        x = np.linspace(mn, mx)

        # to deal with constant functions e.g., y = 1
        if "x" not in equation:
            equation = f"{equation}+0*x"


        # try to convert equation string to real equation for plot it otherwise raise error 
        try:
            y=eval(equation)
        except:
            self.error_message.setText(f"there is an error in this equation {equation}\nrewrite your equation.\ne.g., x^2+2*x-1\n")
            self.error_message.show()
            return
    
        self.axes.clear()
        # plot and draw the equation
        self.axes.plot(x, y)
        self.fig.draw()

    # to center window on screen
    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())
    
''' 
    check whether the current script is being run on its own or being imported somewhere else  
    main.py is run directly,when the interpreter sets the __name__ variable as __main__ 
    and when it is run through test_window.py by importing, the __name__ variable is set as the name of the python script (main)
'''
if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=Window()
    window.show()

    app.exec_()
    sys.exit(0)