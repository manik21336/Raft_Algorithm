# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raft.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nraft.proto\x12\x04raft\"V\n\x08LogEntry\x12\x11\n\toperation\x18\x01 \x01(\t\x12\x0c\n\x04term\x18\x02 \x01(\x05\x12\r\n\x05index\x18\x03 \x01(\x05\x12\x0b\n\x03key\x18\x04 \x01(\t\x12\r\n\x05value\x18\x05 \x01(\t\"\xb1\x01\n\x0f\x41ppendEntryArgs\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x11\n\tleader_id\x18\x02 \x01(\x05\x12\x16\n\x0eprev_log_index\x18\x03 \x01(\x05\x12\x15\n\rprev_log_term\x18\x04 \x01(\x05\x12\x1f\n\x07\x65ntries\x18\x05 \x03(\x0b\x32\x0e.raft.LogEntry\x12\x15\n\rleader_commit\x18\x06 \x01(\x05\x12\x16\n\x0elease_duration\x18\x07 \x01(\x03\"1\n\x10\x41ppendEntryReply\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\x8d\x01\n\x0fRequestVoteArgs\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x14\n\x0c\x63\x61ndidate_id\x18\x02 \x01(\x05\x12\x16\n\x0elast_log_index\x18\x03 \x01(\x05\x12\x15\n\rlast_log_term\x18\x04 \x01(\x05\x12\'\n\x1fremaining_leader_lease_duration\x18\x05 \x01(\x03\"6\n\x10RequestVoteReply\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x14\n\x0cvote_granted\x18\x02 \x01(\x08\">\n\rClientRequest\x12\x11\n\toperation\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"D\n\x10ServeClientReply\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\x11\n\tleader_id\x18\x02 \x01(\t\x12\x0f\n\x07success\x18\x03 \x01(\x08\x32\x8c\x02\n\x0bRaftService\x12>\n\x0b\x41ppendEntry\x12\x15.raft.AppendEntryArgs\x1a\x16.raft.AppendEntryReply\"\x00\x12>\n\x0bRequestVote\x12\x15.raft.RequestVoteArgs\x1a\x16.raft.RequestVoteReply\"\x00\x12<\n\x0bServeClient\x12\x13.raft.ClientRequest\x1a\x16.raft.ServeClientReply\"\x00\x12?\n\x0bReceiveInfo\x12\x16.raft.ServeClientReply\x1a\x16.raft.ServeClientReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'raft_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LOGENTRY']._serialized_start=20
  _globals['_LOGENTRY']._serialized_end=106
  _globals['_APPENDENTRYARGS']._serialized_start=109
  _globals['_APPENDENTRYARGS']._serialized_end=286
  _globals['_APPENDENTRYREPLY']._serialized_start=288
  _globals['_APPENDENTRYREPLY']._serialized_end=337
  _globals['_REQUESTVOTEARGS']._serialized_start=340
  _globals['_REQUESTVOTEARGS']._serialized_end=481
  _globals['_REQUESTVOTEREPLY']._serialized_start=483
  _globals['_REQUESTVOTEREPLY']._serialized_end=537
  _globals['_CLIENTREQUEST']._serialized_start=539
  _globals['_CLIENTREQUEST']._serialized_end=601
  _globals['_SERVECLIENTREPLY']._serialized_start=603
  _globals['_SERVECLIENTREPLY']._serialized_end=671
  _globals['_RAFTSERVICE']._serialized_start=674
  _globals['_RAFTSERVICE']._serialized_end=942
# @@protoc_insertion_point(module_scope)