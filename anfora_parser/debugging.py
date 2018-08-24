import ttp

parser = ttp.Parser()

result = parser.parse('@loco testing @username@mstdn.io')

print(result.html)
print(result.users)

print("========")
result = parser.parse('@username')

print(result.html)
print(result.users)
