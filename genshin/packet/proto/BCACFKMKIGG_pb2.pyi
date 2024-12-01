from genshin.packet.proto import FEEMCGMMDCI_pb2 as _FEEMCGMMDCI_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BCACFKMKIGG(_message.Message):
    __slots__ = ("PFELDFFPKLP", "ECIFINMNLND", "EJNINFFFKJP")
    PFELDFFPKLP_FIELD_NUMBER: _ClassVar[int]
    ECIFINMNLND_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    PFELDFFPKLP: _FEEMCGMMDCI_pb2.FEEMCGMMDCI
    ECIFINMNLND: int
    EJNINFFFKJP: int
    def __init__(self, PFELDFFPKLP: _Optional[_Union[_FEEMCGMMDCI_pb2.FEEMCGMMDCI, _Mapping]] = ..., ECIFINMNLND: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
