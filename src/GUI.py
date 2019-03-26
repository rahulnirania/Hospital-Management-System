import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4 import QtCore
#from AssignDBMS import *

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
Value = "";
Volume = "";
Username = "";
Email = "";
Password = "";
alt_stat = 0;
Ust = "";
Discipline = "";
due = 0;

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
      global Email;
      Email = text;
def f14(text):
      print(text)
      global Password;
      Password = text;
def f15(text):
      print(text)
      global Ust;
      Ust = text;
def f16(text):
      print(text)
      global Discipline;
      Discipline = text;

# def Alt():
#    global alt_stat;
#    if(avl_book(Title) == None):
#       alt_stat = allot_book(str(Name),str(Title),str(insdate),str(Username),str(Password))
#       if(alt_stat==1):
#          print("Success");
#       else:
#          print("Error");
#    elif(avl_book(Title) == -1):
#       alt_stat = 4;
#    else:
#       alt_stat = 3
      

# def ret():
#    global alt_stat, due;
#    alt_stat, due = return_book(str(Name),str(Title),str(retdate),str(Username),str(Password))
#    if(alt_stat==1):
#       print("Success");
#    else:
#       print("Error");

# def show_allot_status():
#    msg = QMessageBox()
#    msg.setIcon(QMessageBox.Information)
#    if(alt_stat == 1):
#       msg.setText("Sucess");
#    elif(alt_stat == 2):
#       msg.setText("Book Limit exceeded");
#    elif(alt_stat == 0):
#       msg.setText("Wrong detail");
#    elif (alt_stat == 3):
#       msg.setText("Book not available");
#    elif (alt_stat == 4):
#       msg.setText("No book of this name");
#    msg.buttonClicked.connect(msgbtn)
#    retval = msg.exec_()
#    print ("value of pressed message box button:"), retval

# def show_ret_status():
#    msg = QMessageBox()
#    msg.setIcon(QMessageBox.Information)
#    aaa = "Sucess and You have Due of Rs"+str(due)
#    if(alt_stat == 1):
#       msg.setText(aaa);
#    elif(alt_stat == 2):
#       msg.setText("Book Doesn't belong to you");
#    elif(alt_stat == 0):
#       msg.setText("Wrong detail");
#    elif (alt_stat == 4):
#       msg.setText("No book of this name");
#    msg.buttonClicked.connect(msgbtn)
#    retval = msg.exec_()
#    print ("value of pressed message box button:"), retval

# def Alt_p():
#    global alt_stat;
#    if(avl_prdcl(Title) == None):
#       alt_stat = allot_prdcl(str(Name),str(Title),str(insdate),str(retdate),str(Username),str(Password))
#       if(alt_stat==1):
#          print("Success");
#       else:
#          print("Error");
#    elif(avl_prdcl(Title) == -1):
#       alt_stat = 4;
#    else:
#       alt_stat = 3
      
# def ret_p():
#    global alt_stat;
#    alt_stat = return_prdcl(str(Name),str(Title),str(Username),str(Password))
#    if(alt_stat==1):
#       print("Success");
#    else:
#       print("Error");

# def show_allot_status_p():
#    msg = QMessageBox()
#    msg.setIcon(QMessageBox.Information)
#    if(alt_stat == 1):
#       msg.setText("Success");
#    elif(alt_stat == 2):
#       msg.setText("Book Limit exceeded");
#    elif(alt_stat == 0):
#       msg.setText("Wrong detail");
#    elif (alt_stat == 3):
#       msg.setText("Periodical not available now");
#    elif(alt_stat == 4):
#       msg.setText("No Periodical of this name");
#    msg.buttonClicked.connect(msgbtn)
#    retval = msg.exec_()
#    print ("value of pressed message box button:"), retval

# def show_ret_status_p():
#    msg = QMessageBox()
#    msg.setIcon(QMessageBox.Information)
#    if(alt_stat == 1):
#       msg.setText("Sucess");
#    elif(alt_stat == 2):
#       msg.setText("Periodical Doesn't belong to you");
#    elif(alt_stat == 0):
#       msg.setText("Wrong detail");
#    msg.buttonClicked.connect(msgbtn)
#    retval = msg.exec_()
#    print ("value of pressed message box button:"), retval

