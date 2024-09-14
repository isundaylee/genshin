from genshin.packet.proto import WeeklyBossResinDiscountInfo_pb2 as _WeeklyBossResinDiscountInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BossChestInfo(_message.Message):
    __slots__ = ("monster_config_id", "resin", "remain_uid_list", "qualify_uid_list", "uid_discount_map")
    class UidDiscountMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _WeeklyBossResinDiscountInfo_pb2.WeeklyBossResinDiscountInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_WeeklyBossResinDiscountInfo_pb2.WeeklyBossResinDiscountInfo, _Mapping]] = ...) -> None: ...
    MONSTER_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    RESIN_FIELD_NUMBER: _ClassVar[int]
    REMAIN_UID_LIST_FIELD_NUMBER: _ClassVar[int]
    QUALIFY_UID_LIST_FIELD_NUMBER: _ClassVar[int]
    UID_DISCOUNT_MAP_FIELD_NUMBER: _ClassVar[int]
    monster_config_id: int
    resin: int
    remain_uid_list: _containers.RepeatedScalarFieldContainer[int]
    qualify_uid_list: _containers.RepeatedScalarFieldContainer[int]
    uid_discount_map: _containers.MessageMap[int, _WeeklyBossResinDiscountInfo_pb2.WeeklyBossResinDiscountInfo]
    def __init__(self, monster_config_id: _Optional[int] = ..., resin: _Optional[int] = ..., remain_uid_list: _Optional[_Iterable[int]] = ..., qualify_uid_list: _Optional[_Iterable[int]] = ..., uid_discount_map: _Optional[_Mapping[int, _WeeklyBossResinDiscountInfo_pb2.WeeklyBossResinDiscountInfo]] = ...) -> None: ...
