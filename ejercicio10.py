# Obtener la dirección de correo electrónico del usuario
email  =  input ( '¿Cuál es su dirección de correo electrónico ?: ').strip()

# Corta el nombre de usuario
usuario  =  email[:email.index('@')]

# Corta el nombre de dominio
dominio  =  email[email.index('@')+1:]

# Formato de mensaje
resultado= "Su nombre de usuario es = {} \nSu nombre de dominio es = {}" . format ( usuario , dominio )

# Mostrar mensaje de salida
print ( resultado)