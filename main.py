from tkinter import *
import math
  
class Player:
    def __init__(self, name, pos, game1,game2,game3):
        self.name = name
        self.pos = pos
        self.game_1 = game1
        self.game_2 = game2
        self.game_3 = game3
    def returnName(self):
        return self.name
    def returnPos(self):
        return self.pos
    def returnGame1(self):
        return self.game_1
    def returnGame2(self):
        return self.game_2
    def returnGame3(self):
        return self.game_3
    def returnPoints(self):
        points = self.game_1 + self.game_2 + self.game_3
        return points
class functions:
    def returnGame1Points(Player1,Player2,Player3,Player4,Player5):
        points = Player1 + Player2 + Player3 + Player4 + Player5
        return points
    def returnGame2Points(Player1,Player2,Player3,Player4,Player5):
        points = Player1 + Player2 + Player3 + Player4 + Player5
        return points
    def returnGame3Points(Player1,Player2,Player3,Player4,Player5):
        points = Player1 + Player2 + Player3 + Player4 + Player5
        return points
    def returnAllPoints(Player1,Player2,Player3,Player4,Player5):
        points = Player1 + Player2 + Player3 + Player4 + Player5
        return points
    def returnAvg(totalPoints):
        points = totalPoints / 3
        return round(points, 3)
class TableList:
    def returnList():
        PG = Player("Skyler","PG",15,20,18)
        SG = Player("Zane","SG",10,15,12)
        C = Player("David","C",15,17,13)
        PF = Player("Carson","PF",15,13,17)
        SF = Player("Ethan","SF",17,15,17)
        Game1 = functions.returnGame1Points(PG.returnGame1(),SG.returnGame1(),C.returnGame1(),PF.returnGame1(),SF.returnGame1())
        Game2 = functions.returnGame2Points(PG.returnGame2(),SG.returnGame2(),C.returnGame2(),PF.returnGame2(),SF.returnGame2())
        Game3 = functions.returnGame3Points(PG.returnGame3(),SG.returnGame3(),C.returnGame3(),PF.returnGame3(),SF.returnGame3())
        Total = functions.returnAllPoints(PG.returnPoints(),SG.returnPoints(),C.returnPoints(),PF.returnPoints(),SF.returnPoints())
        AVG = functions.returnAvg(Total)
        list = [(PG.returnName(),PG.returnPos(),PG.returnGame1(),PG.returnGame2(),PG.returnGame3(),PG.returnPoints()),
                (SG.returnName(),SG.returnPos(),SG.returnGame1(),SG.returnGame2(),SG.returnGame3(),SG.returnPoints()),
                (C.returnName(),C.returnPos(),C.returnGame1(),C.returnGame2(),C.returnGame3(),C.returnPoints()),
                (PF.returnName(),PF.returnPos(),PF.returnGame1(),PF.returnGame2(),PF.returnGame3(),PF.returnPoints()),
                (SF.returnName(),SF.returnPos(),SF.returnGame1(),SF.returnGame2(),SF.returnGame3(),SF.returnPoints()),
                ("","Totals:",Game1,Game2,Game3,Total),
                ("","AVG:","","","",AVG),
                ]
        return list  
class Table:
      
    def __init__(self,root):
          
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                  
                self.e = Entry(root, width=15, fg='blue',
                               font=('Arial',16,'bold'))
                  
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
  
# take the data
lst = TableList.returnList()
   
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
   
# create root window
root = Tk()
root.title("Points By Starting Players")
t = Table(root)
root.mainloop()