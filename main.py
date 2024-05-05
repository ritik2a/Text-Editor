from tkinter import *
from tkinter import ttk, font
from tkinter.scrolledtext import ScrolledText
import os


root = Tk()
filename = "unltitled"
Width = 1500
Height = 800
root.geometry(f"{Width}x{Height}")
root.minsize(width=Width, height=Height)
root.maxsize(width=1920, height=1080)
root.resizable(True, True)
root.title("Text Editor")

#_____________________________________________F-U-C-T-I-O-N-S________________P-A-R-A-M-P-R-E-E-T-_-S-I-N-G-H___________________________________P
#====================M-E-N-U-B-A-R====================P-A-R-A-M====================P
#==========F-I-L-E==========P-A-R-A-M==========P
#_____N-E-W_____P
def New():
    nw = Tk()
    Label(nw, text="Trying").pack()
    nw.mainloop()

#_____O-P-E-N_____P
def Open():
    pass
#_____S-A-V-E_____P
def Save():
    pass
#_____S-A-V-E--A-S_____P
def SaveAs():
    pass
#_____P-R-I-N-T_____P
def Print():
    pass

#==========E-D-I-T==========P-A-R-A-M==========P
#_____U-N-D-O_____P
def Undo():
    pass
#_____R-E-D-O_____P
def Redo():
    pass
#_____C-U-T_____P
def Cut():
    pass
#_____C-O-P-Y_____P
def Copy():
    pass
#_____P-A-S-T-E_____P
def Paste():
    pass
#_____Find_&_Replace_____P
def FindReplace():
    pass
#_____S-E-L-E-C-T-A-L-L_____P
def SelectAll():
    pass

#==========V-I-E-W==========P-A-R-A-M==========P
#_____S-T-A-T-U-S-_-B-A-R_____P
def StatusBar():
    global root, TextArea, fullscreen, Theight, Height
    footer = Frame(root)
    Label(footer, text="hello", padx=50).pack(side=BOTTOM)
    footer.pack(fill=X)
    if (fullscreen==1):
        TextArea.config(height=36)
    else:
        a = root.winfo_height()
        if (a!=Height):
            height_setter()
        elif (a==Height):
            TextArea.config(height=25)


#_____D-A-R-K_____P
def Dark():
    pass
#_____L-I-G-H-T_____P
def Light():
    pass

#==========M-O-R-E==========P-A-R-A-M==========P
#_____H-E-L-P_____P
def Help():
    pass
#_____F-E-E-D-B-A-C-K_____P
def FeedBack():
    pass
#_____A-B-O-U-T_____P
def About():
    pass



#==========F-O-N-T==========P-A-R-A-M-P-R-E-E-T-_-S-I-N-G-H==========P
Fname = False
Fsize = False
Fbold = False
Fitalic = False
Funderline = False
Fstrikethrough = False
Fcolor = False
Fhighlight = False

#_____F-O-N-T-_-N-A-M-E_____P
Font_Names = list
def font_name():
    global Font_Names
    Font_Names = list(font.families())
    for i in Font_Names:
        if (not i[0].isalpha()):
            Font_Names.remove(i)

    return sorted(Font_Names)

#_____F-O-N-T-_-S-I-Z-E_____P
Font_Size = []
def font_size():
    global Font_Size
    for i in range(8, 101, 2):
        Font_Size.append(i)

    return Font_Size

#_____B-O-L-D-_-T-E-X-T_____P
def bold():
    global TextArea, Fname, Fsize, Fbold, Fitalic, Funderline, Fstrikethrough, FNget, FSget
    bold_text = font.Font(TextArea, TextArea.cget("font"))
    if (Fname):
        bold_text.configure(family=FNget, size=FSget, weight="bold")
        print('font_name also')
    else:
        bold_text.configure(weight="bold")
        print('only bold')

    TextArea.tag_configure("bold", font=bold_text)

    if "bold" in TextArea.tag_names("sel.first"):
        TextArea.tag_remove("bold", "sel.first", "sel.last")
        Fbold = False
    else:
        TextArea.tag_add("bold", "sel.first", "sel.last")
        Fbold = True

