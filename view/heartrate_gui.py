from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from model import queue
from model.map import MapMeeker as map

root = Tk()
root.title("Heart Rate Entry")

# global variables
date = ''
dates_entered_list = []
success_label = Label(root)
LOW_RATE_WARNING = 60
HIGH_RESTING_RATE = 100
age = ''
sorted_queue = queue.Queue()

"""Widgets"""
# date entry widget using tkcalendar

cal = Calendar(root, selectmode="day")
cal.grid(row=0, column=1)
date_label = Label(root, text="Enter the Date")
date_label.grid(row=0, column=0)

# resting rate entry
resting_entry = Entry(root)
resting_entry.grid(row=1, column=1)
resting_label = Label(root, text="Enter Resting Heart Rate")
resting_label.grid(row=1, column=0)

# active rate entry
active_entry = Entry(root)
active_entry.grid(row=2, column=1)
active_label = Label(root, text="Enter Active Heart Rate")
active_label.grid(row=2, column=0)

# age entry
age_entry = Entry(root)
age_entry.grid(row=3, column=1)
age_label = Label(root, text="Enter Your Age")
age_label.grid(row=3, column=0)


def grab_date():
    """
    This function gets the date from the calendar
    :return: string
    """
    global date
    date = cal.get_date()
    return date


def get_max_heart_rate(age):
    """
    This function uses the formula for calculating maximum heart rate
    :param age: required
    :return: int
    """
    max_hr = 220-int(age)
    return max_hr


def highest_rate(queue):
    """
    This function will find the highest heart rate of whichever queue is passed into it
    :param queue: required
    :return: int
    """
    global dates_entered_list
    highest_heart_rate = 0
    for i in range(len(dates_entered_list)):
        current_map_object = queue.items[i]
        heart_rate_of_date = current_map_object.find_value_of_key(dates_entered_list[i])
        if int(float(heart_rate_of_date)) > highest_heart_rate:
            highest_heart_rate = int(float(heart_rate_of_date))
    return highest_heart_rate


def lowest_rate(queue):
    """
    This function will find the lowest heart rate of a given queue
    :param queue: required
    :return: int
    """
    global dates_entered_list
    global age
    lowest_rate = get_max_heart_rate(age)
    for i in range(len(dates_entered_list)):
        current_map_object = queue.items[i]
        heart_rate_of_date = current_map_object.find_value_of_key(dates_entered_list[i])
        if int(float(heart_rate_of_date)) < lowest_rate:
            lowest_rate = int(float(heart_rate_of_date))
    return lowest_rate


def sort_lowest_to_highest(input_queue):
    """
    This function will sort a queue using selection sort by heart rate from lowest to highest.
    It will maintain the associated date with each heart rate.
    :param input_queue: required
    :return: queue object
    """
    global dates_entered_list
    sorted_queue = queue.Queue()
    list_of_heart_rates = []
    # get a list of all heart rates from the map objects
    for i in range(len(dates_entered_list)):
        current_map_object = input_queue.items[i]
        heart_rate_of_date = current_map_object.find_value_of_key(dates_entered_list[i])
        list_of_heart_rates.append(heart_rate_of_date)
    # do a selection sort on the list of heart rates
    for i in range(len(dates_entered_list)):
        min_value = i
        for j in range(i+1, len(dates_entered_list)):
            if list_of_heart_rates[min_value] > list_of_heart_rates[j]:
                min_value = j
        list_of_heart_rates[i], list_of_heart_rates[min_value] = list_of_heart_rates[min_value], list_of_heart_rates[i]
    # Build the sorted queue of map objects from the sorted list of heart rates
    for i in range(len(dates_entered_list)):
        for j in range(len(dates_entered_list)):
            if input_queue.items[j].find_value_of_key(dates_entered_list[j]) == list_of_heart_rates[i]:
                sorted_queue.enqueue(input_queue.items[j])
    return sorted_queue


