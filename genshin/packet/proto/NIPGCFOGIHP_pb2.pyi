from genshin.packet.proto import OAIMBJCNJLI_pb2 as _OAIMBJCNJLI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NIPGCFOGIHP(_message.Message):
    __slots__ = ("DFBMBDOMKIG", "PGEJGJMGGOG")
    DFBMBDOMKIG_FIELD_NUMBER: _ClassVar[int]
    PGEJGJMGGOG_FIELD_NUMBER: _ClassVar[int]
    DFBMBDOMKIG: _containers.RepeatedScalarFieldContainer[int]
    PGEJGJMGGOG: _containers.RepeatedCompositeFieldContainer[_OAIMBJCNJLI_pb2.OAIMBJCNJLI]
    def __init__(self, DFBMBDOMKIG: _Optional[_Iterable[int]] = ..., PGEJGJMGGOG: _Optional[_Iterable[_Union[_OAIMBJCNJLI_pb2.OAIMBJCNJLI, _Mapping]]] = ...) -> None: ...
