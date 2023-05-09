import morph_kgc
import rdflib

graph = morph_kgc.materialize('config.ini')

graph.serialize(destination='ej1.nt', format='ntriples', encoding="utf-8")


