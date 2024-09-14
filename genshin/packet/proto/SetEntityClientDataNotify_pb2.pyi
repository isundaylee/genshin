from genshin.packet.proto import EntityClientData_pb2 as _EntityClientData_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetEntityClientDataNotify(_message.Message):
    __slots__ = ("entity_client_data", "entity_id")
    ENTITY_CLIENT_DATA_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    entity_client_data: _EntityClientData_pb2.EntityClientData
    entity_id: int
    def __init__(self, entity_client_data: _Optional[_Union[_EntityClientData_pb2.EntityClientData, _Mapping]] = ..., entity_id: _Optional[int] = ...) -> None: ...
