#!/bin/bash

set -e

rm -rvf genshin/packet/proto
mkdir -p genshin/packet/proto

# Use grpc_tools.protoc (bundled with grpcio-tools) so the generated code
# matches the installed protobuf runtime version.  The system protoc may be
# newer and produce incompatible gencode.
#
# The .proto files in resources/proto already use fully-qualified import
# paths (e.g. import "genshin/packet/proto/Item.proto"), so no sed rewriting
# is needed.
python3 -m grpc_tools.protoc \
    --proto_path genshin/packet/proto=resources/proto \
    --python_out . \
    --pyi_out . \
    resources/proto/*.proto
