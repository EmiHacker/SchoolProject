# SchoolProject
****MANUAL DE USUARIO****

El siguiente programa busca realizar diferentes actividades automaticas vistas en la UA de programación para ciberseguridad, las cuales son las siguientes:
- Web scraping
- Metadata de imagenes
- Encriptación
- Valores HASH
- Envio de correo

Fueron creados 3 archivos:
- PIA.py
- ValHash.py
- Ejecutar.ps1

Se iran dando instrucciones en el orden de la utilización de los archivos y tambien su orden en base al codigo:

Primero, se haran cambios en el script PIA.py por los datos del usuario:
1. Web scraping
En la linea 50, en la función "descargar" se debe cambiar el directorio por el del usuario.

2. Metadata de imagenes
En la linea 96, en la función "printMeta", se debe cambiar el valor de la variable "ruta" por la ruta del directorio del usuario"

3. Encriptación
En la linea 118, en la funcion "SendingtoEncrypt", se debe cambiar el valor de la variable "ruta" por la ruta del directorio del usuario"


Despues, se haran cambios en el script ValHash.py por los datos del usuario:
4. Valores Hash
En la linea 118 se debe cambiar el valor de la variable "ruta" por la ruta del directorio del usuario"

5. Envio de correo 
En la linea 39, en la linea de codigo "smtpObj.login("user", "pwd")", "user" seria el correo del usuario y "pwd" seria la contraseña del usuario
-Ejemplo: smtpObj.login("123@uanl.edu.mx", "1223343")

En la funcion "send_test_email", en la linea 42, la valor de la variable "sender_email" debera cambiar por el correo del emisor del mensaje y, en la linea 43, el valor de la variable "receiver_email" debera cambiar por el correo del receptor del mensaje.

En la linea 54, en la linea de codigo "smtpObj.login("user", "pwd")", "user" seria el correo del usuario y "pwd" seria la contraseña del usuario


Y al final, tambien se haran Despues, se haran cambios en el script Ejecutar.ps1 por los datos del usuario:
En la linea 1, en la linea de codigo "Set-Location" se debe cambiar la ruta por default por la ruta del directorio del usuario.



INSTRUCCIONES DE USO:
- Para poder utilizar los codigos adecuadamente todos deberan estar en una carpeta.
- En la carpeta donde estaran dichos codigos debera crear una carpeta llamada "metadataimgPIA", ya que ahi se guardaran las imagenes descargar y los archivos que se generen en base a ellas.
- Debera ejecutar PRIMERO el codigo "Ejecutar.ps1" en Windows PowerShell, ya que este ejecutara automaticamente los codigos PIA.py y ValHash.py.
- Si desea utilizar el codigo de nuevo, elimine los archivos generados en la carpeta "metadataimgPIA", para no crear algun inconveniente.
