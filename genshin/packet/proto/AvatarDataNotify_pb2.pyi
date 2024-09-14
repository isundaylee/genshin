from genshin.packet.proto import AvatarInfo_pb2 as _AvatarInfo_pb2
from genshin.packet.proto import AvatarTeam_pb2 as _AvatarTeam_pb2
from genshin.packet.proto import AvatarRenameInfo_pb2 as _AvatarRenameInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarDataNotify(_message.Message):
    __slots__ = ("ONAODHDMILI", "temp_avatar_guid_list", "cur_avatar_team_id", "avatar_list", "backup_avatar_team_order_list", "avatar_team_map", "owned_flycloak_list", "owned_costume_list", "avatar_rename_list", "choose_avatar_guid")
    class AvatarTeamMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _AvatarTeam_pb2.AvatarTeam
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_AvatarTeam_pb2.AvatarTeam, _Mapping]] = ...) -> None: ...
    ONAODHDMILI_FIELD_NUMBER: _ClassVar[int]
    TEMP_AVATAR_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    CUR_AVATAR_TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_LIST_FIELD_NUMBER: _ClassVar[int]
    BACKUP_AVATAR_TEAM_ORDER_LIST_FIELD_NUMBER: _ClassVar[int]
    AVATAR_TEAM_MAP_FIELD_NUMBER: _ClassVar[int]
    OWNED_FLYCLOAK_LIST_FIELD_NUMBER: _ClassVar[int]
    OWNED_COSTUME_LIST_FIELD_NUMBER: _ClassVar[int]
    AVATAR_RENAME_LIST_FIELD_NUMBER: _ClassVar[int]
    CHOOSE_AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    ONAODHDMILI: _containers.RepeatedScalarFieldContainer[int]
    temp_avatar_guid_list: _containers.RepeatedScalarFieldContainer[int]
    cur_avatar_team_id: int
    avatar_list: _containers.RepeatedCompositeFieldContainer[_AvatarInfo_pb2.AvatarInfo]
    backup_avatar_team_order_list: _containers.RepeatedScalarFieldContainer[int]
    avatar_team_map: _containers.MessageMap[int, _AvatarTeam_pb2.AvatarTeam]
    owned_flycloak_list: _containers.RepeatedScalarFieldContainer[int]
    owned_costume_list: _containers.RepeatedScalarFieldContainer[int]
    avatar_rename_list: _containers.RepeatedCompositeFieldContainer[_AvatarRenameInfo_pb2.AvatarRenameInfo]
    choose_avatar_guid: int
    def __init__(self, ONAODHDMILI: _Optional[_Iterable[int]] = ..., temp_avatar_guid_list: _Optional[_Iterable[int]] = ..., cur_avatar_team_id: _Optional[int] = ..., avatar_list: _Optional[_Iterable[_Union[_AvatarInfo_pb2.AvatarInfo, _Mapping]]] = ..., backup_avatar_team_order_list: _Optional[_Iterable[int]] = ..., avatar_team_map: _Optional[_Mapping[int, _AvatarTeam_pb2.AvatarTeam]] = ..., owned_flycloak_list: _Optional[_Iterable[int]] = ..., owned_costume_list: _Optional[_Iterable[int]] = ..., avatar_rename_list: _Optional[_Iterable[_Union[_AvatarRenameInfo_pb2.AvatarRenameInfo, _Mapping]]] = ..., choose_avatar_guid: _Optional[int] = ...) -> None: ...
