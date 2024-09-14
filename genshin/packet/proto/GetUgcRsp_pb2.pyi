from genshin.packet.proto import RecordUsage_pb2 as _RecordUsage_pb2
from genshin.packet.proto import UgcType_pb2 as _UgcType_pb2
from genshin.packet.proto import UgcMusicRecord_pb2 as _UgcMusicRecord_pb2
from genshin.packet.proto import UgcMusicBriefInfo_pb2 as _UgcMusicBriefInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUgcRsp(_message.Message):
    __slots__ = ("ugc_record_usage", "ugc_guid", "retcode", "ugc_type", "music_record", "music_brief_info")
    UGC_RECORD_USAGE_FIELD_NUMBER: _ClassVar[int]
    UGC_GUID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    UGC_TYPE_FIELD_NUMBER: _ClassVar[int]
    MUSIC_RECORD_FIELD_NUMBER: _ClassVar[int]
    MUSIC_BRIEF_INFO_FIELD_NUMBER: _ClassVar[int]
    ugc_record_usage: _RecordUsage_pb2.RecordUsage
    ugc_guid: int
    retcode: int
    ugc_type: _UgcType_pb2.UgcType
    music_record: _UgcMusicRecord_pb2.UgcMusicRecord
    music_brief_info: _UgcMusicBriefInfo_pb2.UgcMusicBriefInfo
    def __init__(self, ugc_record_usage: _Optional[_Union[_RecordUsage_pb2.RecordUsage, str]] = ..., ugc_guid: _Optional[int] = ..., retcode: _Optional[int] = ..., ugc_type: _Optional[_Union[_UgcType_pb2.UgcType, str]] = ..., music_record: _Optional[_Union[_UgcMusicRecord_pb2.UgcMusicRecord, _Mapping]] = ..., music_brief_info: _Optional[_Union[_UgcMusicBriefInfo_pb2.UgcMusicBriefInfo, _Mapping]] = ...) -> None: ...
