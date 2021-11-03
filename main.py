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

# Points
class pointsTableList:
    PG = Player("Skyler","PG",15,20,18)
    SG = Player("Zane","SG",10,15,12)
    C = Player("David","C",15,17,13)
    PF = Player("Carson","PF",15,13,17)
    SF = Player("Ethan","SF",17,15,17)
    def returnList():
        Game1 = functions.returnGame1Points(pointsTableList.PG.returnGame1(),pointsTableList.SG.returnGame1(),pointsTableList.C.returnGame1(),pointsTableList.PF.returnGame1(),pointsTableList.SF.returnGame1())
        Game2 = functions.returnGame2Points(pointsTableList.PG.returnGame2(),pointsTableList.SG.returnGame2(),pointsTableList.C.returnGame2(),pointsTableList.PF.returnGame2(),pointsTableList.SF.returnGame2())
        Game3 = functions.returnGame3Points(pointsTableList.PG.returnGame3(),pointsTableList.SG.returnGame3(),pointsTableList.C.returnGame3(),pointsTableList.PF.returnGame3(),pointsTableList.SF.returnGame3())
        Total = functions.returnAllPoints(pointsTableList.PG.returnPoints(),pointsTableList.SG.returnPoints(),pointsTableList.C.returnPoints(),pointsTableList.PF.returnPoints(),pointsTableList.SF.returnPoints())
        AVG = functions.returnAvg(Total)
        list = [("Name:","POS:","Game 1:","Game 2:","Game 3:","Total Points:"),
                (pointsTableList.PG.returnName(),pointsTableList.PG.returnPos(),pointsTableList.PG.returnGame1(),pointsTableList.PG.returnGame2(),pointsTableList.PG.returnGame3(),pointsTableList.PG.returnPoints()),
                (pointsTableList.SG.returnName(),pointsTableList.SG.returnPos(),pointsTableList.SG.returnGame1(),pointsTableList.SG.returnGame2(),pointsTableList.SG.returnGame3(),pointsTableList.SG.returnPoints()),
                (pointsTableList.C.returnName(),pointsTableList.C.returnPos(),pointsTableList.C.returnGame1(),pointsTableList.C.returnGame2(),pointsTableList.C.returnGame3(),pointsTableList.C.returnPoints()),
                (pointsTableList.PF.returnName(),pointsTableList.PF.returnPos(),pointsTableList.PF.returnGame1(),pointsTableList.PF.returnGame2(),pointsTableList.PF.returnGame3(),pointsTableList.PF.returnPoints()),
                (pointsTableList.SF.returnName(),pointsTableList.SF.returnPos(),pointsTableList.SF.returnGame1(),pointsTableList.SF.returnGame2(),pointsTableList.SF.returnGame3(),pointsTableList.SF.returnPoints()),
                ("","Totals:",Game1,Game2,Game3,Total),
                ("","AVG:","","","",AVG),
                ]
        return list
 
class pointsTable:
    def __init__(self,root):
        # code for creating table
        fontColor = "blue"
        for i in range(pointsGUI.total_rows):
            for j in range(pointsGUI.total_columns):
                  
                self.e = Entry(root, width=15, fg=fontColor,
                               font=('Arial',16,'bold'))
                  
                self.e.grid(row=i, column=j)
                self.e.insert(END, pointsGUI.lst[i][j])

class pointsGUI:
    lst = pointsTableList.returnList()
    total_rows = len(lst)
    total_columns = len(lst[0])
    def __init__(self):
        root = Tk()
        root.title("Points By Starting Players")
        t = pointsTable(root)
        root.mainloop()

