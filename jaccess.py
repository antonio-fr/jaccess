#!/usr/bin/python
# -*- coding: ascii -*-

# Jaccess
# Reads Jaxx private seed mnemonic in Windows, Linux and MacOS 
# Copyright (C) 2017  Antoine FERRON

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/># Read Jaxx private seed mnemonic in Windows, Linux and MacOS

import os
import sqlite3
from Crypto.Cipher import AES # Requires pycrypto ('pip install pycrypto')
home = os.path.expanduser("~")
if os.name == 'nt':
	path = '/AppData/Roaming/'
else:
	path = '/.config/'
try:
	conn = sqlite3.connect(home+path+'Jaxx/Local Storage/file__0.localstorage')
except:
	home = '/Library/Application Support/'
	conn = sqlite3.connect(home+path+'Jaxx/Local Storage/file__0.localstorage')
c = conn.cursor()
c.execute("SELECT VALUE FROM ItemTable WHERE key='mnemonic'")
encmneb64 = str(c.fetchone()[0]).decode('utf-16le')
conn.close()
key = "E8B7B40E031300000000DA2475F1226A".decode("hex")
iv  = "987185C4436764B6E27A72F220BA2278".decode("hex")
encmne = encmneb64.decode("base64")
decryption_suite = AES.new(key, AES.MODE_CBC, iv)
seed = decryption_suite.decrypt(encmne) #needs proper decoding
print seed
