from genshin.packet.proto import FKHEIDFJKDO_pb2 as _FKHEIDFJKDO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JBCFNMIAMOE(_message.Message):
    __slots__ = ("JENACEPCGOF", "LPGMAEHCBOB", "HAEAOOFAJNG", "IKDAJELLEAI", "DOMBDIMFFII")
    class JENACEPCGOFEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _FKHEIDFJKDO_pb2.FKHEIDFJKDO
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_FKHEIDFJKDO_pb2.FKHEIDFJKDO, _Mapping]] = ...) -> None: ...
    JENACEPCGOF_FIELD_NUMBER: _ClassVar[int]
    LPGMAEHCBOB_FIELD_NUMBER: _ClassVar[int]
    HAEAOOFAJNG_FIELD_NUMBER: _ClassVar[int]
    IKDAJELLEAI_FIELD_NUMBER: _ClassVar[int]
    DOMBDIMFFII_FIELD_NUMBER: _ClassVar[int]
    JENACEPCGOF: _containers.MessageMap[int, _FKHEIDFJKDO_pb2.FKHEIDFJKDO]
    LPGMAEHCBOB: _containers.RepeatedScalarFieldContainer[int]
    HAEAOOFAJNG: bool
    IKDAJELLEAI: int
    DOMBDIMFFII: int
    def __init__(self, JENACEPCGOF: _Optional[_Mapping[int, _FKHEIDFJKDO_pb2.FKHEIDFJKDO]] = ..., LPGMAEHCBOB: _Optional[_Iterable[int]] = ..., HAEAOOFAJNG: bool = ..., IKDAJELLEAI: _Optional[int] = ..., DOMBDIMFFII: _Optional[int] = ...) -> None: ...
