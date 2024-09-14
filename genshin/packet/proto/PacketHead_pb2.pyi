from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PacketHead(_message.Message):
    __slots__ = ("packet_id", "rpc_id", "client_sequence_id", "enet_channel_id", "enet_is_reliable", "sent_ms", "user_id", "user_ip", "user_session_id", "recv_time_ms", "rpc_begin_time_ms", "ext_map", "sender_app_id", "source_service", "target_service", "service_app_id_map", "is_set_game_thread", "game_thread_index")
    class ExtMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class ServiceAppIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PACKET_ID_FIELD_NUMBER: _ClassVar[int]
    RPC_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    ENET_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ENET_IS_RELIABLE_FIELD_NUMBER: _ClassVar[int]
    SENT_MS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IP_FIELD_NUMBER: _ClassVar[int]
    USER_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    RECV_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    RPC_BEGIN_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    EXT_MAP_FIELD_NUMBER: _ClassVar[int]
    SENDER_APP_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SERVICE_FIELD_NUMBER: _ClassVar[int]
    TARGET_SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_APP_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    IS_SET_GAME_THREAD_FIELD_NUMBER: _ClassVar[int]
    GAME_THREAD_INDEX_FIELD_NUMBER: _ClassVar[int]
    packet_id: int
    rpc_id: int
    client_sequence_id: int
    enet_channel_id: int
    enet_is_reliable: int
    sent_ms: int
    user_id: int
    user_ip: int
    user_session_id: int
    recv_time_ms: int
    rpc_begin_time_ms: int
    ext_map: _containers.ScalarMap[int, int]
    sender_app_id: int
    source_service: int
    target_service: int
    service_app_id_map: _containers.ScalarMap[int, int]
    is_set_game_thread: bool
    game_thread_index: int
    def __init__(self, packet_id: _Optional[int] = ..., rpc_id: _Optional[int] = ..., client_sequence_id: _Optional[int] = ..., enet_channel_id: _Optional[int] = ..., enet_is_reliable: _Optional[int] = ..., sent_ms: _Optional[int] = ..., user_id: _Optional[int] = ..., user_ip: _Optional[int] = ..., user_session_id: _Optional[int] = ..., recv_time_ms: _Optional[int] = ..., rpc_begin_time_ms: _Optional[int] = ..., ext_map: _Optional[_Mapping[int, int]] = ..., sender_app_id: _Optional[int] = ..., source_service: _Optional[int] = ..., target_service: _Optional[int] = ..., service_app_id_map: _Optional[_Mapping[int, int]] = ..., is_set_game_thread: bool = ..., game_thread_index: _Optional[int] = ...) -> None: ...
