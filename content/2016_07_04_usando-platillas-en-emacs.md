Title: Usando plantillas en Emacs
Date: 2016-07-04 01:29
Modified: 2016-07-04 01:29
Category:
Tags: Emacs
Slug: usando-plantillas-en-emacs
Authors: Pablo Rodríguez Robles


Si me conoces seguramente te habré hablado sobre mi aficción por Emacs, si no, a lo largo de la que pretende ser una serie de entradas como esta intentaré que veas cuánto me gusta y con un poco de suerte conseguiré contagiarte.

La "funcionalidad" que voy a explicar no es exclusiva de Emacs, por lo que si tu editor de texto preferido es otro no dudes en buscar cómo utilizarla en él.

Cómo indica el título en esta ocasión estamos hablando de plantillas (para programar), estas plantillas permiten nos permiten programar de una manera más ágil y cómoda.

Usaremos **YASnippet** que según su propia página:

    YASnippet es un sistema de plantillas para emacs. Este nos permite escribir una abreviatura y automáticamente expandirla en forma de plantilla.

Los lenguajes disponibles incluyen: C, C++, C#, Perl, Python, Fortran, Ruby, SQL, LaTeX, HTML, CSS y muchos más.

### Instalación de YASnippet

Para instalar YASnippet tan solo necesitas incluirlo en los paquetes que quieeres que MELPA instale por ti (puede que en otra entrada explique como hago yo esto dentro de los ficheros de configuración de Emacs). De otro modo, y también a través de MELPA, puedes utilizar el comando `M-x list-packages`.

### Descargando snippets

YASnippet no viene con plantillas por decfecto, por lo que tendremos que instalarlas nosotros mismos. En la su página de GitHub se recomiendan distintas colecciones. Yo me he descargado las de [AndreaCrotti](https://github.com/AndreaCrotti/yasnippet-snippets).

Debemos colocar las platillas descargadas en un lugar donde Emacs pueda verlas. En mi caso lo he hecho dentro de la carpeta de los archivos de configuración de Emacs aunque en principio no sería necesario. Dentro he creado dos carpetas `my-snippets` donde irán colocadas las que yo quiera añadir en el futuro y `yasnippet-snippets` donde están las de Andrea.

```
.emacs.d
├── <resto de carpetas>
└── snippets
    ├── my-snippets
    └── yasnippet-snippets
        └── <plantillas de Andrea>
```

### Configurando YASnippet

Tan solo hemos de añadir unas líneas de código en nuestro fichero ìnit.el` que nos permitirán poder empezar a usar nuestras plantillas.

```elisp
;; This code is part of the .emacs.d/init.el file
(require 'yasnippet)
(setq yas-snippet-dirs
      '("~/.emacs.d/snippets/yasnippet-snippets"    ;; the default collection
        "~/.emacs.d/snippets/my-snippets"           ;; personal snippets
        ))
(yas-global-mode 1)
```

La primera línea carga el paquete, el bloque siguiente define los directorios donde YASnippets tiene que buscar las plantillas y la última línea establece el modo de funcionamiento predeterminado.

### Usando las plantillas en Python

La manera de expandir estas plantillas mientras escribimos código es muy sencilla: tan solo debemos escribir una palabra clave (*key*) y presionar `TAB` en ese momento la platilla se expandirá. En caso de haber varios prámetros que completar saltaremos de uno a otro usando `TAB` y lo mismo para salir de la platilla y seguir escribiendo.

Si abrimos cualquiera de las platillas veremos lo siguiente (en este caso `.emacs.d/snippets/yasnippet-snippets/python-mode/from`:

```text
# -*- mode: snippet -*-
# name: from
# key: from
# group : general
# --
from ${1:lib} import ${2:funs}
```

Como podemos ver en este caso habría que escribir `from`y presionar `TAB`para expandir la plantilla, escribir la biblioteca, presionar `TAB` para pasar a escribir el objeto a importar y `TAB` nuevamente para salir de la plantilla.

La siguiente tabla describe las combinaciones más frecuentes:

| `key`    | plantilla                                                     |
|----------|---------------------------------------------------------------|
| `from`   | importar objetos desde un módulo                              |
| `for`    | bucle for                                                     |
| `if`     | condicional if                                                |
| `ife`    | condicional if seguido de condición else                      |
| `p`      | print()                                                       |
| `r`      | return                                                        |
| `script` | plantilla con función main y condición __name__ == '__main__' |
| `with`   | estructura with                                               |
| `uft8`   | # -*- coding: utf-8 -*-                                       |
| `wh`     | while                                                         |
| `try`    | estructura try y except                                       |
| `f`      | función                                                       |
| `fd`     | función con docstring                                         |
| `ass`    | assert                                                        |

https://github.com/joaotavora/yasnippet





