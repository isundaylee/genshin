from genshin.packet.proto import KBAIOMIOCCP_pb2 as _KBAIOMIOCCP_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AEBOJMLMBGE(_message.Message):
    __slots__ = ("JMLABOBCLDE", "OOIPGFEDJMN")
    JMLABOBCLDE_FIELD_NUMBER: _ClassVar[int]
    OOIPGFEDJMN_FIELD_NUMBER: _ClassVar[int]
    JMLABOBCLDE: _KBAIOMIOCCP_pb2.KBAIOMIOCCP
    OOIPGFEDJMN: int
    def __init__(self, JMLABOBCLDE: _Optional[_Union[_KBAIOMIOCCP_pb2.KBAIOMIOCCP, str]] = ..., OOIPGFEDJMN: _Optional[int] = ...) -> None: ...
