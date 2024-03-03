import socket
import webbrowser
from AppOpener import open

new_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name = socket.gethostname()
s_ip = socket.gethostbyname_ex(host_name)[2][1]

port = 8080

new_socket.bind(("", port))
print( "Binding successful!")
print("This is your IP: ", s_ip)


new_socket.listen(5)
conn, add = new_socket.accept()


print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])

client = (conn.recv(1024)).decode()
print(client + ' has connected.')
conn.send("hello".encode())
while True:
    mes=conn.recv(1024).decode()
    webbrowser.register("google", None, webbrowser.BackgroundBrowser(
         "C:\Program Files\Google\Chrome\Application\chrome.exe"))
    if mes=="google":
        open("google chrome")
    elif mes=="facebook":
        webbrowser.get("google").open_new("https://www.facebook.com/")
    elif mes=="youtube":
        webbrowser.get("google").open_new("https://www.youtube.com/")
    elif mes=="PyCharm":
        open("pycharm community edition")
    elif mes=="intelliJ":
        open("intellij idea community edition")
    elif mes=="Clion":
        open("clion")
    elif "search" in mes:
        mes=mes[6:]
        if "http" in mes or "www" in mes or".com" in mes:
            webbrowser.get("Brave").open_new(mes)
        else:
            mes=mes.strip().replace(" ","+",mes.count(" "))
            webbrowser.get("Brave").open_new("https://www.google.com/search?q="+mes)
    elif mes=="stop":
        exit()
