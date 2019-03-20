import enum 
import struct 

from _collections import deque
from collections import namedtuple

BIN_RESULT = namedtuple('BIN_RESULT', 'NO HEX DATA DESC')

@enum.unique
class BinaryTypes(enum.Enum):
        INT8   ='b'
        UINT8  ='B'
        INT16  ='h'
        UINT16 ='H'
        INT32  ='i'
        UINT32 ='I'
        INT64  ='q'
        UINT64 ='Q'
        FLOAT  ='f'
        DOUBLE ='d'
        CHAR   ='s'

class ByteUtils(object):
    @staticmethod 
    def hexlify(_bytearray):
        hbytes = bytes(_bytearray)
        return hbytes.hex()
    
    @staticmethod
    def unhexlify(hexstring):
        return bytes.fromhex(hexstring) 

class BinaryReaderEOFException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return 'Not enough bytes to satisfy read request'
    
class BinaryUtils:
    def __init__(self, hexstring):
        self._origin = hexstring
        self.queue = deque([ "{}{}".format(*x) for x in zip(hexstring[::2], hexstring[1::2])])
        self._results = deque()
        self.data_no = 1 # data count
    
    def read(self,typeName, desc='unknown'):
        typeFormat = BinaryTypes[typeName.upper()].value
        typeSize = struct.calcsize(typeFormat)
        data = "".join([self.queue.popleft() for _ in range(typeSize) ])
        if typeSize != (len(data)/2):
            raise BinaryReaderEOFException
        rs = struct.unpack(typeFormat, ByteUtils.unhexlify(data))[0]
        parse_data = BIN_RESULT._make((self.data_no, data, rs, desc))
        self._results.append(parse_data)
        self.data_no += 1
        return parse_data
    def results(self):
        return self._results
    def origin(self):
        return self._origin
    