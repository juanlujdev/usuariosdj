# funciones extra de la aplicacion user

import random
import string

def code_generator(size=6, chars=string.ascii_uppercase+string.digits):# le digo que el tamño del codigo generado sea 6
    # vamos a generar un string plano y en mayusculas y que alvergue digitos
    return ''.join(random.choice(chars) for _ in range(size))
