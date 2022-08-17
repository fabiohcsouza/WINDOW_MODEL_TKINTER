import tkinter as tk
from tkinter import ttk, messagebox


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
        #self.geometry('500x300') # Size of the window
        #self.iconbitmap('scr\icon.ico') # Icon of the window
        
        self.configure(bg=color_dark_gray1)

        #######################################################################
        # Create bar Menu
        #######################################################################
        parameter_menu = {
            'File': {'Open': lambda: self.pp('Open'), 'Save': lambda: self.pp('Save'), '-': None ,'Exit': lambda: self.quit},
            'Edit': {'Copy': lambda: self.pp('Copy'), 'Paste': lambda: self.pp('Paste'), 'Undo': lambda: self.pp('Undo')},
            'Help': {'About': lambda: self.pp('Abot'), 'Update': lambda: self.pp('Update')}
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

    def pp(self, text):
        print(text)
        messagebox.showinfo('Info', text)

if __name__ == '__main__':
    app = App()
    app.mainloop()

    
                

