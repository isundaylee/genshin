from genshin.packet.proto import ServerBuff_pb2 as _ServerBuff_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServerBuffChangeNotify(_message.Message):
    __slots__ = ("entity_id_list", "server_buff_list", "is_creature_buff", "avatar_guid_list", "server_buff_change_type")
    class ServerBuffChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SERVER_BUFF_CHANGE_TYPE_ADD_SERVER_BUFF: _ClassVar[ServerBuffChangeNotify.ServerBuffChangeType]
        SERVER_BUFF_CHANGE_TYPE_DEL_SERVER_BUFF: _ClassVar[ServerBuffChangeNotify.ServerBuffChangeType]
    SERVER_BUFF_CHANGE_TYPE_ADD_SERVER_BUFF: ServerBuffChangeNotify.ServerBuffChangeType
    SERVER_BUFF_CHANGE_TYPE_DEL_SERVER_BUFF: ServerBuffChangeNotify.ServerBuffChangeType
    ENTITY_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    SERVER_BUFF_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_CREATURE_BUFF_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_LIST_FIELD_NUMBER: _ClassVar[int]
    SERVER_BUFF_CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    entity_id_list: _containers.RepeatedScalarFieldContainer[int]
    server_buff_list: _containers.RepeatedCompositeFieldContainer[_ServerBuff_pb2.ServerBuff]
    is_creature_buff: bool
    avatar_guid_list: _containers.RepeatedScalarFieldContainer[int]
    server_buff_change_type: ServerBuffChangeNotify.ServerBuffChangeType
    def __init__(self, entity_id_list: _Optional[_Iterable[int]] = ..., server_buff_list: _Optional[_Iterable[_Union[_ServerBuff_pb2.ServerBuff, _Mapping]]] = ..., is_creature_buff: bool = ..., avatar_guid_list: _Optional[_Iterable[int]] = ..., server_buff_change_type: _Optional[_Union[ServerBuffChangeNotify.ServerBuffChangeType, str]] = ...) -> None: ...