#_____I-T-A-L-I-C-_-T-E-X-T_____P
def italic():
    global TextArea
    italic_text = font.Font(TextArea, TextArea.cget("font"))
    italic_text.configure(slant="italic")

    TextArea.tag_configure("italic", font=italic_text)

    if "italic" in TextArea.tag_names("sel.first"):
        TextArea.tag_remove("italic", "sel.first", "sel.last")
        Fitalic = False
    else:
        TextArea.tag_add("italic", "sel.first", "sel.last")
        Fitalic = True

#_____U-N-D-E-R-L-I-N-E-_-T-E-X-T_____P
def underline():
    global TextArea
    underline_text = font.Font(TextArea, TextArea.cget("font"))
    underline_text.configure(underline=True)
    
    TextArea.tag_configure("underline", font=underline_text)

    if "underline" in TextArea.tag_names("sel.first"):
        TextArea.tag_remove("underline", "sel.first", "sel.last")
        Funderline = False
    else:
        TextArea.tag_add("underline", "sel.first", "sel.last")
        Funderline = True

#_____O-V-E-R-S-T-R-I-K-E-_-T-E-X-T_____P
def strikethrough():
    global TextArea
    strikethrough_text = font.Font(TextArea, TextArea.cget("font"))
    strikethrough_text.configure(overstrike=True)
    
    TextArea.tag_configure("strikethrough", font=strikethrough_text)

    if "strikethrough" in TextArea.tag_names("sel.first"):
        TextArea.tag_remove("strikethrough", "sel.first", "sel.last")
        Fstrikethrough = False
    else:
        TextArea.tag_add("strikethrough", "sel.first", "sel.last")
        Fstrikethrough = True


#_____F-O-N-T-_-U-P-D-A-T-E_____P
FNget , FSget = '', 0          # global variables for font_name, font_size
def font_update(event):
    global root, tvfn, tvfs, TextArea, Fname, Fsize, FNget, FSget, Fbold, Fitalic, Funderline, Fstrikethrough

    FNget = tvfn.get()
    FSget = tvfs.get()
    TextArea.configure(font=(FNget, FSget))
    Fname = True
    Fsize = True

#_____T-E-X-T-_-C-O-L-O-R_____P
TColor = "red"
def text_color():
    global TextArea, TColor    
    try:
        TColor = "red"
        TextArea.tag_configure("tcolor", foreground=TColor)

        if ("tcolor" not in TextArea.tag_names("sel.first")):
            TextArea.tag_add("tcolor", "sel.first", "sel.last")
            Fcolor = True
        else:
            TextArea.tag_remove("tcolor", "sel.first", "sel.last")
            Fcolor = False

        TextArea.update()
    except TclError:
        pass


#_____H-I-G-H-L-I-G-H-T-_-T-E-X-T-_-C-O-L-O-R_____P
HTColor = "white"
def highlight_text():
    global TextArea, HTColor
    try:
        HTColor = "yellow"
        TextArea.tag_configure("hcolor", background=HTColor)

        if ("hcolor" not in TextArea.tag_names("sel.first")):
            TextArea.tag_add("hcolor", "sel.first", "sel.last")
            Fhighlight = True
        else:
            TextArea.tag_remove("hcolor", "sel.first", "sel.last")
            Fhighlight = False

        TextArea.update()
    except TclError:
        pass

#_____T-E-X-T-_-C-O-L-O-R-_-R-E-M-O-V-E-R_____P
def remove_color():
    global TextArea, HTColor, TColor
    try:
        TextArea.tag_remove("hcolor", "sel.first", "sel.last")
        TextArea.tag_remove("tcolor", "sel.first", "sel.last")
        HTColor = "white"
        TColor = "blacK"
        TextArea.update()
    except TclError:
        pass


