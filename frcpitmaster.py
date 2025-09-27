##################################################################
#                                                                #
#                        Team 4121 Pit Master                    #
#                                                                #
#  This GUI application is designed to be used in an FRC team's  #
#  pit during competitions.  The main window of the application  #
#  shows information related to the current competition and the  #
#  team such as: match schedule, win-loss record, last match     #
#  stats, time until next match, current match number, and team  #
#  statistics for the competition.  The app will also alert the  #
#  team when it is time to prepare for the next match and guide  #
#  the team through pre-match checks and testing. Finally, the   #
#  app will display performance related statistics and graphs    #
#  from the robot in the last match.  All of the competition     #
#  related data is read from The Blue Alliance servers using     #
#  the Read API (v3) provide by The Blue Alliance.               #
#                                                                #
#  Author:  Timothy A. Fuller                      v             #
#  Date:  9/28/2025                                              #
#                                                                #
#  Version:  1.0.0                                               #
#                                                                #
#  Revision Date:  9/28/2025                                     #
#                                                                #
##################################################################


# System module imports
import sys
import os

# PyQT imports
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

# Add parent directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))


# Define main window class
class MainWindow(qtw.QMainWindow):

    # Initialize class
    def __init__(self):
        
        # Call initialization on parent object
        super().__init__()

        # Setup main window
        self.setWindowTitle("FRC Pit Master")
        self.resize(1280,1024)

        # Create central widget
        self.mainarea = qtw.QWidget()
        self.setCentralWidget(self.mainarea)

        # Show the main window
        self.show()


# Define main method
def main():

    # Create the application and open the main window
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())


# Call main function on startup
if __name__ == '__main__':
    main()
