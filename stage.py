from dataclasses import dataclass
TANK_WIDTH=16
TANK_LENGTH=16
COOLDOWN = 10
ROW=20
COL=20
DIM=16
@dataclass
class Tank:
    x:float
    y:float
    direction:str
    vx:float
    vy:float
    state:str
    alive:bool
@dataclass
class Bullet:
    x:float
    y:float
    vx:int
    vy:int
    origin:str
@dataclass
class Cell:
    i:int
    j:int
    width:int
    height:int
    state:str|None
    black_screen:bool



@dataclass
class CellWall:
    i:int
    width:int
    height:int

@dataclass
class Stage:
    name:str
    tanks:list[Tank]
    enemytanks:list[Tank]
    enemies:int
    is_game_over:bool
    cells:list[Cell]
    win:bool

        

class Stages:
     def __init__(self) -> None:
        self.stage1=Stage(name="stage1",tanks=[Tank(175,285,vx=0,vy=0,direction="north",state="player",alive=True),Tank(110,60,vx=0,vy=0,direction="west",state="enemy",alive=True),\
                                ],
                        enemytanks=[Tank(135,30,vx=0,vy=0,direction="south",state="enemy",alive=True),
                               Tank(40,225,vx=0,vy=0,direction="north",state="enemy",alive=True),
                               Tank(230,225,vx=0,vy=0,direction="north",state="enemy",alive=True)
                               ],
                        enemies=4,
                        is_game_over=False,
                        cells=[Cell(18,8,width=DIM,height=DIM,state="home",black_screen=False),
                        Cell(18,7,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(17,7,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(17,8,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(17,9,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(18,9,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(18,4,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(18,13,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(14,8,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(13,8,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(12,8,width=DIM,height=DIM,state="halfbrick",black_screen=False),
                        Cell(3,8,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(4,8,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(5,8,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(6,8,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(5,7,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(5,9,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(7,8,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(8,8,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,8,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(7,8,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,7,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,9,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(8,6,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(8,10,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(6,7,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(7,7,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(8,7,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(6,9,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(7,9,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(8,9,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(5,6,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(6,6,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(5,10,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(6,10,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(5,11,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(5,5,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(5,12,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(5,4,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(5,13,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(5,3,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(6,5,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(6,11,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(7,5,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(7,11,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(7,6,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(7,10,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(6,12,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(6,4,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(8,5,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(8,11,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(9,6,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(9,10,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(10,5,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(10,11,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(11,5,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(11,11,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(12,4,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(12,12,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(10,14,width=DIM,height=DIM,state="northmirror",black_screen=False),
                        ]+[Cell(i, 0, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(ROW)]+\
                        [Cell(0, j, width=DIM, height=DIM, state="stone",black_screen=True) for j in range(ROW)] + \
                        [Cell(COL-1, j, width=DIM, height=DIM, state="stone",black_screen=True) for j in range(ROW)] + \
                        [Cell(i, ROW-1, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(ROW)] + \
                        [Cell(i, ROW-2, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(ROW)] +\
                        [Cell(i, ROW-3, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(ROW)], 
                        win=False
                          )
        self.stage2=Stage(name="stage1",tanks=[Tank(120,120,vx=0,vy=0,direction="north",state="player",alive=True),Tank(50,50,vx=0,vy=0,direction="north",state="enemy",alive=True)],
                        enemytanks=[Tank(200,200,vx=0,vy=0,direction="north",state="enemy",alive=True),
                               Tank(120,120,vx=0,vy=0,direction="north",state="enemy",alive=True),
                               ],
                        enemies=3,
                        is_game_over=False,
                        cells=[Cell(10,10,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(11,10,width=DIM,height=DIM,state="halfbrick",black_screen=False),
                        Cell(11,12,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(10,14,width=DIM,height=DIM,state="northmirror",black_screen=False),
                        Cell(5,5,width=DIM,height=DIM,state="southmirror",black_screen=False),
                        ]+[Cell(i, 0, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(ROW)]+\
                        [Cell(0, j, width=DIM, height=DIM, state="stone",black_screen=True) for j in range(ROW)] + \
                        [Cell(COL-1, j, width=DIM, height=DIM, state="stone",black_screen=True) for j in range(ROW)] + \
                        [Cell(i, ROW-1, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(ROW)] + \
                        [Cell(i, ROW-2, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(ROW)] +\
                        [Cell(i, ROW-3, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(ROW)],
                        win=False
                          )
        self.stages:list[Stage]=[self.stage1,self.stage2]




#