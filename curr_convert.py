# A currency convert python program, using tkinter   
#
# Currencies used in program:
# USD (Dollar of The United States), EUR (Euro), CZK (Czech koruna),
# PLN (Polish Zloty), GBP (British pound sterling)
#
# Values provided in roubles (Actual on 16.10.2021):
# https://www.cbr.ru/currency_base/daily/

from tkinter import *

wind = Tk()
wind.title("Currency convert")
wind.geometry("500x375")

FRGN_CURR = {
        "USD":71.23,
        "EUR":82.72,
        "PLN":18.09,
        "CZK":3.25,
        "GBP":97.77,
    }

def convert(self):
    
    prc = curr_amount.get()
    chsn_curr = var1.get()
    crrs = FRGN_CURR.get(chsn_curr, None)
    rst = round(float(prc) * float(crrs), 2)
    output_text.delete(0, END)
    output_text.insert(INSERT,rst)

tgl = Label(wind, text='Convert your currency here!', font="Verdana 16")
tgl.place(x=115, y=0)

curr_list = Label(wind, text="What's your currency? -->", font="Verdana 16")
curr_list.place(x=0, y=50)

curr = Label(wind, text='How much is it? -->', font="Verdana 16")
curr.place(x=0, y=100)

curr_amount = Entry(wind, width=15, bg='white')
curr_amount.place(x=360, y=102)

var1 = StringVar(wind)
var1.set('Picking ...')

curr_opt = OptionMenu(wind, var1, *FRGN_CURR)
curr_opt.place(x=360, y=52, width=125)

MagicButton = Button(wind, text="Convert", font="Verdana 16")
MagicButton.bind("<Button-1>",convert)
MagicButton.place(x=125, y=175)

output_header = Label(wind, text='Your currency in roubles -->', font="Verdana 16")
output_header.place(x=0, y=250)

output_text = Entry(wind, width=20, bg='white')
output_text.place(x=310, y=253)

wind.mainloop()