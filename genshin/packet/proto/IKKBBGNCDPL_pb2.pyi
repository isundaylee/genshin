from genshin.packet.proto import JJHOBJBAPEI_pb2 as _JJHOBJBAPEI_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IKKBBGNCDPL(_message.Message):
    __slots__ = ("GAAKALGOBCF", "EOGLFOGEKLA", "AGIDBEEINDE", "GJEBAJAJPII")
    GAAKALGOBCF_FIELD_NUMBER: _ClassVar[int]
    EOGLFOGEKLA_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    GJEBAJAJPII_FIELD_NUMBER: _ClassVar[int]
    GAAKALGOBCF: _JJHOBJBAPEI_pb2.JJHOBJBAPEI
    EOGLFOGEKLA: bool
    AGIDBEEINDE: int
    GJEBAJAJPII: int
    def __init__(self, GAAKALGOBCF: _Optional[_Union[_JJHOBJBAPEI_pb2.JJHOBJBAPEI, str]] = ..., EOGLFOGEKLA: bool = ..., AGIDBEEINDE: _Optional[int] = ..., GJEBAJAJPII: _Optional[int] = ...) -> None: ...
