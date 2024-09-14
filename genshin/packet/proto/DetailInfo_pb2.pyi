from genshin.packet.proto import DetailAbilityInfo_pb2 as _DetailAbilityInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetailInfo(_message.Message):
    __slots__ = ("detail_ability_info",)
    DETAIL_ABILITY_INFO_FIELD_NUMBER: _ClassVar[int]
    detail_ability_info: _DetailAbilityInfo_pb2.DetailAbilityInfo
    def __init__(self, detail_ability_info: _Optional[_Union[_DetailAbilityInfo_pb2.DetailAbilityInfo, _Mapping]] = ...) -> None: ...