# #____W-I-N-D-O-W-_-S-I-Z-E-_-C-H-A-N-G-E____P
# def size_change():
#     winwidth = 


#_____H-E-I-G-H-T-_-S-E-T-T-E-R_____P
def height_setter():
    global Height, Theight, root
    current_height = root.winfo_reqheight()
    heights = []
    Text_height = []
    height_dict = {}

    for h in range(Height+31, 1050, 31):
        heights.append(str(h))
    print(heights)
    print(len(heights))

    for Th in range(Theight+1, 36):
        Text_height.append(str(Th))
    print(Text_height)
    print(len(Text_height))

    # for i in range(len(heights)):
    #     height_dict[heights[i]] = Text_height[i]

    # print(height_dict)

    # if (current_height!=Height):
    

#_____C-H-A-N-G-E-_-F-U-L-L-S-C-R-E-E-N____P
fullscreen = 0
def FullScreen(event):
    global fullscreen, Height, TextArea, head
    if (fullscreen==0):
        root.attributes("-fullscreen", TRUE)
        Theight = 36
        TextArea.config(height=Theight)
        fullscreen = 1

    else:
        root.attributes("-fullscreen", FALSE)
        fullscreen = 0

root.bind("<F11>", FullScreen)

#__________________________________M-E-N-U-_-B-A-R___________________________P-A-R-A-M-P-R-E-E-T-_-S-I-N-G-H_____________________________________P
menu = Menu(root)
#===============P-A-R-A-M-P-R-E-E-T-=-S-I-N-G-H===============P
m1 = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=m1)

#_____________F-I-L-E_____________P
m1.add_command(label="New", command=New)
m1.add_command(label="Open", command=Open)
m1.add_command(label="Save", command=Save)
m1.add_command(label="Save As", command=SaveAs)
m1.add_separator()
m1.add_command(label="Print", command=Print)
m1.add_separator()
m1.add_command(label="Exit", command=quit)

#===============P-A-R-A-M-P-R-E-E-T-=-S-I-N-G-H===============P
m2 = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=m2)

#_____________E-D-I-T_____________P
m2.add_command(label="Undo", command=Undo)
m2.add_command(label="Redo", command=Redo)
m2.add_separator()
m2.add_command(label="Cut", command=Cut)
m2.add_command(label="Copy", command=Copy)
m2.add_command(label="Paste", command=Paste)
m2.add_separator()
m2.add_command(label="Find & Replace", command=FindReplace)
m2.add_separator()
m2.add_command(label="Select All", command=SelectAll)

#===============P-A-R-A-M-P-R-E-E-T-=-S-I-N-G-H===============P
m3 = Menu(menu, tearoff=0)
menu.add_cascade(label="View", menu=m3)
#____________V-I-E-W____________P
m3.add_command(label="Status Bar", command=StatusBar)
m3.add_separator()

#_____A-P-P-E-A-R-E-N-C-E_____P
appear = Menu(m3, tearoff=0)
appear.add_radiobutton(label="Dark Mode", command=Dark)
appear.add_radiobutton(label="Light Mode", command=Light)
m3.add_cascade(label="Appearance", menu=appear)

#===============P-A-R-A-M-P-R-E-E-T-=-S-I-N-G-H===============P
m4 = Menu(menu, tearoff=0)
menu.add_cascade(label="More", menu=m4)

#__________H-E-L-P__________P
m4.add_command(label="Help", command=Help)
m4.add_command(label="Feedback", command=FeedBack)
m4.add_separator()
m4.add_command(label="About Notepad", command=About)

