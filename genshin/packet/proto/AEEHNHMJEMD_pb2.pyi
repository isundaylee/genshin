from genshin.packet.proto import ENADNFEKFLF_pb2 as _ENADNFEKFLF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AEEHNHMJEMD(_message.Message):
    __slots__ = ("KOJOOFKPPFO", "KCOIMECCODP")
    class KOJOOFKPPFOEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _ENADNFEKFLF_pb2.ENADNFEKFLF
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_ENADNFEKFLF_pb2.ENADNFEKFLF, _Mapping]] = ...) -> None: ...
    KOJOOFKPPFO_FIELD_NUMBER: _ClassVar[int]
    KCOIMECCODP_FIELD_NUMBER: _ClassVar[int]
    KOJOOFKPPFO: _containers.MessageMap[int, _ENADNFEKFLF_pb2.ENADNFEKFLF]
    KCOIMECCODP: bool
    def __init__(self, KOJOOFKPPFO: _Optional[_Mapping[int, _ENADNFEKFLF_pb2.ENADNFEKFLF]] = ..., KCOIMECCODP: bool = ...) -> None: ...