# Steals
class stealsTableList:
    PG = Player("Skyler","PG",3,2,3)
    SG = Player("Zane","SG",1,0,2)
    C = Player("David","C",0,1,2)
    PF = Player("Carson","PF",1,1,1)
    SF = Player("Ethan","SF",1,1,2)
    def returnList():
        Game1 = functions.returnGame1Points(stealsTableList.PG.returnGame1(),stealsTableList.SG.returnGame1(),stealsTableList.C.returnGame1(),stealsTableList.PF.returnGame1(),stealsTableList.SF.returnGame1())
        Game2 = functions.returnGame2Points(stealsTableList.PG.returnGame2(),stealsTableList.SG.returnGame2(),stealsTableList.C.returnGame2(),stealsTableList.PF.returnGame2(),stealsTableList.SF.returnGame2())
        Game3 = functions.returnGame3Points(stealsTableList.PG.returnGame3(),stealsTableList.SG.returnGame3(),stealsTableList.C.returnGame3(),stealsTableList.PF.returnGame3(),stealsTableList.SF.returnGame3())
        Total = functions.returnAllPoints(stealsTableList.PG.returnPoints(),stealsTableList.SG.returnPoints(),stealsTableList.C.returnPoints(),stealsTableList.PF.returnPoints(),stealsTableList.SF.returnPoints())
        AVG = functions.returnAvg(Total)
        list = [("Name:","POS:","Game 1:","Game 2:","Game 3:","Total Steals:"),
                (stealsTableList.PG.returnName(),stealsTableList.PG.returnPos(),stealsTableList.PG.returnGame1(),stealsTableList.PG.returnGame2(),stealsTableList.PG.returnGame3(),stealsTableList.PG.returnPoints()),
                (stealsTableList.SG.returnName(),stealsTableList.SG.returnPos(),stealsTableList.SG.returnGame1(),stealsTableList.SG.returnGame2(),stealsTableList.SG.returnGame3(),stealsTableList.SG.returnPoints()),
                (stealsTableList.C.returnName(),stealsTableList.C.returnPos(),stealsTableList.C.returnGame1(),stealsTableList.C.returnGame2(),stealsTableList.C.returnGame3(),stealsTableList.C.returnPoints()),
                (stealsTableList.PF.returnName(),stealsTableList.PF.returnPos(),stealsTableList.PF.returnGame1(),stealsTableList.PF.returnGame2(),stealsTableList.PF.returnGame3(),stealsTableList.PF.returnPoints()),
                (stealsTableList.SF.returnName(),stealsTableList.SF.returnPos(),stealsTableList.SF.returnGame1(),stealsTableList.SF.returnGame2(),stealsTableList.SF.returnGame3(),stealsTableList.SF.returnPoints()),
                ("","Totals:",Game1,Game2,Game3,Total),
                ("","AVG:","","","",AVG),
                ]
        return list
 
class stealsTable:
    def __init__(self,root):
        # code for creating table
        fontColor = "blue"
        for i in range(stealsGUI.total_rows):
            for j in range(stealsGUI.total_columns):
                  
                self.e = Entry(root, width=15, fg=fontColor,
                               font=('Arial',16,'bold'))
                  
                self.e.grid(row=i, column=j)
                self.e.insert(END, stealsGUI.lst[i][j])

class stealsGUI:
    lst = stealsTableList.returnList()
    total_rows = len(lst)
    total_columns = len(lst[0])
    def __init__(self):
        root = Tk()
        root.title("Steals By Starting Players")
        t = stealsTable(root)
        root.mainloop()

# Rebounds
class reboundsTableList:
    PG = Player("Skyler","PG",6,7,7)
    SG = Player("Zane","SG",6,7,8)
    C = Player("David","C",5,6,7)
    PF = Player("Carson","PF",8,6,8)
    SF = Player("Ethan","SF",7,8,7)
    def returnList():
        Game1 = functions.returnGame1Points(reboundsTableList.PG.returnGame1(),reboundsTableList.SG.returnGame1(),reboundsTableList.C.returnGame1(),reboundsTableList.PF.returnGame1(),reboundsTableList.SF.returnGame1())
        Game2 = functions.returnGame2Points(reboundsTableList.PG.returnGame2(),reboundsTableList.SG.returnGame2(),reboundsTableList.C.returnGame2(),reboundsTableList.PF.returnGame2(),reboundsTableList.SF.returnGame2())
        Game3 = functions.returnGame3Points(reboundsTableList.PG.returnGame3(),reboundsTableList.SG.returnGame3(),reboundsTableList.C.returnGame3(),reboundsTableList.PF.returnGame3(),reboundsTableList.SF.returnGame3())
        Total = functions.returnAllPoints(reboundsTableList.PG.returnPoints(),reboundsTableList.SG.returnPoints(),reboundsTableList.C.returnPoints(),reboundsTableList.PF.returnPoints(),reboundsTableList.SF.returnPoints())
        AVG = functions.returnAvg(Total)
        list = [("Name:","POS:","Game 1:","Game 2:","Game 3:","Total Rebounds:"),
                (reboundsTableList.PG.returnName(),reboundsTableList.PG.returnPos(),reboundsTableList.PG.returnGame1(),reboundsTableList.PG.returnGame2(),reboundsTableList.PG.returnGame3(),reboundsTableList.PG.returnPoints()),
                (reboundsTableList.SG.returnName(),reboundsTableList.SG.returnPos(),reboundsTableList.SG.returnGame1(),reboundsTableList.SG.returnGame2(),reboundsTableList.SG.returnGame3(),reboundsTableList.SG.returnPoints()),
                (reboundsTableList.C.returnName(),reboundsTableList.C.returnPos(),reboundsTableList.C.returnGame1(),reboundsTableList.C.returnGame2(),reboundsTableList.C.returnGame3(),reboundsTableList.C.returnPoints()),
                (reboundsTableList.PF.returnName(),reboundsTableList.PF.returnPos(),reboundsTableList.PF.returnGame1(),reboundsTableList.PF.returnGame2(),reboundsTableList.PF.returnGame3(),reboundsTableList.PF.returnPoints()),
                (reboundsTableList.SF.returnName(),reboundsTableList.SF.returnPos(),reboundsTableList.SF.returnGame1(),reboundsTableList.SF.returnGame2(),reboundsTableList.SF.returnGame3(),reboundsTableList.SF.returnPoints()),
                ("","Totals:",Game1,Game2,Game3,Total),
                ("","AVG:","","","",AVG),
                ]
        return list
 
