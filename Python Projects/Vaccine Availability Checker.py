# Import modules
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import pytz
import requests

IST = pytz.timezone('Asia/Kolkata')

app = Tk()

# App Geometry and components
app.geometry("700x480+400+200")
app.title(f"Vaccine Availability Checker")
app.resizable(True, True)
app.config(background = '#293241')

# Color value reference
top_left_frame_bg  = "#5c4ce1"
top_right_frame_bg = '#867ae9'

# Frame details
frame1 = Frame(app, height = 120, width=180, bg= top_left_frame_bg, bd=1, relief = FLAT)
frame1.place(x=0,y=0)

frame2 = Frame(app, height = 120, width=520, bg= top_right_frame_bg, bd=1, relief = FLAT)
frame2.place(x=180,y=0)

frame3 = Frame(app, height = 30, width=700, bg= 'black', bd=1, relief = RAISED)
frame3.place(x=0,y=120)

# Labels
label_date_now = Label(text="Current Date", bg = top_left_frame_bg, font = 'Verdana 12 bold')
label_date_now.place(x=20, y=40)

label_time_now = Label(text="Current Time", bg = top_left_frame_bg, font = 'Verdana 12')
label_time_now.place(x=20, y=60)

label_pincode = Label(text="Pincode", bg = top_right_frame_bg, font = 'Verdana 11')
label_pincode.place(x=220, y=15)

label_date = Label(text="Date", bg = top_right_frame_bg, font = 'Verdana 11')
label_date.place(x=380, y=15)

label_dateformat = Label(text="[dd-mm-yyyy]", bg = top_right_frame_bg, font = 'Verdana 7')
label_dateformat.place(x=420, y=18)

label_search_vacc = Label(text="Search \nAvailable Vaccine", bg = top_right_frame_bg, font = 'Verdana 8')
label_search_vacc.place(x=570, y=70)

label_head_result = Label(text=" Status       \tCentre-Name\t              Age-Group    Vaccine       Dose_1     Dose_2     Total", bg = 'black', fg='white', font = 'Verdana 8 bold')
label_head_result.place(x=10, y=125)

# Entry boxes
pincode_text_var = StringVar()
pincode_textbox = Entry(app,width = 11, bg = '#eaf2ae', fg= 'black', textvariable = pincode_text_var, font='verdana 11')
pincode_textbox['textvariable'] = pincode_text_var
pincode_textbox.place(x= 220, y=40)

date_text_var = StringVar()
date_textbox = Entry(app,width = 12, bg = '#eaf2ae', fg= 'black', textvariable = date_text_var, font='verdana 10')
date_textbox['textvariable'] = date_text_var
date_textbox.place(x= 380, y=40)

## TEXT BOX
result_box_avl = Text(app, height = 20, width = 8, bg='#293241',fg='#ecfcff', relief=FLAT, font='verdana 10')
result_box_avl.place(x= 3 , y= 152)
result_box_cent = Text(app, height = 20, width = 30, bg='#293241',fg='#ecfcff', relief=FLAT, font='verdana 10')
result_box_cent.place(x= 75 , y= 152)
result_box_age = Text(app, height = 20, width = 8, bg='#293241',fg='#ecfcff', relief=FLAT, font='verdana 10')
result_box_age.place(x= 330 , y= 152)
result_box_vacc = Text(app, height = 20, width = 10, bg='#293241',fg='#ecfcff', relief=FLAT, font='verdana 10')
result_box_vacc.place(x= 400 , y= 152)
result_box_D1 = Text(app, height = 20, width = 7, bg='#293241',fg='#ecfcff', relief=FLAT, font='verdana 10')
result_box_D1.place(x= 490 , y= 152)
result_box_D2 = Text(app, height = 20, width = 7, bg='#293241',fg='#ecfcff', relief=FLAT, font='verdana 10')
result_box_D2.place(x= 555 , y= 152)
result_box_D1_D2 = Text(app, height = 20, width = 7, bg='#293241',fg='#ecfcff', relief=FLAT, font='verdana 10')
result_box_D1_D2.place(x= 630 , y= 152)

## Defining Functions

def update_clock():
    raw_TS = datetime.now(IST)
    date_now = raw_TS.strftime("%d %b %Y")
    time_now = raw_TS.strftime("%H:%M:%S %p")
    formatted_now = raw_TS.strftime("%d-%m-%Y")
    label_date_now.config(text = date_now)
    label_time_now.config(text = time_now)
    label_time_now.after(1000, update_clock)
    return formatted_now

def refresh_api_call(PINCODE, DATE):
    header = {'User-Agent': 'Chrome/84.0.4147.105 Safari/537.36'}
    request_link = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={PINCODE}&date={DATE}"
    response = requests.get(request_link, headers = header)
    resp_JSON = response.json()
    return resp_JSON

def clear_result_box():
    result_box_avl.delete('1.0', END)
    result_box_cent.delete('1.0', END)
    result_box_age.delete('1.0', END)
    result_box_vacc.delete('1.0', END)
    result_box_D1.delete('1.0', END)
    result_box_D2.delete('1.0', END)
    result_box_D1_D2.delete('1.0', END)

def search_vaccine_avl():
    clear_result_box()
    PINCODE = pincode_text_var.get()
    DATE = date_text_var.get()
    resp_JSON = refresh_api_call(PINCODE, DATE)

    try:
        if len(resp_JSON['sessions']) == 0:
            messagebox.showinfo("INFO","Vaccine not yet arrived for the given date")

        for sess in resp_JSON['sessions']:
            age_limit           = sess['min_age_limit']
            center_name         = sess['name']
            pincode             = sess['pincode']
            vaccine_name        = sess['vaccine']
            available_capacity  = sess['available_capacity']
            qnty_dose_1         = sess['available_capacity_dose1']
            qnty_dose_2         = sess['available_capacity_dose2']
            slot_date           = sess['date']

            if available_capacity > 0:
                curr_status = 'Available'
            else:
                curr_status = 'NA'
            
            if age_limit == 45:
                age_grp = '45+'
            else:
                age_grp = '18-44'

            result_box_avl.insert(END, f"{curr_status:^6s}")
            result_box_avl.insert(END,"\n")
            result_box_cent.insert(END, f"{center_name:<30s}")
            result_box_cent.insert(END,"\n")
            result_box_age.insert(END, f"{age_grp:<6s}")
            result_box_age.insert(END,"\n")
            result_box_vacc.insert(END, f"{vaccine_name:<8s}")
            result_box_vacc.insert(END,"\n")
            result_box_D1.insert(END, f"{qnty_dose_1:>5}")
            result_box_D1.insert(END,"\n")
            result_box_D2.insert(END, f"{qnty_dose_2:>5}")
            result_box_D2.insert(END,"\n")
            result_box_D1_D2.insert(END, f"{available_capacity:<5}")
            result_box_D1_D2.insert(END,"\n")
    except KeyError as KE:
        messagebox.showerror("ERROR","No Available center(s) for the given Pincode and date")
        print (pincode_text_var.get())

# Buttons
search_vaccine_btn = Button(app,text='Find', bg= top_right_frame_bg, command = search_vaccine_avl, relief= RAISED)
search_vaccine_btn.place(x = 600,y = 25)

update_clock()

app.mainloop()
