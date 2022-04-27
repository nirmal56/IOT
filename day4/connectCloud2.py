import time
from azure.iot.device import IoTHubDeviceClient
import os
import threading
 
RECEIVED_MESSAGES = 0
 
CONNECTION_STRING = "HostName=150262-HuseinBhai.azure-devices.net;DeviceId=420.1;SharedAccessKey=dPxQ2ODNTuC3IxDyZfLIKx2szfs/h4QQdtLnls3xw88="
def file1():
    os.system("gedit file1.txt")

def file2():
    os.system("gedit file2.txt")

def message_handler(message):
    global RECEIVED_MESSAGES
    global lst
    RECEIVED_MESSAGES += 1
    print("")
    print("Message received:")
 
    # print data from both system and application (custom) properties
    # lst = []
    for property in vars(message).items():
        if(property[1] == b'1'):
            # os.open("file1.txt",os.O_RDWR | os.O_CREAT,0o666)
            os.system("gedit file1.txt")

        if(property[1]==b'2'):

            # print("yes")
            t1 = threading.Thread(target=file1)
            t2 = threading.Thread(target=file2)
            t1.start()
            # starting thread 2
            t2.start()
            t1.join()
            # wait until thread 2 is completely executed
            t2.join()
        #     f = open("database.py", "r")
        #     print(f.read())
        #     print("file opened")
        #     # print(f.read())
        print ("    {}".format(property))
 
    # print("------------------------------------------------------------------")
    # print(lst)
    print("Total calls received: {}".format(RECEIVED_MESSAGES))
 
def main():
    print ("Starting the Python IoT Hub C2D Messaging device sample...")
 
    # Instantiate the client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
 
    print ("Waiting for C2D messages, press Ctrl-C to exit")
    try:
        # Attach the handler to the client
        client.on_message_received = message_handler
 
        while True:
            time.sleep(1000)
    except KeyboardInterrupt:
        print("IoT Hub C2D Messaging device sample stopped")
    finally:
        # Graceful exit
        print("Shutting down IoT Hub Client")
        client.shutdown()
 
if __name__ == '__main__':
    main()

