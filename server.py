# Importing the required libraries for the code
import socket  # Used to create a socket and that is the main component in network
import cv2  # Uses frame by frame data and sends it over the sockets to simulate a video call
import pickle #
import struct

# Socket Created for server
# the tcp protocol is SOCK.STREAM
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = "localhost"  # Using "localhost" for testing on the same machine
port = 9999
socket_address = (host_ip, port)

# Socket Bind
server_socket.bind(socket_address)

# Socket Listenif
server_socket.listen(1)
print("Listening at:", socket_address)

# Socket Accept
while True:
    client_socket, addr = server_socket.accept()
    print('Connected to:', addr)
    if client_socket:
        vid = cv2.VideoCapture(0)

        while vid.isOpened():
            ret, image = vid.read()
            img_serialize = pickle.dumps(image)
            message = struct.pack("Q", len(img_serialize)) + img_serialize
            client_socket.sendall(message)

            cv2.imshow('Video from Server', image)
            key = cv2.waitKey(10)
            if cv2.waitKey(1) == ord('q'):
                break

        vid.release()
        cv2.destroyAllWindows()
