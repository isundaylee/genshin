from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UpdatePlayerShowAvatarListRsp(_message.Message):
    __slots__ = ("show_avatar_id_list", "retcode", "is_show_avatar", "is_show_constellation_num")
    SHOW_AVATAR_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_AVATAR_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_CONSTELLATION_NUM_FIELD_NUMBER: _ClassVar[int]
    show_avatar_id_list: _containers.RepeatedScalarFieldContainer[int]
    retcode: int
    is_show_avatar: bool
    is_show_constellation_num: bool
    def __init__(self, show_avatar_id_list: _Optional[_Iterable[int]] = ..., retcode: _Optional[int] = ..., is_show_avatar: bool = ..., is_show_constellation_num: bool = ...) -> None: ...
