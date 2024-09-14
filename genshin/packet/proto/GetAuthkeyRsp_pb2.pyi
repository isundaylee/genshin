from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetAuthkeyRsp(_message.Message):
    __slots__ = ("retcode", "auth_appid", "game_biz", "sign_type", "authkey_ver", "authkey")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    AUTH_APPID_FIELD_NUMBER: _ClassVar[int]
    GAME_BIZ_FIELD_NUMBER: _ClassVar[int]
    SIGN_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTHKEY_VER_FIELD_NUMBER: _ClassVar[int]
    AUTHKEY_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    auth_appid: str
    game_biz: str
    sign_type: int
    authkey_ver: int
    authkey: str
    def __init__(self, retcode: _Optional[int] = ..., auth_appid: _Optional[str] = ..., game_biz: _Optional[str] = ..., sign_type: _Optional[int] = ..., authkey_ver: _Optional[int] = ..., authkey: _Optional[str] = ...) -> None: ...