# def ins_book():
#    insert_books(str(Title),int(Year),str(Isbn),int(Pages),str(Publisher),str(Author),int(Value),str(Discipline))

# def ins_periodical():
#    insert_periodicals(str(Title),int(Year),int(Volume),str(Isbn),str(Publisher),int(Value))

# def ins_user():
#    global alt_stat
#    alt_stat = insert_users(str(Name),str(Username),str(Email),str(Password),str(Ust));

# def show_ins_status():
#    msg = QMessageBox()
#    msg.setIcon(QMessageBox.Information)
#    if(alt_stat == 1):
#       msg.setText("Sucess");
#    elif(alt_stat == 0):
#       msg.setText("Wrong Usert_type");
#    msg.buttonClicked.connect(msgbtn)
#    retval = msg.exec_()
#    print ("value of pressed message box button:"), retval

# def ins_papers():
#    insert_papers( str(Name), str(Title), str(Author));

# def showbook():
#    msg = QMessageBox()
#    msg.setIcon(QMessageBox.Information)
#    msg.setText("Choose the type of information")
#    msg.setWindowTitle("Book Detail")
#    (I,T,Y,Is,P,Pu,Au,U,D)= extract_book_detail(str(Title))
#    if(T != None):
#       msg.setDetailedText("Book Name:   '{}'\nYear:   {}\nISBN No.:   '{}'\nNo. of Pages:   {}\nPublisher Name:    '{}'\nAuthor Name:   '{}'\nAllotted to '{}'\nDiscipline    '{}'".format(T,Y,Is,P,Pu,Au,U,D))
#    else:
#       msg.setDetailedText("Book of this name not available")
#    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#    msg.buttonClicked.connect(msgbtn)
#    retval = msg.exec_()
#    print ("value of pressed message box button:"), retval

# def showperiodical():
#    msg = QMessageBox()
#    msg.setIcon(QMessageBox.Information)
#    msg.setText("Choose the type of information")
#    msg.setWindowTitle("Periodical Detail")
#    (T, Y, V, I, P) = extract_periodical_detail(str(Title))
#    if(T!=None):
#       msg.setDetailedText("Book Name:   '{}'\nYear:   {}\nVolume:   {}\nISBN No.:   '{}'\nPublisher Name:    '{}'\n".format(T, Y, V, I, P))
#    else:
#       msg.setDetailedText("Periodical of this name not available")
#    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#    msg.buttonClicked.connect(msgbtn)
#    retval = msg.exec_()
#    print ("value of pressed message box button:"), retval

# def showpaper():
#    msg = QMessageBox()
#    msg.setIcon(QMessageBox.Information)
#    msg.setText("Choose the type of information")
#    msg.setWindowTitle("Paper Detail")
#    (N,P,A) = extract_paper_detail(str(Name))
#    if(N != None):
#       msg.setDetailedText("Paper Name:   '{}'\nPeriodical Name:   '{}'\nAuthor:    '{}'".format(N,P,A))
#    else:
#       msg.setDetailedText("Paper not available")
#    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#    msg.buttonClicked.connect(msgbtn)
#    retval = msg.exec_()
#    print ("value of pressed message box button:"), retval


# def showuser():
#    msg = QMessageBox()
#    msg.setIcon(QMessageBox.Information)
#    msg.setText("Choose the type of information")
#    msg.setWindowTitle("User Detail")
#    (B,M) = User_detail(str(Name),str(Username),str(Email),str(Password))
#    if(B!=None or M!=None):
#       a = "";
#       b = "";
#       if (B!=[]): 
#          for i in range(len(B)):
#             a = a + B[i]+ "\t"
#       else:
#          a = "None"
      
#       if (M != None):
#          for i in range(len(M)):
#             b = b+ M[i] + "\t";
#       else:
#          b = "None"

#       msg.setDetailedText("Messages:   '{}'\nBooks:    '{}'\n".format(b,a))
#    else:
#       msg.setDetailedText("No user of this name available")
       
#    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#    msg.buttonClicked.connect(msgbtn)
#    retval = msg.exec_()
#    print ("value of pressed message box button:"), retval

# class myListWidget(QListWidget):

#    def Clicked(self,item):
#       QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())

