from genshin.packet.proto import MKGJGOIAOAP_pb2 as _MKGJGOIAOAP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CLKHPFDIENM(_message.Message):
    __slots__ = ("PPOCFIEHJAA", "EJNINFFFKJP")
    PPOCFIEHJAA_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    PPOCFIEHJAA: _containers.RepeatedCompositeFieldContainer[_MKGJGOIAOAP_pb2.MKGJGOIAOAP]
    EJNINFFFKJP: int
    def __init__(self, PPOCFIEHJAA: _Optional[_Iterable[_Union[_MKGJGOIAOAP_pb2.MKGJGOIAOAP, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
