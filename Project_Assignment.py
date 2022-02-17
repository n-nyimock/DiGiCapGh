from tkinter import *
from csv import writer

GUI = Tk()
GUI.title("My GUI Assignment")
GUI.geometry("500x500")

Label(GUI, text="My GUI Assignment", font=("New Times Roman", 20, "bold")).pack()
Label(GUI, text="Project Name", font=("New Times Roman", 16)).place(x=15, y=50)
Label(GUI, text="Start Date", font=("New Times Roman", 16)).place(x=15, y=100)
Label(GUI, text="Finish Date", font=("New Times Roman", 16)).place(x=15, y=150)
Label(GUI, text="Project Expenses", font=("New Times Roman", 16)).place(x=15, y=200)


project_name = Entry(GUI, width=25)
start_date = Entry(GUI, width=25)
finish_date = Entry(GUI, width=25)
project_expenses = Entry(GUI, width=25)


project_name.place(x=190, y=50)
start_date.place(x=190, y=100)
finish_date.place(x=190, y=150)
project_expenses.place(x=190, y=200)

button1 = Button(GUI, text='Submit Your Project', fg='white', bg='blue', command='register', font=('arial', 12, 'bold'))
button1.place(x=190, y=250)




new_list = []


def clear_text():
    project_name.delete(0, END)
    start_date.delete(0, END)
    finish_date.delete(0, END)
    project_expenses.delete(0, END)


def save(a_list):
    with open('project.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(a_list)

        def register():
            global new_list
            element1 = project_name.get()
            element2 = start_date.get()
            element3 = finish_date.get()
            element4 = project_expenses.get()

            new_list = [element1, element2, element3, element4]
            save(new_list)
            clear_text()
            register()


GUI.mainloop()
