from genshin.packet.proto import KNPKGPHANDB_pb2 as _KNPKGPHANDB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NOHOKLHHNKD(_message.Message):
    __slots__ = ("DOPJDKEDCBN", "level")
    DOPJDKEDCBN_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    DOPJDKEDCBN: _containers.RepeatedCompositeFieldContainer[_KNPKGPHANDB_pb2.KNPKGPHANDB]
    level: int
    def __init__(self, DOPJDKEDCBN: _Optional[_Iterable[_Union[_KNPKGPHANDB_pb2.KNPKGPHANDB, _Mapping]]] = ..., level: _Optional[int] = ...) -> None: ...
