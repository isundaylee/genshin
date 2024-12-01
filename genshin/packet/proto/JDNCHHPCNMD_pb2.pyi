from genshin.packet.proto import KLKICBNNANF_pb2 as _KLKICBNNANF_pb2
from genshin.packet.proto import JKHPMJDMPJC_pb2 as _JKHPMJDMPJC_pb2
from genshin.packet.proto import OIGOIMJIDLA_pb2 as _OIGOIMJIDLA_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JDNCHHPCNMD(_message.Message):
    __slots__ = ("ALBHAJPGLOE", "date_delete", "count_down_delete", "delay_week_count_down_delete")
    ALBHAJPGLOE_FIELD_NUMBER: _ClassVar[int]
    DATE_DELETE_FIELD_NUMBER: _ClassVar[int]
    COUNT_DOWN_DELETE_FIELD_NUMBER: _ClassVar[int]
    DELAY_WEEK_COUNT_DOWN_DELETE_FIELD_NUMBER: _ClassVar[int]
    ALBHAJPGLOE: bool
    date_delete: _KLKICBNNANF_pb2.KLKICBNNANF
    count_down_delete: _JKHPMJDMPJC_pb2.JKHPMJDMPJC
    delay_week_count_down_delete: _OIGOIMJIDLA_pb2.OIGOIMJIDLA
    def __init__(self, ALBHAJPGLOE: bool = ..., date_delete: _Optional[_Union[_KLKICBNNANF_pb2.KLKICBNNANF, _Mapping]] = ..., count_down_delete: _Optional[_Union[_JKHPMJDMPJC_pb2.JKHPMJDMPJC, _Mapping]] = ..., delay_week_count_down_delete: _Optional[_Union[_OIGOIMJIDLA_pb2.OIGOIMJIDLA, _Mapping]] = ...) -> None: ...
