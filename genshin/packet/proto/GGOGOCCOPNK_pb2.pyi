from genshin.packet.proto import KBAIOMIOCCP_pb2 as _KBAIOMIOCCP_pb2
from genshin.packet.proto import CMGOOOMLAIA_pb2 as _CMGOOOMLAIA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GGOGOCCOPNK(_message.Message):
    __slots__ = ("CDGIKFOLBGH", "OOIPGFEDJMN", "LAPFIKCFDFL", "IMIOGMDOKCB")
    CDGIKFOLBGH_FIELD_NUMBER: _ClassVar[int]
    OOIPGFEDJMN_FIELD_NUMBER: _ClassVar[int]
    LAPFIKCFDFL_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    CDGIKFOLBGH: _containers.RepeatedScalarFieldContainer[int]
    OOIPGFEDJMN: int
    LAPFIKCFDFL: _KBAIOMIOCCP_pb2.KBAIOMIOCCP
    IMIOGMDOKCB: _CMGOOOMLAIA_pb2.CMGOOOMLAIA
    def __init__(self, CDGIKFOLBGH: _Optional[_Iterable[int]] = ..., OOIPGFEDJMN: _Optional[int] = ..., LAPFIKCFDFL: _Optional[_Union[_KBAIOMIOCCP_pb2.KBAIOMIOCCP, str]] = ..., IMIOGMDOKCB: _Optional[_Union[_CMGOOOMLAIA_pb2.CMGOOOMLAIA, str]] = ...) -> None: ...
