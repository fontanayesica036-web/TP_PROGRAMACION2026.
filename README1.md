# TP Programación 2026

**Alumno/a:** Fontana Yesica
**Curso:** 1.er año · Tecnicatura Superior en Desarrollo de Software
**Institución:** ISFD Juan García de Cossio
**Materia:** Programación
**Docente:** Prof. Ricardo Fernández

## Cómo ejecutar los programas

1. Tener instalado Python 3 (se puede verificar con `python --version`).
2. Descargar o clonar este repositorio.
3. Abrir una terminal en la carpeta del proyecto y ejecutar el ejercicio que se quiera probar, por ejemplo:

   ```
   python ejercicio_01.py
   ```

   (se cambia el número según el ejercicio).

## Descripción de los ejercicios

| Archivo | Tema | Descripción |
|---|---|---|
| `ejercicio_01.py` | Entrada de datos y tipos | Pide dos edades por teclado y las suma. Usa `int(input(...))` para convertir el texto a número; sin esa conversión, `input` devuelve texto y el operador `+` concatena en lugar de sumar. |
| `ejercicio_02.py` | Condicionales | Calcula el total a pagar en un comercio. Si el precio es de $20.000 o más aplica un 10 % de descuento (`precio * 0.10`); si es menor, el descuento es 0. Muestra precio original, descuento y total. Rechaza precios negativos con un mensaje de error. |
| `ejercicio_03.py` | Ciclos y acumuladores | Suma los números del 1 al 10 con un `while`. `numero` actúa como contador del ciclo y `total` como acumulador. Muestra el resultado (55). |
| `ejercicio_04.py` | Programa integrador | Registra cantidades de personas por registro de participación. Termina al ingresar 0 y muestra la cantidad de registros (contador) y el total de personas (acumulador). Rechaza cantidades negativas sin contarlas. |
| `ejercicio_05.py` | Detección de errores | Versión corregida del programa de descuento. El original restaba 10 al precio (`2000 - 10 = 1990`) en lugar de calcular el 10 %. Ahora calcula `descuento = precio * 10 / 100` y el total correcto es 1800. |

## Informe

Las explicaciones, predicciones, tablas de seguimiento, pruebas realizadas y la reflexión sobre el uso de IA están en el informe PDF entregado por Google Drive.
