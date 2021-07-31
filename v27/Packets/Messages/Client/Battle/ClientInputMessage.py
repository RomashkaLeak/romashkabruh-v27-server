from Packets.Messages.Server.Battle.VisionUpdate import VisionUpdate

from Utils.Reader import BSMessageReader


class ClientInputMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        pass

    def process(self):
        VisionUpdate(self.client, self.player).send()