from ciphered_gui import CipheredGUI
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

import dearpygui.dearpygui as dpg
import logging
import base64 
import serpent 





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


# code d'exemple : https://cryptography.io/en/latest/fernet/

    def encrypt(self, message):
        
        # Transformation du message string en bytes
        message_bytes = bytes(message, "utf-8")

        # Chiffrement du message
        f = Fernet(self._key)
        message_chiffre = f.encrypt(message_bytes)
        
        return message_chiffre
    

    def decrypt(self, message):

        # Transformation du message en bytes
        message_chiffre = serpent.tobytes(message)
        
        # Dechiffrement du message  
        f = Fernet(self._key)
        message_dechiffre_bytes = f.decrypt(message_chiffre)

        # Transformation du message bytes en string
        message_dechiffre = str(message_dechiffre_bytes, "utf-8")

        return message_dechiffre




if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # instanciate the class, create context and related stuff, run the main loop
    client = FernetGUI()
    client.create()
    client.loop()