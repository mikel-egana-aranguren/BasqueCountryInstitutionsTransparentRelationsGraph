# Ejercicio visualización RDF

RDF es un modelo de datos para grafos, y por tanto se puede visualizar. La visualización de grandes grafos de una manera útil es difícil, pero con grafos pequeños se pueden usar muchas herramientas, como por ejemplo:

* [isSemantic RDF visualiser](https://issemantic.net/rdf-visualizer). Esta herramienta acepta copiar y pegar RDF directamente en el formulario. Prueba con `People/People.nq` o `People/People-metadata.ttl`
* [Gephi](https://gephi.org/). Gephi es un programa muy común para visualizar grafos de todo tipo. Para visualizar Grafos RDF hay que convertir el archivo RDF `People/People.nq` al formato Graphviz en el servicio [EasyRDF](https://www.easyrdf.org/converter), y luego se puede cargar en Gephi. 
* Algunas Triple Stores ofrecen visualización de grafos. [GraphDB](https://www.ontotext.com/products/graphdb/download/) tiene una versión gratuita pero requiere registro; unaz vez instalada se puede cargar RDF directamente.
* [Extension Linked Data VS Code](https://marketplace.visualstudio.com/items?itemName=Elsevier.linked-data). Instalar siguiendo las instrucciones. Seleccionar `People/People.jsonld`, `Cmd-Shift-p` o `Ctrl-Shift-p`, empezar a escribir "Linked Data" y seleccionar "Linked Data: Visualize".
* ...