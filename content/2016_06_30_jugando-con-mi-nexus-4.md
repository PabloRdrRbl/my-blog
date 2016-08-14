Title: Jugando con mi Nexus 4
Date: 2016-1-23 12:21
Modified: 2016-6-30 15:24
Category:
Tags: Android, root
Slug: jugando-con-mi-nexus-4
Authors: Pablo Rodríguez Robles


Mi Nexus 4 ya va teniendo su edad (3 años) y desde hace un tiempo ya no flasheo nuevas roms con la frecuencia que lo hacía al principio. Aprovechando que esta semana me he dignado ha pasarme a Android 6 y que me he juntado con mi amigo Javi para poner al día sendos mako, he querido dejar por escrito cuál es el procedimiento que uso para dejar mi móvil al borde del brick.

<!-- PELICAN_END_SUMMARY -->

Tanto en [HTCMania](http://htcmania.com) como en [XDA Developers](http://xda-developers.com) (lugares tan sagrados para mí durante algún tiempo) se pueden encontrar distintos métodos para hacer esto. A lo largo de estos años yo me he quedado con el que mayor compatibilidad tiene en Mac OS/Linux, además de usar la terminal, que siempre es más hacker.

Actualmente llevo la versión 5.1.1 de Android con la ROM XenonHD (versión: 08/20/2015) junto con el kernel Hellscore (versión: b73-CM).

Tras pasar un rato por HTCMania y XDA he elegido la siguiente combinación buscando algo estable que dure bastante:

* **ROM:** Chroma 01/18/2016 ([enlace a XDA](http://forum.xda-developers.com/nexus-4/development/rom-chroma-03-31-2015-layers-t3069936)).
* Por ahora estoy con el **kernel** que la ROM trae por defecto a la espera de ver cómo rinde y poder comparar con el que ponga.

### Transfiriendo los archivos viejos hasta nuestro ordenador

Antes de empezar hemos de recordar que el proceso completo (supondremos que partimos como si el teléfono está de fábrica) borrará todos los datos. Así que antes debemos pasar todos los datos al ordenador.

**IMPORTANTE:** solo se pasarán los archivos como fotos, vídeos, conversaciones de WhatsApp… no así los datos de las aplicaciones ni ninguna configuración del dispositivo.

Usaremos las `nexus-tools` para acceder a **Android File Transfer** (adb) desde la terminal. `nexus-tools` se puede descargar en el siguiente enlace:

> [https://github.com/corbindavenport/nexus-tools](https://github.com/corbindavenport/nexus-tools)

Para instalar la herramienta solo necesitamos el comando:

``` console
$ bash (curl -s https://raw.githubusercontent.com/corbindavenport/nexus-tools/master/install.sh)
```

Creamos una carpeta donde guardar los datos:

``` console
$ mkdir copia_datos_nexus
```

Tras habilitar `adb` en las opciones de desarrollo, comprobamos que el ordenador reconoce nuestro dispositivo utilizando el comando `adb devices`, tras el que recibiremos como resultado algo parecido a este mensaje:

``` console
  List of devices attached
  00895e64d40es4c6 device
```

Y después transferimos todos los archivos de la tarjeta sd virtual a nuestro ordenador:

``` console
$ adb pull /storage/sdcard0/ <carpeta destino>
```

Por ejemplo `adb pull /storage/sdcard0/ copia_datos_nexus`.

El proceso puede tardar en función de cómo esté de lleno nuestro teléfono. Antes de seguir es recomendable que comprobemos que todo está en la carpeta de destino.

### Desbloqueando el bootloader

En este caso yo empleo el script **Universal Nexus Linux Toolkit**, el cual se puede descargar en este enlace:

> [http://forum.xda-developers.com/nexus-4/orig-development/linux-universal-nexus-linux-toolkit-v2-t1999065](http://forum.xda-developers.com/nexus-4/orig-development/linux-universal-nexus-linux-toolkit-v2-t1999065)

Existen versiones compatibles con Linux y con OS X. Lo descargamos y:

``` console
$ bash unltlauncherosx100.sh
```

Seleccionamos el dispositivo y el modo automático:

![Terminal image 1]({attach}images/nexus_4/terminal-1.jpg)

![Terminal image 2]({attach}images/nexus_4/terminal-2.jpg)

Primero desbloquearemos el bootloader, para ello entramos en el modo fastboot (encender presionando la tecla de bajar el volumen) y en Universal Nexus Linux Toolkit seleccionamos la opción 1.

![Terminal image 3]({attach}images/nexus_4/terminal-3.jpg)

Con las teclas de volumen para subir y bajar y con el botón de encendido para confirmar escogemos `Sí` (desbloquear). El teléfono se reiniciará y después de una pantalla de carga se cargará el sistema operativo.

Para instalar **TWRP** descargaremos la última versión en su página web:

> [https://dl.twrp.me/mako/](https://dl.twrp.me/mako/)

Y desde el fastboot introducimos en el terminal:

``` console
$ adb reboot bootloader
$ fastboot flash recovery twrp-2.8.7.0-mako.img
```

Ya estamos listos para instalar nuestra rom.

### Instalando ROMs desde adb sideload

Desde el recovery entramos en el `adb sideload`, para hacer la instalación en limpio marcaremos las opciones de `wipe` (última imagen).

![Recovery image 1]({attach}images/nexus_4/recovery-1.jpg){: .center-image }

![Recovery image 2]({attach}images/nexus_4/recovery-2.jpg){: .center-image }

![Recovery image 3]({attach}images/nexus_4/recovery-3.jpg){: .center-image }

![Recovery image 4]({attach}images/nexus_4/recovery-4.jpg){: .center-image }

Y una vez descargado todo lo necesario (ROM y **GApps**, las cuales están en el mismo post que la ROM) introducimos:

``` console
$ adb sideload <ruta de la ROM>
```

Y cuando esta se haya instalado:

``` console
$ adb sideload <ruta de las GApps>
```

La ROM ya está instalada, ahora solamente tenemos que reiniciar el teléfono y configurarlo.
