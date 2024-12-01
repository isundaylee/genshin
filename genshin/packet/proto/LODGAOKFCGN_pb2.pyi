from genshin.packet.proto import PKBDLALMJML_pb2 as _PKBDLALMJML_pb2
from genshin.packet.proto import IELANAFKGKO_pb2 as _IELANAFKGKO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LODGAOKFCGN(_message.Message):
    __slots__ = ("DDKBFLGFCOI", "order_info", "exam_info")
    DDKBFLGFCOI_FIELD_NUMBER: _ClassVar[int]
    ORDER_INFO_FIELD_NUMBER: _ClassVar[int]
    EXAM_INFO_FIELD_NUMBER: _ClassVar[int]
    DDKBFLGFCOI: _containers.RepeatedScalarFieldContainer[int]
    order_info: _PKBDLALMJML_pb2.PKBDLALMJML
    exam_info: _IELANAFKGKO_pb2.IELANAFKGKO
    def __init__(self, DDKBFLGFCOI: _Optional[_Iterable[int]] = ..., order_info: _Optional[_Union[_PKBDLALMJML_pb2.PKBDLALMJML, _Mapping]] = ..., exam_info: _Optional[_Union[_IELANAFKGKO_pb2.IELANAFKGKO, _Mapping]] = ...) -> None: ...
