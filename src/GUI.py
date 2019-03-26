import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4 import QtCore
#from AssignDBMS import *
from insert_patient import add_patient
from insert_doctor import add_doctor
from insert_staff import add_staff
Name = "";
Gender = "";
DOB = "";
Mother_name = "";
Contact = "";
Address = "";
Weight = "";
Admitted = "";
email = "";
salary = "";
types = "";
Qual ="";
clss = "";
ward = "";
bed = "";
adm_no = "";
ADM = "";
DCH = "";
Pid = "";
Did = "";
Date = "";
T_type = "";
Lab_Name = "";
Rid = "";
Dpt = "";
Lab_res = "";
Lab_amt = "";
curr = "";
crit = "";

def f1(text):
      print(text)
      global Name;
      Name = text;
def f2(text):
      print(text)
      global Gender;
      Gender = text;
def f3(text):
      print(text)
      global DOB;
      DOB = text;
def f4(text):
      print(text)
      global Mother_name;
      Mother_name = text;
def f5(text):
      print(text)
      global Contact;
      Contact = text;
def f6(text):
      print(text)
      global Address;
      Address = text;
def f7(text):
      print(text)
      global Weight
      Weight = text;
def f8(text):
      print(text)
      global Admitted;
      Admitted = text;
def f9(text):
      print(text)
      global email;
      email = text;
def f10(text):
      print(text)
      global salary;
      salary = text;
def f11(text):
      print(text)
      global types;
      types = text;
def f12(text):
      print(text)
      global Qual;
      Qual = text;
def f13(text):
      print(text)
      global clss;
      clss = text;
def f14(text):
      print(text)
      global ward;
      ward = text;
def f15(text):
      print(text)
      global bed;
      bed = text;
def f16(text):
      print(text)
      global adm_no;
      adm_no = text;
def f17(text):
      print(text)
      global ADM;
      ADM = text;
def f18(text):
      print(text)
      global DCH;
      DCH = text;
def f19(text):
      print(text)
      global Pid;
      Pid = text;
def f20(text):
      print(text)
      global Did;
      Did = text;
def f21(text):
      print(text)
      global Date;
      Date = text;
def f22(text):
      print(text)
      global T_type;
      T_type = text;
def f23(text):
      print(text)
      global Lab_Name;
      Lab_Name = text;
def f24(text):
      print(text)
      global Rid;
      Rid = text;
def f25(text):
      print(text)
      global Dpt;
      Dpt = text;
def f26(text):
      print(text)
      global Lab_res;
      Lab_res = text;
def f27(text):
      print(text)
      global Lab_amt;
      Lab_amt = text;
def f28(text):
      print(text)
      global curr;
      curr = text;
def f29(text):
      print(text)
      global crit;
      crit = text;


def insert_patient():
      add_patient(str(Name), str(Gender), str(DOB), str(Mother_name), str(Contact), str(Address), Weight, str(Admitted))
      print(str(Name),str(Gender),str(DOB),str(Mother_name),str(Contact),str(Address), str(Weight), str(Admitted));

def insert_doctor():
      add_doctor(str(Name), str(Gender), str(DOB), str(Qual), str(Contact), str(Address), str(email), str(salary), str(Dpt))
      print(str(Name),str(Gender),str(DOB),str(Qual),str(Contact),str(Address), str(email), str(salary));

def insert_staff():
      add_staff(str(Name), str(Gender), str(DOB), str(Qual), str(Contact), str(Address), str(email), str(salary), str(types))
      print(str(Name),str(Gender),str(DOB),str(Qual),str(Contact),str(Address), str(email), str(salary), str(types));

