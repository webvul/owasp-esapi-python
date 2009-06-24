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

"""
Security Rationale:

random.SystemRandom uses os.urandom(), a proxy to an OS based source of 
entropy, to generate pseudo random numbers. On UNIX-like system, os.urandom() 
will use /dev/urandom. On Windows, it will use CryptGenRandom. If an OS level 
source of entropy is not found, a NotImplementedError() will be thrown.
"""

# Todo
# Change alpha_numerics and hex once Encoder is written

from random import SystemRandom

import esapi.core
from esapi.logger import Logger
from esapi.randomizer import Randomizer
from esapi.translation import _

class DefaultRandomizer(Randomizer):
    alpha_numerics = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    hex = '0123456789abcdef'

    def __init__(self):
        Randomizer.__init__(self)
        self.secure_random = SystemRandom()
        self.logger = esapi.core.getLogger("Randomizer")

    def get_random_string(self, length, character_set):
        ret = ""
        for i in range(length):
            ret += self.get_random_choice(character_set)
        return ret

    def get_random_boolean(self):
        return self.get_random_choice([True, False])

    def get_random_integer(self, min_, max_):
        return self.secure_random.randint(min_, max_)

    def get_random_filename(self, extension):
        filename = self.get_random_string(12, self.alpha_numerics) + \
                   "." + extension
        self.logger.debug(Logger.SECURITY_SUCCESS, 
                          _("Generated a new random filename: ") + filename)
        return filename
        
    def get_random_float(self, min_, max_):
        return self.secure_random.uniform(min_, max_)

    def get_random_guid(self):
        parts = [None] * 5
        parts[0] = self.get_random_string(8, self.hex)
        parts[1] = self.get_random_string(4, self.hex)
        # Sets GUID version to 4 
        parts[2] = '4' + self.get_random_string(3, self.hex)
        # Sets high bits
        parts[3] = self.get_random_choice('89ab') + \
                   self.get_random_string(3, self.hex) 
        parts[4] = self.get_random_string(12, self.hex)
        return '-'.join(parts)
                    
    def get_random_choice(self, seq):
        return self.secure_random.choice(seq)
        


