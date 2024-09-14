from genshin.packet.proto import UgcType_pb2 as _UgcType_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CheckUgcUpdateRsp(_message.Message):
    __slots__ = ("retcode", "update_ugc_guid_list", "ugc_type")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_UGC_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    UGC_TYPE_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    update_ugc_guid_list: _containers.RepeatedScalarFieldContainer[int]
    ugc_type: _UgcType_pb2.UgcType
    def __init__(self, retcode: _Optional[int] = ..., update_ugc_guid_list: _Optional[_Iterable[int]] = ..., ugc_type: _Optional[_Union[_UgcType_pb2.UgcType, str]] = ...) -> None: ...
