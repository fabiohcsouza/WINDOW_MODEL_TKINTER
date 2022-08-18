import tkinter as tk
from tkinter import ttk, messagebox, dialog
import webbrowser

color_dark_gray1 = '#2e2e2e'
color_dark_gray2 = '#333333'
color_dark_gray3 = '#4d4d4d'
color_dark_gray4 = '#cccccc'
color_dark_gray5 = '#e6e6e6'
color_dark_gray6 = '#fafafa'


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.title('App') # Title of the window
        self.resizable(width=False, height=False) # Disable resizing the window
        self.geometry('600x400+700+200') # Size of the window
        #self.iconbitmap('img\icon.ico') # Icon of the window
        
        self.configure(bg=color_dark_gray1)

        ########################################################################
        # Variables
        self.selected_theme = tk.StringVar()

        #######################################################################
        # Create bar Menu
        #######################################################################
        parameter_menu = {
            'File': {'Open': lambda: self.open('Open'), 'Save': lambda: self.save('Save'), '-': None ,'Exit': lambda: self.exit()},
            'Edit': {'Copy': lambda: self.copy('Copy'), 'Paste': lambda: self.paste('Paste'), 'Undo': lambda: self.undo('Undo')},
            'Settings': {'Preferences': lambda: self.preferences(self.window()), 'Style': lambda: self.charge_style(self.window()), '-': None},
            'Help': {'About': lambda: self.about(self.window()), 'Update': lambda: self.update()}
        }
    
        menu = tk.Menu(self)
        self.config(menu=menu)

        for key, value in parameter_menu.items():
            menu_item = tk.Menu(menu, tearoff=0)
            menu.add_cascade(label=key, menu=menu_item)
            for label, command in value.items():
                if label == '-':
                    menu_item.add_separator()
                else: 
                    menu_item.add_command(label=label, command=command)    


        #######################################################################
        ttk.Button(self, text='Exit', command=self.exit).pack(side=tk.LEFT, expand=True)

        self.style = ttk.Style()
        self.style.configure('TFrame', foreground=color_dark_gray5, background=color_dark_gray3)
        self.style.configure('TLabel', foreground=color_dark_gray5, background=color_dark_gray3)
        self.style.configure('TLabelFrame', foreground=color_dark_gray5, background=color_dark_gray3, relief=tk.SUNKEN)
        self.style.configure('TButton', backgroundcolor=color_dark_gray3, borderwidth=0, font=('Arial', 11))
        self.style.configure('TRadiobutton', foreground=color_dark_gray5, background=color_dark_gray3)

        #######################################################################

    def window(self):
        window = tk.Toplevel(self)
        window.resizable(width=False, height=False)
        window.geometry('400x200+800+300')
        window.configure(bg=color_dark_gray2)
        window.transient(self)#
        window.focus_force()#
        window.grab_set()#
        ttk.Button(window, text='Close', command=window.destroy).pack(side=tk.BOTTOM, expand=True)

        return window

    def pp(self, text):
        messagebox.showinfo('Info', text)


    def open(self, text):
        self.pp(text)

    def save(self, text):
        self.pp(text)

    def exit(self):
        self.destroy()

    def copy(self, text):
        self.pp(text)

    def paste(self, text):
        self.pp(text)

    def undo(self, text):
        self.pp(text)

    def preferences(self, window):
        self.pp('Preferences')


    def charge_style(self, window):
        # radio button
        theme_frame = ttk.LabelFrame(window, text='Themes')
        theme_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        for theme_name in self.style.theme_names():
            rb = ttk.Radiobutton(
                theme_frame,
                text=theme_name,
                value=theme_name,
                variable=self.selected_theme,
                command=self.change_theme)
            rb.pack(expand=True, fill='both')
            

    def about(self, window):
        window.title('About')
        frame = ttk.Frame(window, relief=tk.RIDGE, borderwidth=2) ; frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        var_version = '1.0'
        var_author = 'Fabio Souza'
        var_email = 'fabio.souza@pm.me'
        var_website = 'https://github.com/fabiohcsouza/'

        lbl_version = ttk.Label(frame, text='Version: '+var_version, font=('Arial', 12))
        lbl_version.pack(pady=10)

        lbl_author = ttk.Label(frame, text='Author: '+var_author, font=('Arial', 12))
        lbl_author.pack(pady=5)

        lbl_email = ttk.Label(frame, text='E-mail: '+var_email, font=('Arial', 12))
        lbl_email.pack(pady=5)

        lbl_website = ttk.Label(frame, text='Website: '+var_website, font=('Arial', 12))
        lbl_website.pack(pady=5)

        lbl_website.bind('<Button-1>', lambda event: webbrowser.open('https://github.com/fabiohcsouza'))

    def update(self):
        webbrowser.open('https://github.com/fabiohcsouza/WINDOW_MODEL_TKINTER')


    def change_theme(self):
        self.style.theme_use(self.selected_theme.get())

if __name__ == '__main__':
    app = App()
    app.mainloop()
    #

    
                

