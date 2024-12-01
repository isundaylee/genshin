from genshin.packet.proto import JNKFGJMMHMA_pb2 as _JNKFGJMMHMA_pb2
from genshin.packet.proto import GHJFBLOBGPA_pb2 as _GHJFBLOBGPA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PDMPNOBCKPK(_message.Message):
    __slots__ = ("BIPADACDOFI", "JIELCLOAEAA", "KNGBDMDCNHK", "EJNINFFFKJP")
    BIPADACDOFI_FIELD_NUMBER: _ClassVar[int]
    JIELCLOAEAA_FIELD_NUMBER: _ClassVar[int]
    KNGBDMDCNHK_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    BIPADACDOFI: _containers.RepeatedScalarFieldContainer[_JNKFGJMMHMA_pb2.JNKFGJMMHMA]
    JIELCLOAEAA: _GHJFBLOBGPA_pb2.GHJFBLOBGPA
    KNGBDMDCNHK: int
    EJNINFFFKJP: int
    def __init__(self, BIPADACDOFI: _Optional[_Iterable[_Union[_JNKFGJMMHMA_pb2.JNKFGJMMHMA, str]]] = ..., JIELCLOAEAA: _Optional[_Union[_GHJFBLOBGPA_pb2.GHJFBLOBGPA, str]] = ..., KNGBDMDCNHK: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
