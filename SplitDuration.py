"""
==============================================================================
~~~ SplitDuration ~~~

 Calculate the expected time periods of time-delay (acquired from shear-wave splitting)
 increase and decrease according to the empirical relation
 of Crampin et al. (2013).

For inquiries, bug reports or other information please contact me at:

ispingos[at]geol.uoa.gr


Ioannis Spingos (c) 2019


Reference:
Crampin, S., Gao, Y. & De Santis, A. (2013) A few earthquake conundrums resolved. 
  J Asian Earth Sci 62, 501-509. doi: 10.1016/j.jseaes.2012.10.036
==============================================================================
"""

#########################################################################################
#########################################################################################

# intial imports
from __future__ import division
from builtins import input
import sys, getopt

# console?
consoleMode=False
opts,args=getopt.getopt(sys.argv[1:],"c:",["console="])

for opt,arg in opts:
    if opt in ("-c","--console"):
        consoleMode = arg
        # make sure it's true or false in any form
        consoleMode = eval(consoleMode[0].upper()+consoleMode[1:].lower())
##
try:
    from PyQt5 import QtWidgets, QtCore
except ImportError:
    print("..: PyQt5 is not installed! Reverting to console mode...")
    consoleMode=True

##
_VERSION="1.0.0"
_VERDATE="30/01/2019"

## functions ##
def accumulation(M):
    """
    calculate accumulation period from equation
    M = 2.16log10(days)+0.37 => log10(days) = (M-0.37)/2.16
    days = 10**((M-0.37)/2.16)
    """
    return 10 ** (( M - 0.37 ) / 2.16)

def relaxation(M):
    """
    calculate relaxation period from equation
    M = 1.17log10(days)+4.01 => 
    days = 10**((M-4.01)/1.17)
    """
    return 10 ** (( M - 4.01) / 1.17)

def days2time(inp):
    """
    convert the input time (in days) to a more
    convenient format (yy-MM-DD hh:mm:ss)
    """
    # first get years
    years = inp // 365
    yy = years
    # months
    months = (inp % 365) // 30
    MM = months
    #
    days = (inp % 365) % 30
    DD = days // 1
    # now get the hours
    hours = 24 * (days % 1)
    hh = hours // 1
    # now converts minutes
    minutes = 60 * (hours % 1)
    mm =  minutes // 1
    # now seconds
    seconds = 60 *(minutes % 1)
    ss = seconds
    return "%03d year(s), %02d month(s), %02d day(s) %02d:%02d:%06.3f (%.2e days in total)" \
           % (yy,MM,DD,hh,mm,ss,inp)

## get cute?
if consoleMode:
    class SplitDurationConsole():
        def __init__(self):
            self.globName="SplitDuration"
            self.titleString="%s v.%s" % (self.globName,_VERSION)
            print("\n")
            print(self.titleString)
            print("\n")
            M=float(input("Please specify an input earthquake magnitude: "))
            print("\n")
            # calculations
            acc=accumulation(M)
            rel=relaxation(M)
            #
            print("Accumulation period: %s" % days2time(acc))
            print("Relaxation period:   %s" % days2time(rel))
            print("\n")
else:
    class SplitDuration(QtWidgets.QMainWindow):
        def __init__(self):
            """
            initialize
            """
            self.globName="SplitDuration"
            self.titleString="%s v.%s" % (self.globName,_VERSION)
            QtWidgets.QMainWindow.__init__(self)
            self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.setFocusPolicy(QtCore.Qt.StrongFocus)
            self.setWindowTitle(self.titleString)
            self.resize(400, 150)
            self.mainWidg=QtWidgets.QWidget(self)
            self.gLayout=QtWidgets.QGridLayout(self.mainWidg)
            # make labels
            self.magLabel=QtWidgets.QLabel("Magnitude:",self)
            self.magInput=QtWidgets.QLineEdit("0",self)
            self.accLabel=QtWidgets.QLabel("Accumulation (days):",self)
            self.accResLabel=QtWidgets.QLabel("",self)
            self.relLabel=QtWidgets.QLabel("Relaxation (days):",self)
            self.relResLabel=QtWidgets.QLabel("",self)
            self.updButton=QtWidgets.QPushButton("Calculate",self)
            self.updButton.clicked.connect(self.launch)
            ## add created to layout
            self.gLayout.addWidget(self.magLabel)
            self.gLayout.addWidget(self.magInput)
            self.gLayout.addWidget(self.accLabel)
            self.gLayout.addWidget(self.accResLabel)
            self.gLayout.addWidget(self.relLabel)
            self.gLayout.addWidget(self.relResLabel)
            self.gLayout.addWidget(self.updButton)
            self.setCentralWidget(self.mainWidg)

        def launch(self,consoleMode=False):
            """
            do the calculations
            """
            M=float(self.magInput.text())
            acc=accumulation(M)
            rel=relaxation(M)
            # set results to view
            self.accResLabel.setText(days2time(acc))
            self.relResLabel.setText(days2time(rel))

## LAUNCH
if not consoleMode:
    if __name__=='__main__':
        ## initialize app ##
        app=QtWidgets.QApplication(sys.argv)
        SplitDuration=SplitDuration()
        ## show app ##
        SplitDuration.show()
        sys.exit(app.exec_())
else:
    SplitDurationConsole()