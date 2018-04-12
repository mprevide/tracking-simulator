import requests
import logging

# logger
logger = logging.getLogger('trackingsim.devices')

# list of attributes
device_attributes_model = [
    {"label": "protocol",               "type": "meta",    "value_type": "string", "static_value": "mqtt"},
    {"label": "imsi",                   "type": "dynamic", "value_type": "string"},
    {"label": "vehicleID",              "type": "dynamic", "value_type": "string"},
    {"label": "ts",                     "type": "dynamic", "value_type": "string"},
    {"label": "ue_status",              "type": "dynamic", "value_type": "string"},
    {"label": "grower",                 "type": "dynamic", "value_type": "string"},
    {"label": "farm",                   "type": "dynamic", "value_type": "string"},
    {"label": "field",                  "type": "dynamic", "value_type": "string"},
    {"label": "task",                   "type": "dynamic", "value_type": "string"},
    {"label": "taskSUID",               "type": "dynamic", "value_type": "string"},
    {"label": "tags",                   "type": "dynamic", "value_type": "string"},
    {"label": "displayAlarmCode",       "type": "dynamic", "value_type": "string"},
    {"label": "tiv_id",                 "type": "dynamic", "value_type": "string"},
    {"label": "rfid_tag_id",            "type": "dynamic", "value_type": "string"},
    {"label": "operator",               "type": "dynamic", "value_type": "string"},
    {"label": "rssi",                   "type": "dynamic", "value_type": "integer"},
    {"label": "cell_id",                "type": "dynamic", "value_type": "integer"},
    {"label": "sinr",                   "type": "dynamic", "value_type": "integer"},
    {"label": "sattelites",             "type": "dynamic", "value_type": "integer"},
    {"label": "quality",                "type": "dynamic", "value_type": "integer"},
    {"label": "fix",                    "type": "dynamic", "value_type": "integer"},
    {"label": "test_time_elapsed",      "type": "dynamic", "value_type": "integer"},
    {"label": "rpm",                    "type": "dynamic", "value_type": "integer"},
    {"label": "cutterHeight",           "type": "dynamic", "value_type": "integer"},
    {"label": "cutterStatus",           "type": "dynamic", "value_type": "integer"},
    {"label": "elevatorUpTime",         "type": "dynamic", "value_type": "integer"},
    {"label": "elevatorStatus",         "type": "dynamic", "value_type": "integer"},
    {"label": "extractorRpm",           "type": "dynamic", "value_type": "integer"},
    {"label": "workCondition",          "type": "dynamic", "value_type": "integer"},
    {"label": "fieldMode",              "type": "dynamic", "value_type": "integer"},
    {"label": "engineUpTime",           "type": "dynamic", "value_type": "integer"},
    {"label": "coolantTemp",            "type": "dynamic", "value_type": "integer"},
    {"label": "engineLoad",             "type": "dynamic", "value_type": "integer"},
    {"label": "manifoldTemperature",    "type": "dynamic", "value_type": "integer"},
    {"label": "oilTemperature",         "type": "dynamic", "value_type": "integer"},
    {"label": "hidrOilTemperature",     "type": "dynamic", "value_type": "integer"},
    {"label": "farmingAreaRemain",      "type": "dynamic", "value_type": "integer"},
    {"label": "area",                   "type": "dynamic", "value_type": "integer"},
    {"label": "workStatus",             "type": "dynamic", "value_type": "integer"},
    {"label": "weightWet",              "type": "dynamic", "value_type": "integer"},
    {"label": "idleReason",             "type": "dynamic", "value_type": "integer"},
    {"label": "idleDuration",           "type": "dynamic", "value_type": "integer"},
    {"label": "crop",                   "type": "dynamic", "value_type": "integer"},
    {"label": "fuelTheft",              "type": "dynamic", "value_type": "integer"},
    {"label": "displayAlarmStatus",     "type": "dynamic", "value_type": "integer"},
    {"label": "rfid_antenna",           "type": "dynamic", "value_type": "integer"},
    {"label": "rfid_rssi",              "type": "dynamic", "value_type": "integer"},
    {"label": "rfid_read_count",        "type": "dynamic", "value_type": "integer"},
    {"label": "rfid_read_elapsed_time", "type": "dynamic", "value_type": "integer"},
    {"label": "temperature",            "type": "dynamic", "value_type": "float"},
    {"label": "track",                  "type": "dynamic", "value_type": "float"},
    {"label": "speed",                  "type": "dynamic", "value_type": "float"},
    {"label": "lat",                    "type": "dynamic", "value_type": "float"},
    {"label": "lng",                    "type": "dynamic", "value_type": "float"},
    {"label": "alt",                    "type": "dynamic", "value_type": "float"},
    {"label": "number_of_tests",        "type": "dynamic", "value_type": "float"},
    {"label": "number_of_ok",           "type": "dynamic", "value_type": "float"},
    {"label": "number_of_failed",       "type": "dynamic", "value_type": "float"},
    {"label": "average_latency_msec",   "type": "dynamic", "value_type": "float"},
    {"label": "maximum_latency_msec",   "type": "dynamic", "value_type": "float"},
    {"label": "minimum_latency_msec",   "type": "dynamic", "value_type": "float"},
    {"label": "latency_std_deviation",  "type": "dynamic", "value_type": "float"},
    {"label": "latency_variance",       "type": "dynamic", "value_type": "float"},
    {"label": "fuelRate",               "type": "dynamic", "value_type": "float"},
    {"label": "boostPressure",          "type": "dynamic", "value_type": "float"},
    {"label": "oilPressure",            "type": "dynamic", "value_type": "float"},
    {"label": "fuelLevel",              "type": "dynamic", "value_type": "float"},
    {"label": "cutterPressure",         "type": "dynamic", "value_type": "float"},
    {"label": "groundSpeed",            "type": "dynamic", "value_type": "float"},
    {"label": "fuelRateAverage",        "type": "dynamic", "value_type": "float"},
    {"label": "fuelAreaAverage",        "type": "dynamic", "value_type": "float"},
    {"label": "fuelUsedField",          "type": "dynamic", "value_type": "float"},
    {"label": "fuelUsedRoad",           "type": "dynamic", "value_type": "float"},
    {"label": "yieldWet",               "type": "dynamic", "value_type": "float"},
    {"label": "yieldWetAverage",        "type": "dynamic", "value_type": "float"},
    {"label": "flowWet",                "type": "dynamic", "value_type": "float"},
    {"label": "flowWetAverage",         "type": "dynamic", "value_type": "float"},
    {"label": "coordinates",            "type": "dynamic", "value_type": "geo:point"},
]


