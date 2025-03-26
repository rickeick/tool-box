from tkinter import Tk, Label, Listbox, Text
from tkinter.messagebox import showerror
from os import listdir

ROOT = '/caminho/para/raiz'

def list_dir(path):
	dirs = list()
	files = list()
	for item in listdir(path):
		if item[0] == '.': continue
		elif '.' in item: files.append(item)
		else: dirs.append(item)
	dirs.sort(); files.sort()
	return dirs + files


class App:
	def __init__(self):
		self.path = ROOT
		self.contents = str()
		self.selected = str()
		self.master = Tk()
		self.master.title('Viewer File')
		self.master.resizable(width=False,height=False)
		self.infor = Label(self.master)
		self.infor.configure(width=90)
		self.infor.configure(text=ROOT)
		self.infor.configure(relief='groove')
		self.infor.configure(font='arial 12')
		self.infor.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
		self.explorer = Listbox(self.master)
		self.explorer.configure(height=24)
		self.explorer.configure(relief='solid')
		self.explorer.configure(font='arial 12')
		self.explorer.configure(selectmode='single')
		self.explorer.bind('<Control-w>', self.clear)
		self.explorer.bind('<Double-Button-1>', self.main)
		self.explorer.grid(row=2, column=1, padx=5, pady=5)
		for item in list_dir(ROOT): self.explorer.insert('end', item)
		self.editor = Text(self.master)
		self.editor.configure(tabs=True)
		self.editor.configure(width=70)
		self.editor.configure(height=25)
		self.editor.configure(relief='solid')
		self.editor.configure(font='arial 12')
		self.editor.bind('<Control-w>', self.clear)
		self.editor.grid(row=2, column=2, padx=5, pady=5)
		self.master.mainloop()

	def main(self, _):
		try:
			index = self.explorer.curselection()[0]
			self.selected = self.explorer.get(index)
			if self.selected == '..': self.back()
			elif '.' in self.selected: self.open_file()
			else: self.open_dir()
		except IndexError:
			pass

	def open_file(self):
		try:
			self.file = f'{self.path}/{self.selected}'
			self.editor.delete('1.0', 'end')
			with open(self.file, mode='r') as file:
				for line in file: self.editor.insert('end', line)
		except UnicodeDecodeError:
			showerror('Error!', 'Não Foi Possível Decodificar o Arquivo!')

	def open_dir(self):
		try:
			list_dir(f'{self.path}/{self.selected}')
		except NotADirectoryError:
			self.open_file()
		else:
			self.path += f'/{self.selected}'
			self.contents = list_dir(self.path)
			self.infor.configure(text=self.path)
			self.explorer.delete(0, 'end')
			for item in self.contents:
				self.explorer.insert('end', item)
			if self.path != ROOT:
				self.explorer.insert('end', '..')

	def back(self):
		self.path = self.path.split('/')[:-1]
		self.path = '/'.join(self.path)
		self.infor.configure(text=self.path)
		self.explorer.delete(0, 'end')
		for item in list_dir(self.path):
			self.explorer.insert('end', item)
		self.selected = self.path.split('/').pop()
		if self.path != ROOT:
			self.explorer.insert('end', '..')

	def clear(self, _): self.editor.delete('1.0', 'end')


if __name__ == '__main__': App()
