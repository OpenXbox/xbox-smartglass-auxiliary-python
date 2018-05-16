"""
Cryptography portion used for Title Channel aka Auxiliary Stream
"""
import hmac
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class AuxiliaryStreamCrypto(object):
    _backend = default_backend()

    def __init__(self, crypto_key, hash_key, server_iv, client_iv):
        """
        Initialize Auxiliary Stream Crypto-context.
        """

        self._encrypt_key = crypto_key
        self._hash_key = hash_key
        self._server_iv = server_iv
        self._client_iv = client_iv

    @classmethod
    def from_connection_info(cls, connection_info):
        """
        Initialize Crypto context via AuxiliaryStream-message
        connection info.
        """
        return cls(
            connection_info.crypto_key,
            connection_info.sign_hash,
            connection_info.server_iv,
            connection_info.client_iv
        )

    def encrypt(self, plaintext):
        """
        Encrypts plaintext with AES-128-CBC

        No padding is added here, data has to be aligned to
        block size (16 bytes).

        Args:
            plaintext (bytes): The plaintext to encrypt.

        Returns:
            bytes: Encrypted Data
        """
        return AuxiliaryStreamCrypto._encrypt(self._encrypt_key, self._client_iv, plaintext)

    def encrypt_server(self, plaintext):
        return AuxiliaryStreamCrypto._encrypt(self._encrypt_key, self._server_iv, plaintext)

    def decrypt(self, ciphertext):
        """
        Decrypts ciphertext

        No padding is removed here.

        Args:
            ciphertext (bytes): Ciphertext to be decrypted

        Returns:
            bytes: Decrypted data
        """
        return AuxiliaryStreamCrypto._decrypt(self._encrypt_key, self._server_iv, ciphertext)

    def decrypt_client(self, ciphertext):
        return AuxiliaryStreamCrypto._decrypt(self._encrypt_key, self._client_iv, ciphertext)

    def hash(self, data):
        """
        Securely hashes data with HMAC SHA-256

        Args:
            data (bytes): The data to securely hash.

        Returns:
            bytes: Hashed data
        """
        return AuxiliaryStreamCrypto._secure_hash(self._hash_key, data)

    def verify(self, data, secure_hash):
        """
        Verifies that the given data generates the given secure_hash

        Args:
            data (bytes): The data to validate.
            secure_hash (bytes): The secure hash to validate against.

        Returns:
            bool: True on success, False otherwise
        """
        return secure_hash == self.hash(data)

    @staticmethod
    def _secure_hash(key, data):
        return hmac.new(key, data, hashlib.sha256).digest()

    @staticmethod
    def _encrypt(key, iv, data):
        return AuxiliaryStreamCrypto._crypt(key=key, iv=iv, encrypt=True, data=data)

    @staticmethod
    def _decrypt(key, iv, data):
        return AuxiliaryStreamCrypto._crypt(key=key, iv=iv, encrypt=False, data=data)

    @staticmethod
    def _crypt(key, iv, encrypt, data):
        cipher = Cipher(
            algorithms.AES(key), modes.CBC(iv), backend=AuxiliaryStreamCrypto._backend
        )
        if encrypt:
            cryptor = cipher.encryptor()
        else:
            cryptor = cipher.decryptor()

        return cryptor.update(data) + cryptor.finalize()
