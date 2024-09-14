from genshin.packet.proto import GivingRecord_pb2 as _GivingRecord_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GivingRecordNotify(_message.Message):
    __slots__ = ("giving_record_list",)
    GIVING_RECORD_LIST_FIELD_NUMBER: _ClassVar[int]
    giving_record_list: _containers.RepeatedCompositeFieldContainer[_GivingRecord_pb2.GivingRecord]
    def __init__(self, giving_record_list: _Optional[_Iterable[_Union[_GivingRecord_pb2.GivingRecord, _Mapping]]] = ...) -> None: ...
