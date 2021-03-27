import subprocess
import re

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

profiles_names = (re.findall("All User Profile         : (.*)\r", command_output))

wifi_list = list()

if len(profiles_names) != 0:
    for name in profiles_names:
        wifi_profil = dict()
        profile_info = subprocess.run(["netsh", "wlan", "show", "profiles", name], capture_output = True).stdout.decode()

    if re.search("Security key        : Absent", profile_info):
        continue
    else:
        wifi_profile["ssid"] = name
        profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"])

        password = re.search("Key Content       : (.*)\r", profile_info_pass)

        if password == None:
            wifi_profile["password"] = None
        else:
            wifi_profile["password"] = password[1]

    wifi_list.apprend(wifi_profil)

    for x in range(len(wifi_list)):
        print(wifi_list[x])
