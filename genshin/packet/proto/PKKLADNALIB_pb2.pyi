from genshin.packet.proto import CMGOOOMLAIA_pb2 as _CMGOOOMLAIA_pb2
from genshin.packet.proto import KBAIOMIOCCP_pb2 as _KBAIOMIOCCP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PKKLADNALIB(_message.Message):
    __slots__ = ("ACCDKGEOICN", "CDGIKFOLBGH", "IMIOGMDOKCB", "LKPBOEINOGN", "OOIPGFEDJMN", "JFCOFCLPEOE")
    ACCDKGEOICN_FIELD_NUMBER: _ClassVar[int]
    CDGIKFOLBGH_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    LKPBOEINOGN_FIELD_NUMBER: _ClassVar[int]
    OOIPGFEDJMN_FIELD_NUMBER: _ClassVar[int]
    JFCOFCLPEOE_FIELD_NUMBER: _ClassVar[int]
    ACCDKGEOICN: _containers.RepeatedScalarFieldContainer[int]
    CDGIKFOLBGH: _containers.RepeatedScalarFieldContainer[int]
    IMIOGMDOKCB: _CMGOOOMLAIA_pb2.CMGOOOMLAIA
    LKPBOEINOGN: _KBAIOMIOCCP_pb2.KBAIOMIOCCP
    OOIPGFEDJMN: int
    JFCOFCLPEOE: _KBAIOMIOCCP_pb2.KBAIOMIOCCP
    def __init__(self, ACCDKGEOICN: _Optional[_Iterable[int]] = ..., CDGIKFOLBGH: _Optional[_Iterable[int]] = ..., IMIOGMDOKCB: _Optional[_Union[_CMGOOOMLAIA_pb2.CMGOOOMLAIA, str]] = ..., LKPBOEINOGN: _Optional[_Union[_KBAIOMIOCCP_pb2.KBAIOMIOCCP, str]] = ..., OOIPGFEDJMN: _Optional[int] = ..., JFCOFCLPEOE: _Optional[_Union[_KBAIOMIOCCP_pb2.KBAIOMIOCCP, str]] = ...) -> None: ...
