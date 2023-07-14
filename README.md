## Table of contents

* [Project's Title](#Project's-Title)
* [Project Description](#Project-Description)
* [Running the Project](#Running-the-Project)
* [Running the Tests](#Running-the-Tests)
* [Working and Wrong Examples](#Working-and-Wrong-Examples)
* [Tools](#Tools)

## Project's Title
  - "Function Plotter"

## Project Description
- Take a function of x from the user, e.g., 5*x^3 + 2*x.
- Take min and max values of x from the user.
- The supported operators : + - / * ^.
- Then plots an arbitrary user-entered function through Python GUI.
- when the user enters the wrong input, display messages to explain any wrong input.

## Running the Project

To run this project, you'll need to have the following libraries installed:

- Pyside2
- Matplotlib
- pytest
- pytest-qt

You can install these libraries using pip. First, make sure that pip is installed on your system. Then, run the following commands:

```
pip install pyside2
pip install matplotlib
pip install pytest
pip install pytest-qt
```

Once you have installed these libraries, you can run the project by running the main.py file.

```
python main.py
```

## Running the Tests

To run the tests for this project, navigate to the project directory in your terminal and run the following command:

```
pytest
```

### Working and Wrong Examples

- Working Examples
  - ![start and linear function](https://github.com/Mohamed-Nabi1/Function-Plotter-Task/blob/main/project%20images/linear%20function.JPG)
  
  - ![working function](https://github.com/Mohamed-Nabi1/Function-Plotter-Task/blob/main/project%20images/square%20function.JPG)
  
  - ![constant function](https://github.com/Mohamed-Nabi1/Function-Plotter-Task/blob/main/project%20images/constant%20function.JPG)

- Wrong Examples
  - ![Function error](https://github.com/Mohamed-Nabi1/Function-Plotter-Task/blob/main/project%20images/function%20error.JPG)
  
  - ![min >= max error](https://github.com/Mohamed-Nabi1/Function-Plotter-Task/blob/main/project%20images/error%20min%2Cmax.JPG)
 
### Tools

- Python
- pyside2
- pytest
  
