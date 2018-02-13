import logging
import threading
from optparse import OptionParser
from trackingsim.sim import Simulator

# set logger
logger = logging.getLogger('trackingsim')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - Thread %(thread)d - %(levelname)s - %(message)s')
channel = logging.StreamHandler()
channel.setFormatter(formatter)
logger.addHandler(channel)


# thread
def worker(host, port, service, device, latitude, longitude):
    s = Simulator(host, port, service, device, latitude, longitude)
    s.run()


if __name__ == '__main__':
    # parse arguments
    parser = OptionParser()

    # MQTT broker - IP
    parser.add_option("-H", "--host", dest="host", default="127.0.0.1",
                      help="Host to connect. Defaults to localhost.")

    # MQTT broker - Port
    parser.add_option("-P", "--port", dest="port", type="int", default=1883,
                      help="Port to connect to. Defaults to 1883.")

    # dojot - Service ID
    parser.add_option("-s", "--service", dest="service", default="admin",
                      help="Service identifier in dojot. Defaults to admin.")

    # dojot - Device ID list
    parser.add_option("-d", "--device", dest="devices", default=[], action="append",
                      help="Device identifier in dojot. Multiple devices can be simulated "
                           "simultaneously repeating this option.")

    # Simulation - Starting latitude
    parser.add_option("-x", "--latitude", dest="latitude", default="-22.815970",
                      help="Starting latitude for the simulation. Defaults to -22.815970.")

    # Simulation - Starting longitude
    parser.add_option("-y", "--longitude", dest="longitude", default="-47.045121",
                      help="Starting longitude for the simulation. Defaults to -47.045121.")

    (options, args) = parser.parse_args()
    logger.info("Options: {0}".format(options))

    # run one thread for each device
    for d in options.devices:
        logger.info("Starting thread for device {0}".format(d))
        t = threading.Thread(target=worker, args=(options.host, options.port, options.service, d,
                                                  options.latitude, options.longitude))
        t.start()
