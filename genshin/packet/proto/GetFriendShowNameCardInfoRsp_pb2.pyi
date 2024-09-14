from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetFriendShowNameCardInfoRsp(_message.Message):
    __slots__ = ("uid", "show_name_card_id_list", "retcode")
    UID_FIELD_NUMBER: _ClassVar[int]
    SHOW_NAME_CARD_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    uid: int
    show_name_card_id_list: _containers.RepeatedScalarFieldContainer[int]
    retcode: int
    def __init__(self, uid: _Optional[int] = ..., show_name_card_id_list: _Optional[_Iterable[int]] = ..., retcode: _Optional[int] = ...) -> None: ...
