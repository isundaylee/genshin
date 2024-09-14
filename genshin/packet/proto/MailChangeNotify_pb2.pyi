from genshin.packet.proto import MailData_pb2 as _MailData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MailChangeNotify(_message.Message):
    __slots__ = ("del_mail_id_list", "mail_list")
    DEL_MAIL_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    MAIL_LIST_FIELD_NUMBER: _ClassVar[int]
    del_mail_id_list: _containers.RepeatedScalarFieldContainer[int]
    mail_list: _containers.RepeatedCompositeFieldContainer[_MailData_pb2.MailData]
    def __init__(self, del_mail_id_list: _Optional[_Iterable[int]] = ..., mail_list: _Optional[_Iterable[_Union[_MailData_pb2.MailData, _Mapping]]] = ...) -> None: ...
