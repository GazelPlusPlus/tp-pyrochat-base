from basic_gui import BasicGUI
import dearpygui.dearpygui as dpg

# Modification de DEFAULT_VALUES, la deuxieme valeur de la liste definit si le champ de texte est un password
DEFAULT_VALUES = {
    "host"      : ["127.0.0.1", False],
    "port"      : ["6666", False],
    "name"      : ["foo", False],
    "password"  : ["", True]
}

class CipheredGUI(BasicGUI):
    def __init__(self, host:str, port:int) -> None:
        super(host, port).__init__()    
        self._key = None 

    def _create_connection_window(self)->None:
        # windows about connexion
        with dpg.window(label="Connection", pos=(200, 150), width=400, height=300, show=False, tag="connection_windows"):
            
            for field in DEFAULT_VALUES.values():
                with dpg.group(horizontal=True):
                    dpg.add_text(field[0])
                    dpg.add_input_text(default_value=field[0], tag=f"connection_{field[0]}", password=field[1])

            dpg.add_button(label="Connect", callback=self.run_chat)

    def run_chat(self, sender, app_data) -> None:
        password=dpg.get_value("connection_password")
        return super().run_chat(sender, app_data)