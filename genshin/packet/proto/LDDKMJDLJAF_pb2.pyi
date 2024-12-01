from genshin.packet.proto import CHGNHDCHNDD_pb2 as _CHGNHDCHNDD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LDDKMJDLJAF(_message.Message):
    __slots__ = ("GMCBENMCOKN", "JDGLALAAHIG")
    GMCBENMCOKN_FIELD_NUMBER: _ClassVar[int]
    JDGLALAAHIG_FIELD_NUMBER: _ClassVar[int]
    GMCBENMCOKN: _containers.RepeatedCompositeFieldContainer[_CHGNHDCHNDD_pb2.CHGNHDCHNDD]
    JDGLALAAHIG: int
    def __init__(self, GMCBENMCOKN: _Optional[_Iterable[_Union[_CHGNHDCHNDD_pb2.CHGNHDCHNDD, _Mapping]]] = ..., JDGLALAAHIG: _Optional[int] = ...) -> None: ...
