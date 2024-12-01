from genshin.packet.proto import GCAAPKLDDNE_pb2 as _GCAAPKLDDNE_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JNNMDOJAKNJ(_message.Message):
    __slots__ = ("HHPLJCPFNKF", "FFHPDCIBKOD")
    class HHPLJCPFNKFEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _GCAAPKLDDNE_pb2.GCAAPKLDDNE
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_GCAAPKLDDNE_pb2.GCAAPKLDDNE, _Mapping]] = ...) -> None: ...
    HHPLJCPFNKF_FIELD_NUMBER: _ClassVar[int]
    FFHPDCIBKOD_FIELD_NUMBER: _ClassVar[int]
    HHPLJCPFNKF: _containers.MessageMap[int, _GCAAPKLDDNE_pb2.GCAAPKLDDNE]
    FFHPDCIBKOD: int
    def __init__(self, HHPLJCPFNKF: _Optional[_Mapping[int, _GCAAPKLDDNE_pb2.GCAAPKLDDNE]] = ..., FFHPDCIBKOD: _Optional[int] = ...) -> None: ...
