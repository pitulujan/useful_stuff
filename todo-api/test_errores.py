import jwt
private_key = open("jwt-key").read()
public_key = open("jwt-key.pub").read()

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE1ODY1NDg5ODAuMjM4NjgzNX0.fkMTF75JNItuSwguioP4kPffLaSUxIU9n3ZegvKCxVo5f2TJYjlHIsf-bds6tbOtc9K6vdADIOj7I2BZ1JU06HFejZciEvgs-FI0FZBBu7tFd86WbHHiN9vNkDnnN7qfIAFzjVMyGI7UcZV1ZRfDzJKBMyG1ya61FnTTNS3gPUJetVt_cXJD6RU4jn23lkUaFOTMemcmuxcwFALuC47htE9RXmkFF_Kr-J0Rlw4Uzenka4vojboszQGXmUEMhhHwp4dGthaTz_5CnR5escpzcK2RDDssXOHNsztgo4QKVoqeDeAaGVRoy7BHKtN89iDE37wcyUaY_em6tItTsOW5QobJpZanVBhrCvKUn87pxpr7HtsEme-AehMhHHTS_LuBc2KMNC8qTTkMLwHY6Y3OCITDFQDe0zZfNm0EOdjieOrh7fJdr7pTA2DGR3FdahxB_lAOa4urInxLCuTFonGkTs8IueBw_6DKit5YDxk-zHX6lGNXXyA5w6WGEaZWZkj2hBcIo5OuCe8wOp0o-_ZdateeQHGEq67UMaTulR4uDIX6sqGHRodepeEIn-7T2LupGqrKUVoqqYqMI_QkssEv8WMgvIEH-sqoL-eGM5lc7GXYydz55cz64iWVLhu5fNTSMQHLUOcKunijeTEvUfts-a4IySqhcbsmL6WI12Pu3rQ'

try:
    payload= jwt.decode(token, public_key,algorithms=["RS256"])

except jwt.InvalidSignatureError:
    print('entre mal')

except jwt.ExpiredSignatureError:
    print ('entre bien tiempo')

except jwt.DecodeError:
    print ('entre bien decode')