#________________________________T-T-K-_-S-T-Y-L-E___________________________P-A-R-A-M-P-R-E-E-T-_-S-I-N-G-H_____________________________________P
root.config(menu=menu)
style = ttk.Style()
style.theme_create(themename="ParamStyle", settings={
    ".": {                          # All except tabs
        "configure": {
            "background" : "gold",       
            "highlightedBackground" : "yellow",
        },
        "map" : {
            "background": [("active", "yellow"), ("selected", "red"), ("!disabled" , "grey")],
            "foreground": [("selected", "blue")],
        }
    },

    "TNotebook": {              # Notebook and widgets inside it
        "configure": {
            "background" : "red",     
            "tabposition" : "nw",
            "bordercolor" : "yellow",
        },

        "map": {
            "background": [("selected", "red")],
            "foreground": [("selected", "blue")],
        }
    },

    "TNotebook.Tab": {          # tabs of Notebook
        "configure": {
            "background": "green",        # tab color when not selected
            "foreground" : "gold",
            "padding": [50, 3],         # [space between text and horizontal tab-button border, space between text and vertical tab_button border]
        },

        "map": {
            "background": [("active", "black"), ("selected", "red"), ("disabled" , "grey")],    # Tab color when selected
            "foreground": [("selected", "blue")],   # Text color of tab when selected
        }
    },

    "TCombobox" : {            # Combobox
        "configure" : {
            "arrowcolor" : "red",
            "arrowsize" : 18,
            "background" : "gold",
            "darkcolor" : "red",
            "fieldbackground" : "lightgoldenrod",
            "relief" : "solid",
            "selectbackground" : "gold",
            "selectforeground" : "black"
        },
    },

    "Vertical.TScrollbar" : {       # Scrollbar inside combobox but also for normal scrollbar
        "configure" : {
            "background" : "gold",
            "arrowcolor" : "black",
            "arrowsize" : 18,
            "relief" : "solid",
            "troughcolor" : "lightgoldenrod",
            "troughborderwidth" : 10,
            "troughrelief" : "raised",
            "width" : 2,
        },
    }
})

style.theme_use("ParamStyle")

#_____Changes_the_font_of_the_tab_header_____P
style.configure("TNotebook.Tab", font=("Arial", 16, "bold"))
Combobox_font = ("Arial", 12)
root.option_add("*TCombobox*Listbox.font", Combobox_font)
root.option_add("*TCombobox*Listbox.background", "lightgoldenrod")
root.option_add("*TCombobox*Listbox.foreground", "red")
root.option_add("*TCombobox*Listbox.selectBackground", "goldenrod")
root.option_add("*TCombobox*Listbox.selectForeground", "black")


#_____Changing_path_for_icons_____P
os.chdir(".\\images\\")

#_________________________________H-E-A-D-_-F-R-A-M-E_____________________________P-A-R-A-M-P-R-E-E-T-_-S-I-N-G-H___________________________________P
head = Frame(root)
Tabs = ttk.Notebook(head, height=130)

#========================F-I-L-E-_-T-A-==============================P
File = Frame(Tabs)

#========================F-I-L-E-_-E-N-D-S===========================P
File.pack(fill=BOTH, expand=TRUE)
Tabs.add(File, text="File")

#========================E-D-I-T-_-T-A-B=============================P
Edit = Frame(Tabs)

#========================E-D-I-T-_-E-N-D-S===========================P
Edit.pack(fill=BOTH, expand=TRUE)
Tabs.add(Edit, text="Edit")

#========================F-O-N-T-_-T-A-B=============================P
FONT = Frame(Tabs, bg="gold")

#==============F-O-N-T-_-S-T-Y-L-E================P-A-R-A-M=======P
FontStyle = LabelFrame(FONT, text="Font Style", font=("Arial", 12, "bold"), relief="solid", bg="gold", padx=10, pady=10, labelanchor=N)

#_____F-O-N-T-_-N-A-M-E_____P
tvfn = StringVar()
fn = font_name()
FontName = ttk.Combobox(FontStyle, width=30, font=Combobox_font, textvariable=tvfn, values=fn, state="readonly", height=15)
FontName.current(3)     # Arial
FontName.bind("<<ComboboxSelected>>", font_update)
FontName.grid(row=0, column=0)

