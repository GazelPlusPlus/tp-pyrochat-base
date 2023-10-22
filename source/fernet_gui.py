from ciphered_gui import CipheredGUI
from cryptography.hazmat.primitives import hashes

import dearpygui.dearpygui as dpg
import logging
import base64 





class FernetGUI(CipheredGUI):
    def __name__(self) -> None:
        super().__init__()

    def run_chat(self, sender, app_data) -> None:
        # Utilise la fonction runchat de la classe CipheredGUI
        super().run_chat(sender, app_data)

        # Surchage de la donnée membre self._key
        password=dpg.get_value("connection_password")

        digest = hashes.Hash(hashes.SHA256())
        digest.update(bytes(password, "utf-8"))
        password_apres_SHA256 = digest.finalize()

        self._key = base64.b64encode(password_apres_SHA256) 





if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # instanciate the class, create context and related stuff, run the main loop
    client = FernetGUI()
    client.create()
    client.loop()