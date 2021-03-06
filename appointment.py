# Importing necessary modules and classes:
from http import client
import sys
from turtle import title
from PyQt5.QtWidgets import (QApplication, QWidget,QFormLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton,QSpinBox,QComboBox,QMessageBox,QCheckBox,QDateTimeEdit)
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
        self.setStyleSheet("QWidget"
                           "{"
                           "background:#fff"
                           "}"
                           "")
        self.fist_appoint = False # to use it later on
        self.display_components()
    
    def display_components(self):
        """
        Setup the component to the main window screen
        """
        # Labels of: 
        # 1: title: 
        title_lbl = QLabel("برنامج حجز المواعيد الطبية")
        title_lbl.setStyleSheet("background:#00B6FF;padding:40px;")
        title_lbl.setFont(QFont("Calibri",25))        
        title_lbl.setAlignment(Qt.AlignCenter)
        # 2: client: 
        client_lbl =  QLabel("الزبـــــون:")     
        client_lbl.setFont(QFont("Calibri",13))
        
        # 3: client: 
        age_lbl =  QLabel("العمـــــــر:")     
        age_lbl.setFont(QFont("Calibri",13))
        
        # 4: client: 
        sex_lbl =  QLabel("الجـــنــــــس:")     
        sex_lbl.setFont(QFont("Calibri",13))
        # 5: Phone: 
        phone_lbl =  QLabel("رقـــــم الهاتف:")     
        phone_lbl.setFont(QFont("Calibri",13))
        
        # 6: Address: 
        address_lbl =  QLabel("العنــــوان :")     
        address_lbl.setFont(QFont("Calibri",13))
        
        # 7: first_time: 
        first_appoi_lbl =  QLabel("هل هذا الموعد الأول :")     
        first_appoi_lbl.setFont(QFont("Calibri",13))
        
        # 8: Address: 
        book_appoi_lbl =  QLabel(" المـــوعــد :")     
        book_appoi_lbl.setFont(QFont("Calibri",13))
        
        # 9 : Other info: 
        additional_lbl =  QLabel(" معلومات إضافية :")     
        additional_lbl.setFont(QFont("Calibri",13))
        
        # Input componets:
        # QlineEdit:
        self.f_name = QLineEdit()
        self.f_name.setPlaceholderText("الإســـــم")
        self.f_name.setStyleSheet("QLineEdit"
                             "{"
                             "font-family:Calibri;"
                             "border-radius:5px;"
                             "padding:15px;"
                             "text-align: right;"
                             "background: #97CFFF;"
                             "font-size:20px"                         
                             "}"
                             "QLineEdit::hover"
                             "{"
                             "background: #74B1FF;"
                             "}"
                             )
        
        
        self.l_name = QLineEdit()
        self.l_name.setPlaceholderText("اللقــــــــــب")
        self.l_name.setStyleSheet("QLineEdit"
                             "{"
                             "font-family:Calibri;"
                             "border-radius:5px;"
                             "padding:15px;"
                             "text-align: right;"
                             "background: #97CFFF;"
                             "font-size:20px"                         
                             "}"
                             "QLineEdit::hover"
                             "{"
                             "background: #74B1FF;"
                             "}"
                             )
        
        self.phone = QLineEdit()
        self.phone.setMinimumWidth(400)
        self.phone.setInputMask('00-00-00-00-00')
        self.phone.setAlignment(Qt.AlignRight)
        self.phone.setStyleSheet("QLineEdit"
                             "{"
                             "font-family:Calibri;"
                             "border-radius:5px;"
                             "padding:15px;"
                             "text-align: right;"
                             "background: #97CFFF;"
                             "font-size:20px;"                          
                             "}"
                             "QLineEdit::hover"
                             "{"
                             "background: #74B1FF;"
                             "}"
                             )
        self.address = QLineEdit()
        self.address.setPlaceholderText(" العنـــوان كامل")
        self.address.setStyleSheet("QLineEdit"
                             "{"
                             "font-family:Calibri;"
                             "border-radius:5px;"
                             "padding:15px;"
                             "text-align: right;"
                             "background: #97CFFF;"
                             "font-size:20px"                         
                             "}"
                             "QLineEdit::hover"
                             "{"
                             "background: #74B1FF;"
                             "}"
                             )
        
        # QSpinBoxes
        age = QSpinBox()
        age.setRange(5, 100)
        age.setFont(QFont('Calibri',25))
        age.setStyleSheet("QSpinBox"
                             "{"
                             "border-radius:5px;"
                             "padding:15px;"
                             "background: #97CFFF;"
                             "font-size:20px"                         
                             "}"
                             "QSpinBox::hover"
                             "{"
                             "background: #74B1FF;"
                             "}"
                             )
        
        sex_lbl = QLabel('حدد الجنس')
        sex_lbl.setFont(QFont("Calibri",13))
        
        # QComboBoxes
        # sexes list
        sex_list = ["ذكر","أنثى"]
        sex_cb = QComboBox()
        sex_cb.setStyleSheet("QComboBox"
                             "{"
                             "font-family:Calibri;"
                             "border-radius:5px;"
                             "padding:15px;"
                             "text-align: right;"
                             "background: #97CFFF;"
                             "font-size:20px"                         
                             "}"
                             "QComboBox::hover"
                             "{"
                             "background: #74B1FF;"
                             "}"
                             )
        sex_cb.addItems(sex_list)
        
        # DateEdit
        self.date_appoint = QDateTimeEdit()
        self.date_appoint.setMinimumWidth(400)
        self.date_appoint.setStyleSheet("QDateTimeEdit"
                             "{"
                             "font-family:Calibri;"
                             "border-radius:5px;"
                             "padding:15px;"
                             "text-align: right;"
                             "background: #97CFFF;"
                             "font-size:20px"                         
                             "}"
                             "QDateTimeEdit::hover"
                             "{"
                             "background: #74B1FF;"
                             "}"
                             )

        self.is_first_appoint = QCheckBox("نعم")
        self.is_first_appoint.setStyleSheet("QCheckBox"
                             "{"
                             "font-family:Calibri;"
                             "border-radius:5px;"
                             "padding:15px;"
                             "text-align: right;"
                             "background: #97CFFF;"
                             "font-size:20px"                         
                             "}"
                             "QCheckBox::hover"
                             "{"
                             "background: #74B1FF;"
                             "}"
                             )
        self.is_first_appoint.stateChanged.connect(self.is_not_firstappoin)
        book_btn = QPushButton("إضافــــة موعـــد")
        book_btn.setStyleSheet("QPushButton"
                             "{"
                             "font-family:Calibri;"
                             "border-radius:15px;"
                             "padding:25px;"
                             "height:80px;"
                             "text-align: center;"
                             "background: #D386E3;"
                             "border:1px solid #D3C5E3;"
                             
                             "font-size:20px"                         
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background: #D347E3;"
                             "color: #ffffff;"
                             "border:3px solid #D300E3;"
                             
                             "}"
                             )
        book_btn.clicked.connect(self.add_appointment)
        # II Layout:
        # 1: Client:
        client_fn_ln_hbox = QHBoxLayout()
        client_fn_ln_hbox.addWidget(self.f_name)
        client_fn_ln_hbox.setSpacing(50)
        client_fn_ln_hbox.addWidget(self.l_name)
             
        
        sex_age_lbl_hbox = QHBoxLayout()
        sex_age_lbl_hbox.addWidget(sex_lbl)
        sex_age_lbl_hbox.setSpacing(50)
        sex_age_lbl_hbox.addWidget(age_lbl)
        
        sex_age_input_hbox = QHBoxLayout()
        sex_age_input_hbox.addWidget(sex_cb)
        sex_age_input_hbox.setSpacing(50)
        sex_age_input_hbox.addWidget(age)
        
        
        phone_h_box = QHBoxLayout()
        phone_h_box.addStretch()
        phone_h_box.addWidget(self.phone)
        
        
        appoint_data_h_box = QHBoxLayout()
        appoint_data_h_box.addStretch()
        appoint_data_h_box.addWidget(self.date_appoint)
        
        
        fist_appint_sb_h_box = QHBoxLayout()
        fist_appint_sb_h_box.addStretch()
        fist_appint_sb_h_box.addWidget(self.is_first_appoint)
        

        # form layout
        form_layout = QFormLayout()
        form_layout.setSpacing(10)
        form_layout.setAlignment(Qt.AlignRight)
        form_layout.addRow(title_lbl)
        form_layout.addRow(client_lbl)
        form_layout.addRow(client_fn_ln_hbox)
        form_layout.addRow(client_fn_ln_hbox)
        form_layout.addRow(sex_age_lbl_hbox)
        form_layout.addRow(sex_age_input_hbox)
        form_layout.addRow(address_lbl)
        form_layout.addRow(self.address)
        form_layout.addRow(phone_lbl)
        form_layout.addRow(phone_h_box)
        form_layout.addRow(book_appoi_lbl)
        form_layout.addRow(appoint_data_h_box)
        form_layout.addRow(first_appoi_lbl)
        form_layout.addRow(fist_appint_sb_h_box)
        form_layout.addRow(book_btn)
        
        self.setLayout(form_layout)
    
    def is_not_firstappoin(self,state):
        """
        Function to Change state of is_first_appointment checkbox
        """
        if state == Qt.Checked:
            self.fist_appoint == True
        
    def add_appointment(self,state):
        """
        Funtion that submit the form and show messagebox for result
        """
        if (self.f_name.text() !="" and self.l_name.text() !="" and self.phone.text() !="" and self.date_appoint.text() !=""):
            
            QMessageBox.information(self,"Success Creating Appointment","The appointment create successfuly.",QMessageBox.Ok,QMessageBox.Ok)
            
            try:
                with open("dataAppointment.txt","a+") as db:
                        line = f"{self.f_name.text()} | {self.l_name.text()} | {self.phone.text()} | {self.date_appoint.text() } | {str(self.fist_appoint)}\n"
                        db.write(line)
                        
                self.f_name.clear()
                self.l_name.clear()
                self.phone.clear()
                self.address.clear()
                
                        
            except FileNotFoundError:
                print('file not found')
                open('dataAppointment.txt',"w")
        else:
            QMessageBox.warning(self,"Error","Check the required fields.",QMessageBox.Ok,QMessageBox.Ok)
           
                
             
        


# Execution code lines:
if __name__ =="__main__":
    app = QApplication(sys.argv)
    app_appointment = RequestAppointment()
    sys.exit(app.exec_())