def create_devices(host, user, password, number_of_devices, prefix='trackingsim'):
    devices = []

    # Get JWT token
    url = 'http://{}:8000/auth'.format(host)
    data = {"username" : "{}".format(user), "passwd" : "{}".format(password)}
    response = requests.post(url=url, json=data)
    token = response.json()['jwt']
    if response.status_code != 200:
        raise Exception("HTTP POST failed {}.".
                        format(response.status_code))
    auth_header = {"Authorization": "Bearer {}".format(token)}

    # Create Template
    url = 'http://{}:8000/template'.format(host)
    data = {"label": "{}".format(prefix),
            "attrs" : device_attributes_model}
    response = requests.post(url=url, headers=auth_header, json=data)
    if response.status_code != 200:
        raise Exception("HTTP POST failed {}.".
                        format(response.status_code))
    template_id = response.json()['template']['id']

    # Create devices
    url = 'http://{}:8000/device'.format(host)
    for n in range(1,number_of_devices+1):
        data = {"templates" : ["{}".format(template_id)],
                "label" : "{0}-{1}".format(prefix,n)}
        response = requests.post(url=url, headers=auth_header, json=data)
        if response.status_code != 200:
            raise Exception("HTTP POST failed {}.".
                            format(response.status_code))
        device_id = response.json()['devices'][0]['id']
        if response.status_code != 200:
            raise Exception("HTTP POST failed {}.".
                            format(response.status_code))
        devices.append(device_id)

    logger.info("Created devices: {}".format(devices))

    return devices


def remove_devices(host, user, password, prefix='trackingsim'):
    # Get JWT token
    url = 'http://{}:8000/auth'.format(host)
    data = {"username" : "{}".format(user), "passwd" : "{}".format(password)}
    response = requests.post(url=url, json=data)
    if response.status_code != 200:
        raise Exception("HTTP POST failed {}.".
                        format(response.status_code))
    token = response.json()['jwt']
    auth_header = {"Authorization": "Bearer {}".format(token)}

    # Get devices
    # TODO handle pagination
    url = 'http://{}:8000/device?page_size=128'.format(host)
    response = requests.get(url=url, headers=auth_header)
    if response.status_code != 200:
        raise Exception("HTTP GET failed {}.".
                        format(response.status_code))
    all_devices = list(response.json()['devices'])

    devices_to_be_removed = []
    for dev in all_devices:
        if dev['label'].startswith(prefix):
            devices_to_be_removed.append(dev['id'])

    # Remove devices
    removed_devices = []
    for dev in devices_to_be_removed:
        url = 'http://{0}:8000/device/{1}'.format(host, dev)
        response = requests.delete(url=url, headers=auth_header)
        if response.status_code == requests.codes.ok:
            removed_devices.append(dev)
        else:
            logger.error("Failed to remove device {}".format(dev))

    logger.info("Removed devices: {}".format(removed_devices))

    # Get templates
    # TODO handle pagination
    url = 'http://{}:8000/template?page_size=1000'.format(host)
    response = requests.get(url=url, headers=auth_header)
    if response.status_code != 200:
        raise Exception("HTTP GET failed {}.".
                        format(response.status_code))
    all_templates = list(response.json()['templates'])

    templates_to_be_removed = []
    for tpl in all_templates:
        if tpl['label'].startswith(prefix):
            templates_to_be_removed.append(tpl['id'])

    # Remove templates
    removed_templates = []
    for tpl in templates_to_be_removed:
        url = 'http://{0}:8000/template/{1}'.format(host, tpl)
        response = requests.delete(url=url, headers=auth_header)
        if response.status_code == requests.codes.ok:
            removed_templates.append(tpl)
        else:
            logger.error("Failed to remove template {}".format(tpl))

    logger.info("Removed templates: {}".format(removed_templates))
