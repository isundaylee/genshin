from genshin.packet.proto import JCFCDCONMKB_pb2 as _JCFCDCONMKB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MOKBEACHIEB(_message.Message):
    __slots__ = ("PMJGJNILMBP", "EJNINFFFKJP")
    PMJGJNILMBP_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    PMJGJNILMBP: _containers.RepeatedCompositeFieldContainer[_JCFCDCONMKB_pb2.JCFCDCONMKB]
    EJNINFFFKJP: int
    def __init__(self, PMJGJNILMBP: _Optional[_Iterable[_Union[_JCFCDCONMKB_pb2.JCFCDCONMKB, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
