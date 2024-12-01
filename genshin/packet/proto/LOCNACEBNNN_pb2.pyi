from genshin.packet.proto import IBOEPABCDMC_pb2 as _IBOEPABCDMC_pb2
from genshin.packet.proto import FDNFFENOFKF_pb2 as _FDNFFENOFKF_pb2
from genshin.packet.proto import JGCGFHPEIJM_pb2 as _JGCGFHPEIJM_pb2
from genshin.packet.proto import MCLPEEKLGMC_pb2 as _MCLPEEKLGMC_pb2
from genshin.packet.proto import EMEKKIANDLE_pb2 as _EMEKKIANDLE_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LOCNACEBNNN(_message.Message):
    __slots__ = ("sorush_info", "creator_info", "camera_info", "thunder_bird_feather_info", "location_info", "KJFPPJKHCAO")
    SORUSH_INFO_FIELD_NUMBER: _ClassVar[int]
    CREATOR_INFO_FIELD_NUMBER: _ClassVar[int]
    CAMERA_INFO_FIELD_NUMBER: _ClassVar[int]
    THUNDER_BIRD_FEATHER_INFO_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    KJFPPJKHCAO_FIELD_NUMBER: _ClassVar[int]
    sorush_info: _IBOEPABCDMC_pb2.IBOEPABCDMC
    creator_info: _FDNFFENOFKF_pb2.FDNFFENOFKF
    camera_info: _JGCGFHPEIJM_pb2.JGCGFHPEIJM
    thunder_bird_feather_info: _MCLPEEKLGMC_pb2.MCLPEEKLGMC
    location_info: _EMEKKIANDLE_pb2.EMEKKIANDLE
    KJFPPJKHCAO: bool
    def __init__(self, sorush_info: _Optional[_Union[_IBOEPABCDMC_pb2.IBOEPABCDMC, _Mapping]] = ..., creator_info: _Optional[_Union[_FDNFFENOFKF_pb2.FDNFFENOFKF, _Mapping]] = ..., camera_info: _Optional[_Union[_JGCGFHPEIJM_pb2.JGCGFHPEIJM, _Mapping]] = ..., thunder_bird_feather_info: _Optional[_Union[_MCLPEEKLGMC_pb2.MCLPEEKLGMC, _Mapping]] = ..., location_info: _Optional[_Union[_EMEKKIANDLE_pb2.EMEKKIANDLE, _Mapping]] = ..., KJFPPJKHCAO: bool = ...) -> None: ...
