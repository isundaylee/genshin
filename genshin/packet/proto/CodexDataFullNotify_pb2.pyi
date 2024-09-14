from genshin.packet.proto import CodexTypeData_pb2 as _CodexTypeData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CodexDataFullNotify(_message.Message):
    __slots__ = ("recent_viewed_pushtips_list", "type_data_list")
    RECENT_VIEWED_PUSHTIPS_LIST_FIELD_NUMBER: _ClassVar[int]
    TYPE_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    recent_viewed_pushtips_list: _containers.RepeatedScalarFieldContainer[int]
    type_data_list: _containers.RepeatedCompositeFieldContainer[_CodexTypeData_pb2.CodexTypeData]
    def __init__(self, recent_viewed_pushtips_list: _Optional[_Iterable[int]] = ..., type_data_list: _Optional[_Iterable[_Union[_CodexTypeData_pb2.CodexTypeData, _Mapping]]] = ...) -> None: ...
