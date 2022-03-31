# Importing necessary modules and classes:
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,QFormLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton,QSpinBox,QComboBox,QMessageBox,QCheckBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Appointment GUI:
class RequestAppointment(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()



# Execution code lines:
if __name__ =="__main__":
    app = QApplication(sys.argv)
    app_appointment = RequestAppointment()
    sys.exit(app.exec_())

