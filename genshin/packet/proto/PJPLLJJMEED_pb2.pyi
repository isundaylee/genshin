from genshin.packet.proto import BKJKCHOKLKG_pb2 as _BKJKCHOKLKG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PJPLLJJMEED(_message.Message):
    __slots__ = ("LOIHNGEDHEA", "EKEACKKIEGH")
    LOIHNGEDHEA_FIELD_NUMBER: _ClassVar[int]
    EKEACKKIEGH_FIELD_NUMBER: _ClassVar[int]
    LOIHNGEDHEA: _containers.RepeatedCompositeFieldContainer[_BKJKCHOKLKG_pb2.BKJKCHOKLKG]
    EKEACKKIEGH: int
    def __init__(self, LOIHNGEDHEA: _Optional[_Iterable[_Union[_BKJKCHOKLKG_pb2.BKJKCHOKLKG, _Mapping]]] = ..., EKEACKKIEGH: _Optional[int] = ...) -> None: ...
