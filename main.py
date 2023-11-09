import tkinter as tk


def red_color():
    my_window['bg'] = 'red'


def green_color():
    my_window['bg'] = 'green'


def blue_color():
    my_window['bg'] = 'blue'


# my_window = tk.Tk()
# my_menu = tk.Menu(my_window)
# my_menu.add_command(label='Red', command=red_color)
# my_menu.add_command(label='Green', command=green_color)
# my_menu.add_command(label='Blue', command=blue_color)
# my_window.config(menu=my_menu)

my_window = tk.Tk()
my_menubar = tk.Menu(my_window)
my_dropdown_menu = tk.Menu(my_menubar)
my_dropdown_menu.add_command(label='Red', command=red_color)
my_dropdown_menu.add_command(label='Green', command=green_color)
my_dropdown_menu.add_command(label='Blue', command=blue_color)
my_menubar.add_cascade(label='Color', menu=my_dropdown_menu)
my_window.config(menu=my_menubar)
my_window.mainloop()