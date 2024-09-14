from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RecordUsage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UGC_RECORD_USAGE_NONE: _ClassVar[RecordUsage]
    UGC_RECORD_USAGE_IMPORT: _ClassVar[RecordUsage]
    UGC_RECORD_USAGE_PLAY: _ClassVar[RecordUsage]
    UGC_RECORD_USAGE_TRIAL: _ClassVar[RecordUsage]
    UGC_RECORD_USAGE_COMPARE: _ClassVar[RecordUsage]
UGC_RECORD_USAGE_NONE: RecordUsage
UGC_RECORD_USAGE_IMPORT: RecordUsage
UGC_RECORD_USAGE_PLAY: RecordUsage
UGC_RECORD_USAGE_TRIAL: RecordUsage
UGC_RECORD_USAGE_COMPARE: RecordUsage
