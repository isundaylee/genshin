from genshin.packet.proto import CompoundQueueData_pb2 as _CompoundQueueData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetCompoundDataRsp(_message.Message):
    __slots__ = ("retcode", "unlockCompoundList", "compoundQueueDataList")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    UNLOCKCOMPOUNDLIST_FIELD_NUMBER: _ClassVar[int]
    COMPOUNDQUEUEDATALIST_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    unlockCompoundList: _containers.RepeatedScalarFieldContainer[int]
    compoundQueueDataList: _containers.RepeatedCompositeFieldContainer[_CompoundQueueData_pb2.CompoundQueueData]
    def __init__(self, retcode: _Optional[int] = ..., unlockCompoundList: _Optional[_Iterable[int]] = ..., compoundQueueDataList: _Optional[_Iterable[_Union[_CompoundQueueData_pb2.CompoundQueueData, _Mapping]]] = ...) -> None: ...
