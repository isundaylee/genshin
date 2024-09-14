from genshin.packet.proto import UgcType_pb2 as _UgcType_pb2
from genshin.packet.proto import UgcMusicBriefInfo_pb2 as _UgcMusicBriefInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUgcBriefInfoRsp(_message.Message):
    __slots__ = ("ugc_type", "ugc_guid", "retcode", "music_brief_info")
    UGC_TYPE_FIELD_NUMBER: _ClassVar[int]
    UGC_GUID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    MUSIC_BRIEF_INFO_FIELD_NUMBER: _ClassVar[int]
    ugc_type: _UgcType_pb2.UgcType
    ugc_guid: int
    retcode: int
    music_brief_info: _UgcMusicBriefInfo_pb2.UgcMusicBriefInfo
    def __init__(self, ugc_type: _Optional[_Union[_UgcType_pb2.UgcType, str]] = ..., ugc_guid: _Optional[int] = ..., retcode: _Optional[int] = ..., music_brief_info: _Optional[_Union[_UgcMusicBriefInfo_pb2.UgcMusicBriefInfo, _Mapping]] = ...) -> None: ...
