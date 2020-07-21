from tkinter import *
from time import sleep
import tkinter.messagebox

class TicTacToe(Tk):

    def __init__(self, *args, **kwargs):
        #Tk.__init__(self, *args, **kwargs)
        self.root = Tk()
        self.root.title("Tic Tac Toe")
        #self.root.withdraw()
        self.bclick = True
        self.flag = 0
        self.btn_nr = -1
        self.btns = []

        self.exit_button = Button(text='Exit Game',height =2, width=15, bg = "grey", command=self.root.destroy)
        self.exit_button.grid(row=4, column=3, columnspan=15)

        self.restart_button = Button(text="Restart Game", height=2, width=15,bg = "grey", command=self.restart)
        self.restart_button.grid(row=4, column=1, columnspan=1)
        
        self.play_game()

    
        

    def action(self, button):
        self.bclick
        self.flag
        if self.btns[button].cget('text') == ' ' and self.bclick:
            self.btns[button].configure(text='X')
            self.bclick = False
            self.flag +=1

        elif self.btns[button].cget('text') == ' ':
            self.btns[button].configure(text='O')
            self.bclick = True
            self.flag +=1
        
        else:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

        
        if self.flag>=5:
            self.evaluate()


    def disableButton(self):
        for i in self.btns:
            i.configure(state=DISABLED)



    def evaluate(self):
        if (self.btns[0].cget('text') == 'X' and self.btns[1].cget('text') == 'X' and self.btns[2].cget('text') == 'X' or
            self.btns[3].cget('text') == 'X' and self.btns[4].cget('text') == 'X' and self.btns[5].cget('text') == 'X' or
            self.btns[6].cget('text') == 'X' and self.btns[7].cget('text') == 'X' and self.btns[8].cget('text') == 'X' or

            self.btns[0].cget('text') == 'X' and self.btns[3].cget('text') == 'X' and self.btns[6].cget('text') == 'X' or
            self.btns[1].cget('text') == 'X' and self.btns[4].cget('text') == 'X' and self.btns[7].cget('text') == 'X' or
            self.btns[2].cget('text') == 'X' and self.btns[5].cget('text') == 'X' and self.btns[8].cget('text') == 'X' or

            self.btns[0].cget('text') == 'X' and self.btns[4].cget('text') == 'X' and self.btns[8].cget('text') == 'X' or
            self.btns[2].cget('text') == 'X' and self.btns[4].cget('text') == 'X' and self.btns[6].cget('text') == 'X'  ):

            self.disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe","Player 1 wins!")
        
        elif self.flag==8:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        
        elif (self.btns[0].cget('text') == 'O' and self.btns[1].cget('text') == '0' and self.btns[2].cget('text') == 'O' or
            self.btns[3].cget('text') == 'O' and self.btns[4].cget('text') == 'O' and self.btns[5].cget('text') == 'O' or
            self.btns[6].cget('text') == 'O' and self.btns[7].cget('text') == 'O' and self.btns[8].cget('text') == 'O' or

            self.btns[0].cget('text') == 'O' and self.btns[3].cget('text') == 'O' and self.btns[6].cget('text') == 'O' or
            self.btns[1].cget('text') == 'O' and self.btns[4].cget('text') == 'O' and self.btns[7].cget('text') == 'O' or
            self.btns[2].cget('text') == 'O' and self.btns[5].cget('text') == 'O' and self.btns[8].cget('text') == 'O' or

            self.btns[0].cget('text') == 'O' and self.btns[4].cget('text') == 'O' and self.btns[8].cget('text') == 'O' or
            self.btns[2].cget('text') == 'O' and self.btns[4].cget('text') == 'O' and self.btns[6].cget('text') == 'O' ):

            self.disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player 2 wins!")
            
        

    def restart(self):
        self.btns, self.btn_nr, self.bclick, self.flag
        self.btn_nr=-1
        self.bclick=True
        self.flag=0
        for x in self.btns:
            x.configure(text=' ')
        
        self.play_game()





    def play_game(self):
        self.btn_nr, self.btns, self.bclick, self.flag
        self.btns.clear()

        for x in range(1, 4):

            for y in range(1, 4):

                self.btn_nr += 1

                self.btns.append(Button(text=' ', height = 5, width = 15, bg = "#6ef49a", command=lambda x=self.btn_nr: self.action(x)))
                self.btns[self.btn_nr].grid(row=x, column=y)

        
    

if __name__ == "__main__":
    app = TicTacToe()    
    app.root.mainloop()



        