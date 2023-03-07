# Registro de licitadores y empresas clasificadas

## Dataset

* Name: Registro de licitadores y empresas clasificadas
* Source:
  * https://www.contratacion.euskadi.eus/webkpe00-kperoc/es/k60aSolicitudesWar/inicioBusqEmpresas.do
  * "Busqueda de empresas", "Informes": `Empresas-2023-03-05.pdf`
  * https://www.adobe.com/acrobat/online/pdf-to-excel.html: `Empresas-2023-03-05.csv`
* Metadata: `Empresas-2023-03-05-metadata.ttl`

## Convert to RDF Graph

* URI pattern:
  * Graph URI: https://data.ehu.eus/bcitr/graph
  * Base URI: https://data.ehu.eus/bcitr/
  * Company: https://data.ehu.eus/bcitr/company/['Número inscripción']
* Vocabularies used:
  * [Transparent Relations Ontology](https://w3id.org/TRO)
* `python3 CSV2RDF.py` (`pip install rdflib`)

## Store Graph

* Blazegraph: `java -server -Xmx4g -jar blazegraph.jar`
* Upload `Empresas-2023-03-05.nq`
* Upload `Empresas-2023-03-05-metadata.ttl`