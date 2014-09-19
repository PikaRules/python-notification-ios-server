import webapp2
import ssl
import json
import socket
import struct
import binascii

class NotificationController(webapp2.RequestHandler):


	def test(self):


		TOKEN = 'd319226142e39ee2401a99bd647f526557a032128f7c8ecb1dc973673b823636'
		PAYLOAD = {
		    'aps': {
		        'alert': 'Hello Push!',
		        'sound': 'default'
		    }
		}
		PASSPHRASE = 'pushchat'

		self.send_push(TOKEN,json.dumps(PAYLOAD))

		self.response.write('sdfd')


	def send_push(self,token, payload):
	    # Your certificate file
	    cert = 'ck.pem'
	    key = 'ck.key'

	    # APNS development server
	    apns_address = ('ssl://gateway.sandbox.push.apple.com', 2195)

	    # Use a socket to connect to APNS over SSL
	    s = socket.socket()
	    sock = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv3, certfile=cert, keyfile = key )
	    sock.connect(apns_address)

	    # Generate a notification packet
	    token = binascii.unhexlify(token)
	    fmt = '!cH32sH{0:d}s'.format(len(payload))
	    cmd = '\x00'
	    message = struct.pack(fmt, cmd, len(token), token, len(payload), payload)
	    sock.write(message)
	    #socket_status = sock.recv(1024)
	    sock.close()