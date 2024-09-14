from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetAuthkeyReq(_message.Message):
    __slots__ = ("auth_appid", "authkey_ver", "sign_type")
    AUTH_APPID_FIELD_NUMBER: _ClassVar[int]
    AUTHKEY_VER_FIELD_NUMBER: _ClassVar[int]
    SIGN_TYPE_FIELD_NUMBER: _ClassVar[int]
    auth_appid: str
    authkey_ver: int
    sign_type: int
    def __init__(self, auth_appid: _Optional[str] = ..., authkey_ver: _Optional[int] = ..., sign_type: _Optional[int] = ...) -> None: ...
