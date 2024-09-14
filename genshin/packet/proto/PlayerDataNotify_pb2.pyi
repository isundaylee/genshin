from genshin.packet.proto import PropValue_pb2 as _PropValue_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerDataNotify(_message.Message):
    __slots__ = ("nick_name", "is_first_login_today", "region_id", "prop_map", "server_time")
    class PropMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _PropValue_pb2.PropValue
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_PropValue_pb2.PropValue, _Mapping]] = ...) -> None: ...
    NICK_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_FIRST_LOGIN_TODAY_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    PROP_MAP_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    nick_name: str
    is_first_login_today: bool
    region_id: int
    prop_map: _containers.MessageMap[int, _PropValue_pb2.PropValue]
    server_time: int
    def __init__(self, nick_name: _Optional[str] = ..., is_first_login_today: bool = ..., region_id: _Optional[int] = ..., prop_map: _Optional[_Mapping[int, _PropValue_pb2.PropValue]] = ..., server_time: _Optional[int] = ...) -> None: ...
