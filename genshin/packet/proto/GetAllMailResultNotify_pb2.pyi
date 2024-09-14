from genshin.packet.proto import MailData_pb2 as _MailData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAllMailResultNotify(_message.Message):
    __slots__ = ("total_page_count", "page_index", "transaction", "is_collected", "retcode", "mail_list")
    TOTAL_PAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_INDEX_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    IS_COLLECTED_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    MAIL_LIST_FIELD_NUMBER: _ClassVar[int]
    total_page_count: int
    page_index: int
    transaction: str
    is_collected: bool
    retcode: int
    mail_list: _containers.RepeatedCompositeFieldContainer[_MailData_pb2.MailData]
    def __init__(self, total_page_count: _Optional[int] = ..., page_index: _Optional[int] = ..., transaction: _Optional[str] = ..., is_collected: bool = ..., retcode: _Optional[int] = ..., mail_list: _Optional[_Iterable[_Union[_MailData_pb2.MailData, _Mapping]]] = ...) -> None: ...
