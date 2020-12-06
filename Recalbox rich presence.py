from pypresence import Presence
import time

RPC = Presence(client_id="784921205656125452") #Don't touch!!
RPC.connect()
RPC.clear()

while True:
    RPC.update(large_image="recalbox_logo_white", large_text="Play again!",
           state = "In the menus",
           details = None)
    time.sleep(60)
