#    Copyright 2022 Loki2442

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from msvcrt import getch
import pypresence
import time
import json
from cryptography.fernet import Fernet
import base64

code = b"""
starttime = time.time()

def configFileRead():
    configFile = open("config.json", 'r')
    config = json.loads(configFile.read())
    return config

def UpdateRPC(config):
    try:
        state = config["state"]
    except KeyError:
        state="Not Set"

    try:
        details = config["details"]
    except KeyError:
        details = "Not Set"

    try:
        start = config["start"]
    except KeyError:
        start = 1

    try:
        end = config["end"]
    except KeyError:
        end = 1

    try:
        large_image = config["large_image"]
    except KeyError:
        large_image = "Not Set"

    try:
        large_text = config["large_image_text"]
    except KeyError:
        large_text = "Not Set"

    try:
        small_image = config["small_image"]
    except KeyError:
        small_image = "Not Set"

    try:
        small_text = config["small_image_text"]
    except KeyError:
        small_text = "Not Set"

    try:
        buttons = config["buttons"]
    except KeyError:
        buttons = None

    RPC.update(
        state = state,
        details = details,
        start = start,
        end = end,
        large_image = large_image,
        large_text = large_text,
        small_image = small_image,
        small_text = small_text,
        buttons = buttons
        )

    print("Presence Updated!")

try:
    config = configFileRead()
    try:
        client_id = config["clientID"]
    except KeyError:
        print("Client ID not set!")

    try:
        state = config["state"]
    except KeyError:
        state="Not Set"

    try:
        details = config["details"]
    except KeyError:
        details = "Not Set"

    try:
        start = config["start"]
    except KeyError:
        start = 1

    try:
        end = config["end"]
    except KeyError:
        end = 1

    try:
        large_image = config["large_image"]
    except KeyError:
        large_image = "Not Set"

    try:
        large_text = config["large_image_text"]
    except KeyError:
        large_text = "Not Set"

    try:
        small_image = config["small_image"]
    except KeyError:
        small_image = "Not Set"

    try:
        small_text = config["small_image_text"]
    except KeyError:
        small_text = "Not Set"

    try:
        buttons = config["buttons"]
    except KeyError:
        buttons = None

    RPC = pypresence.Presence(client_id)
    RPC.connect()

    RPC.update(
        state = state,
        details = details,
        start = start,
        end = end,
        large_image = large_image,
        large_text = large_text,
        small_image = small_image,
        small_text = small_text,
        buttons = buttons
        )  # Sets the presence

    print("Rich Presence has been set!")
        
except Exception as e:
    print(e)
    junk = getch()

while True:
    time.sleep(15)
    x = configFileRead()
    if x != config:
        UpdateRPC(x)
        config = x

"""

key = Fernet.generate_key()
encryption_type = Fernet(key)
encrypted_message = encryption_type.encrypt(code)

decrypted_message = encryption_type.decrypt(encrypted_message)

exec(decrypted_message)
