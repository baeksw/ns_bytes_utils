from ns.bytes.byte_utils import BinaryUtils

if __name__ == '__main__':
    payload = '018201018E4D753A7544754E75587562756C75767580758A7594759E75A875B275BC75C675D075DA75E475EE75F87602760C76167620762A7634763E76487652765C76667670767A7684768E769876A276AC76B676C076CA76D476DE76E876F276FC77067710771A7724772E77387742774C77567760776A7774777E77887792779C77A677B077BA77C477CE77D877E277EC77F67800780A7814781E78287832000000000848282828282828285000050700000000000000000000000000001388'
    parser = BinaryUtils(payload)
    d001 = parser.read('uint8','addr')
    d002 = parser.read('uint8', 'cmd')
    d003 = parser.read('uint8', 'protocol version')
    d004 = parser.read('uint16', 'frame length')
    d005 = parser.read('uint8','BMS Connect Cell Total Count')
    for idx, _ in enumerate(range(d005.DATA)):
        d = parser.read('uint16','Connect Cell {} Cell Voltage'.format(idx+1))
    d083 = parser.read('uint16', 'Charge_C')
    d084 = parser.read('uint16', 'Discharge_C')
    d085 = parser.read('uint8', 'HW Temp = SYS Temp+FET Temp+Cell Temp')
    for idx, _ in enumerate(range(d085.DATA)):
        d = parser.read('uint8','{} - System ADC Connect Temperature'.format(idx+1))
    for idx, _ in enumerate(range(d085.DATA)):
        d = parser.read('uint8','{} - FET ADC Connect Temperature'.format(idx+1))
    for idx, _ in enumerate(range(d085.DATA)):
        d = parser.read('uint8','{} - LTC6803 Connect Temperature'.format(idx+1))
    d110 = parser.read('uint16', 'Alarm State')
    d111 = parser.read('uint8', 'FET State')
    d112 = parser.read('uint8', 'LTC Board Number')
#     for idx, _ in enumerate(range(12)):
#         d = parser.read('uint16','Balance V{}'.format(idx+1))
    
    
    q = parser.results()
    while q:
        print(q.popleft()) 