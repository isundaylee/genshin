from genshin.packet.proto import PCLLABLBNGA_pb2 as _PCLLABLBNGA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AOIBIJLDFPK(_message.Message):
    __slots__ = ("JEILNPELIAB", "AGIDBEEINDE")
    JEILNPELIAB_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    JEILNPELIAB: _containers.RepeatedCompositeFieldContainer[_PCLLABLBNGA_pb2.PCLLABLBNGA]
    AGIDBEEINDE: int
    def __init__(self, JEILNPELIAB: _Optional[_Iterable[_Union[_PCLLABLBNGA_pb2.PCLLABLBNGA, _Mapping]]] = ..., AGIDBEEINDE: _Optional[int] = ...) -> None: ...
