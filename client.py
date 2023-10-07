import socket,cv2, pickle,struct
# create socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#  server ip address here
host_ip = '192.168.101.176' 
port = 3000
client_socket.connect((host_ip,port)) 
data = b""
metadata_size = struct.calcsize("Q")
while True:
 while len(data) < metadata_size:
  packet = client_socket.recv(4*1024) 
  if not packet: break
  data += packet
 packed_msg_size = data[:metadata_size]
 data = data[metadata_size:]
 msg_size = struct.unpack("Q",packed_msg_size)[0]
 
 while len(data) < msg_size:
  data += client_socket.recv(4*1024)
  frame_data = data[:msg_size]
  data  = data[msg_size:]
  frame = pickle.loads(frame_data)
  cv2.imshow("Receiving Video ",frame)
  key = cv2.waitKey(10) 
  if key  == 13:
   break
client_socket.close()