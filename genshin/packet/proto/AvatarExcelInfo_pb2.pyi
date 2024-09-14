from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarExcelInfo(_message.Message):
    __slots__ = ("prefab_path_hash", "prefab_path_remote_hash", "controller_path_hash", "controller_path_remote_hash", "combat_config_hash")
    PREFAB_PATH_HASH_FIELD_NUMBER: _ClassVar[int]
    PREFAB_PATH_REMOTE_HASH_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_PATH_HASH_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_PATH_REMOTE_HASH_FIELD_NUMBER: _ClassVar[int]
    COMBAT_CONFIG_HASH_FIELD_NUMBER: _ClassVar[int]
    prefab_path_hash: int
    prefab_path_remote_hash: int
    controller_path_hash: int
    controller_path_remote_hash: int
    combat_config_hash: int
    def __init__(self, prefab_path_hash: _Optional[int] = ..., prefab_path_remote_hash: _Optional[int] = ..., controller_path_hash: _Optional[int] = ..., controller_path_remote_hash: _Optional[int] = ..., combat_config_hash: _Optional[int] = ...) -> None: ...
