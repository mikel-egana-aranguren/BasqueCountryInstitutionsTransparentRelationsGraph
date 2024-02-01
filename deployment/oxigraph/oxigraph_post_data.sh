#!/bin/sh

curl http://localhost:7878/store?default -H 'Content-Type: text/turtle' -T ./$1
