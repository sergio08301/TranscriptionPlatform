Plaforma de transcripción de documentos implementada usando Django, con conexión a la API de OpenAI.
HTML y CSS propios, aunque no eran el foco del proyecto.
El funcionamiento es simple, en la primera pantalla puedes escoger una imagen de tu pc y subirla, 
entonces se envia una requestde transcripción a la API, esta obtiene un resultado y lo envía de 
vuelta para que el usuario lo pueda leer.
Si el usuario esta logueado puede acceder a un historial donde podrá ver el resto de imagenes que 
ha subido. Puede ver las fechas, una preview de la transcripción, la propia imagen, tambien puede
exportar como txt la transcripción o eliminar esta entrada del registro. En caso del usuario no 
estar logueado no podrá acceder a este historial.
![Image](https://github.com/user-attachments/assets/2937735f-0faf-4027-b904-b3f7167a1572)
![Image](https://github.com/user-attachments/assets/8866b514-db53-4d67-9e7f-1d823aaf0599)
![Image](https://github.com/user-attachments/assets/c991088e-d62b-4ef5-b2cc-60834ef81a3a)
