from genshin.packet.proto import EOABCGEOJHI_pb2 as _EOABCGEOJHI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DGBKPBINNJE(_message.Message):
    __slots__ = ("BAGJBBKNADL", "EAIPGEMKNPO", "GLKNGDDNOCN")
    BAGJBBKNADL_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    BAGJBBKNADL: _containers.RepeatedCompositeFieldContainer[_EOABCGEOJHI_pb2.EOABCGEOJHI]
    EAIPGEMKNPO: int
    GLKNGDDNOCN: bool
    def __init__(self, BAGJBBKNADL: _Optional[_Iterable[_Union[_EOABCGEOJHI_pb2.EOABCGEOJHI, _Mapping]]] = ..., EAIPGEMKNPO: _Optional[int] = ..., GLKNGDDNOCN: bool = ...) -> None: ...
