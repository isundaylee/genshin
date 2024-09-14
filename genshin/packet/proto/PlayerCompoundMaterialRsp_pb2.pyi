from genshin.packet.proto import CompoundQueueData_pb2 as _CompoundQueueData_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerCompoundMaterialRsp(_message.Message):
    __slots__ = ("retcode", "compoundQueueData")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    COMPOUNDQUEUEDATA_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    compoundQueueData: _CompoundQueueData_pb2.CompoundQueueData
    def __init__(self, retcode: _Optional[int] = ..., compoundQueueData: _Optional[_Union[_CompoundQueueData_pb2.CompoundQueueData, _Mapping]] = ...) -> None: ...
