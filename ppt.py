" Piedra, papel o tijera."

import ramdom

def jugar():
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.").lower()
    computadora = ramdom.choice(['pi','pa','ti'])