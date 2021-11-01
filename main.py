from tkinter import *
import math
  
# Global FUnctions
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

# Steals
class StealsTableList:
    PG = Player("Skyler","PG",3,2,3)
    SG = Player("Zane","SG",1,0,2)
    C = Player("David","C",0,1,2)
    PF = Player("Carson","PF",1,1,1)
    SF = Player("Ethan","SF",1,1,2)
    def returnList():
        Game1 = functions.returnGame1Points(StealsTableList.PG.returnGame1(),StealsTableList.SG.returnGame1(),StealsTableList.C.returnGame1(),StealsTableList.PF.returnGame1(),StealsTableList.SF.returnGame1())
        Game2 = functions.returnGame2Points(StealsTableList.PG.returnGame2(),StealsTableList.SG.returnGame2(),StealsTableList.C.returnGame2(),StealsTableList.PF.returnGame2(),StealsTableList.SF.returnGame2())
        Game3 = functions.returnGame3Points(StealsTableList.PG.returnGame3(),StealsTableList.SG.returnGame3(),StealsTableList.C.returnGame3(),StealsTableList.PF.returnGame3(),StealsTableList.SF.returnGame3())
        Total = functions.returnAllPoints(StealsTableList.PG.returnPoints(),StealsTableList.SG.returnPoints(),StealsTableList.C.returnPoints(),StealsTableList.PF.returnPoints(),StealsTableList.SF.returnPoints())
        AVG = functions.returnAvg(Total)
        list = [("Name:","POS:","Game 1:","Game 2:","Game 3:","Total Steals:"),
                (StealsTableList.PG.returnName(),StealsTableList.PG.returnPos(),StealsTableList.PG.returnGame1(),StealsTableList.PG.returnGame2(),StealsTableList.PG.returnGame3(),StealsTableList.PG.returnPoints()),
                (StealsTableList.SG.returnName(),StealsTableList.SG.returnPos(),StealsTableList.SG.returnGame1(),StealsTableList.SG.returnGame2(),StealsTableList.SG.returnGame3(),StealsTableList.SG.returnPoints()),
                (StealsTableList.C.returnName(),StealsTableList.C.returnPos(),StealsTableList.C.returnGame1(),StealsTableList.C.returnGame2(),StealsTableList.C.returnGame3(),StealsTableList.C.returnPoints()),
                (StealsTableList.PF.returnName(),StealsTableList.PF.returnPos(),StealsTableList.PF.returnGame1(),StealsTableList.PF.returnGame2(),StealsTableList.PF.returnGame3(),StealsTableList.PF.returnPoints()),
                (StealsTableList.SF.returnName(),StealsTableList.SF.returnPos(),StealsTableList.SF.returnGame1(),StealsTableList.SF.returnGame2(),StealsTableList.SF.returnGame3(),StealsTableList.SF.returnPoints()),
                ("","Totals:",Game1,Game2,Game3,Total),
                ("","AVG:","","","",AVG),
                ]
        return list
 
class StealTable:
    def __init__(self,root):
        # code for creating table
        fontColor = "blue"
        for i in range(StealsGUI.total_rows):
            for j in range(StealsGUI.total_columns):
                  
                self.e = Entry(root, width=15, fg=fontColor,
                               font=('Arial',16,'bold'))
                  
                self.e.grid(row=i, column=j)
                self.e.insert(END, StealsGUI.lst[i][j])

class StealsGUI:
    lst = StealsTableList.returnList()
    total_rows = len(lst)
    total_columns = len(lst[0])
    def __init__(self):
        root = Tk()
        root.title("Steals By Starting Players")
        t = StealTable(root)
        root.mainloop()

# Points
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

# Main GUI
class MainGUI:
    def __init__(self):
        root = Tk()
        root.title("Options")
        root.geometry("500x200")
        menubar = Menu(root)
        Options = Menu(menubar, tearoff=0)
        Options.add_command(label="Points", command=PointsGUI)
        Options.add_command(label="Steals", command=StealsGUI)
        Options.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="Options", menu=Options)
        root.config(menu=menubar)
        root.mainloop()
MainGUI()