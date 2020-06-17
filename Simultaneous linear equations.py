"""This program was created for students who want to how to solve Simultaneous equation and this program which was created by obaloluwa sonil can solve equations and show the workings. After you have finished reading the text, delete it to start using the program.  please! DO NOT CHANGE THIS PROGRAM UNLESS YOU ARE A PROGRAMMER AND YOU KNOW HOW TO PROGRAM WITH PYTHON BUT IF YOU HAVE CHANGED IT, RETURN IT TO ME(Obaloluwa sonil) Or VISIT ME ON Facebook TO COMPLAIN YOUR PROBLEMS TO ME. FB USERNAME:OBALOLUWA SONIL. HAVE A NICE DAY WHILE USING MY PROGRAM, THANK YOU"""
__all__ = ['ScrolledText']
from turtle import*
from tkinter import Frame, Text, Scrollbar, Pack, Grid, Place
from tkinter.constants import RIGHT, LEFT, Y, BOTH
class ScrolledText(Text):
    def __init__(self, master=None, **kw):
        self.frame = Frame(master)
        self.vbar = Scrollbar(self.frame)
        self.vbar.pack(side=RIGHT, fill=Y)

        kw.update({'yscrollcommand': self.vbar.set})
        Text.__init__(self, self.frame, **kw)
        self.pack(side=LEFT, fill=BOTH, expand=True)
        self.vbar['command'] = self.yview

        # Copy geometry methods of self.frame without overriding Text
        # methods -- hack!
        text_meths = vars(Text).keys()
        methods = vars(Pack).keys() | vars(Grid).keys() | vars(Place).keys()
        methods = methods.difference(text_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))

    def __str__(self):
        return str(self.frame)


def example():
    from tkinter.constants import END

    stext = ScrolledText(bg='white', height=10)
    stext.insert(END, __doc__)
    stext.pack(fill=BOTH, side=LEFT, expand=True)
    stext.focus_set()
    stext.mainloop()
if __name__ == "__main__":
    example()


shape("turtle")
pencolor("blue")
write("Simultaneous Linear and Quadratic Equation prod by Obaloluwa", move = ("True"), align=("center"), font =("bond",17,"normal"))
print("Simultaneous Linear and Quadratic Equation prod by Obaloluwa")
goto(0, 0)
pu()
lt(90)
fd(50)
write("HELP", align =("center"), font =("bold",30,"normal"))
def HELP(x, y):
    pencolor("black")
    pu()
    goto(0, 0)
    lt(-180)
    fd(100)
    pd()
    write("If your equation is like this, e.g 2x - y = 8, 3x + y = 17...", align = ("center"), font =("bold",20,"normal"))
    pu()
    goto(0, 0)
    fd(150)
    pd()
    write("Represent y as 1y which is 2x -1y = 8, 3x + 1y = 17...So input (B) = 1.", align =("center"), font =("bold",20,"normal"))
    ht()

onclick(HELP)
listen()
print("Question")
print("(A)x + (B)y = (C)")
print("(D)x + (E)y = (F)")
(A) =int(input("(A):"))
(B) =int(input("(B):"))
(C) =int(input("(C):"))
(D) =int(input("(D):"))
(E) =int(input("(E):"))
(F) =int(input("(F):"))
write((A), align =("center"), font =("bold",20,"normal"))
(a) =(D) * (A)
(b) =(D) * (B)
(c) =(D) * (C)
(d) =(A) * (D)
(e) =(A) * (E)
(f) =(A) * (F)

print((a),"x +", (b),"y =", (c),"....(1).")
print((d),"x +", (e),"Y =", (f),"....(2).")
(b) =(b)-(e)
(c) =(c)-(f)
print((b),"y=",(c),"divide both sides by",(b),"y")
(b) =(c) / (b)
print((b),"= y")
print("Substitute",(b),"for y in equ(1)")
print((A),"x +",(B),"(",(b),")","=",(C),"")
(bb) = (B) * (b)
print((A),"x +",(bb),"=",(C),"")
(ccc)= (bb) - (C)
print((A),"=",(ccc),"")
(dddd) =(ccc) / (A)
print("x =",(dddd),"")
print("Main answer is not",(dddd),"")
print("IF answer is -X then the main answer is +X")
print("BUT If answer is +X or X, then answer is -X")

done()

