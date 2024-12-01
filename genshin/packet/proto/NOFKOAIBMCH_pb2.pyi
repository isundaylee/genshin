from genshin.packet.proto import HDHMIANBIHC_pb2 as _HDHMIANBIHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NOFKOAIBMCH(_message.Message):
    __slots__ = ("JNJLFLJNHCJ", "IDFMKKFIEGO")
    JNJLFLJNHCJ_FIELD_NUMBER: _ClassVar[int]
    IDFMKKFIEGO_FIELD_NUMBER: _ClassVar[int]
    JNJLFLJNHCJ: _containers.RepeatedCompositeFieldContainer[_HDHMIANBIHC_pb2.HDHMIANBIHC]
    IDFMKKFIEGO: int
    def __init__(self, JNJLFLJNHCJ: _Optional[_Iterable[_Union[_HDHMIANBIHC_pb2.HDHMIANBIHC, _Mapping]]] = ..., IDFMKKFIEGO: _Optional[int] = ...) -> None: ...
