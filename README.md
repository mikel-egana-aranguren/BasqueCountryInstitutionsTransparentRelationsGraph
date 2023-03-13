# Basque Country Institutions Transparent Relations Graph

RDF Knowledge Graph for Transparent relations involving Basque Country institutions.

## Data sources

Each folder represents a data source that will result in a Named Graph in the Triple Store. Thus, regardless of the data source, the data will be converted to RDF following certain conventions (That should be documented soon). Therefore, the `README.md` file in the folder should include, at least:

* Origin of the data.
* URI conventions and ontologies used to produce the RDF.
* Documented program to convert the data to RDF.
* Resulting file in RDF (`nq` for Named Graphs).
* Metadata file in RDF, including pointers to the Named Graph.

See `/People` and `/RegistroLicitadoresYEmpresasClasificadas` for examples.

## Data storage

Since RDF is a W3C standard, you should be able to load the resulting RDF files in any Triple Store of your choice. Blazegraph is provided for convenience, to execute it do a `java -server -Xmx4g -jar blazegraph.jar` and then check `localhost:9999`.
