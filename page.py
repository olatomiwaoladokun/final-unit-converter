import tkinter as tk
import requests as rs
import PIL
from PIL import Image,ImageTk
# from PIL import *
import time as tm
import _tkinter
# def start():
    # window.resizable(width=False, height=False)

window = tk.Tk() 
window.title("Converter")
window.geometry("500x500")
window.config(bg="sky blue")
frame = tk.Frame(width=10, height=10)
frame.place(anchor="s", relx=0.5, rely=0.4)
logo = ImageTk.PhotoImage(Image.open("unit converter_2.png"))
lb = tk.Label(frame, image=logo)
# help(w)
lb.pack()
# labels

f = tk.Label(text="FROM:", bg="sky blue")
f.place(x=100, y=230)

t = tk.Label(text="TO:", bg="sky blue")
t.place(x=300,y=230)

# entrys
te = tk.Entry()
te.place(x=300, y=250)
fvar = tk.IntVar()
fe = tk.Entry(textvariable=fvar)
fe.get()
fe.place(x=100,y=250 )
fc = None
fmeter = tk.Button(text="meter", command=lambda: fc == "meter")
fkilometer = tk.Button(text ="Kilometer", command=lambda : fc == "kilometer" )
fcentimeter = tk.Button(text="centimeter", command=lambda : fc == "centimeter")
fmilimeter  = tk.Button(text="milimeter", command=lambda : fc == "milimeter")
fyard = tk.Button(text="yard", command=lambda : fc=="yard")
ffoot = tk.Button(text="foot", command=lambda : fc == "foot")
# froms = [fmeter, fkilometer, fcentimeter, fmilimeter, fyard, ffoot]
tc = None
tmeter = tk.Button(text="meter", command=lambda : tc == "meter" )
tkilometer = tk.Button(text ="Kilometer", command=lambda : tc == "kilometer")
tcentimeter = tk.Button(text="centimeter", command=lambda : tc == "centimeter")
tmilimeter  = tk.Button(text="milimeter", command=lambda : tc == "milimeter")
tyard = tk.Button(text="yard", command=lambda : tc == "yard")
tfoot = tk.Button(text="foot", command= lambda : tc == "foot")
fmeter.config(bg="sky blue")
fmeter.place(x=100,y=280)
fkilometer.config(bg="sky blue")
fkilometer.place(x=100,y=310)
fcentimeter.config(bg="sky blue")
fcentimeter.place(x=100,y=340)
fmilimeter.config(bg="sky blue")
fmilimeter.place(x=100,y=370)
fyard.config(bg="sky blue")
fyard.place(x=100,y=400)
ffoot.config(bg="sky blue")
ffoot.place(x=100,y=430)


tmeter.config(bg="sky blue")
tmeter.place(x=300,y=280)
tkilometer.config(bg="sky blue")
tkilometer.place(x=300,y=310)
tcentimeter.config(bg="sky blue")
tcentimeter.place(x=300,y=340)
tmilimeter.config(bg="sky blue")
tmilimeter.place(x=300,y=370)
tyard.config(bg="sky blue")
tyard.place(x=300,y=400)
tfoot.config(bg="sky blue")
tfoot.place(x=300,y=430)
# done = None
# meter


URL = "https://akshayanand.herokuapp.com/api/unit/?type=type&from=from&to=to&value=value"
par =  {
    "type" : "length",
    "from" : "meter",
    "to" : "centimeter",
    "value" : 1
}
results = rs.get(url=URL, json=par)
print(results)
print(rs.status_codes())

# do()
window.mainloop()
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