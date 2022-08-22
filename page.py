import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests as rs
import PIL
import numpy as nu
import pint as pt 
from PIL import Image,ImageTk
# from PIL import *
import formulas as fum
import time as tm
import _tkinter




# MAIN WINDOW

window = tk.Tk() 
window.title("Converter")
window.geometry("500x500")
window.config(bg="sky blue")
window.resizable(height=False, width=False)
frame = tk.Frame(width=10, height=10)
frame.place(anchor="s", relx=0.5, rely=0.4)
logo = ImageTk.PhotoImage(Image.open("unit converter_2.png"))
lb = tk.Label(frame, image=logo)
lb.pack()

# labels
f = tk.Label(text="FROM:", bg="sky blue")
f.place(x=100, y=230)

t = tk.Label(text="TO:", bg="sky blue")
t.place(x=300,y=230)

# entrys
to_var = tk.IntVar()
te = tk.Entry(window, textvariable=to_var)
te.place(x=300, y=250)
from_var = tk.IntVar()
fg = tk.Entry(window, textvariable=from_var)

fg.place(x=100,y=250 )
# tool = pt.UnitRegistry()
fe = fg.get()



# LOGIN ACTIVITIES
meter = fum.Meter()
km = fum.Kilometer()
mm = fum.Milimeter()
cm = fum.Centimeter()
yard = fum.Yard()
foot = fum.Foot()


