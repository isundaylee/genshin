from genshin.packet.proto import BFMAJBBMIOH_pb2 as _BFMAJBBMIOH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NIHODIJKPKE(_message.Message):
    __slots__ = ("CNAJAFLIBED", "GLKNGDDNOCN", "EAIPGEMKNPO")
    CNAJAFLIBED_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    CNAJAFLIBED: _containers.RepeatedCompositeFieldContainer[_BFMAJBBMIOH_pb2.BFMAJBBMIOH]
    GLKNGDDNOCN: bool
    EAIPGEMKNPO: int
    def __init__(self, CNAJAFLIBED: _Optional[_Iterable[_Union[_BFMAJBBMIOH_pb2.BFMAJBBMIOH, _Mapping]]] = ..., GLKNGDDNOCN: bool = ..., EAIPGEMKNPO: _Optional[int] = ...) -> None: ...