# def albk():
#    msg = QMessageBox()
#    msg.setIcon(QMessageBox.Information)
#    msg.setText("Want to see all Books")
#    #msg.setInformativeText("This is additional information")
#    msg.setWindowTitle("All Book");
#    a = All_books();
#    st = "";
#    for i in xrange(len(a)):
#       st = st + str(i+1) + "\t" + a[i][0] + "\n";
#    msg.setDetailedText("{}".format(st))
#    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#    msg.buttonClicked.connect(msgbtn)
#    retval = msg.exec_()
#    print ("value of pressed message box button:"), retval


# def alpd():
#    msg = QMessageBox()
#    msg.setIcon(QMessageBox.Information)
#    msg.setText("Want to see all Periodicals")
#    msg.setWindowTitle("All Periodicals");
#    a = All_periodicals();
#    st = "";
#    for i in xrange(len(a)):
#       st = st + str(i+1) + "\t" + a[i][0] + "\n";
#    msg.setDetailedText("{}".format(st))
#    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#    msg.buttonClicked.connect(msgbtn)
#    retval = msg.exec_()
#    print ("value of pressed message box button:"), retval

# def alpp():
#    msg = QMessageBox()
#    msg.setIcon(QMessageBox.Information)
#    msg.setText("Want to see all Papers")
#    msg.setWindowTitle("All Papers");
#    a = All_papers();
#    st = "";
#    for i in xrange(len(a)):
#       st = st + str(i+1) + "\t" + a[i][0] + "\n";
#    msg.setDetailedText("{}".format(st))
#    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#    msg.buttonClicked.connect(msgbtn)
#    retval = msg.exec_()
#    print ("value of pressed message box button:"), retval

# def alus():
#    msg = QMessageBox()
#    msg.setIcon(QMessageBox.Information)
#    msg.setText("Want to see all Users")
#    msg.setWindowTitle("All Users");
#    a = All_users();
#    st = "";
#    for i in xrange(len(a)):
#       st = st + str(i+1) + "\t" + a[i][0] + "\n";
#    msg.setDetailedText("{}".format(st))
#    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#    msg.buttonClicked.connect(msgbtn)
#    retval = msg.exec_()
#    print ("value of pressed message box button:"), retval
   

# def msgbtn(i):
#    print ("Button pressed is:"),i.text()

def insert_patient():
      print(str(Name),str(Gender),str(DOB),str(Mother_name),str(Contact),str(Address), str(Weight), str(Admitted));

def insert_doctor():
      print(str(Name),str(Gender),str(DOB),str(Qual),str(Contact),str(Address), str(email), str(salary));

def insert_staff():
      print(str(Name),str(Gender),str(DOB),str(Qual),str(Contact),str(Address), str(email), str(salary), str(types));