#_____F-O-N-T-_-S-I-Z-E_____P
tvfs = IntVar()
fs = font_size()
FontSize = ttk.Combobox(FontStyle, width=5, font=Combobox_font, textvariable=tvfs, values=fs, state="readonly", height=15)
FontSize.current(3)     # 14 size
FontSize.bind("<<ComboboxSelected>>", font_update)
FontSize.grid(row=0, column=1, padx=10)

#_____S-E-P-A-R-A-T-O-R-_-1_____P
font_style_sep = Frame(FontStyle, bg="black", width=2)
font_style_sep.grid(row=0, column=2, sticky=N+S, padx=10)

#_____B-O-L-D_____P
Bold = Button(FontStyle, text="B", font=("Arial", 24 ,"bold"), command=bold, overrelief="solid")
Bold.grid(row=0, column=3, padx=5, ipadx=2, ipady=2)

#_____I-T-A-L-I-C_____P
Italic = Button(FontStyle, text="I", font=("Arial", 24, "bold", "italic"), padx=5, command=italic, overrelief="solid")
Italic.grid(row=0, column=4, padx=5, ipadx=2, ipady=2)

#_____U-N-D-E-R-L-I-N-E_____P
Underline = Button(FontStyle, text="U", font=("Arial", 24, "bold", "underline"), command=underline, overrelief="solid")
Underline.grid(row=0, column=5, padx=5, ipadx=2, ipady=2)

Strikerthrough = Button(FontStyle, text="T", font=("Arial", 24, "bold", "overstrike"), command=strikethrough, overrelief="solid")
Strikerthrough.grid(row=0, column=6, padx=5, ipadx=2, ipady=2)

#_____S-U-P-E-R-S-C-R-I-P-T_____P
SuperScript = Button(FontStyle, text=u"x\u00B2", font=("Sans Serif", 22, "bold"), command=underline, overrelief="solid")
SuperScript.grid(row=0, column=7, padx=5, ipadx=2, ipady=5)

#_____S-U-B-S-C-R-I-P-T_____P
SubScript = Button(FontStyle, text=u"x\u2082", font=("Sans Serif", 22, "bold"), command=underline, overrelief="solid")
SubScript.grid(row=0, column=8, padx=5, ipady=5)

#_____S-E-P-A-R-A-T-O-R-_-2_____P
font_style_sep_2 = Frame(FontStyle, bg="black", width=2, height=10)
font_style_sep_2.grid(row=0, column=9, sticky=N+S, padx=10)

#_____T-E-X-T-_-C-O-L-O-R_____P
Text_Color = Button(FontStyle, text="T", font=("Arial", 24 ,"bold"), fg="red", command=text_color, overrelief="solid")
Text_Color.grid(row=0, column=10, padx=5)

#_____T-E-X-T-_-H-I-G-H-L-I-G-H-T-O-R_____P
Text_Highlighter = Button(FontStyle, text="T", font=("Arial", 24 ,"bold"), bg="yellow", command=highlight_text, overrelief="solid")
Text_Highlighter.grid(row=0, column=11, padx=5)

#_____C-L-E-A-R-_-C-O-L-O-R_____P
clearcolor = PhotoImage(file="text_clear.png")
Clear_Color = Button(FontStyle, image=clearcolor, command=remove_color, overrelief="solid")
Clear_Color.grid(row=0, column=12, ipadx=5, ipady=2, padx=5)

#========F-O-N-T-_-S-T-Y-L-E-_-E-N-D-S============P-A-R-A-M=======P
FontStyle.grid(row=0, column=0, padx=20, pady=5)

#===============S-E-P-E-R-A-T-O-R-=-1==============P-A-R-A-M=======P
font_separator1 = Frame(FONT, bg="black", width=2, height=125)
font_separator1.grid(row=0, column=1, sticky=N+S)

#===================F-O-N-T-_-E-N-D-S=================P-A-R-A-M===================P
FONT.pack(fill=BOTH, expand=TRUE)
Tabs.add(FONT, text="Font")

