from genshin.packet.proto import GachaInfo_pb2 as _GachaInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetGachaInfoRsp(_message.Message):
    __slots__ = ("gacha_random", "retcode", "gacha_info_list", "is_under_minors_restrict", "is_under_general_restrict", "daily_gacha_times")
    GACHA_RANDOM_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    GACHA_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_UNDER_MINORS_RESTRICT_FIELD_NUMBER: _ClassVar[int]
    IS_UNDER_GENERAL_RESTRICT_FIELD_NUMBER: _ClassVar[int]
    DAILY_GACHA_TIMES_FIELD_NUMBER: _ClassVar[int]
    gacha_random: int
    retcode: int
    gacha_info_list: _containers.RepeatedCompositeFieldContainer[_GachaInfo_pb2.GachaInfo]
    is_under_minors_restrict: bool
    is_under_general_restrict: bool
    daily_gacha_times: int
    def __init__(self, gacha_random: _Optional[int] = ..., retcode: _Optional[int] = ..., gacha_info_list: _Optional[_Iterable[_Union[_GachaInfo_pb2.GachaInfo, _Mapping]]] = ..., is_under_minors_restrict: bool = ..., is_under_general_restrict: bool = ..., daily_gacha_times: _Optional[int] = ...) -> None: ...
