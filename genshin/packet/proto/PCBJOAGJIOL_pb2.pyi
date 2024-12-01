from genshin.packet.proto import GDFFBGABIND_pb2 as _GDFFBGABIND_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PCBJOAGJIOL(_message.Message):
    __slots__ = ("NEHPGMLDKMF", "ODCMKOFFKKL")
    NEHPGMLDKMF_FIELD_NUMBER: _ClassVar[int]
    ODCMKOFFKKL_FIELD_NUMBER: _ClassVar[int]
    NEHPGMLDKMF: _containers.RepeatedCompositeFieldContainer[_GDFFBGABIND_pb2.GDFFBGABIND]
    ODCMKOFFKKL: int
    def __init__(self, NEHPGMLDKMF: _Optional[_Iterable[_Union[_GDFFBGABIND_pb2.GDFFBGABIND, _Mapping]]] = ..., ODCMKOFFKKL: _Optional[int] = ...) -> None: ...
