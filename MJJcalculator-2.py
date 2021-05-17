import tkinter as tk
from math import *

button_params = {
    'padx':14, # for the padding in left and right, (only for the buttons)
    'pady':1, # Additional padding above and below the text and characters
    'bd':5,  #Border width in pixels
    'fg':'black', #Normal foreground (text) color
    'bg':'pink',   #Normal background color
    'font':('Batang',18),  #type of font
    'width':2,  #Width of the button char
    'height':1 ,  #Height of the button char
    'relief':'groove', #specifies the type of the border(SUNKEN, RAISED, GROOVE, and RIDGE.)
    'activebackground':"white"   #Background color when the button is under the cursor
    } 
#a class called calculator is created and the __init__() method is used to initialize values of that class
class Calculator:
#self represents the instance of the class
# init method or constructor
    def __init__(self, master):
        # expression that will be displayed on screen
        self.expression = ""

        # be used to store data in memory
        self.recall = "" # for memory recall
        self.clear = "" #

        # create string for text input
        self.text_input = tk.StringVar()

        # assign instance to master
        self.master = master

        # set frame showing inputs and title
        top_frame = tk.Frame(master,  bd=4, relief='ridge', bg='white' ,width=100)
        top_frame.pack(side=tk.TOP)

        # set frame showing all buttons
        bottom_frame = tk.Frame(master,  bd=4,relief='flat', bg='white')
        bottom_frame.pack(side=tk.BOTTOM)

        # name of calculator
        item = tk.Label(top_frame,text="3J'S Scientific Calculator")

        #  text inputs
        text_display = tk.Entry(top_frame, font=('Harrington',40),relief='groove',bg='white',fg='black', textvariable=self.text_input,width=100,bd=20,justify='right')
        text_display.pack()

        #row 0
        # takes exit
        self.button_in = tk.Button( bottom_frame, **button_params,text='Exit', command=quit)
        self.button_in.grid(row=0, column=2)
        

        # constant pi
        self.button_pi = tk.Button(bottom_frame, **button_params, text="π", command=lambda: self.button_click('pi'))
        self.button_pi.grid(row=0, column=3)

        # clears self.expression
        self.button_clear = tk.Button(bottom_frame, **button_params, text="C", command=self.button_clear_all)
        self.button_clear.grid(row=0, column=4)

        # deletes last string input
        self.button_del = tk.Button(bottom_frame, **button_params, text="Del", command=self.button_clear1)
        self.button_del.grid(row=0, column=5)

        # inputs a negative sign to the next entry
        self.button_change_sign = tk.Button(bottom_frame, **button_params, text="+/-", command=self.change_signs)
        self.button_change_sign.grid(row=0, column=6)
        # stores previous expression as an answer value
        self.button_ans = tk.Button(bottom_frame, **button_params, text="Ans", command=self.answer)
        self.button_ans.grid(row=0, column=7)

        # square root
        self.button_sqrt = tk.Button(bottom_frame, **button_params, text="sqrt", command=lambda: self.button_click('sqrt('))
        self.button_sqrt.grid(row=0, column=8)
        # row 1
        # seven
        self.button_7 = tk.Button(bottom_frame, **button_params, text="7", command=lambda: self.button_click(7))
        self.button_7.configure(activebackground="pink", bg='white')
        self.button_7.grid(row=1, column=2)
        # eight
        self.button_8 = tk.Button(bottom_frame, **button_params, text="8", command=lambda: self.button_click(8))
        self.button_8.configure(activebackground="pink", bg='white')
        self.button_8.grid(row=1, column=3)
        # nine
        self.button_9 = tk.Button(bottom_frame, **button_params, text="9", command=lambda: self.button_click(9))
        self.button_9.configure(activebackground="pink", bg='white')
        self.button_9.grid(row=1, column=4)
        # multiplication
        self.button_mult = tk.Button(bottom_frame, **button_params, text="x", command=lambda: self.button_click('*'))
        self.button_mult.grid(row=1, column=5)
        # square function
        self.button_sqr = tk.Button(bottom_frame, **button_params, text=u"x\u00B2", command=lambda: self.button_click('**2'))
        self.button_sqr.grid(row=1, column=6)
        
        # cubes a value
    
        self.cube = tk.Button(bottom_frame, **button_params, text=u"x\u00B3", command=lambda: self.button_click('**3'))
        self.cube.grid(row=1, column=7)
        
        
        # 'memory clear' button. Wipes self.recall to an empty string
        self.button_MC = tk.Button(bottom_frame, **button_params, text="MC", command=self.memory_clear)
        self.button_MC.grid(row=1, column=8)
        # row 2
        # four
        self.button_4 = tk.Button(bottom_frame, **button_params, text="4", command=lambda: self.button_click(4))
        self.button_4.configure(activebackground="pink", bg='white')
        self.button_4.grid(row=2, column=2)
        # five
        self.button_5 = tk.Button(bottom_frame, **button_params, text="5", command=lambda: self.button_click(5))
        self.button_5.configure(activebackground="pink", bg='white')
        self.button_5.grid(row=2, column=3)
        # six
        self.button_6 = tk.Button(bottom_frame, **button_params, text="6", command=lambda: self.button_click(6))
        self.button_6.configure(activebackground="pink", bg='white')
        self.button_6.grid(row=2, column=4)
        # subtraction
        self.buttonSub = tk.Button(bottom_frame, **button_params, text="-", command=lambda: self.button_click('-'))
        self.buttonSub.grid(row=2, column=5)
        # factorial function
        self.button_fact = tk.Button(bottom_frame, **button_params, text="n!", command=lambda: self.button_click('factorial('))
        self.button_fact.grid(row=2, column=6)
        
        #percent
        self.button_per= tk.Button(bottom_frame, **button_params, text="%", command=lambda: self.button_click('%('))
        self.button_per.grid(row=2, column=7)
        
        # outputs what is in self.recall
        self.button_MR = tk.Button(bottom_frame, **button_params, text="MR", command=self.memory_recall)
        self.button_MR.grid(row=2, column=8)
        # row 3
        
       
        # one
        self.button_1 = tk.Button(bottom_frame, **button_params, text="1", command=lambda: self.button_click(1))
        self.button_1.configure(activebackground="pink", bg='white')
        self.button_1.grid(row=3, column=2)
        # two
        self.button_2 = tk.Button(bottom_frame, **button_params, text="2", command=lambda: self.button_click(2))
        self.button_2.configure(activebackground="pink", bg='white')
        self.button_2.grid(row=3, column=3)
        # three
        self.button_3 = tk.Button(bottom_frame, **button_params, text="3", command=lambda: self.button_click(3))
        self.button_3.configure(activebackground="pink", bg='white')
        self.button_3.grid(row=3, column=4)
        # addition
        self.button_add = tk.Button(bottom_frame, **button_params, text="+", command=lambda: self.button_click('+'))
        self.button_add.grid(row=3, column=5)
        # left bracket button
        self.button_left_brack = tk.Button(bottom_frame, **button_params, text="(", command=lambda: self.button_click('('))
        self.button_left_brack.grid(row=3, column=6)
        # right bracket button
        self.button_right_brack = tk.Button(bottom_frame, **button_params, text=")", command=lambda: self.button_click(')'))
        self.button_right_brack.grid(row=3, column=7)
        # adds current self.expression to self.recall string
        self.button_M_plus = tk.Button(bottom_frame, **button_params, text="M+", command=self.memory_add)
        self.button_M_plus.grid(row=3, column=8)
        # row 4
         # zero
        self.button_0 = tk.Button(bottom_frame, **button_params, text="0", command=lambda: self.button_click(0))
        self.button_0.configure(activebackground="pink", bg='white', width=7, bd=5)
        self.button_0.grid(row=4, column=2, columnspan=2)
        # equals button
        self.button_eq = tk.Button(bottom_frame, **button_params, text="=", command=self.button_equal)
        self.button_eq.configure(bg='white', activebackground='pink')
        self.button_eq.grid(row=4, column=4)
        
        # to the power of function
        self.button_power = tk.Button(bottom_frame, **button_params, text="x^y", command=lambda: self.button_click('**'))
        self.button_power.grid(row=4, column=6)
        
        # division
        self.button_div = tk.Button(bottom_frame, **button_params, text="/", command=lambda: self.button_click('/'))
        self.button_div.grid(row=4, column=5)
        # decimal to convert to float
        self.button_dec = tk.Button(bottom_frame, **button_params, text=".", command=lambda: self.button_click('.'))
        self.button_dec.grid(row=4, column=6)
        # comma to allow for more than one parameter!
        self.button_comma = tk.Button(bottom_frame, **button_params, text=",", command=lambda: self.button_click(','))
        self.button_comma.grid(row=4, column=7)
         # to the power of function
        self.button_power = tk.Button(bottom_frame, **button_params, text="x^y", command=lambda: self.button_click('**'))
        self.button_power.grid(row=4, column=8)

    # functions
    # allows button you click to be put into self.expression

    def button_click(self, expression_val):
        if len(self.expression) >= 25:
            self.expression = self.expression
            self.text_input.set(self.expression)
        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)

    # clears last item in string

    def button_clear1(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)
  

    # adds in a negative sign

    def change_signs(self):
        self.expression = self.expression + '-'
        self.text_input.set(self.expression)

    # clears memory_recall

    def memory_clear(self):
        self.clear=""
        self.expression="0"
        self.text_input.set(self.expression)
        

    # adds whatever is on the screen to self.recall

    def memory_add(self):
        self.recall = self.recall + '+' + self.expression
        

    # uses whatever is stored in memory_recall

    def answer(self):
        self.answer = self.sum_up
        self.expression = self.expression + self.answer
        self.text_input.set(self.expression)

    # uses whatever is stored in memory_recall

    
    def memory_recall(self):
        if (self.expression==""):
            self.expression = self.expression + str(self.recall)
            self.text_input.set("0"+self.expression)
        else:
            self.expression = self.expression + self.recall
            self.text_input.set(self.expression)  

    # changes self.convert_constant to a string that allows degree conversion when button is clicked

    # clears self.expression

    def button_clear_all(self):
        self.expression = ""
        self.text_input.set("")

    # converts self.expression into a mathematical expression and evaluates it

    def button_equal(self):
        self.sum_up = str(eval(self.expression))
        print(self.sum_up)
        self.text_input.set(self.sum_up)
        self.expression = self.sum_up


# tkinter layout
# tkinter layout
root = tk.Tk()
b = Calculator(root)
root.title("3J's Scientific Calculator")
root.geometry("500x400")
root.resizable(False,False)
root.mainloop()
