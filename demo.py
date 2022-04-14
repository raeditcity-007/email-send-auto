import tkinter as tk
from tkinter import filedialog
from utils import emails

list_attechment = []

def generate_window(msg, status=False):
    bg = 'green' if status else 'red'
    fg = 'white' if status else 'black'
    window = tk.Tk()
    window.title('STATUS')
    window_label = tk.Label(window, text=msg, height=3,padx=100, bg=bg, fg=fg)
    window_label.pack()
    window.mainloop()


# This Function called when you press Send Email button
def generate_content():
    """Function to send email"""
    msg = emails.generate_email(reciever=email_input.get(),
                                subject=subject_input.get(),
                                content=text_input.get('1.0',tk.END),
                                attechment_list=list_attechment)
    try:
        emails.send_email(msg)
        generate_window('SUCCESS: \nEmail Sent !', 'success')
    except Exception as e:
        generate_window('ERROR: \nPlease enter the correct value !')

def add_attechment():
    global list_attechment
    filename = filedialog.askopenfilename(initialdir='/', title='Select File',filetypes=[('all files','*.*')])
    list_attechment.append(filename)
    generate_window(f'STATUS: \n{", ".join(list_attechment)} Added to Attachment','sucess')

# init tkinter window root
root = tk.Tk()

# create frame for div in root window to place widget in it
canvas = tk.Canvas(root, width=800, height=600, bg='#faebd7')
canvas.pack()
frame = tk.Frame(root, bg='white')
frame.place(relwidth=.8, relheight=.8, relx=.1, rely=.1)

greeting = tk.Label(frame, text='----- EMAIL SENDER -----', height=4, bg='white')
greeting.pack()

# Blank Space
blank = tk.Label(frame, text='', height=2, bg='white')

email = tk.Label(frame, text='Destination: ', height=2, bg='white')
email_input = tk.Entry(frame)
subject = tk.Label(frame, text='Subject: ', height=2, bg='white')
subject_input = tk.Entry(frame)
text = tk.Label(frame, text='Content: ', height=2, bg='white')
text_input = tk.Text(frame, width=50, height=6)
btn_attechment = tk.Button(frame, text='Add Attetchment', padx=10, pady=5, command=add_attechment)
email.pack()
email_input.pack()
subject.pack()
subject_input.pack()
text.pack()
text_input.pack()
btn_attechment.pack()

blank.pack()
# send email button to call generate_email function above
button = tk.Button(frame, text='SEND EMAIL', padx=50, pady=3, bg='#bed0b0', fg='black', command=generate_content)
button.pack()

root.title('Email Sender')
root.resizable(False, False) 
root.mainloop()