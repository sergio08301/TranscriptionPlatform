Plaforma de transcripción de documentos implementada usando Django, con conexión a la API de OpenAI.
HTML y CSS propios, aunque no eran el foco del proyecto.
El funcionamiento es simple, en la primera pantalla puedes escoger una imagen de tu pc y subirla, 
entonces se envia una requestde transcripción a la API, esta obtiene un resultado y lo envía de 
vuelta para que el usuario lo pueda leer.
Si el usuario esta logueado puede acceder a un historial donde podrá ver el resto de imagenes que 
ha subido. Puede ver las fechas, una preview de la transcripción, la propia imagen, tambien puede
exportar como txt la transcripción o eliminar esta entrada del registro. En caso del usuario no 
estar logueado no podrá acceder a este historial.
