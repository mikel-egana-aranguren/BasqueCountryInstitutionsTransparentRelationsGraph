# Ejercicion transformación de datos CSV a RDF

## Introducción

El objetivo de este ejercicio es transformar unos datos inventados, en formato CSV, a un grafo de conocimiento RDF, para familiarizarse con el proceso y entender el modelo de datos. A coninuación se muestra un primer ejemplo muy abstracto (Proceso general) con diferentes métodos que se pueden usar para transformar los datos a RDF, siendo el método manual el más recomendado para entender bien el modelo de datos RDF. Después se ofrecen los ejercicios propiamente dichos (Ejercicio 1, ...) que exploran diferentes áreas del modelado de datos en RDF. 

## Proceso general (Ejemplo)

Supongamos el siguiente CSV con las columnas "c1", "c2" y "c3" y dos líneas de valores:

```csv
c1,c2,c3
v11,v12,v13
v21,v22,v23
```

Para traducirlo a RDF debemos crear un archivo en texto plano que contenga los mismos datos, pero en forma de grafo en vez de en forma de tabla. Nuestro grafo puede tener cualquier topología que nos parezca buena, simplemente se trata de crear tripletas sujeto-predicado-objeto con los datos, dando a cada entidad una URI para identificarla (`<>`):

```nt
<http://ex.com/v11> <http://ex.com/c2> <http://ex.com/v12> .
```

Ya tenemos nuestra primera tripleta. Si copiamos y pegamos ese texto en https://issemantic.net/rdf-visualizer veremos su representación gráfica:

![Primera tripleta](ex1.png "Primera tripleta")

Lo elementos de esa tripleta son:

* `http://ex.com/v11` (Sujeto): la entidad que estamos describiendo (Por ejemplo "Bilbo Data Lab").
* `http://ex.com/c2` (Predicado): una propiedad de esa entidad (Por ejemplo "parte de").
* `http://ex.com/v12` (Objeto): el valor de esa propiedad para esa entidad (Por ejemplo "Wikitoki").

El archivo que acabamos de crear sigue una sintaxis concreta, en este caso [NTriples](https://www.w3.org/TR/n-triples/), que consiste en poner una tripleta por linea acabando en punto. Hay muchas sintaxis disponibles (xml/rdf, ttl, nq, nt, json-ld, ...) pero es importante acordarse de que usemos la sintaxis que usemos, el grafo es el mismo.

Podemos subir el archivo a la Triple Store Blazegraph y así hacer consultas sobre el grafo, publicarlo etc. Para ello lo primero es ejecutar Blazegraph con Java:

```bash
java -server -Xmx4g -jar blazegraph.jar
```

Si vamos a `localhost:9999` deberíamos ver:

![Blazegraph](blazegraph.png "Blazegraph")

Si vamos a la pestaña `UPDATE` podemos subir el archivo (`Choose file`;`Update`). Después, para comprobar que los datos se han subido correctamente, en la pestaña `QUERY` podemos ejecutar la siguiente consulta SPARQL:

```sparql
SELECT *
WHERE {
  ?s ?p ?o
}
```

Y debería devolver los mismos datos.

### Manual (Recomendado)

### Con Python (Opcional)

### Con herramientas declarativas (Opcional)

### Con herramientas gráficas (Opcional)

## Ejercicio 1

## Ejercicio 2

## Ejercicio 3

## Ejercicio 4

## Ejercicio 5

## Ejercicio 6