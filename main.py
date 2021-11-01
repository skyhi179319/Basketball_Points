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
    PG = Player("Skyler","PG",15,20,18)
    SG = Player("Zane","SG",10,15,12)
    C = Player("David","C",15,17,13)
    PF = Player("Carson","PF",15,13,17)
    SF = Player("Ethan","SF",17,15,17)
    def returnList():
        Game1 = functions.returnGame1Points(TableList.PG.returnGame1(),TableList.SG.returnGame1(),TableList.C.returnGame1(),TableList.PF.returnGame1(),TableList.SF.returnGame1())
        Game2 = functions.returnGame2Points(TableList.PG.returnGame2(),TableList.SG.returnGame2(),TableList.C.returnGame2(),TableList.PF.returnGame2(),TableList.SF.returnGame2())
        Game3 = functions.returnGame3Points(TableList.PG.returnGame3(),TableList.SG.returnGame3(),TableList.C.returnGame3(),TableList.PF.returnGame3(),TableList.SF.returnGame3())
        Total = functions.returnAllPoints(TableList.PG.returnPoints(),TableList.SG.returnPoints(),TableList.C.returnPoints(),TableList.PF.returnPoints(),TableList.SF.returnPoints())
        AVG = functions.returnAvg(Total)
        list = [("Name:","POS:","Game 1:","Game 2:","Game 3:","Total Points:"),
                (TableList.PG.returnName(),TableList.PG.returnPos(),TableList.PG.returnGame1(),TableList.PG.returnGame2(),TableList.PG.returnGame3(),TableList.PG.returnPoints()),
                (TableList.SG.returnName(),TableList.SG.returnPos(),TableList.SG.returnGame1(),TableList.SG.returnGame2(),TableList.SG.returnGame3(),TableList.SG.returnPoints()),
                (TableList.C.returnName(),TableList.C.returnPos(),TableList.C.returnGame1(),TableList.C.returnGame2(),TableList.C.returnGame3(),TableList.C.returnPoints()),
                (TableList.PF.returnName(),TableList.PF.returnPos(),TableList.PF.returnGame1(),TableList.PF.returnGame2(),TableList.PF.returnGame3(),TableList.PF.returnPoints()),
                (TableList.SF.returnName(),TableList.SF.returnPos(),TableList.SF.returnGame1(),TableList.SF.returnGame2(),TableList.SF.returnGame3(),TableList.SF.returnPoints()),
                ("","Totals:",Game1,Game2,Game3,Total),
                ("","AVG:","","","",AVG),
                ]
        return list
 
class Table:
    def __init__(self,root):
        # code for creating table
        fontColor = "blue"
        for i in range(GUI.total_rows):
            for j in range(GUI.total_columns):
                  
                self.e = Entry(root, width=15, fg=fontColor,
                               font=('Arial',16,'bold'))
                  
                self.e.grid(row=i, column=j)
                self.e.insert(END, GUI.lst[i][j])

class GUI:
    lst = TableList.returnList()
    total_rows = len(lst)
    total_columns = len(lst[0])
    def __init__(self):
        root = Tk()
        root.title("Points By Starting Players")
        t = Table(root)
        root.mainloop()

GUI()