from genshin.packet.proto import MailTextContent_pb2 as _MailTextContent_pb2
from genshin.packet.proto import MailItem_pb2 as _MailItem_pb2
from genshin.packet.proto import MailCollectState_pb2 as _MailCollectState_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MailData(_message.Message):
    __slots__ = ("mail_id", "mail_text_content", "item_list", "send_time", "expire_time", "importance", "is_read", "is_attachment_got", "config_id", "argument_list", "collect_state")
    MAIL_ID_FIELD_NUMBER: _ClassVar[int]
    MAIL_TEXT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    SEND_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
    IS_READ_FIELD_NUMBER: _ClassVar[int]
    IS_ATTACHMENT_GOT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    COLLECT_STATE_FIELD_NUMBER: _ClassVar[int]
    mail_id: int
    mail_text_content: _MailTextContent_pb2.MailTextContent
    item_list: _containers.RepeatedCompositeFieldContainer[_MailItem_pb2.MailItem]
    send_time: int
    expire_time: int
    importance: int
    is_read: bool
    is_attachment_got: bool
    config_id: int
    argument_list: _containers.RepeatedScalarFieldContainer[str]
    collect_state: _MailCollectState_pb2.MailCollectState
    def __init__(self, mail_id: _Optional[int] = ..., mail_text_content: _Optional[_Union[_MailTextContent_pb2.MailTextContent, _Mapping]] = ..., item_list: _Optional[_Iterable[_Union[_MailItem_pb2.MailItem, _Mapping]]] = ..., send_time: _Optional[int] = ..., expire_time: _Optional[int] = ..., importance: _Optional[int] = ..., is_read: bool = ..., is_attachment_got: bool = ..., config_id: _Optional[int] = ..., argument_list: _Optional[_Iterable[str]] = ..., collect_state: _Optional[_Union[_MailCollectState_pb2.MailCollectState, str]] = ...) -> None: ...
