from tkinter import *
import math
FONT=('Microsoft YaHei',12)
buttons_name=('%','CE','C','←','1/x','x^2','sqrt','÷','7','8','9','x','4','5','6','-','1','2','3','+','±','0','.','=')

class CalcPage():
    def __init__(self,master):
        self.master=master
        self.calc_flag=False
        self.initUI()
    def initUI(self):
        self.display=StringVar()
        self.result=Entry(self.master,
                          relief=RIDGE,
                          textvariable=self.display,
                          justify='right',
                          font=FONT,
                          bd=5,
                          bg='powder blue')
        self.result.pack(side=TOP,expand=YES,fill=X)
        self.center_window()
        self.buttons_frame=Frame(self.master)
        self.buttons_frame.pack(side=BOTTOM,pady=2)
        self.create_buttons(self.click_handler)
    def center_window(self):
        screen_width=self.master.winfo_screenwidth()
        screen_height=self.master.winfo_screenheight()
        x=(screen_width-200)/2
        y=(screen_height-100)/2
        self.master.geometry('246x260+%d+%d' %(x,y))
        self.master.title('计算器')
    def create_buttons(self,click_method,names=buttons_name,cols=4):
        for i,name in enumerate(names):
            row,col=i//cols,i % cols
            b=Button(self.buttons_frame,text=name,font=FONT,width=5)
            b.grid(row=row,column=col)
            b.bind('<Button-1>',click_method)
    def click_handler(self,event):
        c=event.widget['text']
        s=self.display.get()
        if 'ERROR' in s:
            s=''
        if c=='←':
            self.display.set(s[:-1])
        elif c=='C' or c=='CE':
            self.display.set('')
        elif c=='x^2':
            self.display.set(eval(s)**2)
        elif c=='sqrt':
            try:
                self.display.set(math.sqrt(eval(s)))
            except:
                self.display.set('ERROR')
        elif c=='1/x':
            try:
                self.display.set(1/eval(s))
            except:
                self.display.set('ERROR')
        elif c=='±':
            if '-' in s:
                self.display.set(s[1:])
            else:
                self.display.set('-' + s)
        elif c in '0123456789.':
            if self.calc_flag:
                self.calc_flag=False
                self.display.set(c)
            else:
                self.display.set(s + c)
        elif c in '+-x÷':
            self.display.set(s + c)
        elif c == '=':
            self.calc()
            self.calc_flag=True
        self.result.icursor(len(self.display.get()))
    def calc(self):
        try:
            s=self.display.get()
            if '÷' in s:
                s=s.replace('÷','/')
            elif 'x' in s:
                s=s.replace('x','*')
            self.display.set(eval(s))
        except:
            self.display.set('ERROR')