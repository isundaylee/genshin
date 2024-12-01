from genshin.packet.proto import DECPHDLMILB_pb2 as _DECPHDLMILB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JIICLALONNO(_message.Message):
    __slots__ = ("ELEOLJDIADF", "IGBDOEBPPHO")
    ELEOLJDIADF_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    ELEOLJDIADF: _containers.RepeatedCompositeFieldContainer[_DECPHDLMILB_pb2.DECPHDLMILB]
    IGBDOEBPPHO: int
    def __init__(self, ELEOLJDIADF: _Optional[_Iterable[_Union[_DECPHDLMILB_pb2.DECPHDLMILB, _Mapping]]] = ..., IGBDOEBPPHO: _Optional[int] = ...) -> None: ...
