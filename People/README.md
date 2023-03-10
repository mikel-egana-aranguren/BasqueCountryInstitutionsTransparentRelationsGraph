# People

## Dataset

* Name: People
* Source: Various sources, collected manually
* Metadata: `People.ttl` (Produced manually)

## Convert to RDF Graph

* URI pattern:
  * Graph URI: https://data.ehu.eus/bcitr/people/graph
  * Base URI: https://data.ehu.eus/bcitr/
  * Person: https://data.ehu.eus/bcitr/person/[normalised-person-name]
  * Role: https://data.ehu.eus/bcitr/role/[normalised-person-name][officer|president|director|...][dates]
* Vocabularies used:
  * [Transparent Relations Ontology](https://w3id.org/TRO)
* `python3 CSV2RDF.py` (`pip install rdflib`)

## Store Graph

* Upload `People.nq` (Data)
* Upload `People.ttl` (Metadata)