class reboundsTable:
    def __init__(self,root):
        # code for creating table
        fontColor = "blue"
        for i in range(reboundsGUI.total_rows):
            for j in range(reboundsGUI.total_columns):
                  
                self.e = Entry(root, width=15, fg=fontColor,
                               font=('Arial',16,'bold'))
                  
                self.e.grid(row=i, column=j)
                self.e.insert(END, reboundsGUI.lst[i][j])

class reboundsGUI:
    lst = reboundsTableList.returnList()
    total_rows = len(lst)
    total_columns = len(lst[0])
    def __init__(self):
        root = Tk()
        root.title("Rebounds By Starting Players")
        t = reboundsTable(root)
        root.mainloop()

# Fouls
class foulssTableList:
    PG = Player("Skyler","PG",1,2,1)
    SG = Player("Zane","SG",1,3,2)
    C = Player("David","C",1,1,2)
    PF = Player("Carson","PF",1,0,2)
    SF = Player("Ethan","SF",1,0,0)
    def returnList():
        Game1 = functions.returnGame1Points(foulssTableList.PG.returnGame1(),foulssTableList.SG.returnGame1(),foulssTableList.C.returnGame1(),foulssTableList.PF.returnGame1(),foulssTableList.SF.returnGame1())
        Game2 = functions.returnGame2Points(foulssTableList.PG.returnGame2(),foulssTableList.SG.returnGame2(),foulssTableList.C.returnGame2(),foulssTableList.PF.returnGame2(),foulssTableList.SF.returnGame2())
        Game3 = functions.returnGame3Points(foulssTableList.PG.returnGame3(),foulssTableList.SG.returnGame3(),foulssTableList.C.returnGame3(),foulssTableList.PF.returnGame3(),foulssTableList.SF.returnGame3())
        Total = functions.returnAllPoints(foulssTableList.PG.returnPoints(),foulssTableList.SG.returnPoints(),foulssTableList.C.returnPoints(),foulssTableList.PF.returnPoints(),foulssTableList.SF.returnPoints())
        AVG = functions.returnAvg(Total)
        list = [("Name:","POS:","Game 1:","Game 2:","Game 3:","Total Fouls:"),
                (foulssTableList.PG.returnName(),foulssTableList.PG.returnPos(),foulssTableList.PG.returnGame1(),foulssTableList.PG.returnGame2(),foulssTableList.PG.returnGame3(),foulssTableList.PG.returnPoints()),
                (foulssTableList.SG.returnName(),foulssTableList.SG.returnPos(),foulssTableList.SG.returnGame1(),foulssTableList.SG.returnGame2(),foulssTableList.SG.returnGame3(),foulssTableList.SG.returnPoints()),
                (foulssTableList.C.returnName(),foulssTableList.C.returnPos(),foulssTableList.C.returnGame1(),foulssTableList.C.returnGame2(),foulssTableList.C.returnGame3(),foulssTableList.C.returnPoints()),
                (foulssTableList.PF.returnName(),foulssTableList.PF.returnPos(),foulssTableList.PF.returnGame1(),foulssTableList.PF.returnGame2(),foulssTableList.PF.returnGame3(),foulssTableList.PF.returnPoints()),
                (foulssTableList.SF.returnName(),foulssTableList.SF.returnPos(),foulssTableList.SF.returnGame1(),foulssTableList.SF.returnGame2(),foulssTableList.SF.returnGame3(),foulssTableList.SF.returnPoints()),
                ("","Totals:",Game1,Game2,Game3,Total),
                ("","AVG:","","","",AVG),
                ]
        return list
 
class foulsTable:
    def __init__(self,root):
        # code for creating table
        fontColor = "blue"
        for i in range(foulsGUI.total_rows):
            for j in range(foulsGUI.total_columns):
                  
                self.e = Entry(root, width=15, fg=fontColor,
                               font=('Arial',16,'bold'))
                  
                self.e.grid(row=i, column=j)
                self.e.insert(END, foulsGUI.lst[i][j])

class foulsGUI:
    lst = foulssTableList.returnList()
    total_rows = len(lst)
    total_columns = len(lst[0])
    def __init__(self):
        root = Tk()
        root.title("Fouls By Starting Players")
        t = foulsTable(root)
        root.mainloop()

# Main GUI
class MainGUI:
    def __init__(self):
        root = Tk()
        root.title("Options")
        root.geometry("500x200")
        menubar = Menu(root)
        Options = Menu(menubar, tearoff=0)
        Options.add_command(label="Points", command=pointsGUI)
        Options.add_command(label="Steals", command=stealsGUI)
        Options.add_command(label="Rebounds", command=reboundsGUI)
        Options.add_command(label="Fouls", command=foulsGUI)
        Options.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="Options", menu=Options)
        root.config(menu=menubar)
        root.mainloop()

# Program
MainGUI()