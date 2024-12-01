from genshin.packet.proto import JCMLPBAEMDC_pb2 as _JCMLPBAEMDC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LOJLABAAFOA(_message.Message):
    __slots__ = ("CNAJAFLIBED", "EAIPGEMKNPO", "GLKNGDDNOCN")
    CNAJAFLIBED_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    CNAJAFLIBED: _containers.RepeatedCompositeFieldContainer[_JCMLPBAEMDC_pb2.JCMLPBAEMDC]
    EAIPGEMKNPO: int
    GLKNGDDNOCN: bool
    def __init__(self, CNAJAFLIBED: _Optional[_Iterable[_Union[_JCMLPBAEMDC_pb2.JCMLPBAEMDC, _Mapping]]] = ..., EAIPGEMKNPO: _Optional[int] = ..., GLKNGDDNOCN: bool = ...) -> None: ...
