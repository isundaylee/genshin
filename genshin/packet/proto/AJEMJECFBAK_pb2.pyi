from genshin.packet.proto import NDJFLPJBAEJ_pb2 as _NDJFLPJBAEJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AJEMJECFBAK(_message.Message):
    __slots__ = ("HKPCCHJEOBL", "LKOFKODPMGO")
    class HKPCCHJEOBLEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _NDJFLPJBAEJ_pb2.NDJFLPJBAEJ
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_NDJFLPJBAEJ_pb2.NDJFLPJBAEJ, _Mapping]] = ...) -> None: ...
    HKPCCHJEOBL_FIELD_NUMBER: _ClassVar[int]
    LKOFKODPMGO_FIELD_NUMBER: _ClassVar[int]
    HKPCCHJEOBL: _containers.MessageMap[int, _NDJFLPJBAEJ_pb2.NDJFLPJBAEJ]
    LKOFKODPMGO: int
    def __init__(self, HKPCCHJEOBL: _Optional[_Mapping[int, _NDJFLPJBAEJ_pb2.NDJFLPJBAEJ]] = ..., LKOFKODPMGO: _Optional[int] = ...) -> None: ...
