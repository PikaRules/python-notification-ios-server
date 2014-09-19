#http://nthn.me/posts/2012/push.html
import ssl
import json
import socket
import struct
import binascii



def test():


	TOKEN = 'd319226142e39ee2401a99bd647f526557a032128f7c8ecb1dc973673b823636'
	PAYLOAD = {
	    'aps': {
	        'alert': 'Hello Push!',
	        'sound': 'default'
	    }
	}
	PASSPHRASE = 'pushchat'

	send_push(TOKEN,json.dumps(PAYLOAD))


def send_push(token, payload):
    # Your certificate file
    cert = 'ck.pem'
    key = 'ck.key'
    host = 'gateway.sandbox.push.apple.com';
    host_ip = socket.gethostbyname( host )

    try:

	    # APNS development server
	    apns_address = (host_ip, 2195)

	    # Use a socket to connect to APNS over SSL
	    s = socket.socket()
	    sock = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv3, certfile=cert, keyfile=key )
	    sock.connect(apns_address)

	    # Generate a notification packet
	    token = binascii.unhexlify(token)
	    fmt = '!cH32sH{0:d}s'.format(len(payload))
	    cmd = '\x00'
	    message = struct.pack(fmt, cmd, len(token), token, len(payload), payload)
	    sock.write(message)
	    sock.close()

    except Exception, e:
    	print("Something's wrong with %s. Exception type is %s" % (apns_address, e))


test()