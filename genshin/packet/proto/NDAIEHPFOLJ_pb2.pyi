from genshin.packet.proto import NFDGAFNBIGP_pb2 as _NFDGAFNBIGP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NDAIEHPFOLJ(_message.Message):
    __slots__ = ("IIMNKBOIDBK", "BLLIPODNDHA", "POKJGLHPEEJ")
    IIMNKBOIDBK_FIELD_NUMBER: _ClassVar[int]
    BLLIPODNDHA_FIELD_NUMBER: _ClassVar[int]
    POKJGLHPEEJ_FIELD_NUMBER: _ClassVar[int]
    IIMNKBOIDBK: _containers.RepeatedScalarFieldContainer[int]
    BLLIPODNDHA: _containers.RepeatedScalarFieldContainer[int]
    POKJGLHPEEJ: _containers.RepeatedCompositeFieldContainer[_NFDGAFNBIGP_pb2.NFDGAFNBIGP]
    def __init__(self, IIMNKBOIDBK: _Optional[_Iterable[int]] = ..., BLLIPODNDHA: _Optional[_Iterable[int]] = ..., POKJGLHPEEJ: _Optional[_Iterable[_Union[_NFDGAFNBIGP_pb2.NFDGAFNBIGP, _Mapping]]] = ...) -> None: ...