def submit_click():
    """
    This function grabs all the data in the fields and validates it
    :return:
    """
    # import global variables
    global LOW_RATE_WARNING
    global HIGH_RESTING_RATE
    global age
    global dates_entered_list

    # clear success output
    global success_label
    success_label.destroy()

    # Ready a new success output
    success_label = Label(root)
    success_label.grid(row=5, column=0)

    # get date from calendar
    date = grab_date()

    # add date to global dates entered list for use in validation step
    if date not in dates_entered_list:
        dates_entered_list.append(date)
    else:
        messagebox.showwarning("Date Warning", "Date already used.")
        success_label.config(text="Entry Not Successful")
        return

    # get max heart rate
    age = age_entry.get()
    if age.strip() == "" or int(float(age)) < 0 or int(float(age)) > 125:
        messagebox.showwarning("Age Error", "Not a valid age")
        dates_entered_list.remove(date)
        success_label.config(text="Entry Not Successful")
        return
    if 0 < int(float(age)) <= 125:
        max_heart_rate = get_max_heart_rate(age)

    # create instances of resting and active rate maps
    resting_map = map()
    active_map = map()

    # read entry's for rate
    resting_rate = resting_entry.get()
    active_rate = active_entry.get()

    # validate heart rate entries
    if resting_rate.strip() == "" or active_rate.strip() == "":
        messagebox.showwarning("Heart Rate Entry Error", "Heart Rate can't be blank")
        dates_entered_list.remove(date)
        success_label.config(text="Entry Not Successful")
        return
    if int(float(resting_rate)) < 0 or int(float(active_rate)) < 0:
        messagebox.showwarning("Heart Rate Entry Error", "Heart Rate Can't Be Negative!")
        dates_entered_list.remove(date)
        success_label.config(text="Entry Not Successful")
        return
    if int(float(resting_rate)) > int(float(active_rate)):
        messagebox.showwarning("Heart Rate Entry Error", "Resting Rate Should Be Lower Than Active Rate!")
        dates_entered_list.remove(date)
        success_label.config(text="Entry Not Successful")
        return
    if int(float(resting_rate)) <= LOW_RATE_WARNING:
        messagebox.showwarning("Low Rate Warning", "Heart Rate is Low.")
    if int(float(resting_rate)) >= HIGH_RESTING_RATE:
        messagebox.showwarning("High Rate Warning", "Resting Heart Rate is Elevated")
    if int(float(active_rate)) >= max_heart_rate:
        messagebox.showwarning("High Rate Warning", "Active Heart Rate Dangerously High")

    # insert info into map
    resting_map.insert(date, resting_rate)
    active_map.insert(date, active_rate)

    # insert map into queue
    active_rate_queue.enqueue(active_map)
    resting_rate_queue.enqueue(resting_map)

    # clear heart rate entry fields
    resting_entry.delete(0, END)
    active_entry.delete(0, END)

    # indicate success
    success_label.config(text="Entry Successful")

    # copy queue to pass to highest_rate function
    copy_active_queue = active_rate_queue

    # create sorted queues
    sorted_resting_queue = sort_lowest_to_highest(resting_rate_queue)
    sorted_active_queue = sort_lowest_to_highest(active_rate_queue)

    output_label_lr = Label(root, text="Lowest Resting:  " + str(lowest_rate(resting_rate_queue)))
    output_label_lr.grid(row=5, column=1)

    output_label_ha = Label(root, text="Highest Active:  " + str(highest_rate(copy_active_queue)))
    output_label_ha.grid(row=6, column=1)

    output_label_ar = Label(root, text="Active Rates:  " + str(active_rate_queue.print_queue()))
    output_label_ar.grid(row=7, column=0)

    output_label_rr = Label(root, text="Resting Rates:  " + str(resting_rate_queue.print_queue()))
    output_label_rr.grid(row=8, column=0)

    output_label_sar = Label(root, text="Lowest-to-Highest Active Rates:  " + str(sorted_active_queue.print_queue()))
    output_label_sar.grid(row=7, column=1)

    output_label_srr = Label(root, text="Lowest-to-Highest Resting Rates:  " + str(sorted_resting_queue.print_queue()))
    output_label_srr.grid(row=8, column=1)


submit_button = Button(root, text="Submit Entry!", padx=50, command=submit_click)
submit_button.grid(row=4, columnspan=2)

resting_rate_queue = queue.Queue()
active_rate_queue = queue.Queue()

root.mainloop()
