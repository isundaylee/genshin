from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MpSettingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MP_SETTING_TYPE_NO_ENTER: _ClassVar[MpSettingType]
    MP_SETTING_TYPE_ENTER_FREELY: _ClassVar[MpSettingType]
    MP_SETTING_TYPE_ENTER_AFTER_APPLY: _ClassVar[MpSettingType]
MP_SETTING_TYPE_NO_ENTER: MpSettingType
MP_SETTING_TYPE_ENTER_FREELY: MpSettingType
MP_SETTING_TYPE_ENTER_AFTER_APPLY: MpSettingType
