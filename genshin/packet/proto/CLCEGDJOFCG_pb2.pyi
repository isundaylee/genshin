from genshin.packet.proto import CBMCENPMIHI_pb2 as _CBMCENPMIHI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CLCEGDJOFCG(_message.Message):
    __slots__ = ("MKIFGEHEBLD", "DBFGJNBBDKC")
    MKIFGEHEBLD_FIELD_NUMBER: _ClassVar[int]
    DBFGJNBBDKC_FIELD_NUMBER: _ClassVar[int]
    MKIFGEHEBLD: _containers.RepeatedCompositeFieldContainer[_CBMCENPMIHI_pb2.CBMCENPMIHI]
    DBFGJNBBDKC: int
    def __init__(self, MKIFGEHEBLD: _Optional[_Iterable[_Union[_CBMCENPMIHI_pb2.CBMCENPMIHI, _Mapping]]] = ..., DBFGJNBBDKC: _Optional[int] = ...) -> None: ...
