# Importing necessary modules and classes:
from http import client
import sys
from turtle import title
from PyQt5.QtWidgets import (QApplication, QWidget,QFormLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton,QSpinBox,QComboBox,QMessageBox,QCheckBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Appointment GUI:
class RequestAppointment(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
        
    def initialize_ui(self):
        """
        Initialize the main window and to add its componets widgets
        """
        self.setGeometry(400,50,700,950)
        self.setWindowTitle("Book an Appointment v. 0.1")
        self.display_components()
    
    def display_components(self):
        """
        Setup the component to the main window screen
        """
        # Labels of: 
        # 1: title: 
        title_lbl = QLabel("برنامج حجز المواعيد الطبية")
        title_lbl.setFont(QFont("Calibri",25))        
        title_lbl.setAlignment(Qt.AlignCenter)
        # 2: client: 
        client_lbl =  QLabel("الزبـــــون:")     
        client_lbl.setFont(QFont("Calibri",16))
        
        # 3: client: 
        client_lbl =  QLabel("العمـــــــر:")     
        client_lbl.setFont(QFont("Calibri",16))
        
        # 4: client: 
        client_lbl =  QLabel("الجـــنــــــس:")     
        client_lbl.setFont(QFont("Calibri",16))
        # 5: Phone: 
        client_lbl =  QLabel("رقـــــم الهاتف:")     
        client_lbl.setFont(QFont("Calibri",16))
        
        # 6: Address: 
        client_lbl =  QLabel("العنــــوان :")     
        client_lbl.setFont(QFont("Calibri",16))
        
        # 7: first_time: 
        client_lbl =  QLabel("هل هذا الموعد الأول :")     
        client_lbl.setFont(QFont("Calibri",16))
        
        # 8: Address: 
        client_lbl =  QLabel(" المـــوعــد :")     
        client_lbl.setFont(QFont("Calibri",16))
        
        # 9 : Other info: 
        client_lbl =  QLabel(" معلومات إضافية :")     
        client_lbl.setFont(QFont("Calibri",16))
        
        
             
        



# Execution code lines:
if __name__ =="__main__":
    app = QApplication(sys.argv)
    app_appointment = RequestAppointment()
    sys.exit(app.exec_())

