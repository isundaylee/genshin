#!/bin/bash

rm -rvf genshin/packet/proto

find resources/proto -name '*.proto' | xargs -I % sed -i '' -E '/.*google.*/! s/import "/import "genshin\/packet\/proto\//' %
protoc --proto_path genshin/packet/proto=resources/proto --python_out . resources/proto/*.proto
git checkout resources/proto