#=======================P-A-R-A-G-R-A-P-H-_-T-A-B===========================P
Paragraph = Frame(Tabs, bg="gold")

#===============-================P-A-R-A-M=======P
Alignment = LabelFrame(Paragraph, text="Alignment", font=("Arial", 14, "bold"), relief="solid", bg="gold", labelanchor=N)

#_____Left_Alignment_____P
Left_align = LabelFrame(Alignment, text="Left", font=("Arial", 12, "bold"), relief="flat", bg="gold", labelanchor=S)
LI = PhotoImage(file="left_align.png")
LA = Button(Left_align, image=LI, overrelief="solid")
LA.pack()
Left_align.pack(side=LEFT, padx=20, ipady=3)

#_____Right_Alignment_____P
Right_align = LabelFrame(Alignment, text="Right", font=("Arial", 12, "bold"), relief="flat", bg="gold", labelanchor=S)
RI = PhotoImage(file="right_align.png")
RA = Button(Right_align, image=RI, overrelief="solid")
RA.pack()
Right_align.pack(side=LEFT, padx=10, ipady=3)

#_____Center_Alignment_____P
Center_align = LabelFrame(Alignment, text="Center", font=("Arial", 12, "bold"), relief="flat", bg="gold", labelanchor=S)
CI = PhotoImage(file="center_align.png")
CA = Button(Center_align, image=CI, relief="flat", bg="gold", overrelief="solid")
CA.pack(ipadx=2, ipady=3)
Center_align.pack(side=LEFT, padx=10, ipady=3)

#_____Justified_Alignemnt_____P
Justify_align = LabelFrame(Alignment, text="Justify", font=("Arial", 12, "bold"), relief="flat", bg="gold", labelanchor=S)
JI = PhotoImage(file="justify_align.png")
JA = Button(Justify_align, image=JI, overrelief="solid")
JA.pack(ipady=5)
Justify_align.pack(side=LEFT, padx=10, ipady=3)

#===============A-L-I-G-N-M-E-N-T-_-E-N-D-S=======P-A-R-A-M=======P
Alignment.grid(row=0, column=0, padx=30, ipadx=10, ipady=3)

#_____Indentation_____P
Indentation = LabelFrame(Paragraph, text="Indentation", font=("Arial", 14, "bold"), relief="solid", bg="gold", labelanchor=N)
Button(Indentation, text="try").grid(row=0, column=0)
Indentation.grid(row=0, column=2, ipadx=20, ipady=10, padx=10)

#_____Line_Spacing_____P
Line_Spacing = LabelFrame(Paragraph, text="Line Spacing", font=("Arial", 14, "bold"), relief="solid", bg="gold", labelanchor=N)
Button(Line_Spacing, text="try").grid(row=0, column=0)
Line_Spacing.grid(row=0, column=4, ipadx=20, ipady=10, padx=10)


#========================F-I-L-E-_-E-N-D-S===============P-A-R-A-M-P-R-E-E-T-_-S-I-N-G-H===========================P
Paragraph.pack(fill=BOTH, expand=TRUE)
Tabs.add(Paragraph, text="Paragraph")

#===================T-A-B-S-_-E-N-D-S=================P-A-R-A-M===================P
Tabs.pack(fill=BOTH)
Tabs.select(FONT)

#------------------------------------H-E-A-D-_-E-N-D-S----------------------------P-A-R-A-M-P-R-E-E-T-_-S-I-N-G-H--------------------P
head.pack(side=TOP, anchor=NW, fill=X)

#==================T-E-X-T-=-A-R-E-A==================P-A-R-A-M===================P
Theight = 27
TextArea = ScrolledText(root, font=("Arial", 14), padx=50, pady=30, height=Theight, wrap="word")
TextArea.pack(fill=BOTH, expand=True)
# TextArea.config(tabs=("9c", CENTER))

#_________________________________E-N-D_____________________________P-A-R-A-M-P-R-E-E-T-_-S-I-N-G-H___________________________________P
root.mainloop()