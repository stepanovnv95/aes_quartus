from intelhex import IntelHex

KEY_SHELDURE = [
        0x82, 0xea, 0x4c, 0x91, 0x7c, 0x8a, 0x34, 0xf8, 0xcb, 0x70, 0xa1, 0x4e, 0xe, 0x6c, 0x68, 0x7b, 
        0x7b, 0x91, 0xdd, 0x4c, 0x32, 0xb8, 0x8c, 0x74, 0xb0, 0xc0, 0x61, 0x2f, 0x9f, 0xf3, 0x9b, 0xe0, 
        0xd, 0x9c, 0x41, 0xd, 0x1d, 0xa5, 0x29, 0x5d, 0x50, 0x90, 0xf1, 0xde, 0xd3, 0x20, 0xbb, 0x5b, 
        0x54, 0xc8, 0x89, 0x84, 0xc3, 0x66, 0x4f, 0x12, 0xb, 0x9b, 0x6a, 0xb4, 0xde, 0xfe, 0x45, 0x1e, 
        0x4e, 0x86, 0xf, 0x8b, 0x77, 0x11, 0x5e, 0x4c, 0x15, 0x8e, 0xe4, 0x50, 0x5a, 0xa4, 0xe1, 0xff, 
        0x12, 0x94, 0x9b, 0x10, 0x27, 0x36, 0x68, 0x24, 0xea, 0x64, 0x80, 0xd0, 0xd1, 0x75, 0x94, 0x6b, 
        0x16, 0x82, 0x19, 0x9, 0xf7, 0xc1, 0xa9, 0x8d, 0x81, 0xe5, 0x65, 0xb5, 0xc1, 0xb4, 0x20, 0x4b, 
        0xdb, 0x59, 0x40, 0x49, 0x42, 0x83, 0x2a, 0xa7, 0xca, 0x2f, 0x4a, 0xff, 0xc8, 0x7c, 0x5c, 0x17, 
        0xfc, 0xa5, 0xe5, 0xac, 0xbd, 0x3e, 0x14, 0xb3, 0xdd, 0xf2, 0xb8, 0x47, 0x81, 0xfd, 0xa1, 0xb6, 
        0x54, 0xf1, 0x14, 0xb8, 0xfa, 0xc4, 0xd0, 0x63, 0x6b, 0x99, 0x21, 0x66, 0x2d, 0xd0, 0x71, 0xc7, 
        0x1, 0xf0, 0xe4, 0x5c, 0x9c, 0x58, 0x88, 0xeb, 0xac, 0x35, 0x14, 0x72, 0x95, 0x45, 0x34, 0xf3
    ]

if __name__ == '__main__':

    filename = 'key_sheldure.hex'
    ih = IntelHex()

    for address in range(len(KEY_SHELDURE)):
        ih[address] = KEY_SHELDURE[address]

    ih.write_hex_file(filename)
        
        
    
