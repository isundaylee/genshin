from genshin.packet.proto import GadgetBornType_pb2 as _GadgetBornType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateGadgetInfo(_message.Message):
    __slots__ = ("born_type", "chest")
    class Chest(_message.Message):
        __slots__ = ("chest_drop_id", "is_show_cutscene")
        CHEST_DROP_ID_FIELD_NUMBER: _ClassVar[int]
        IS_SHOW_CUTSCENE_FIELD_NUMBER: _ClassVar[int]
        chest_drop_id: int
        is_show_cutscene: bool
        def __init__(self, chest_drop_id: _Optional[int] = ..., is_show_cutscene: bool = ...) -> None: ...
    BORN_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHEST_FIELD_NUMBER: _ClassVar[int]
    born_type: _GadgetBornType_pb2.GadgetBornType
    chest: CreateGadgetInfo.Chest
    def __init__(self, born_type: _Optional[_Union[_GadgetBornType_pb2.GadgetBornType, str]] = ..., chest: _Optional[_Union[CreateGadgetInfo.Chest, _Mapping]] = ...) -> None: ...
