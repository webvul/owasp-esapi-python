#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
OWASP Enterprise Security API (ESAPI)
 
This file is part of the Open Web Application Security Project (OWASP)
Enterprise Security API (ESAPI) project. For details, please see
<a href="http://www.owasp.org/index.php/ESAPI">http://www.owasp.org/index.php/ESAPI</a>.
Copyright (c) 2009 - The OWASP Foundation

The ESAPI is published by OWASP under the BSD license. You should read and 
accept the LICENSE before you use, modify, and/or redistribute this software.

@author Craig Younkins (craig.younkins@owasp.org)
"""

class Encryptor():
    """
    The Encryptor interface provides a set of methods for performing common
    encryption and hashing operations. Implementations should
    rely on a strong cryptographic implementation, such as PyCrypto.
    Implementors should take care to ensure that they initialize their
    implementation with a strong "master key", and that they protect this secret
    as much as possible.
    <P>
    <img src="doc-files/Encryptor.jpg">
    <P>
    Possible future enhancements (depending on feedback) might include:
    <UL>
    <LI>encryptFile</LI>
    </UL>

    @author Craig Younkins (craig.younkins@owasp.org)
    """
    
    def __init__(self):
        pass

    def hash(self, plaintext, salt, iterations=1):
        """
        Returns a string representation of the hash of the provided plaintext and
        salt. The salt helps to protect against a rainbow table attack by mixing
        in some extra data with the plaintext. Some good choices for a salt might
        be an account name or some other string that is known to the application
        but not to an attacker.
        See <a href="http://www.matasano.com/log/958/enough-with-the-rainbow-tables-what-you-need-to-know-about-secure-password-schemes/">
        this article</a> for more information about hashing as it pertains to password schemes.

        @param plaintext
                the plaintext string to encrypt
        @param salt
             the string salt to add to the plaintext string before hashing
        @param iterations
            the number of times to iterate the hash. Defaults to 1.
             
        @return
                the encrypted hash of 'plaintext' stored as a String

        @throws EncryptionException
             if the specified hash algorithm could not be found or another problem exists with
             the hashing of 'plaintext'
        """
        raise NotImplementedError()

    def encrypt(self, plaintext):
        """
        Encrypts the provided plaintext and returns a ciphertext string.

        @param plaintext
             the plaintext string to encrypt

        @return
                the encrypted string representation of 'plaintext'

        @throws EncryptionException
             if the specified encryption algorithm could not be found or another problem exists with
             the encryption of 'plaintext'
        """
        raise NotImplementedError()

    def decrypt(self, ciphertext):
        """
        Decrypts the provided ciphertext string (encrypted with the encrypt
        method) and returns a plaintext string.

        @param ciphertext
             the ciphertext (encrypted plaintext)

        @return
                the decrypted ciphertext

        @throws EncryptionException
             if the specified encryption algorithm could not be found or another problem exists with
             the encryption of 'plaintext'
        """
        raise NotImplementedError()

    def sign(self, data):
        """
        Create a digital signature for the provided data and return it in a
        string.

        @param data
             the data to sign

        @return
                the digital signature stored as a String

        @throws EncryptionException
                if the specified signature algorithm cannot be found
        """
        raise NotImplementedError()

    def verify_signature(self, signature, data):
        """
        Verifies a digital signature (created with the sign method) and returns
        the boolean result.

        @param signature
             the signature to verify against 'data'
        @param data
             the data to verify against 'signature'

        @return
                true, if the signature is verified, false otherwise

        """
        raise NotImplementedError()

    def seal(self, data, timestamp):
        """
        Creates a seal that binds a set of data and includes an expiration timestamp.

        @param data
             the data to seal
        @param timestamp
             the absolute expiration date of the data, expressed as seconds since the epoch

        @return
                the seal
        @throws IntegrityException

        """
        raise NotImplementedError()

    def unseal(self, seal):
        """
        Unseals data (created with the seal method) and throws an exception
        describing any of the various problems that could exist with a seal, such
        as an invalid seal format, expired timestamp, or decryption error.

        @param seal
             the sealed data

        @return
                the original (unsealed) data

        @throws EncryptionException
                if the unsealed data cannot be retrieved for any reason
        """
        raise NotImplementedError()

    def verify_seal(self, seal):
        """
        Verifies a seal (created with the seal method) and throws an exception
        describing any of the various problems that could exist with a seal, such
        as an invalid seal format, expired timestamp, or data mismatch.

        @param seal
             the seal to verify

        @return
                true, if the seal is valid.  False otherwise
        """
        raise NotImplementedError()

    def get_relative_timestamp(self, offset):
        """
        Gets an absolute timestamp representing an offset from the current time to be used by
        other functions in the library.

        @param offset
                the offset to add to the current time

        @return
                the absolute timestamp
        """
        raise NotImplementedError()

    def get_timestamp(self):
        """
        Gets a timestamp representing the current date and time to be used by
        other functions in the library.

        @return
                a timestamp representing the current time
        """
        raise NotImplementedError()