def convert():
    try:    
        from_e = from_var.get()
        from_entry = float(from_e)
        print(from_entry)
        to_entry = to_var.get()

        fastfrom = _from.get()
        fasto = _to.get()

        # Meter
        te.delete(0, "end")
        if _from.get() =="Meter" and _to.get() == "Meter":
            result = 1
            te.insert("end", result)
        elif _from.get() == "Meter" and _to.get() == "Kilometer":
            result = meter.meter_kilometer(from_entry)
            print(from_entry)
            te.insert("end", result)
        elif fastfrom == "Meter" and fasto == "Centimeter":
            result = meter.meter_centimeter(from_entry)
            te.insert("end", result)
        elif fastfrom == "Meter" and fasto == "Foot":
            result = meter.meter_foot(from_entry)
            te.insert("end", result)
        elif fastfrom == "Meter" and fasto == "Yard":
            result = meter.meter_yard(from_entry)
            te.insert("end", result)

        elif fastfrom == "Meter" and fasto == "Kilometer":
            result = meter.meter_kilometer(from_entry)
            te.insert("end", result)

    #   Kilometer
        if fastfrom == "Kilometer" and fasto == "Meter":
            result = km.kilometer_meter(from_entry)
            te.insert("end", result)
        elif fastfrom == "Kilometer" and fasto == "Kilometer":
            result = 1
            te.insert("end", result)    
        elif fastfrom == "Kilometer" and fasto == "Milimeter":
            result = km.kilometer_milimeter(from_entry)
            te.insert("end", result)
        elif fastfrom == "Kilometer" and fasto == "Centimeter":
            result = km.kilometer_centimeter(from_entry)
            te.insert("end", result)
        elif fastfrom == "Kilometer" and fasto == "Yard":
            result = km.kilometer_yard(from_entry)
            te.insert("end", result)
        elif fastfrom == "Kilometer" and fasto == "Foot":
            result = km.kilometer_foot(from_entry)
            te.insert("end", result)

    #   centimeter
        if fastfrom == "Centimeter" and fasto == "Meter":
            result = cm.cetimeter_meter(from_entry)
            te.insert("end", result)
        elif fastfrom == "Centimeter" and fasto == "Centimeter":
            result = 1
            te.insert("end", result)    
        elif fastfrom == "Centimeter" and fasto == "Kilometer":
            result = cm.centimeter_kilometer
            te.insert("end", result)
        elif fastfrom == "Centimeter" and fasto == "Milimeter":
            result = cm.centimeter_milimemter(from_entry)
            te.insert("end", result)
        elif fastfrom == "Centimeter" and fasto == "Centimeter":
            result = cm.centimeter_centimeter(from_entry)
            te.insert("end", result)
        elif fastfrom == "Centimeter" and fasto == "Yard":
            result = cm.centimeter_yard(from_entry)
            te.insert("end", result)
        elif fastfrom == "Centimeter" and fasto == "Foot":
            result = cm.centimeter_foot(from_entry)
            te.insert("end", result)

    #   milimeter
        if fastfrom == "Milimeter" and fasto == "Meter":
            result = mm.milimeter_meter(from_entry)
            te.insert("end", result)
        elif fastfrom == "Milimeter" and fasto == "Milimeter":
            result = 1
            te.insert("end", result)    
        elif fastfrom == "Milimeter" and fasto == "Milimeter":
            result = mm.milimeter_milimeter(from_entry)
            te.insert("end", result)
        elif fastfrom == "Milimeter" and fasto == "Kilometer":
            result = mm.milimeter_kilometer(from_entry)
            te.insert("end", result)
        elif fastfrom == "Milimeter" and fasto == "Centimeter":
            result = mm.milimeter_centimeter(from_entry)
            te.insert("end", result)
        elif fastfrom == "Milimeter" and fasto == "Milimeter":
            result = mm.milimeter_yard(from_entry)
            te.insert("end", result)
        elif fastfrom == "Milimeter" and fasto == "Foot":
            result = mm.milimeter_foot(from_entry)
            te.insert("end", result)


    #   Yard
        if fastfrom == "Yard" and fasto == "Meter":
            result = yard.yard_meter(from_entry)
            te.insert("end", result)  
        elif fastfrom == "Yard" and fasto == "Milimeter":
            result = yard.yard_milimeter(from_entry)
            te.insert("end", result)
        elif fastfrom == "Yard" and fasto == "Kilometer":
            result = yard.yard_kilometer(from_entry)
            te.insert("end", result)
        elif fastfrom == "Yard" and fasto == "Centimeter":
            result = yard.yard_centimeter(from_entry)
            te.insert("end", result)
        elif fastfrom == "Yard" and fasto == "Yard":
            result = 1
            te.insert("end", result)
        elif fastfrom == "Yard" and fasto == "Foot":
            result = yard.yard_foot(from_entry)
            te.insert("end", result)
        
    #   Foot
        if fastfrom == "Foot" and fasto == "Meter":
            result = foot.foot_meter(from_entry)
            te.insert("end", result)  
        elif fastfrom == "Foot" and fasto == "Milimeter":
            result = foot.foot_milimeter(from_entry)
            te.insert("end", result)
        elif fastfrom == "Foot" and fasto == "Kilometer":
            result = foot.foot_kilometer(from_entry)
            te.insert("end", result)
        elif fastfrom == "Foot" and fasto == "Centimeter":
            result = foot.foot_centimeter(from_entry)
            te.insert("end", result)
        elif fastfrom == "Foot" and fasto == "Yard":
            result = foot.foot_yard(from_entry)
            te.insert("end", result)
        elif fastfrom == "Foot" and fasto == "Foot":
            result = 1
            te.insert("end", result)
    except _tkinter.TclError:
        messagebox.showerror(title = "Bad input!!", message="Your input is not valid")
        fg.delete(0, "end")

options = [
    None,
    "Meter",
    "Kilometer",
    "Centimeter",
    "Millimeter",
    "Yard",
    "Foot"
]

_from = tk.StringVar()
# print(type(_from))
_from.set("Meter")
from_drop_down = ttk.OptionMenu(window, _from, *options)
from_drop_down.place(x=100,y=280)

_to = tk.StringVar()
_to.set("Meter")
to_drop_down = ttk.OptionMenu(window, _to, *options)
to_drop_down.place(x=300,y=280)

convert_btn = tk.Button(window, text="Convert", command=convert)
convert_btn.config(bg="sky blue")
convert_btn.place(x=210,y=350)







