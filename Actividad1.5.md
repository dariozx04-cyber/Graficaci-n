# Actividad

Alumno: Dario Padillla Moreno

Grupo B

<img src="C:\Users\jaime\OneDrive\Escritorio\tareasGrafi\Mascara sin limpiar.png" width="200" height= "200">

<img src="C:\Users\jaime\OneDrive\Escritorio\tareasGrafi\Mascara limpia.png" width="200" height= "200">

<img src="C:\Users\jaime\OneDrive\Escritorio\tareasGrafi\Color Verde.png" width="200" height= "200">

<img src="C:\Users\jaime\OneDrive\Escritorio\tareasGrafi\Color Rojo.png" width="200" height= "200">

<img src="C:\Users\jaime\OneDrive\Escritorio\tareasGrafi\Color amarillo.png"
width="200" height= "200">

## Objetivo

  • Aplicar el modelo de color HSV para segmentar objetos.

  
 •  Analizar resultados directamente sobre una máscara binaria.
  
  • Identificar y contar regiones conectadas.
  
  • Evaluar el impacto del rango de color en la segmentación.
## Actividad 1

- ¿Que ocurre cuando  el rango es muy estrecho?


Solo capturas los colores precisos que están en el rango

- ¿Que ocurre cuando el rango es muy amplio?

Se termina mezclando con el resto de colores no deseados

## Actividad 2
- ¿Qué tipo de ruido aparece?
  
  
 Ruido aislado, formado por píxeles individuales que no pertenecen al objeto que nos interesa.
  
  
- ¿Por qué es necesario eliminarlo antes del conteo?

Si no se elimina, esos píxeles se contarían como fruta lo que llevara a conteos equivocsados y mediddas inexactas.

## Actividad 3

 Número total de frutas detectadas :23
 
  Área aproximada de cada región válida: 5127
## Actividad 4
¿Qué color fue más fácil segmentar?

Verde

¿Cuál presentó más ruido?

Verde

¿Por qué ocurre esto?

Algunos colores están presentes en el entorno.

La iluminación altera tonos claros.

| Color | Número Detectado de objetos| Observaciones |
|------|------|------|
| Rojo | 5 | Fácil detección, poco ruido |
| Verde | 4 | Confusión con fondo |
| Amarillo | 6 | Sensible a iluminación |

## Actividad 5
Por qué HSV es más adecuado que RGB?

Porque separa tono de saturación y brillo, haciendo más fácil segmentar colores independientemente de la iluminación.

¿Cómo afecta la iluminación al canal V?

Cambios de luz afectan el canal V, pudiendo alterar la percepción del color si solo se usa RGB.

¿Qué sucede si dos frutas tienen tonos similares?

Se detectarán juntas o como una sola región.Se necesita otro criterio para diferenciarlas.

¿Qué limitaciones tiene la segmentación por color?

Sensible a sombras, reflejos y variaciones de luz.

Colores similares entre objetos diferentes pueden confundirse.

No distingue objetos del mismo color que se toquen.

## Conclusión

En esta práctica se utilizó el espacio de color HSV para detectar frutas según su color. Se dictaron diferentes rangos para segmentar frutas rojas, verdes y amarillas, donde la elección correcta del rango es muy importante. Cuando el rango es muy estrecho, no se detecta toda la fruta; cuando es muy amplio, aparece ruido y se detectan objetos que no corresponden.


También se comprobó que la máscara original puede contener pequeños puntos  que pueden llegar a afectar el conteo. Por eso es necesario aplicar un metodo de limpieza antes de contar las regiones conectadas ya que esto permite obtener un número más preciso de las frutas detectadas y calcular su área.

La práctica  me ayudó a entender cómo es que funciona la segmentación por color y cómo factores como la iluminación y el fondo influyen en los resultados al igual que poner datos precisoso para así obetner los resultados que se piden.
