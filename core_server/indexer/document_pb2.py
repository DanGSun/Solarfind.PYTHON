# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: document.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='document.proto',
  package='go.alphase.ru',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x64ocument.proto\x12\rgo.alphase.ru\"3\n\x08\x64ocument\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\tb\x06proto3')
)




_DOCUMENT = _descriptor.Descriptor(
  name='document',
  full_name='go.alphase.ru.document',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='go.alphase.ru.document.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='go.alphase.ru.document.body', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='go.alphase.ru.document.text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['document'] = _DOCUMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

document = _reflection.GeneratedProtocolMessageType('document', (_message.Message,), dict(
  DESCRIPTOR = _DOCUMENT,
  __module__ = 'document_pb2'
  # @@protoc_insertion_point(class_scope:go.alphase.ru.document)
  ))
_sym_db.RegisterMessage(document)


# @@protoc_insertion_point(module_scope)
