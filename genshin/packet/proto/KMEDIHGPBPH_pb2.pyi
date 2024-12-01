from genshin.packet.proto import ABDNLACDCNI_pb2 as _ABDNLACDCNI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KMEDIHGPBPH(_message.Message):
    __slots__ = ("GDINBILAIMF", "LKOFKODPMGO")
    class GDINBILAIMFEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _ABDNLACDCNI_pb2.ABDNLACDCNI
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_ABDNLACDCNI_pb2.ABDNLACDCNI, _Mapping]] = ...) -> None: ...
    GDINBILAIMF_FIELD_NUMBER: _ClassVar[int]
    LKOFKODPMGO_FIELD_NUMBER: _ClassVar[int]
    GDINBILAIMF: _containers.MessageMap[int, _ABDNLACDCNI_pb2.ABDNLACDCNI]
    LKOFKODPMGO: int
    def __init__(self, GDINBILAIMF: _Optional[_Mapping[int, _ABDNLACDCNI_pb2.ABDNLACDCNI]] = ..., LKOFKODPMGO: _Optional[int] = ...) -> None: ...
