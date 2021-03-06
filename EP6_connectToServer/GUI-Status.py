from tkinter import *
import socket
import threading

def runServer():
    #####################
    serverip = '192.168.1.18'
    port = 9000
    #####################

    buffsize = 4096

    while True:
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        server.bind((serverip,port))
        server.listen(1)
        print('waiting micropython...')

        client, addr = server.accept()
        print('connected from:', addr)

        data = client.recv(buffsize).decode('utf-8')
        print('Data from MicroPython: ',data)
        # data = 'LED:ON' / 'LED:OFF'
        data_split = data.split(':')
        if data_split[1] == 'ON':
            v_status.set('LED Status: {}'.format(data_split[1]))
            L2.configure(fg='green')
        else:
            v_status.set('LED Status: {}'.format(data_split[1]))
            L2.configure(fg='red')
        client.send('received your messages.'.encode('utf-8'))
        client.close()

GUI = Tk()
GUI.title('หน้าต่างแสดงสถานะ')
GUI.geometry('600x600')

#ข้อความแสดง - ไม่เปลี่ยนแปลง
FONT = ('Angsana New',30)
L1 = Label(GUI,text='สถานะสัญญาณไฟ LED',font=FONT)
L1.pack()

#ข้อความแสดง - เปลี่ยนแปลง
v_status = StringVar()
v_status.set('<<< No Status >>>')
L2 = Label(GUI, textvariable=v_status, font=FONT)
L2.pack()

#-------------------------------------Run Server-------------------------------------
task = threading.Thread(target=runServer)
task.start()

GUI.mainloop()