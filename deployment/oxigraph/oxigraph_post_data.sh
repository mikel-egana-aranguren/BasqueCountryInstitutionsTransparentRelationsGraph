#!/bin/sh

curl http://localhost:7878/store?default -H 'Content-Type: text/turtle' -T ./$1

# https://github.com/zazuko/trifid/issues/193#issuecomment-1992018917

# curl -X POST http://localhost:7878/update \
# -H "Content-Type: application/sparql-update" \
# --data-binary 'PREFIX ex: <http://example.org/>
#                INSERT DATA {
#                  ex:subject ex:predicate ex:object .
#                }'
