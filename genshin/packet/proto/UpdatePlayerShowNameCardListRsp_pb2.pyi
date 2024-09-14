from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UpdatePlayerShowNameCardListRsp(_message.Message):
    __slots__ = ("show_name_card_id_list", "retcode")
    SHOW_NAME_CARD_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    show_name_card_id_list: _containers.RepeatedScalarFieldContainer[int]
    retcode: int
    def __init__(self, show_name_card_id_list: _Optional[_Iterable[int]] = ..., retcode: _Optional[int] = ...) -> None: ...
