import socket
# 创建socket对象
socket_client = socket.socket()
# 连接到服务器
socket_client.connect(("192.168.137.1", 8888))
 
while True:
    send_msg = input("请输入要发送给服务端的消息：")
    if send_msg == "exit":
        break
    # 发送消息
    socket_client.send(send_msg.encode("UTF-8"))
    # 接受消息
    recv_data = socket_client.recv(1024).decode("UTF-8")    # 1024是缓冲区大小，一般就填1024， recv是阻塞式
    print(f"服务端回复的消息是：{recv_data}")
 
# 关闭连接
socket_client.close()