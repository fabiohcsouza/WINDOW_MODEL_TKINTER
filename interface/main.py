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
        #self.geometry('300x200+800+300') # Size of the window
        #self.iconbitmap('scr\icon.ico') # Icon of the window
        
        self.configure(bg=color_dark_gray1)

        #######################################################################
        # Create bar Menu
        #######################################################################
        parameter_menu = {
            'File': {'Open': lambda: self.open('Open'), 'Save': lambda: self.save('Save'), '-': None ,'Exit': lambda: self.exit()},
            'Edit': {'Copy': lambda: self.copy('Copy'), 'Paste': lambda: self.paste('Paste'), 'Undo': lambda: self.undo('Undo')},
            'Settings': {'Preferences': lambda: self.pp('Preferences'), 'Style': lambda: self.pp('Style'), '-': None},
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

    def window(self):
        window = tk.Toplevel(self)
        window.resizable(width=False, height=False)
        window.geometry('300x200+800+300')
        window.configure(bg=color_dark_gray1)
        window.transient(self)#
        window.focus_force()#
        window.grab_set()#
        tk.Button(window, text='Close', command=window.destroy, bg=color_dark_gray3, fg=color_dark_gray5, font=('Arial', 11), bd=0).pack(side=tk.BOTTOM, fill=tk.X, expand=True)

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

    def about(self, window):
        window.title('About')
        
        var_version = '1.0'
        var_author = 'Fabio Souza'
        var_email = 'fabio.souza@pm.me'
        var_website = 'https://github.com/fabiohcsouza/'

        lbl_version = tk.Label(window, text='Version: '+var_version, bg=color_dark_gray1, fg=color_dark_gray5, font=('Arial', 12))
        lbl_version.pack(pady=10)

        lbl_author = tk.Label(window, text='Author: '+var_author, bg=color_dark_gray1, fg=color_dark_gray5, font=('Arial', 12))
        lbl_author.pack(pady=5)

        lbl_email = tk.Label(window, text='E-mail: '+var_email, bg=color_dark_gray1, fg=color_dark_gray5, font=('Arial', 12))
        lbl_email.pack(pady=5)

        lbl_website = tk.Label(window, text='Website: '+var_website, bg=color_dark_gray1, fg=color_dark_gray5, font=('Arial', 12))
        lbl_website.pack(pady=5)

        lbl_website.bind('<Button-1>', lambda event: webbrowser.open('https://github.com/fabiohcsouza'))

    def update(self):
        webbrowser.open('https://github.com/fabiohcsouza/WINDOW_MODEL_TKINTER')

if __name__ == '__main__':
    app = App()
    app.mainloop()
    #

    
                