window.mainloop()


















# URL = "https://akshayanand.herokuapp.com/api/unit/?type=type&from=from&to=to&value=value"
# par =  {
#     "type" : "length",
#     "from" : "meter",
#     "to" : "centimeter",
#     "value" : 1
# }
# results = rs.get(url=URL, json=par)
# print(results.status_code)
# print(results)
# print(rs.status_codes())

# do()
# "#220033"
# win.destroy()
# button places
# fromval = None
# toomval = None
# toomval =  ""
# fromval = ""
# def frmeter():
#     fromval == "meter"
#     return fromval
# def frkilometer():
#     fromval == "kilometer"
#     return fromval
# def frcentimeter():
#     fromval == "centimeter"
#     return fromval
# def frmilimeter():
#     fromval == "milimeter"
#     return fromval
# def fryard():
#     fromval == "yard"
#     return fromval
# def frfoot():
#     fromval == "foot"
# return fromval
# centimeter

# if __name__ == '__main__':
#     window().mainloop() 
# start()

    # for fs in froms:
    #     yc = 280
    #     fs.place(x=100, y=280)
    #     yc -= 0.002

    # frame = tk.Frame(width=10, height=10)
# def tokilometer():
#     toomval == "kilometer"
#     return toomval
# def tocentimeter():
#     toomval == "centimeter"
#     return toomval

# def tomilimeter():
#     toomval == "milimeter"
#     return toomval

# def toyard():
#     toomval == "yard"
#     return toomval

# def tofoot():
#     toomval == "foot"
#     return toomval
# if fromval == meter and toomval == "kilometer":
#     done == meter.meter_kilometer(fe)
# if fromval == meter and toomval == "centimeter":
#     done == meter.meter_centimeter(fe)
# if fromval == meter and toomval == "milimeter":
#     done == meter.meter_milimeter(fe)
# if fromval == meter and toomval == "yard":
#     done == meter.meter_yard(fe)
# if fromval == meter and toomval == "foot":
#     done == meter.meter_foot(fe)
# # kilometer
# if fromval == kilometer and toomval == "meter":
#     done == kilometer.kilometer_meter(fe)
#     print(done)        
# if fromval == kilometer and toomval == "kilometer":
#     done == kilometer.kilometer_kilometer(fe)
# if fromval == kilometer and toomval == "milimeter":
#     done == kilometer.kilometer_milimeter(fe)
# if fromval == kilometer and toomval == "centimeter":
#     done == kilometer.kilometer_centimeter(fe)
# if fromval == kilometer and toomval == "yard":
#     done == kilometer.kilometer_yard(fe)
# if fromval == kilometer and toomval == "foot":
#     done == kilometer.kilometer_foot(fe)
# # milimeter
# if fromval == milimeter and toomval == meter:
#     done == milimeter.milimeter_meter(fe)
# if fromval == milimeter and toomval == "kilometer":
#     done == milimeter.milimeter_kilometer(fe)
# if fromval == milimeter and toomval == "milimeter":
#     done == milimeter.milimeter_milimeter(fe)
# if fromval == milimeter and toomval == "centimeter":
#     done == milimeter.milimeter_centimeter(fe)
# if fromval == milimeter and toomval == "foot":
#     done == milimeter.milimeter_foot(fe)
# if fromval == milimeter and toomval == "yard":
#     done == milimeter.milimeter_yard(fe)
# def tometer():
#     toomval = "meter"
#     if fromval == "meter" and toomval == "meter":
#         done == meter.meter_meter(fe)
#         print(done)
#         print(toomval)
#         return done
#     return toomval
    # frame.place(anchor="s", relx=0.5, rely=0.5)
    # logo = ImageTk.PhotoImage(Image.open("padlock-icon.jpg"))
    # label = tk.Label(frame, image=logo)
    # label.pack()
    # print(dir(pl))
    # m = tk.Text()
    # m.place(x=100,y=120)

    # m.place(x=300,y=200)
