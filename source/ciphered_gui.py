from basic_gui import BasicGUI
from cryptography.hazmat.primitives import hashes 
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC 
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import dearpygui.dearpygui as dpg
import logging
import os
import serpent

# Modification de DEFAULT_VALUES, la deuxieme valeur de la liste definit si le champ de texte est un password
DEFAULT_VALUES = {
    "host"      : ["127.0.0.1", False],
    "port"      : ["6666", False],
    "name"      : ["foo", False],
    "password"  : ["", True]
}

# Nombre de bytes pour la génération de l'iv et de la taille de la clé
NB_BYTES = 16

# Fonction de dérivation de clé
key_derivate_function = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=NB_BYTES,
    salt=b'MoiAimePasPython',
    iterations=480000
)


class CipheredGUI(BasicGUI):
    # Constructeur
    def __init__(self) -> None:
        super().__init__()    
        self._key = None 
    # Surchage de la fonction _create_connection_window de la classe BasicGUI
    def _create_connection_window(self)->None:
        # windows about connexion
        with dpg.window(label="Connection", pos=(200, 150), width=400, height=300, show=False, tag="connection_windows"):
            
            for field in DEFAULT_VALUES.keys():
                with dpg.group(horizontal=True):
                    dpg.add_text(field)
                    dpg.add_input_text(default_value=DEFAULT_VALUES[field][0], tag=f"connection_{field}", password=DEFAULT_VALUES[field][1])

            dpg.add_button(label="Connect", callback=self.run_chat)

    def run_chat(self, sender, app_data) -> None:
        super().run_chat(sender, app_data)
        password=dpg.get_value("connection_password")

        # Génération de la clé
        self._key = key_derivate_function.derive(bytes(password, "utf-8"))
        print(self._key)


# code d'exemple : https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/

    def encrypt(self, message):
        # Génération de l'Initial Value
        iv = os.urandom(NB_BYTES)
        # Chiffrement du message grâ à l'algorithme AES (CTR)
        cipher = Cipher(algorithms.AES(self._key), modes.CTR(iv))
        encryptor = cipher.encryptor()
        message_chiffre = encryptor.update(bytes(message, "utf-8")) + encryptor.finalize()
        # return (iv, message_chiffre)
        return (serpent.tobytes(iv), serpent.tobytes(message_chiffre))


    def decrypt(self, tuple_iv_message_chiffre):
        # Déconcaténation du tuple 
        iv, message_chiffre = tuple_iv_message_chiffre
        # Retransformation en bytes
        iv = serpent.tobytes(iv)
        message_chiffre = serpent.tobytes(message_chiffre)
        # Déchiffrement du message
        cipher = Cipher(algorithms.AES(self._key), modes.CTR(bytes(iv)))
        decryptor = cipher.decryptor()
        message_dechiffre = decryptor.update(message_chiffre) + decryptor.finalize()
        # Return le message_dechiffre
        return str(message_dechiffre, "utf-8")

    def send(self, text) -> None:
        text_chiffre = self.encrypt(text)
        return super().send(text_chiffre)

    def recv(self) -> None:
        if self._callback is not None:
            for user, message in self._callback.get():
                message_dechiffre = self.decrypt(message)
                self.update_text_screen(f"{user} : {message_dechiffre}")
            self._callback.clear()
    


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # instanciate the class, create context and related stuff, run the main loop
    client = CipheredGUI()
    client.create()
    client.loop()