from genshin.packet.proto import PMNJNCLEONJ_pb2 as _PMNJNCLEONJ_pb2
from genshin.packet.proto import KGPHJFJGGDJ_pb2 as _KGPHJFJGGDJ_pb2
from genshin.packet.proto import OOJGOKPCGNJ_pb2 as _OOJGOKPCGNJ_pb2
from genshin.packet.proto import NJFHDJNKJKK_pb2 as _NJFHDJNKJKK_pb2
from genshin.packet.proto import LLCGHKFBADC_pb2 as _LLCGHKFBADC_pb2
from genshin.packet.proto import PFNKKMIOAEE_pb2 as _PFNKKMIOAEE_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KJGMHFIGABD(_message.Message):
    __slots__ = ("EJNINFFFKJP", "ENOEKKLHBNH", "sync_snap_shot", "sync_finish_game", "sync_create_connect", "sync_ping", "sync_action")
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    ENOEKKLHBNH_FIELD_NUMBER: _ClassVar[int]
    SYNC_SNAP_SHOT_FIELD_NUMBER: _ClassVar[int]
    SYNC_FINISH_GAME_FIELD_NUMBER: _ClassVar[int]
    SYNC_CREATE_CONNECT_FIELD_NUMBER: _ClassVar[int]
    SYNC_PING_FIELD_NUMBER: _ClassVar[int]
    SYNC_ACTION_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP: int
    ENOEKKLHBNH: _PMNJNCLEONJ_pb2.PMNJNCLEONJ
    sync_snap_shot: _KGPHJFJGGDJ_pb2.KGPHJFJGGDJ
    sync_finish_game: _OOJGOKPCGNJ_pb2.OOJGOKPCGNJ
    sync_create_connect: _NJFHDJNKJKK_pb2.NJFHDJNKJKK
    sync_ping: _LLCGHKFBADC_pb2.LLCGHKFBADC
    sync_action: _PFNKKMIOAEE_pb2.PFNKKMIOAEE
    def __init__(self, EJNINFFFKJP: _Optional[int] = ..., ENOEKKLHBNH: _Optional[_Union[_PMNJNCLEONJ_pb2.PMNJNCLEONJ, str]] = ..., sync_snap_shot: _Optional[_Union[_KGPHJFJGGDJ_pb2.KGPHJFJGGDJ, _Mapping]] = ..., sync_finish_game: _Optional[_Union[_OOJGOKPCGNJ_pb2.OOJGOKPCGNJ, _Mapping]] = ..., sync_create_connect: _Optional[_Union[_NJFHDJNKJKK_pb2.NJFHDJNKJKK, _Mapping]] = ..., sync_ping: _Optional[_Union[_LLCGHKFBADC_pb2.LLCGHKFBADC, _Mapping]] = ..., sync_action: _Optional[_Union[_PFNKKMIOAEE_pb2.PFNKKMIOAEE, _Mapping]] = ...) -> None: ...
