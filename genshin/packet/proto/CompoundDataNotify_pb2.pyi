from genshin.packet.proto import CompoundQueueData_pb2 as _CompoundQueueData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompoundDataNotify(_message.Message):
    __slots__ = ("compoundQueueDataList", "unlockCompoundList")
    COMPOUNDQUEUEDATALIST_FIELD_NUMBER: _ClassVar[int]
    UNLOCKCOMPOUNDLIST_FIELD_NUMBER: _ClassVar[int]
    compoundQueueDataList: _containers.RepeatedCompositeFieldContainer[_CompoundQueueData_pb2.CompoundQueueData]
    unlockCompoundList: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, compoundQueueDataList: _Optional[_Iterable[_Union[_CompoundQueueData_pb2.CompoundQueueData, _Mapping]]] = ..., unlockCompoundList: _Optional[_Iterable[int]] = ...) -> None: ...
