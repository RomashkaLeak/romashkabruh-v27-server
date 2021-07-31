from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
from Logic.Player import Players

class VisionUpdate(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24109
        self.player = player


    def encode(self):
        self.writeVint(self.player.battleTick) # Battle Ticks
        self.writeVint(int(self.player.battleTick / 10))
        self.writeVint(2) # Commands Count
        self.writeVint(self.player.battleTick)
        self.writeBoolean(True) # Live Boolean