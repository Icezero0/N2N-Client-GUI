import json
import os
import traceback


class ConfigTool:
    _filePath: str

    def __init__(self, filePath="settings.json"):
        self._filePath = filePath

    # ErrorCode     Cause
    # 0             Normal
    # 1             Missing json file
    # 2             Fail to read/decode json file
    def readSettings(self):
        jsonObj = {}
        if os.path.exists(self._filePath):
            try:
                f = open(self._filePath, "r", encoding="utf8")
                jsonText = f.read()
                jsonObj = json.loads(jsonText)
            except Exception as e:
                return 2, jsonObj
                # traceback.print_exc(e)
        else:
            return 1, jsonObj
        return 0, jsonObj

    def saveSettings(self, jsonObj: dict):
        jsonText = json.dumps(jsonObj, indent=4)
        try:
            f = open(self._filePath, "w", encoding="utf8")
            f.write(jsonText)
            f.close()
        except Exception as e:
            traceback.print_exc(e)
            return -1
        return 0