class tabdemo(QTabWidget):
   def __init__(self, parent = None):
      super(tabdemo, self).__init__(parent)
      self.tab1 = QWidget()
      self.tab2 = QWidget()
      self.tab3 = QWidget()
      self.tab4 = QWidget()
      self.tab5 = QWidget()
      self.tab6 = QWidget()
      self.tab7 = QWidget()
      
      self.addTab(self.tab1,"Tab 1")
      self.addTab(self.tab2,"Tab 2")
      self.addTab(self.tab3,"Tab 3")
      self.addTab(self.tab4,"Tab 4")
      self.addTab(self.tab5,"Tab 5")
      self.addTab(self.tab6,"Tab 6")
      self.addTab(self.tab7,"Tab 7")
      self.tab1UI()
      self.tab2UI()
      self.tab3UI()
      self.tab4UI()
      self.tab5UI()
      self.tab6UI()
      self.tab7UI()
      self.setWindowTitle("LMS System")

   #def patient(self):
 
      
      

   def tab1UI(self):
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
      e2.textChanged.connect(f2)
      e3.textChanged.connect(f3)
      e4.textChanged.connect(f4)
      e5.textChanged.connect(f5)
      e6.textChanged.connect(f6)
      e7.textChanged.connect(f7)
      e8.textChanged.connect(f8)
      hbox = QHBoxLayout()
      a = QPushButton("Insert")
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

   def tab2UI(self):
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
      hbox = QHBoxLayout()
      a = QPushButton("Insert")
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
      self.setTabText(1,"Insert Doctor")
      #print(e1.text())
      # a.clicked.connect(Alt)
      # a.clicked.connect(show_allot_status)
      # b.clicked.connect(ret)
      # b.clicked.connect(show_ret_status)
      self.tab2.setLayout(layout)
      
   def tab3UI(self):
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
      e6 = QLineEdit()
      e7 = QLineEdit()
      layout.addRow("Title",e1)
      layout.addRow("Year Published",e2)
      layout.addRow("Volume.",e3)
      layout.addRow("ISBN No.",e4)
      layout.addRow("Publisher Name",e6)
      layout.addRow("Price",e7)
      e1.textChanged.connect(f2)
      e2.textChanged.connect(f5)
      e3.textChanged.connect(f11)
      e4.textChanged.connect(f6)
      e6.textChanged.connect(f8)
      hbox = QHBoxLayout()
      a = QPushButton("Insert")
      b = QPushButton("Detail")
      hbox.addWidget(a)
      hbox.addStretch()
      hbox.addWidget(b)      
      layout.addRow(hbox)
      # a.clicked.connect(ins_periodical);
      # b.clicked.connect(showperiodical)
      self.setTabText(3,"Search/Insert Periodicals")
      self.tab4.setLayout(layout)

   def tab5UI(self):
      layout = QFormLayout()
      e1 = QLineEdit()
      e2 = QLineEdit()
      e3 = QLineEdit()
      layout.addRow("Name",e1)
      layout.addRow("Periodical Name",e2)
      layout.addRow("Author",e3)
      e1.textChanged.connect(f1)
      e2.textChanged.connect(f2)
      e3.textChanged.connect(f9)
      hbox = QHBoxLayout()
      a = QPushButton("Insert")
      b = QPushButton("Detail")
      hbox.addWidget(a)
      hbox.addStretch()
      hbox.addWidget(b)      
      layout.addRow(hbox)
      # a.clicked.connect(ins_papers);
      # b.clicked.connect(showpaper)
      self.setTabText(4,"Search/Insert Papers")
      self.tab5.setLayout(layout)

   def tab6UI(self):
      layout = QFormLayout()
      e1 = QLineEdit()
      e2 = QLineEdit()
      e3 = QLineEdit()
      e4 = QLineEdit()
      e5 = QLineEdit()
      layout.addRow("Name",e1)
      layout.addRow("Username",e2)
      layout.addRow("Email address",e3)
      layout.addRow("Password",e4)
      layout.addRow("Usert_type (must be Students, Guest, Staff, Faculty)",e5)
      e1.textChanged.connect(f1)
      e2.textChanged.connect(f12)
      e3.textChanged.connect(f13)
      e4.textChanged.connect(f14)
      e5.textChanged.connect(f15)
      hbox = QHBoxLayout()
      a = QPushButton("Insert")
      b = QPushButton("Detail")
      hbox.addWidget(a)
      hbox.addStretch()
      hbox.addWidget(b)      
      layout.addRow(hbox)
      # a.clicked.connect(ins_user);
      # a.clicked.connect(show_ins_status);
      # b.clicked.connect(showuser)
      self.setTabText(5,"Search/Insert User")
      self.tab6.setLayout(layout)

   def tab7UI(self):
      layout = QFormLayout()
      hbox = QVBoxLayout()
      a = QPushButton("Books")
      b = QPushButton("Periodicals")
      c = QPushButton("Papers")
      d = QPushButton("Users")
      hbox.addWidget(a)
      hbox.addStretch()
      hbox.addWidget(b)
      hbox.addStretch()
      hbox.addWidget(c)
      hbox.addStretch()
      hbox.addWidget(d)      
      layout.addRow(hbox)
      listWidget = QListWidget()
      # a.clicked.connect(albk);
      # b.clicked.connect(alpd);
      # c.clicked.connect(alpp);
      # d.clicked.connect(alus);
      self.setTabText(6,"Database")
      self.tab7.setLayout(layout)
      
def main():
   app = QApplication(sys.argv)
   ex = tabdemo()
   ex.show()
   sys.exit(app.exec_())
   
if __name__ == '__main__':
   main()