from genshin.packet.proto import CMGOOOMLAIA_pb2 as _CMGOOOMLAIA_pb2
from genshin.packet.proto import KBAIOMIOCCP_pb2 as _KBAIOMIOCCP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CDGHIAOFOEF(_message.Message):
    __slots__ = ("CDGIKFOLBGH", "GJEBAJAJPII", "IMIOGMDOKCB", "LAPFIKCFDFL", "OOIPGFEDJMN")
    CDGIKFOLBGH_FIELD_NUMBER: _ClassVar[int]
    GJEBAJAJPII_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    LAPFIKCFDFL_FIELD_NUMBER: _ClassVar[int]
    OOIPGFEDJMN_FIELD_NUMBER: _ClassVar[int]
    CDGIKFOLBGH: _containers.RepeatedScalarFieldContainer[int]
    GJEBAJAJPII: int
    IMIOGMDOKCB: _CMGOOOMLAIA_pb2.CMGOOOMLAIA
    LAPFIKCFDFL: _KBAIOMIOCCP_pb2.KBAIOMIOCCP
    OOIPGFEDJMN: int
    def __init__(self, CDGIKFOLBGH: _Optional[_Iterable[int]] = ..., GJEBAJAJPII: _Optional[int] = ..., IMIOGMDOKCB: _Optional[_Union[_CMGOOOMLAIA_pb2.CMGOOOMLAIA, str]] = ..., LAPFIKCFDFL: _Optional[_Union[_KBAIOMIOCCP_pb2.KBAIOMIOCCP, str]] = ..., OOIPGFEDJMN: _Optional[int] = ...) -> None: ...
