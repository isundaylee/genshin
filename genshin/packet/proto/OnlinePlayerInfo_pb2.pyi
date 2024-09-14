from genshin.packet.proto import MpSettingType_pb2 as _MpSettingType_pb2
from genshin.packet.proto import ProfilePicture_pb2 as _ProfilePicture_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OnlinePlayerInfo(_message.Message):
    __slots__ = ("uid", "nickname", "cur_player_num_in_world", "avatar_id", "mp_setting_type", "player_level", "world_level", "online_id", "name_card_id", "blacklist_uid_list", "signature", "profile_picture", "psn_id")
    UID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    CUR_PLAYER_NUM_IN_WORLD_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    MP_SETTING_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    WORLD_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ONLINE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_CARD_ID_FIELD_NUMBER: _ClassVar[int]
    BLACKLIST_UID_LIST_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PICTURE_FIELD_NUMBER: _ClassVar[int]
    PSN_ID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    nickname: str
    cur_player_num_in_world: int
    avatar_id: int
    mp_setting_type: _MpSettingType_pb2.MpSettingType
    player_level: int
    world_level: int
    online_id: str
    name_card_id: int
    blacklist_uid_list: _containers.RepeatedScalarFieldContainer[int]
    signature: str
    profile_picture: _ProfilePicture_pb2.ProfilePicture
    psn_id: str
    def __init__(self, uid: _Optional[int] = ..., nickname: _Optional[str] = ..., cur_player_num_in_world: _Optional[int] = ..., avatar_id: _Optional[int] = ..., mp_setting_type: _Optional[_Union[_MpSettingType_pb2.MpSettingType, str]] = ..., player_level: _Optional[int] = ..., world_level: _Optional[int] = ..., online_id: _Optional[str] = ..., name_card_id: _Optional[int] = ..., blacklist_uid_list: _Optional[_Iterable[int]] = ..., signature: _Optional[str] = ..., profile_picture: _Optional[_Union[_ProfilePicture_pb2.ProfilePicture, _Mapping]] = ..., psn_id: _Optional[str] = ...) -> None: ...
