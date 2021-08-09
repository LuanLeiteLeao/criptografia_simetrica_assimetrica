from cryptography.fernet import Fernet

class SymmetricEncryption:
	data_file_path = "../data/"
	def read_file(self,file_path):
		file = open(self.data_file_path+file_path, 'rb')
		key = file.read()
		file.close()

		return key

	def write_file(self,file_path,text):
		file = open(self.data_file_path+file_path, "wb")
		file.write(text)
		file.close()

	def read_key(self):
		return self.read_file('key.txt')

	def generate_key(self):
		key = Fernet.generate_key()
		self.write_file("key.txt",key)
		
	def encrypt(self, file_path):
		cipher_suite = Fernet(self.read_key())
		cipher_text = cipher_suite.encrypt(self.read_file(file_path))
		self.write_file("text_encrypt.txt",cipher_text)
		
	def decrypt(self, file_path):
		cipher_suite = Fernet(self.read_key())
		plain_text = cipher_suite.decrypt(self.read_file(file_path))		
		self.write_file("text_decrypt.txt",plain_text)


a = SymmetricEncryption()
a.generate_key()
a.encrypt('fernando-pessoa.txt')
a.decrypt("text_encrypt.txt")
