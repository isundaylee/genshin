from genshin.packet.proto import HomeLimitedShopInfo_pb2 as _HomeLimitedShopInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeBasicInfo(_message.Message):
    __slots__ = ("owner_nick_name", "exp", "cur_module_id", "limited_shop_info", "level", "home_owner_uid", "FCMIKLCEAKA", "is_in_edit_mode", "cur_room_scene_id")
    OWNER_NICK_NAME_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    CUR_MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    LIMITED_SHOP_INFO_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    HOME_OWNER_UID_FIELD_NUMBER: _ClassVar[int]
    FCMIKLCEAKA_FIELD_NUMBER: _ClassVar[int]
    IS_IN_EDIT_MODE_FIELD_NUMBER: _ClassVar[int]
    CUR_ROOM_SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    owner_nick_name: str
    exp: int
    cur_module_id: int
    limited_shop_info: _HomeLimitedShopInfo_pb2.HomeLimitedShopInfo
    level: int
    home_owner_uid: int
    FCMIKLCEAKA: int
    is_in_edit_mode: bool
    cur_room_scene_id: int
    def __init__(self, owner_nick_name: _Optional[str] = ..., exp: _Optional[int] = ..., cur_module_id: _Optional[int] = ..., limited_shop_info: _Optional[_Union[_HomeLimitedShopInfo_pb2.HomeLimitedShopInfo, _Mapping]] = ..., level: _Optional[int] = ..., home_owner_uid: _Optional[int] = ..., FCMIKLCEAKA: _Optional[int] = ..., is_in_edit_mode: bool = ..., cur_room_scene_id: _Optional[int] = ...) -> None: ...
