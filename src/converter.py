import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import pandas as pd

__auther__ = 'Florin Dorcu'
__email__ = 'florin.dorcu@gmail.com'
__maintainer__ = __auther__

__all__ = []





class FileConversion:
    def __init__(self, file_path):
        self.file_path = file_path
        self.ext = os.path.splitext(self.file_path)[1]

    def text_to_csv(self):
        pass

    def csv_to_xlsx(self):
        df = pd.read_csv(self.file_path)
        df.to_excel(self.file_path.replace(self.ext, '.xlsx'), index=False)

class ConverterGUI(tk.Frame):
    def __init__(self, master, color):
        super().__init__()
        self.filename = None
        self.path = None
        self.master = master
        self.configure(bg=color, width=500, height=500)
        self.grid(row=0, column=0)
        self.label_file_explorer = tk.Label(self, text='Choose file', width=10, height=2,
                                            bg=color, fg='white', font=('Arial', 14))
        self.label_file_explorer.grid(row=0, column=0)
        self.label_file_type = tk.Label(self, text='File type', width=10, height=2,
                                            bg=color, fg='white', font=('Arial', 14))
        self.label_file_type.grid(row=0, column=1)

        self.button_explorer = tk.Button(self, text='Button Explorer',
                                         bg='red', fg='blue', command=self._browse_files)
        self.button_explorer.grid(row=1, column=0)

        self.list_box = tk.Listbox(self)
        self.list_box.grid(row=1, column=1)
        self.list_box.insert(1, '.csv')
        self.list_box.insert(2, '.txt')
        self.list_box.insert(3, '.xlsx')
        self.list_box.selection_set(0)
        self.grid_propagate(False)

        self.button_convert = tk.Button(self, text='Convert',
                                         bg='red', fg='blue', command=self._convert)
        self.button_convert.grid(row=2, column=1, padx=10, pady=10)

    def _browse_files(self):
        self.path = filedialog.askopenfilename(initialdir='/', title='Select a file')
        # self.path =
        self.filename = self.path[self.path.rfind('/')::]
        self.label_file_explorer.configure(width=len(self.filename), text=self.filename)
        print(self.filename)

    def _get_extension(self):
        selection = {
            0: '.csv',
            1: '.txt',
            2: '.xlsx'
        }

        try:
            return selection[self.list_box.curselection()[0]]
        except IndexError:
            messagebox.showerror(message='Please select an option!')
    def _convert(self):
        if not self.path:
            messagebox.showerror(message='Please select a file!')
        else:
            selected_ext = self._get_extension()
            file = FileConversion(self.path)
            try:
                result = _get_method(file, (file.ext, selected_ext))
                print(result)
                # result()
                messagebox.showinfo(message='Conversion successfully done!')
            except KeyError:
                messagebox.showerror(message='Conversion not successfully done!')
            print(self.path)
            print(selected_ext)

def _get_method(obj: FileConversion, ext_pair):

    file_type = {
        ('.csv', '.xlsx'): obj.csv_to_xlsx()
    }
    return file_type[ext_pair]

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('500x300')
    cvt = ConverterGUI(root, 'purple')

    root.mainloop()