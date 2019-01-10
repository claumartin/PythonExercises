# Clase Fecha
Construye una clase de nombre Fecha que represente el tipo de dato abstracto ADT fecha como tres enteros de nombres dia, mes y año. 

## Propiedades de la clase (todas ellas privadas):

* dia: de tipo entero (01 - 31)
* mes: de tipo entero (01 - 12)
* año: de tipo entero (1900 - 3000)

## Constructor (inicializador en Python):

* Constructor que, por defecto, inicialice las propiedades de la clase a la fecha 01-01-1900 [programación defensiva].

* Constructor al que se le pasen como argumentos tres enteros y se los asigne a las propiedades de la clase. Si la cantidad recibida no satisface las restricciones de los valores impuestos a dia, mes y año, el valor que se fija es 01 o 1900 [Manejo de errores]: (devolver un valor neutro, aunque en este caso no lo sea).

## Métodos de la clase (públicos):

* Método de nombre **setFecha()** que recibe como argumentos tres enteros y se los asigna a las propiedades de la clase (utiliza el mismo nombre en las variables que reciben los argumentos y en las propiedades de la clase). Este método ha de diseñarse mediante programación por contrato, es decir, debe incluir una precondición: si los valores recibidos no satisfacen las restricciones de los valores impuestos a dia, mes y año, el valor que se establece es 01 o 1900 [Manejo de errores: devolver un valor neutro, aunque en este caso no lo sea]. Ya que va a ser utilizado en el constructor, este precondición podría implementarse en su propia rutina para ser llamada desde este método y desde el “constructor”.

* **incrementarFecha()**: recibe un entero que representa un número de días e incrementa la fecha en dicha cantidad de dias.

* **imprimirFecha()**: escribe la fecha en el formato dia-mes-año en consola. Se mostrará el nombre del mes, no el número.

* método privado **mesLetra()** que devuelve el mes en letras asociado al mes numérico guardado en una determinada instancia (objeto) de la clase; este método será invocado desde imprimirFecha().

* método **getFecha()** que devuelve un string que contenga la fecha en el formato día-mes-año.