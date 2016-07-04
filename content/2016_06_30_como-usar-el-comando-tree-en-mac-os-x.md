Title: Cómo usar el comando tree en Mac OS X
Date: 2016-1-28 13:44
Modified: 2016-6-30 13:44
Category:
Tags: OS X, Command line
Slug: como-usar-el-comando-tree-en-mac-os-x
Authors: Pablo Rodríguez Robles


El usuario inexperto de la terminal OS X/Linux habrá llevado a cabo la secuencia `cd` - `ls` - `cd` - `ls`… en busca de saber que es lo que habita en los directorios de su ordenador. Pero esta no es la opción más rápida ni la que proporciona una visión general de la estructura de cualquiera de nuestros proyectos.

Este puede ser un ejemplo del resultado que tiene el comando `tree <directorio>`. El uso de este comando no es recomendable cunado los directorios explorados son demasiado grandes puesto que la infromación proporcionada será inútil dado el esperpento que resulta de mostrar, por ejemplo, el árbol de directorios de `/home`.


```
├── MovimientoRB
│ ├── MovimientoRB.cpp
│ ├── MovimientoRB.h
│ └── keywords.txt
├── README.md
├── SensoresRB
│ ├── SensoresRB.cpp
│ ├── SensoresRB.h
│ └── keywords.txt
├── movimiento_bt
│ └── movimiento_bt.ino
└── movimiento_teclado
└── movimiento_teclado.ino
```

Muy bien, hasta aquí todo es genial, pero algún maquero ha corrido a teclear su nuevo comando en la terminal y lo más que ha recibido como respuesta es un triste:

```
-bash: tree: command not found
```

Bueno, hay algunas maneras de conseguir el comando en OS X. Desde luego yo contaré la más fácil, y es que para ella solamente tenemos que instalar (si no lo tienes ya) Homebrew.

### Usando Homebrew para instalar tree en Mac OS

Homebrew es un gestor de paquetes al más puro estilo del `sudo apt-get install paquete` que nos permite (como ellos mismos dicen) instalar todas las cosas que necesitamos pero Apple no. Todo esto a través de una serie de [recetas](http://brewformulas.org).

Instalarlo es muy fácil y solo necesitamos un comando para ello:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Tras la instalación únicamente necesitamos una de las mágicas recetas:

```
brew install tree
```

Y ahora sí, todos podemos probar `tree /`, `tree ~` o todas las burradas que te apetezcan pero olvidándonos de `cd` - `ls` - `cd` - `ls`…

#### **Recursos utilizados:**

1. http://superuser.com/questions/359723/mac-os-x-equivalent-of-the-ubuntu-tree-command
2. http://brew.sh