class tabdemo(QTabWidget):
   def __init__(self, parent = None):
      super(tabdemo, self).__init__(parent)
      stylesheet = """ 
      QTabBar::tab:selected {background: grey;}
      QTabWidget>QWidget>QWidget{background: pink;}
      """
      self.setStyleSheet(stylesheet)
      self.tab1 = QWidget()
      self.tab2 = QWidget()
      self.tab3 = QWidget()
      self.tab4 = QWidget()
      self.tab5 = QWidget()
      self.tab6 = QWidget()
      self.tab7 = QWidget()
      self.tab8 = QWidget()
      self.tab9 = QWidget()
      
      self.addTab(self.tab1,"Tab 1")
      self.addTab(self.tab2,"Tab 2")
      self.addTab(self.tab3,"Tab 3")
      self.addTab(self.tab4,"Tab 4")
      self.addTab(self.tab5,"Tab 5")
      self.addTab(self.tab6,"Tab 6")
      self.addTab(self.tab7,"Tab 7")
      self.addTab(self.tab8,"Tab 8")
      self.addTab(self.tab9,"Tab 9")
      self.tab1UI()
      self.tab2UI()
      self.tab3UI()
      self.tab4UI()
      self.tab5UI()
      self.tab6UI()
      self.tab7UI()
      self.tab8UI()
      self.tab9UI()
      self.setWindowTitle("LMS System")

   #def patient(self):
 
      
      

   def tab1UI(self):
      # label = QLabel() 
      # pixmap = QPixmap('IIT_JAMMU_LOGO.png')
      # label.setPixmap(pixmap)
      layout = QFormLayout()
      e1 = QLineEdit()
      e2 = QLineEdit()
      e3 = QLineEdit()
      e4 = QLineEdit()
      e5 = QLineEdit()
      e6 = QLineEdit()
      e7 = QLineEdit()
      e8 = QLineEdit()
      layout.addRow("Name",e1)
      layout.addRow("Gender",e2)
      layout.addRow("DOB",e3)
      layout.addRow("Mother's Name",e4)
      layout.addRow("Contact No.",e5)
      layout.addRow("Address",e6)
      layout.addRow("Weight",e7)
      layout.addRow("Admitted",e8)
      e1.textChanged.connect(f1)
      e1.setStyleSheet('color: black;')
      e2.textChanged.connect(f2)
      e3.textChanged.connect(f3)
      e4.textChanged.connect(f4)
      e5.textChanged.connect(f5)
      e6.textChanged.connect(f6)
      e7.textChanged.connect(f7)
      e8.textChanged.connect(f8)
      hbox = QHBoxLayout()
      a = QPushButton("Insert")
      a.setStyleSheet('background-color: green; color: black;')
      hbox.addWidget(a)      
      layout.addRow(hbox)
      self.setTabText(0,"Insert Patient")
      a.clicked.connect(insert_patient);
      a.clicked.connect(e1.clear);
      a.clicked.connect(e2.clear);
      a.clicked.connect(e3.clear);
      a.clicked.connect(e4.clear);
      a.clicked.connect(e5.clear);
      a.clicked.connect(e6.clear);
      a.clicked.connect(e7.clear);
      a.clicked.connect(e8.clear);
      #print(e1.text())
      # a.clicked.connect(Alt)
      # a.clicked.connect(show_allot_status)
      # b.clicked.connect(ret)
      # b.clicked.connect(show_ret_status)
      self.tab1.setLayout(layout)
      #self.tab1.setLayout(label)

   def tab2UI(self):
      layout = QFormLayout()
      e1 = QLineEdit()
      e2 = QLineEdit()
      e3 = QLineEdit()
      e4 = QLineEdit()
      layout.addRow("Department",e1)
      layout.addRow("Current Time",e2)
      layout.addRow("Criticality",e3)
      layout.addRow("Date",e4)
      e1.textChanged.connect(f25)
      e2.textChanged.connect(f28)
      e3.textChanged.connect(f29)
      e4.textChanged.connect(f21)
      hbox = QHBoxLayout()
      a = QPushButton("Search")
      a.setStyleSheet('background-color: green; color: black;')
      hbox.addWidget(a)
      layout.addRow(hbox)
      #a.clicked.connect(insert_doctor);
      a.clicked.connect(e1.clear);
      a.clicked.connect(e2.clear);
      a.clicked.connect(e3.clear);
      self.setTabText(1,"Search Doctor")
      #print(e1.text())
      # a.clicked.connect(Alt)
      # a.clicked.connect(show_allot_status)
      # b.clicked.connect(ret)
      # b.clicked.connect(show_ret_status)
      self.tab2.setLayout(layout)
      
   def tab3UI(self):
      layout = QFormLayout()
      e0 = QLineEdit()
      e1 = QLineEdit()
      e2 = QLineEdit()
      e3 = QLineEdit()
      e4 = QLineEdit()
      e5 = QLineEdit()
      e6 = QLineEdit()
      e7 = QLineEdit()
      e8 = QLineEdit()
      e9 = QLineEdit()
      layout.addRow("Name",e1)
      layout.addRow("Gender",e2)
      layout.addRow("DOB",e3)
      layout.addRow("Qualification",e4)
      layout.addRow("Contact No.",e5)
      layout.addRow("Address",e6)
      layout.addRow("Email",e7)
      layout.addRow("Salary",e8)
      layout.addRow("type",e9)
      e1.textChanged.connect(f1)
      e2.textChanged.connect(f2)
      e3.textChanged.connect(f3)
      e4.textChanged.connect(f12)
      e5.textChanged.connect(f5)
      e6.textChanged.connect(f6)
      e7.textChanged.connect(f9)
      e8.textChanged.connect(f10)
      e9.textChanged.connect(f11)
      hbox = QHBoxLayout()
      a = QPushButton("Insert")
      a.setStyleSheet('background-color: green; color: black;')
      hbox.addWidget(a)
      layout.addRow(hbox)
      a.clicked.connect(insert_staff);
      a.clicked.connect(e1.clear);
      a.clicked.connect(e2.clear);
      a.clicked.connect(e3.clear);
      a.clicked.connect(e4.clear);
      a.clicked.connect(e5.clear);
      a.clicked.connect(e6.clear);
      a.clicked.connect(e7.clear);
      a.clicked.connect(e8.clear);
      a.clicked.connect(e9.clear);
      self.setTabText(2,"Insert Staff")
      self.tab3.setLayout(layout)
      
   def tab4UI(self):
      layout = QFormLayout()
      e1 = QLineEdit()
      e2 = QLineEdit()
      e3 = QLineEdit()
      e4 = QLineEdit()

      layout.addRow("Type of ward",e1)
      hbox = QHBoxLayout()
      a = QPushButton("List of available ward of this class")
      a.setStyleSheet('background-color: green; color: black;')
      hbox.addWidget(a)     
      layout.addRow(hbox)
      #hbox.addStretch()

      layout.addRow("Ward no.",e2)
      b = QPushButton("Get ward detail")
      b.setStyleSheet('background-color: green; color: black;')
      hbox1 = QHBoxLayout()
      hbox1.addWidget(b)     
      layout.addRow(hbox1)
      #hbox1.addStretch()

      layout.addRow("Bed No.",e3)
      layout.addRow("Ward No.",e4)
      hbox2 = QHBoxLayout()
      c = QPushButton("Get bed detail")
      c.setStyleSheet('background-color: green; color: black;')
      hbox2.addWidget(c)     
      layout.addRow(hbox2)
      #hbox2.addStretch()

      e1.textChanged.connect(f13)
      e2.textChanged.connect(f14)
      e3.textChanged.connect(f15)
      e4.textChanged.connect(f14)

      # a.clicked.connect(ins_periodical);
      # b.clicked.connect(showperiodical)
      self.setTabText(3,"Update Patient Info")
      self.tab4.setLayout(layout)

   def tab5UI(self):
      layout = QFormLayout()
      e1 = QLineEdit()
      e2 = QLineEdit()
      e3 = QLineEdit()
      e4 = QLineEdit()
      e5 = QLineEdit()
      e6 = QLineEdit()
      layout.addRow("Admission no.",e1)
      layout.addRow("Name",e2)
      layout.addRow("ward no.",e3)
      layout.addRow("Bed no.",e4)
      layout.addRow("Addmission Date",e5)
      layout.addRow("Release date",e6)
      e1.textChanged.connect(f16)
      e2.textChanged.connect(f1)
      e3.textChanged.connect(f14)
      e4.textChanged.connect(f15)
      e5.textChanged.connect(f17)
      e6.textChanged.connect(f18)
      hbox = QHBoxLayout()
      a = QPushButton("Admit")
      b = QPushButton("Discharge")
      a.setStyleSheet('background-color: green; color: black;')
      b.setStyleSheet('background-color: green; color: black;')
      hbox.addWidget(a)
      hbox.addStretch()
      hbox.addWidget(b)      
      layout.addRow(hbox)
      # a.clicked.connect(ins_papers);
      # b.clicked.connect(showpaper)
      self.setTabText(4,"Admit/Discharge Patient from bed");
      self.tab5.setLayout(layout)

   def tab6UI(self):
      layout = QFormLayout()
      
      hbox10 = QHBoxLayout()
      blank = QPushButton("Submit Report");
      blank.setStyleSheet('background-color: pink; color: red;')
      hbox10.addWidget(blank)
      layout.addRow(hbox10)

      e1 = QLineEdit()
      e2 = QLineEdit()
      e3 = QLineEdit()
      e4 = QLineEdit()
      e5 = QLineEdit()
      e6 = QLineEdit()
      e7 = QLineEdit()
      layout.addRow("Patient Id",e1)
      layout.addRow("Doctor Id",e2)
      layout.addRow("Date",e3)
      layout.addRow("Test_type",e4)
      layout.addRow("Lab Name",e5)
      layout.addRow("Result",e6)
      layout.addRow("Amount",e7)
      e1.textChanged.connect(f19)
      e2.textChanged.connect(f20)
      e3.textChanged.connect(f21)
      e4.textChanged.connect(f22)
      e5.textChanged.connect(f23)
      e6.textChanged.connect(f26)
      e7.textChanged.connect(f27)
      hbox = QHBoxLayout()
      a = QPushButton("Insert Lab report request")
      a.setStyleSheet('background-color: green; color: black;')
      hbox.addWidget(a)     
      layout.addRow(hbox)
      #layout.setSpacing(0);

      hbox11 = QHBoxLayout()
      blank = QPushButton(" ");
      blank.setStyleSheet('background-color: pink; color: pink;')
      hbox11.addWidget(blank)
      layout.addRow(hbox11)
      #layout.setSpacing(0);
      hbox12 = QHBoxLayout()
      blank = QPushButton(" ");
      blank.setStyleSheet('background-color: pink; color: pink;')
      hbox12.addWidget(blank)
      layout.addRow(hbox12)
      #layout.setSpacing(0);
      hbox13 = QHBoxLayout()
      blank = QPushButton("Extract Report");
      blank.resize(100,10)
      blank.setStyleSheet('background-color: pink; color: red;')
      hbox13.addWidget(blank)
      layout.addRow(hbox13)
      #layout.setSpacing(0);

      # vbox = QVBoxLayout()
      # F = QPushButton("Insert", self)
      # F.resize(100,50);
      # vbox.addWidget(F)     
      # layout.addRow(vbox)

      e6 = QLineEdit()
      e7 = QLineEdit()
      layout.addRow("Patient Id",e6)
      layout.addRow("Report Id",e7)
      e6.textChanged.connect(f19)
      e7.textChanged.connect(f24)
      hbox1 = QHBoxLayout()
      b = QPushButton("Extract Lab report")
      b.setStyleSheet('background-color: green; color: black;')
      hbox1.addWidget(b)     
      layout.addRow(hbox1)
      # a.clicked.connect(ins_user);
      # a.clicked.connect(show_ins_status);
      # b.clicked.connect(showuser)
      self.setTabText(5,"Lab report")
      self.tab6.setLayout(layout)

   def tab7UI(self):
      layout = QFormLayout()
      hbox = QVBoxLayout()
      a = QPushButton("All doctors")
      b = QPushButton("All Medicines")
      c = QPushButton("All Equipment")
      d = QPushButton("All Staff Member")
      e = QPushButton("All Ward/bed Info")
      hbox.addWidget(a)
      hbox.addStretch()
      hbox.addWidget(b)
      hbox.addStretch()
      hbox.addWidget(c)
      hbox.addStretch()
      hbox.addWidget(d)
      hbox.addStretch()
      hbox.addWidget(e)      
      layout.addRow(hbox)
      listWidget = QListWidget()
      # a.clicked.connect(albk);
      # b.clicked.connect(alpd);
      # c.clicked.connect(alpp);
      # d.clicked.connect(alus);
      self.setTabText(6,"Database")
      self.tab7.setLayout(layout)

   def tab8UI(self):
      layout = QFormLayout()
      e1 = QLineEdit()
      e2 = QLineEdit()
      e3 = QLineEdit()
      e4 = QLineEdit()
      e5 = QLineEdit()
      e6 = QLineEdit()
      e7 = QLineEdit()
      e8 = QLineEdit()
      e9 = QLineEdit()
      layout.addRow("Name",e1)
      layout.addRow("Gender",e2)
      layout.addRow("DOB",e3)
      layout.addRow("Department",e9)
      layout.addRow("Qualification",e4)
      layout.addRow("Contact No.",e5)
      layout.addRow("Address",e6)
      layout.addRow("Email",e7)
      layout.addRow("Salary",e8)
      e1.textChanged.connect(f1)
      e2.textChanged.connect(f2)
      e3.textChanged.connect(f3)
      e4.textChanged.connect(f12)
      e5.textChanged.connect(f5)
      e6.textChanged.connect(f6)
      e7.textChanged.connect(f9)
      e8.textChanged.connect(f10)
      e9.textChanged.connect(f25)
      hbox = QHBoxLayout()
      a = QPushButton("Insert")
      a.setStyleSheet('background-color: green; color: black;')
      hbox.addWidget(a)
      layout.addRow(hbox)
      a.clicked.connect(insert_doctor);
      a.clicked.connect(e1.clear);
      a.clicked.connect(e2.clear);
      a.clicked.connect(e3.clear);
      a.clicked.connect(e4.clear);
      a.clicked.connect(e5.clear);
      a.clicked.connect(e6.clear);
      a.clicked.connect(e7.clear);
      a.clicked.connect(e8.clear);
      self.setTabText(7,"Insert Doctor")
      #print(e1.text())
      # a.clicked.connect(Alt)
      # a.clicked.connect(show_allot_status)
      # b.clicked.connect(ret)
      # b.clicked.connect(show_ret_status)
      self.tab8.setLayout(layout)
   
   def tab9UI(self):
      layout = QFormLayout()
      e1 = QLineEdit()
      e2 = QLineEdit()
      e3 = QLineEdit()
      e4 = QLineEdit()
      e5 = QLineEdit()
      e6 = QLineEdit()
      e7 = QLineEdit()
      e8 = QLineEdit()
      e9 = QLineEdit()
      layout.addRow("Name",e1)
      layout.addRow("Gender",e2)
      layout.addRow("DOB",e3)
      layout.addRow("Qualification",e4)
      layout.addRow("Contact No.",e5)
      layout.addRow("Address",e6)
      layout.addRow("Email",e7)
      layout.addRow("Salary",e8)
      layout.addRow("type",e9)
      e1.textChanged.connect(f1)
      e2.textChanged.connect(f2)
      e3.textChanged.connect(f3)
      e4.textChanged.connect(f12)
      e5.textChanged.connect(f5)
      e6.textChanged.connect(f6)
      e7.textChanged.connect(f9)
      e8.textChanged.connect(f10)
      e9.textChanged.connect(f11)
      hbox = QHBoxLayout()
      a = QPushButton("Insert")
      a.setStyleSheet('background-color: green; color: black;')
      hbox.addWidget(a)
      layout.addRow(hbox)
      a.clicked.connect(insert_staff);
      a.clicked.connect(e1.clear);
      a.clicked.connect(e2.clear);
      a.clicked.connect(e3.clear);
      a.clicked.connect(e4.clear);
      a.clicked.connect(e5.clear);
      a.clicked.connect(e6.clear);
      a.clicked.connect(e7.clear);
      a.clicked.connect(e8.clear);
      a.clicked.connect(e9.clear);
      self.setTabText(8,"Insert Staff")
      self.tab9.setLayout(layout)
      
def main():
   app = QApplication(sys.argv)
   ex = tabdemo()
   ex.show()
   sys.exit(app.exec_())
   
if __name__ == '__main__':
   main()