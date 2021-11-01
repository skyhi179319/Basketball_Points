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

class PointsTableList:
    PG = Player("Skyler","PG",15,20,18)
    SG = Player("Zane","SG",10,15,12)
    C = Player("David","C",15,17,13)
    PF = Player("Carson","PF",15,13,17)
    SF = Player("Ethan","SF",17,15,17)
    def returnList():
        Game1 = functions.returnGame1Points(PointsTableList.PG.returnGame1(),PointsTableList.SG.returnGame1(),PointsTableList.C.returnGame1(),PointsTableList.PF.returnGame1(),PointsTableList.SF.returnGame1())
        Game2 = functions.returnGame2Points(PointsTableList.PG.returnGame2(),PointsTableList.SG.returnGame2(),PointsTableList.C.returnGame2(),PointsTableList.PF.returnGame2(),PointsTableList.SF.returnGame2())
        Game3 = functions.returnGame3Points(PointsTableList.PG.returnGame3(),PointsTableList.SG.returnGame3(),PointsTableList.C.returnGame3(),PointsTableList.PF.returnGame3(),PointsTableList.SF.returnGame3())
        Total = functions.returnAllPoints(PointsTableList.PG.returnPoints(),PointsTableList.SG.returnPoints(),PointsTableList.C.returnPoints(),PointsTableList.PF.returnPoints(),PointsTableList.SF.returnPoints())
        AVG = functions.returnAvg(Total)
        list = [("Name:","POS:","Game 1:","Game 2:","Game 3:","Total Points:"),
                (PointsTableList.PG.returnName(),PointsTableList.PG.returnPos(),PointsTableList.PG.returnGame1(),PointsTableList.PG.returnGame2(),PointsTableList.PG.returnGame3(),PointsTableList.PG.returnPoints()),
                (PointsTableList.SG.returnName(),PointsTableList.SG.returnPos(),PointsTableList.SG.returnGame1(),PointsTableList.SG.returnGame2(),PointsTableList.SG.returnGame3(),PointsTableList.SG.returnPoints()),
                (PointsTableList.C.returnName(),PointsTableList.C.returnPos(),PointsTableList.C.returnGame1(),PointsTableList.C.returnGame2(),PointsTableList.C.returnGame3(),PointsTableList.C.returnPoints()),
                (PointsTableList.PF.returnName(),PointsTableList.PF.returnPos(),PointsTableList.PF.returnGame1(),PointsTableList.PF.returnGame2(),PointsTableList.PF.returnGame3(),PointsTableList.PF.returnPoints()),
                (PointsTableList.SF.returnName(),PointsTableList.SF.returnPos(),PointsTableList.SF.returnGame1(),PointsTableList.SF.returnGame2(),PointsTableList.SF.returnGame3(),PointsTableList.SF.returnPoints()),
                ("","Totals:",Game1,Game2,Game3,Total),
                ("","AVG:","","","",AVG),
                ]
        return list
 
class PointsTable:
    def __init__(self,root):
        # code for creating table
        fontColor = "blue"
        for i in range(PointsGUI.total_rows):
            for j in range(PointsGUI.total_columns):
                  
                self.e = Entry(root, width=15, fg=fontColor,
                               font=('Arial',16,'bold'))
                  
                self.e.grid(row=i, column=j)
                self.e.insert(END, PointsGUI.lst[i][j])

class PointsGUI:
    lst = PointsTableList.returnList()
    total_rows = len(lst)
    total_columns = len(lst[0])
    def __init__(self):
        root = Tk()
        root.title("Points By Starting Players")
        t = PointsTable(root)
        root.mainloop()
class MainGUI:
    def __init__(self):
        root = Tk()
        root.title("Options")
        root.geometry("500x200")
        menubar = Menu(root)
        Options = Menu(menubar, tearoff=0)
        Options.add_command(label="Points", command=PointsGUI)
        menubar.add_cascade(label="Options", menu=Options)
        root.config(menu=menubar)
        root.mainloop()
MainGUI()