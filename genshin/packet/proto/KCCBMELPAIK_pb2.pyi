from genshin.packet.proto import LIPHHIENHHK_pb2 as _LIPHHIENHHK_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KCCBMELPAIK(_message.Message):
    __slots__ = ("GFMEKOGIHJN", "AGIDBEEINDE")
    GFMEKOGIHJN_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    GFMEKOGIHJN: _LIPHHIENHHK_pb2.LIPHHIENHHK
    AGIDBEEINDE: int
    def __init__(self, GFMEKOGIHJN: _Optional[_Union[_LIPHHIENHHK_pb2.LIPHHIENHHK, _Mapping]] = ..., AGIDBEEINDE: _Optional[int] = ...) -> None: ...
