from tkinter import Label,Tk,Button,messagebox,DISABLED,NORMAL
import random as r
import sys

class TicTacToe:

	def __init__(self):
		self.player = r.choice(['O','X'])
		self.board = [[],[],[]]
		self.root = Tk()
		self.root.title("Unbeatable Tic-Tac-Toe")
		self.color={'O':'blue','X':'red'}


	def run(self):

		for i in range(3):
			for j in range(3):
				self.board[i].append(self.button(self.root))
				self.board[i][j].config(command = lambda row=i,col=j:self.click(row,col))
				self.board[i][j].grid(row=i,column=j)

		self.label = Label(text=self.player+"'s turn",font=('arial',20,'bold'))
		self.label.grid(row=3,column=0,columnspan=3)
		self.root.mainloop()

	def button(self,frame):

		b = Button(frame,padx=1,bg="white",width=3,text="",font=('arial',60,'bold'),relief='sunken',bd=10)
		return b

	def change_turn(self):
		
		for i in ['O','X']:
			if i != self.player:
				self.player=i
				break


	def all_equal(self,line):

		return len(set(line)) == 1


	def is_tie(self):
		elements = []

		for i in range(3):
			for j in range(3):
				elements.append(self.board[i][j]['state'])

		if (self.all_equal(elements) and elements[0]==DISABLED):
			return True
		return False


	def check_win(self):
		main_diagonal = []
		secondary_diagonal = []
		lines = []
		cols = []

		for i in range(3):
			
			line = []
			
			for j in range(3):
				line.append(self.board[i][j]['text'].strip())    

				if i==j:
					main_diagonal.append(self.board[i][j]['text'].strip())

				if i+j == 2:
					secondary_diagonal.append(self.board[i][j]['text'].strip())
			
			lines.append(line)
		
		cols = map(list,zip(*lines))

		# check diagonal win
		if (self.all_equal(main_diagonal) and main_diagonal[0] != '') or (self.all_equal(secondary_diagonal) and secondary_diagonal[0] != ''):
			return True                
		
		# check row win
		for line in lines:
			if (self.all_equal(line) and line[0] != ''):
				return True
		
		# check column win
		for col in cols:
			if (self.all_equal(col) and col[0] != ''):
				return True

		return False



	def check_board(self):

		if self.is_tie():
			messagebox.showinfo("Match tied.")
			self.reset()

		if self.check_win():
			messagebox.showinfo("{} has won.".format(self.player))
			self.reset()

	def reset(self):
		for i in range(3):
			for j in range(3):
				self.board[i][j]["text"] = ""
				self.board[i][j]["state"] = NORMAL
		self.player=r.choice(['O','X'])


	def click(self,row,col):
		self.board[row][col].config(text=self.player,state=DISABLED,disabledforeground=self.color[self.player])
		self.check_board()
		self.change_turn()
		self.label.config(text=self.player+"'s turn")


