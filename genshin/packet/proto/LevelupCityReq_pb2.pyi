from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LevelupCityReq(_message.Message):
    __slots__ = ("item_num", "area_id", "scene_id")
    ITEM_NUM_FIELD_NUMBER: _ClassVar[int]
    AREA_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    item_num: int
    area_id: int
    scene_id: int
    def __init__(self, item_num: _Optional[int] = ..., area_id: _Optional[int] = ..., scene_id: _Optional[int] = ...) -> None: ...
