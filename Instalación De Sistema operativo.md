INSTALACIÓN DE SISTEMA OPERATIVO RASPBERRY PI OS

# Descargar ISO
Buscamos la página oficial Raspberry:
www.rasberrypi.com, luego accedemos al apartado software, bajamos hasta encontrar Raspberry Pi OS, accedemos, y descargamos la versión de 54 bit (dependiendo el modelo de Raspberry y su uso).

Descargamos la versión que elegimos y comenzara la descarga de la ISO del sistema operativo.

## USB BOOTEABLE

### OPCIÓN DE WINDOWS
Descargar la aplicación Rufus desde la página web: Rufus.ie (asegúrate de tener un pendrive conectado a la computadora).

Ejecutamos el programa Rufus, seleccionamos el pendrive que haremos Booteable, también seleccionaremos la ISO del sistema operativo y haremos click en comenzar (tener en cuenta que se borrarán todos los datos del pendrive)

### OPCIÓN DE LINUX
Ejecuta la terminal que este utilizando el Linux, escribe `lsblk` te mostrara: "todos los dispositivos conectados" (de almacenamiento ).
Busca el pendrive que desee hacerlo Booteable.

Una vez identificado ejecutaremos:
`sudo dd if=/ruta/de/tu/archivo.iso of=/dev/SdX bs=4M status=progress conv=fsync` luego de presionar enter, empezara a eliminar todo lo que tiene su pendrive y el instalador del sistema operativo sera puesto dentro.

## INSTALACIÓN DE SISTEMA OPERATIVO
