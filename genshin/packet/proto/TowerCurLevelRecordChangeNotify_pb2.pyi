from genshin.packet.proto import TowerCurLevelRecord_pb2 as _TowerCurLevelRecord_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TowerCurLevelRecordChangeNotify(_message.Message):
    __slots__ = ("cur_level_record",)
    CUR_LEVEL_RECORD_FIELD_NUMBER: _ClassVar[int]
    cur_level_record: _TowerCurLevelRecord_pb2.TowerCurLevelRecord
    def __init__(self, cur_level_record: _Optional[_Union[_TowerCurLevelRecord_pb2.TowerCurLevelRecord, _Mapping]] = ...) -> None: ...
