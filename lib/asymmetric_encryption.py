from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class AsymmetricEncryption:

	def __init__(self):
		private_key = rsa.generate_private_key(
		    public_exponent=65537,
		    key_size=2048,
		    backend=default_backend()
		)
		self.private_key = private_key
		self.public_key = private_key.public_key()

		

	def _storing_private_key(self):
		pem = self.private_key.private_bytes(
		    encoding=serialization.Encoding.PEM,
		    format=serialization.PrivateFormat.PKCS8,
		    encryption_algorithm=serialization.NoEncryption()
		)

		with open('private_key.pem', 'wb') as f:
		    f.write(pem)	

	def _storing_public_key(self):
		pem = self.public_key.public_bytes(
		    encoding=serialization.Encoding.PEM,
		    format=serialization.PublicFormat.SubjectPublicKeyInfo
		)

		with open('public_key.pem', 'wb') as f:
		    f.write(pem)
	
	def storing_keys(self):
		self._storing_public_key()
		self._storing_private_key()

	def reading_private_key(self):
		with open("private_key.pem", "rb") as key_file:
			self.private_key = serialization.load_pem_private_key(
				key_file.read(),
				password=None,
				backend=default_backend()
			)	

	def reading_public_key(self):	
		with open("public_key.pem", "rb") as key_file:
			self.public_key = serialization.load_pem_public_key(
				key_file.read(),
				backend=default_backend()
			)


	def encrypt(self,message):		
		encrypted = self.public_key.encrypt(
			message,
			padding.OAEP(
				mgf=padding.MGF1(algorithm=hashes.SHA256()),
				algorithm=hashes.SHA256(),
				label=None
			)
		)

		return encrypted
		
	def decrypt(self,encrypted):
		original_message = self.private_key.decrypt(
			encrypted,
			padding.OAEP(
				mgf=padding.MGF1(algorithm=hashes.SHA256()),
				algorithm=hashes.SHA256(),
				label=None
			)
		)
		return original_message
	
a = AsymmetricEncryption()
a.storing_keys()
a.reading_private_key()
a.reading_public_key()
encrypt = a.encrypt('Seria outro hoje, e talvez o universo inteiro')
print(encrypt)
original_message = a.decrypt(encrypt)
print(original_message)