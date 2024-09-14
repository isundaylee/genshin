from genshin.packet.proto import GetUgcType_pb2 as _GetUgcType_pb2
from genshin.packet.proto import UgcType_pb2 as _UgcType_pb2
from genshin.packet.proto import RecordUsage_pb2 as _RecordUsage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUgcReq(_message.Message):
    __slots__ = ("get_ugc_type", "ugc_type", "is_require_brief", "ugc_guid", "ugc_record_usage", "schedule_id")
    GET_UGC_TYPE_FIELD_NUMBER: _ClassVar[int]
    UGC_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_REQUIRE_BRIEF_FIELD_NUMBER: _ClassVar[int]
    UGC_GUID_FIELD_NUMBER: _ClassVar[int]
    UGC_RECORD_USAGE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    get_ugc_type: _GetUgcType_pb2.GetUgcType
    ugc_type: _UgcType_pb2.UgcType
    is_require_brief: bool
    ugc_guid: int
    ugc_record_usage: _RecordUsage_pb2.RecordUsage
    schedule_id: int
    def __init__(self, get_ugc_type: _Optional[_Union[_GetUgcType_pb2.GetUgcType, str]] = ..., ugc_type: _Optional[_Union[_UgcType_pb2.UgcType, str]] = ..., is_require_brief: bool = ..., ugc_guid: _Optional[int] = ..., ugc_record_usage: _Optional[_Union[_RecordUsage_pb2.RecordUsage, str]] = ..., schedule_id: _Optional[int] = ...) -> None: ...
