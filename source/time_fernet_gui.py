from fernet_gui import FernetGUI
from cryptography.fernet import Fernet, InvalidToken

import logging
import serpent
import time

TTL = 30 # Time To Live en s



class TimeFernetGUI(FernetGUI):
    def __name__(self) -> None:
        return super().__name__()
    
    def encrypt(self, message):
    
        # Transformation du message string en bytes
        message_bytes = bytes(message, "utf-8")

        # Chiffrement du message
        f = Fernet(self._key)
        message_chiffre = f.encrypt_at_time(message_bytes, int(time.time()) - 45)
        
        return message_chiffre
    
    def decrypt(self, message):

        # Transformation du message en bytes
        message_chiffre = serpent.tobytes(message)
        
        # Dechiffrement du message  
        f = Fernet(self._key)

        try:
            message_dechiffre_bytes = f.decrypt_at_time(token=message_chiffre, 
                                                        ttl=TTL, 
                                                        current_time=int(time.time()))
             
        except InvalidToken as e:
            return self._log.error(f"Couldn't decrypt the message. InvalidToken")
            
        message_dechiffre = str(message_dechiffre_bytes, "utf-8")
        return message_dechiffre
        


        # Transformation du message bytes en string

    
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # instanciate the class, create context and related stuff, run the main loop
    client = TimeFernetGUI()
    client.create()
    client.loop()