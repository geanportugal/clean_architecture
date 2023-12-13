from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class CardEncryptor:
    """A class that encrypts and decrypts credit card numbers.
    AES symmetry algorithm was used for encryption. For more details, see
    https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
    """

    def __init__(self, encryption_key, salt):
        """Initialize the encryptor."""
        self.encryption_key = encryption_key.encode()
        self.key = self.derive_key(salt.encode())

    def derive_key(self, salt):
        """Derive the encryption key from the salt."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,  # A unique salt is used for each encryption process
            iterations=100000,
            backend=default_backend(),
        )
        return kdf.derive(self.encryption_key)

    # Encrypt the credit card number using AES encryption
    def encrypt_card(self, card_number):
        cipher = Cipher(
            algorithms.AES(self.key), modes.ECB(), backend=default_backend()
        )
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(card_number.encode()) + padder.finalize()
        encrypted_card = encryptor.update(padded_data) + encryptor.finalize()
        return encrypted_card

    # Decrypt the encrypted credit card number using AES decryption
    def decrypt_card(self, encrypted_card):
        encrypted_card = bytes.fromhex(encrypted_card)
        cipher = Cipher(
            algorithms.AES(self.key), modes.ECB(), backend=default_backend()
        )
        decryptor = cipher.decryptor()
        decrypted_padded_data = decryptor.update(encrypted_card) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        decrypted_card = unpadder.update(decrypted_padded_data) + unpadder.finalize()
        return decrypted_card.decode()
