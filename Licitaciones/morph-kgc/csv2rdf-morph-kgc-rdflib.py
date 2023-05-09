import morph_kgc
import rdflib

graph = morph_kgc.materialize('config.ini')

graph.serialize(destination='licitaciones_euskadi.nt', format='ntriples', encoding="utf-8")


