from genshin.packet.proto import HDNFFPFFNDN_pb2 as _HDNFFPFFNDN_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PCLLABLBNGA(_message.Message):
    __slots__ = ("NMLMHPPDLIB", "BDNKLFDGOHK")
    NMLMHPPDLIB_FIELD_NUMBER: _ClassVar[int]
    BDNKLFDGOHK_FIELD_NUMBER: _ClassVar[int]
    NMLMHPPDLIB: _HDNFFPFFNDN_pb2.HDNFFPFFNDN
    BDNKLFDGOHK: int
    def __init__(self, NMLMHPPDLIB: _Optional[_Union[_HDNFFPFFNDN_pb2.HDNFFPFFNDN, _Mapping]] = ..., BDNKLFDGOHK: _Optional[int] = ...) -> None: ...
