import base64

ashis={
    'algo':'eyJhbGciOiJIUzI1NiJ9',
    'payload':'eyJpZCI6InN1YmhvIn0',
    "sig":"kL2x4zRRVPYKAICb4UsLlULTuuQeQvJP4rnK9A4mHuw",
    }
# subho={
#     "algo":"eyJhbGciOiJIUzI1NiJ9"
#     "payload":"eyJpZCI6InN1YmhvIn0"
#     "sig":"kL2x4zRRVPYKAICb4UsLlULTuuQeQvJP4rnK9A4mHuw"
#     }
d = {'k':'hello'}
    
# data=base64.urlsafe_b64decode(ashis["payload"])
print(ashis["payload"])