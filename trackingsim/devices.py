import requests
import logging
# TODO: handle errors

logger = logging.getLogger('trackingsim.devices')


def create_devices(host, user, password, number_of_devices, prefix='trackingsim'):
    devices = []

    # Get JWT token
    url = 'http://{}:8000/auth'.format(host)
    data = {"username" : "{}".format(user), "passwd" : "{}".format(password)}
    result = requests.post(url=url, json=data)
    token = result.json()['jwt']
    auth_header = {"Authorization" : "Bearer {}".format(token)}

    # Create Template
    url = 'http://{}:8000/template'.format(host)
    data = {"label": "{}".format(prefix),
            "attrs" : [{"label" : "gps",
                        "type" : "dynamic",
                        "value_type" : "geo:point"},
                       {"label" : "sinr",
                        "type" : "dynamic",
                        "value_type" : "float"}]}
    result = requests.post(url=url, headers=auth_header, json=data)
    template_id = result.json()['template']['id']

    # Create devices
    url = 'http://{}:8000/device'.format(host)
    for n in range(1,number_of_devices+1):
        data = {"templates" : ["{}".format(template_id)],
                "label" : "{0}-{1}".format(prefix,n)}
        result = requests.post(url=url, headers=auth_header, json=data)
        device_id = result.json()['devices'][0]['id']
        devices.append(device_id)

    logger.info("Created devices: {}".format(devices))

    return devices


def remove_devices(host, user, password, prefix='trackingsim'):
    # Get JWT token
    url = 'http://{}:8000/auth'.format(host)
    data = {"username" : "{}".format(user), "passwd" : "{}".format(password)}
    result = requests.post(url=url, json=data)
    token = result.json()['jwt']
    auth_header = {"Authorization": "Bearer {}".format(token)}

    # Get devices
    # TODO handle pagination
    url = 'http://{}:8000/device?page_size=128'.format(host)
    result = requests.get(url=url, headers=auth_header)
    all_devices = list(result.json()['devices'])

    devices_to_be_removed = []
    for dev in all_devices:
        if dev['label'].startswith(prefix):
            devices_to_be_removed.append(dev['id'])

    # Remove devices
    removed_devices = []
    for dev in devices_to_be_removed:
        url = 'http://{0}:8000/device/{1}'.format(host, dev)
        result = requests.delete(url=url, headers=auth_header)
        if result.status_code == requests.codes.ok:
            removed_devices.append(dev)
        else:
            logger.error("Failed to remove device {}".format(dev))

    logger.info("Removed devices: {}".format(removed_devices))

    # Get templates
    # TODO handle pagination
    url = 'http://{}:8000/template?page_size=1000'.format(host)
    result = requests.get(url=url, headers=auth_header)
    all_templates = list(result.json()['templates'])

    templates_to_be_removed = []
    for tpl in all_templates:
        if tpl['label'].startswith(prefix):
            templates_to_be_removed.append(tpl['id'])

    # Remove templates
    removed_templates = []
    for tpl in templates_to_be_removed:
        url = 'http://{0}:8000/template/{1}'.format(host, tpl)
        result = requests.delete(url=url, headers=auth_header)
        if result.status_code == requests.codes.ok:
            removed_templates.append(tpl)
        else:
            logger.error("Failed to remove template {}".format(tpl))

    logger.info("Removed templates: {}".format(removed_templates))
