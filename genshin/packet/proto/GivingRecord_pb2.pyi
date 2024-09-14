from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GivingRecord(_message.Message):
    __slots__ = ("config_id", "is_gadget_giving", "last_group_id", "giving_id", "is_finished", "material_cnt_map", "group_id")
    class MaterialCntMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    IS_GADGET_GIVING_FIELD_NUMBER: _ClassVar[int]
    LAST_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GIVING_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FINISHED_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_CNT_MAP_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    config_id: int
    is_gadget_giving: bool
    last_group_id: int
    giving_id: int
    is_finished: bool
    material_cnt_map: _containers.ScalarMap[int, int]
    group_id: int
    def __init__(self, config_id: _Optional[int] = ..., is_gadget_giving: bool = ..., last_group_id: _Optional[int] = ..., giving_id: _Optional[int] = ..., is_finished: bool = ..., material_cnt_map: _Optional[_Mapping[int, int]] = ..., group_id: _Optional[int] = ...) -> None: ...
