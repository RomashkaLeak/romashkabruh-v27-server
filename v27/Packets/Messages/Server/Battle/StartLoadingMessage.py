from Utils.Writer import Writer
import random

class StartLoadingMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20559
        self.player = player

    def encode(self):
        self.writeInt(6) #6
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeInt(6) #players count
        
        self.writeInt(self.player.high_id) #High ID
        self.writeInt(self.player.low_id) #Low ID
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeInt(0) #unk
        
        self.writeScId(16, self.player.brawler_id)
        self.writeScId(29, 0)
        self.writeByte(0)
        self.writeString(self.player.name)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        
        self.writeInt(0) #High ID
        self.writeInt(1) #Low ID
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeInt(0) #unk
        
        self.writeScId(16, 0)
        self.writeScId(29, 0)
        self.writeByte(0)
        self.writeString("Bot 1")
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeInt(0) #High ID
        self.writeInt(2) #Low ID
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeInt(0) #unk
        
        self.writeScId(16, 0)
        self.writeScId(29, 0)
        self.writeByte(0)
        self.writeString("Bot 2")
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeInt(0) #High ID
        self.writeInt(3) #Low ID
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        
        self.writeInt(0) #unk
        
        self.writeScId(16, 0)
        self.writeScId(29, 0)
        self.writeByte(0)
        self.writeString("Bot 3")
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeInt(0) #High ID
        self.writeInt(4) #Low ID
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        
        self.writeInt(0) #unk
        
        self.writeScId(16, 0)
        self.writeScId(29, 0)
        self.writeByte(0)
        self.writeString("Bot 4")
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeInt(0) #High ID
        self.writeInt(5) #Low ID
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        
        self.writeInt(0) #unk
        
        self.writeScId(16, 0)
        self.writeScId(29, 0)
        self.writeByte(0)
        self.writeString("Bot 5")
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)   
        #PLAYERS SLOT END#
        
        self.writeInt(0) #count...
        
        self.writeInt(0) #Count
        
        self.writeInt(1) # Unknown
        
        self.writeVint(1)
        self.writeVint(1) #DrawMap
        self.writeVint(1)
        
        self.writeByte(0) #2, 39 - Spectating
        self.writeVint(0) # Unknown
        self.writeVint(0)
        
        self.writeScId(15, random.randrange(1, 150))
        
        print("StartLoadingMessage sent.")