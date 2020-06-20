import socket  # for socket
import sys




ip = "127.0.0.1"
port = 8230
FIRST_MSG_BYTES = bytearray(r"configMsg,01-06-20 12:17:07,DSWA,1234,VIO1.3,en_AU\015\012".encode("utf-8"))
# SECOND_MSG_BYTES = bytearray(r"signOn,01-06-20 12:30:03,DSWA,1234\015\012".encode("utf-8"))
SECOND_MSG_BYTES = bytearray(r"signOn,01-06-20 12:30:03,DSWA,1234".encode("utf-8"))

try:
    s = socket.socket()
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" % err)

# connecting to the server
con = s.connect((ip, port))

print("Successfully connected on {}:{}".format(ip, port))
try:
    response = s.send(FIRST_MSG_BYTES)
    print("First Response:", response)

    # response = s.send(SECOND_MSG_BYTES)
    # print("Second Response:", response)
    # print(s.recv(10))
finally:
    # close the connection
    s.close()
    print("DONE")
