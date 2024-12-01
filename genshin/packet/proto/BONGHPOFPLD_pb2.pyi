from genshin.packet.proto import EHLKDKHKIFL_pb2 as _EHLKDKHKIFL_pb2
from genshin.packet.proto import CMGOOOMLAIA_pb2 as _CMGOOOMLAIA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BONGHPOFPLD(_message.Message):
    __slots__ = ("HEPDPIOILGD", "OOIPGFEDJMN", "IMIOGMDOKCB")
    HEPDPIOILGD_FIELD_NUMBER: _ClassVar[int]
    OOIPGFEDJMN_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    HEPDPIOILGD: _containers.RepeatedCompositeFieldContainer[_EHLKDKHKIFL_pb2.EHLKDKHKIFL]
    OOIPGFEDJMN: int
    IMIOGMDOKCB: _CMGOOOMLAIA_pb2.CMGOOOMLAIA
    def __init__(self, HEPDPIOILGD: _Optional[_Iterable[_Union[_EHLKDKHKIFL_pb2.EHLKDKHKIFL, _Mapping]]] = ..., OOIPGFEDJMN: _Optional[int] = ..., IMIOGMDOKCB: _Optional[_Union[_CMGOOOMLAIA_pb2.CMGOOOMLAIA, str]] = ...) -> None: ...
