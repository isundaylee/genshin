from genshin.packet.proto import EquipParam_pb2 as _EquipParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMailItemRsp(_message.Message):
    __slots__ = ("mail_id_list", "item_list", "retcode")
    MAIL_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    mail_id_list: _containers.RepeatedScalarFieldContainer[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_EquipParam_pb2.EquipParam]
    retcode: int
    def __init__(self, mail_id_list: _Optional[_Iterable[int]] = ..., item_list: _Optional[_Iterable[_Union[_EquipParam_pb2.EquipParam, _Mapping]]] = ..., retcode: _Optional[int] = ...) -> None: ...
