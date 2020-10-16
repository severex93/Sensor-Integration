# coding: utf8
import struct
import csv
import socket
import sys, select, msvcrt
import os
import time
import matplotlib as mpl
    # Use the OS display for the spectrum plot
#if os.environ.get('DISPLAY','') == '':
    #print('no display found. Using non-interactive Agg backend')
    #mpl.use('Agg')
import matplotlib.pyplot as plt
sk=None
sk2=None

        # Open a socket sk (to send) and sk2 (to receive)

def connect():
    host = "192.168.137.2"
    write_port = 5000
    read_port = 5001
    
    global sk
    sk= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect((host, write_port))

    global sk2
    sk2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk2.connect((host, read_port))
   

        # Operation number 1
        # the data must be bytes coded on 4 bytes in hexadecimal in little Endian
def readModuleID():
    connect()
    print("**** readModuleID ****\n")
    Operation = bytearray([0x01,0x00,0x00,0x00])
    resolution = bytearray([0x00,0x00,0x00,0x00])
    Mode = bytearray([0x00,0x00,0x00,0x00])
    zeroPadding = bytearray([0x00,0x00,0x00,0x00])
    scanTime = bytearray([0x00,0x00,0x00,0x00])
    commonWavNum = bytearray([0x00,0x00,0x00,0x00])
    opticalGain = bytearray([0x00,0x00,0x00,0x00])
    apodizationSel = bytearray([0x00,0x00,0x00,0x00])
    GeneralData = bytearray([0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00])
          # Data packet to send to execute command no: 1
    pr = Operation #+ resolution + Mode + zeroPadding + scanTime + commonWavNum + opticalGain + apodizationSel + GeneralData
         # Send package
    sk.send(pr)
    print("Bytes Sent : {}".format(len(pr)))
         # Closing the sending socket. If it remains open, the program loops and the socket to receive does not work.
    sk.close()

        # Data reception in bytes
        # The first 4 bytes indicate the length of the data that we receive
    id = sk2.recv(1024)

        # Return of the function for sending by Bluetooth without lengthing it
    #blt = id[4:]
        # Conversion to table
    id = list(id)
    print("LENGTH of data : {}".format(id[0:4]))
    print("moduleID : {}".format(id[4:]))
        # Convert each byte to character with a no-line display
    x = id[4:]
    for i in x:
        print(chr(i), end='')
    print(" \n")
    # Closing the reception socket
    sk2.close()
    #return blt


        # Operation number 2
def checkBoard():
    connect()
    print("**** checkBoard ****\n")
    Operation = bytearray([0x02,0x00,0x00,0x00])
    #resolution = bytearray([0x00,0x00,0x00,0x00])
    #Mode = bytearray([0x00,0x00,0x00,0x00])
    #zeroPadding = bytearray([0x03,0x00,0x00,0x00])
    #scanTime = bytearray([0xD0,0x07,0x00,0x00])
    #commonWavNum = bytearray([0x07,0x00,0x00,0x00])
    #opticalGain = bytearray([0x00,0x00,0x00,0x00])
    #apodizationSel = bytearray([0x00,0x00,0x00,0x00])
    #GeneralData = bytearray([0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                           # 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                           # 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                           # 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                           # 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00])
    pr = Operation #+ resolution + Mode + zeroPadding + scanTime + commonWavNum + opticalGain + apodizationSel + GeneralData
    sk.send(pr)
    print("Octets envoyes : {}".format(sk.send(pr)))
    sk.close()
    board = sk2.recv(1024)
    board = list(board)
    #blt = board[4:]
    print("LENGTH of data : {}".format(board[0:4]))
    print("BoardStatus  : {}".format(board[4:]))
    sk2.close()
    #return blt

        # Operation number 3
def runPSD():
    connect()
    print("**** runPSD ****\n")
    Operation = bytearray([0x03,0x00,0x00,0x00])
    resolution = bytearray([0x00,0x00,0x00,0x00])
    Mode = bytearray([0x00,0x00,0x00,0x00])
    zeroPadding = bytearray([0x03,0x00,0x00,0x00])
    scanTime = bytearray([0xD0,0x07,0x00,0x00])
    commonWavNum = bytearray([0x07,0x00,0x00,0x00])
    opticalGain = bytearray([0x00,0x00,0x00,0x00])
    apodizationSel = bytearray([0x00,0x00,0x00,0x00])
    GeneralData = bytearray([0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00])
    pr = Operation +resolution + Mode + zeroPadding + scanTime + commonWavNum + opticalGain + apodizationSel #+ GeneralData
    sk.send(pr)
    print("Bytes Sent : {}".format(sk.send(pr)))
    sk.close()

        # Several recv () to receive the entire data, i.e. 65548 bytes
    dataAll1 = sk2.recv(20480)
    dataAll2 = sk2.recv(20480)
    dataAll3 = sk2.recv(20480)
    dataAll4 = sk2.recv(20480)
    dataAll5 = sk2.recv(20480)
    dataAll6 = sk2.recv(20480)
        # concatenation of the data received
    dataAll = dataAll1 + dataAll2 + dataAll3 + dataAll4 + dataAll5 + dataAll6

    dataBytes = dataAll[12:]
    dataList = list(dataAll)
    print("LENGTH of data : {}".format(dataList[0:4]))
    print("STATUS : {}".format(dataList[4:8]))
    print("Length PSD et wavenumber : {}".format(dataList[8:12]))

        # Retrieving PSD values, each is coded on 8 bytes
        # Conversion of each 8 bytes => one value
    j=0
    psd = []
    for i in range(4096):
        val_1 = dataBytes[j:(j+8)]
        j+=8
        val_1 = int.from_bytes(val_1, "little")
            # Returned values ​​are quantized. It should be divided by 2 power (33) to de-quantize them.
        val_1 /= (2**33)
        psd.append(float("%.3f"%val_1))
    psd.reverse()


        # Recovery of the waveNumber values, each one is coded on 8 bytes
        # Conversion of each 8 bytes => one value
        # Returned values ​​are quantized. It should be divided by 2power (33) to de-quantize them.
    k = 4096*8
    wavNum = []
    for i in range(4096):
        val_2 = dataBytes[k:(k+8)]
        k+=8
        val_2 = int.from_bytes(val_2, "little")
        val_2/=(2**33)
            # Conversion of wavenumber from (cm-1) to wavelength (nm)
        val_2 = (10000000/val_2)
        wavNum.append(float("%.3f"%val_2))
    wavNum.reverse()

        # Writing the .csv file
    with open("dataRunPSD.csv", "w") as myFile:
        myFile = csv.writer(myFile)
        myFile.writerow(wavNum)
        myFile.writerow(psd)
        ## displayed on the graph
    plt.title("Spectre")
    plt.plot(wavNum, psd)
    #    plt.xlabel('Wave length')
    #    plt.ylabel('PSD')
    #    plt.grid(True)
    #    plt.show()
    sk2.close()

        # Operation warmup
def runWarmup():
    
    print("**** runWarmup ****\n")
    timer = time.time()
    warmtime = 600
    while True:
        connect()
        Operation = bytearray([0x04,0x00,0x00,0x00])
        resolution = bytearray([0x00,0x00,0x00,0x00])
        Mode = bytearray([0x00,0x00,0x00,0x00])     #single mode
        zeroPadding = bytearray([0x00,0x00,0x00,0x00])
        scanTime = bytearray([0xD0,0x07,0x00,0x00]) 
        commonWavNum = bytearray([0x00,0x00,0x00,0x00])
        opticalGain = bytearray([0x00,0x00,0x00,0x00])
        apodizationSel = bytearray([0x00,0x00,0x00,0x00])
        GeneralData = bytearray([0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                                0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                                0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                                0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                                0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00])
        
        pr = Operation + resolution + Mode + zeroPadding + scanTime + commonWavNum + opticalGain + apodizationSel + GeneralData
        sk.send(pr)
        print("Bytes Sent : {}".format(sk.send(pr)))
        sk.close()
        current_time = time.time()
        elapsed_time = current_time-timer
        print('\rElapsed time out of 600 seconds: '"%.2f" % elapsed_time)
        print('\rEnter Ctrl-C to escape')
        time.sleep(5)

        if elapsed_time > warmtime:
            print('warmup completed')
            break
    #time.sleep(600) #10min warmup
    #print("Warmup completed")
    back = sk2.recv(1024)
    back = list(back)
    print("LENGTH of data : {}".format(back[0:4]))
    print("STATUS : {}".format(back[4:])) # Status 0 = No error
    sk2.close()
def runKeepwarm():
    
    print("**** runKeepwarm ****\n")
    timer = time.time()
    warmtime = 600
    status = ''
    while status != 's':
        connect()
        Operation = bytearray([0x04,0x00,0x00,0x00])
        resolution = bytearray([0x00,0x00,0x00,0x00])
        Mode = bytearray([0x00,0x00,0x00,0x00])     #single mode
        zeroPadding = bytearray([0x00,0x00,0x00,0x00])
        scanTime = bytearray([0xD0,0x07,0x00,0x00]) 
        commonWavNum = bytearray([0x00,0x00,0x00,0x00])
        opticalGain = bytearray([0x00,0x00,0x00,0x00])
        apodizationSel = bytearray([0x00,0x00,0x00,0x00])
        GeneralData = bytearray([0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                                0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                                0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                                0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                                0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00])
        
        pr = Operation + resolution + Mode + zeroPadding + scanTime + commonWavNum + opticalGain + apodizationSel #+ GeneralData
        sk.send(pr)
        print("Bytes Sent : {}".format(sk.send(pr)))
        sk.close()

        #user input with timeout
        #systm will run through warming sequence until user inputs 
        t=0
        current_time = time.time()
        elapsed_time = current_time - timer
        print('Elapsed time '"%.2f" % elapsed_time)

        def readInput( caption, default, timeout = 5): #set timeout for user input
            start_time = time.time()
            sys.stdout.write('%s(%s):'%(caption, default))
            sys.stdout.flush()
            input = ''
            while True:
                if msvcrt.kbhit():
                    byte_arr = msvcrt.getche()
                    if ord(byte_arr) == 13: # enter_key
                        break
                    elif ord(byte_arr) >= 32: #space_char
                        input += "".join(map(chr,byte_arr))
                if len(input) == 0 and (time.time() - start_time) > timeout:
                    
                    print("Timed Out. Continuing Keepwarm")
                    print("initialisation is completed.")
                    break

            print('')  # needed to move to next line
            if len(input) > 0:
                return input
            else:
                return default

        status = readInput('Enter "s" to stop', ' ')
        print( 'Running Keepwarm %s' % status)
    
        if status == 's':
            break

    back = sk2.recv(1024)
    back = list(back)
    print("LENGTH of data : {}".format(back[0:4]))
    print("STATUS : {}".format(back[4:])) # Status 0 = No error
    sk2.close()  
def runBackground():
    connect()
    print("**** runBackground ****\n")
    Operation = bytearray([0x04,0x00,0x00,0x00])
    resolution = bytearray([0x00,0x00,0x00,0x00])   #16nm resolution
    Mode = bytearray([0x00,0x00,0x00,0x00])         #Using single run mode
    zeroPadding = bytearray([0x03,0x00,0x00,0x00])  #32k points used in the FFT
    scanTime = bytearray([0xD0,0x07,0x00,0x00])     #  ms ( Decimal to Hex to little endian) 
    #https://www.rapidtables.com/convert/number/decimal-to-hex.html 
    #https://www.scadacore.com/tools/programming-calculators/online-hex-converter/
    commonWavNum = bytearray([0x07,0x00,0x00,0x00]) #4096 points used for the wave number
    opticalGain = bytearray([0x00,0x00,0x00,0x00])  #using optical gain settings saved on the DVK
    apodizationSel = bytearray([0x00,0x00,0x00,0x00])   #Boxcar Apodization window
    GeneralData = bytearray([0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00])
                           
    pr = Operation + resolution + Mode + zeroPadding + scanTime + commonWavNum + opticalGain + apodizationSel #+ GeneralData
    sk.send(pr)
    print("Bytes Sent : {}".format(sk.send(pr)))
    sk.close()
    back = sk2.recv(1024)
    back = list(back)
    print("LENGTH of data : {}".format(back[0:4]))
    print("STATUS : {}".format(back[4:])) # Status 0 = No error
    sk2.close()

        # Operation number 5
def runAbsorbance():
    connect()
    print("**** runAbsorbance ****\n")
    #ref page 23 of SDK guide
    Operation = bytearray([0x05,0x00,0x00,0x00])    # 5 = absorbance operation
    resolution = bytearray([0x00,0x00,0x00,0x00])   #16nm resolution
    Mode = bytearray([0x00,0x00,0x00,0x00])         #Using single run mode
    zeroPadding = bytearray([0x03,0x00,0x00,0x00])  #32k points used in the FFT
    scanTime = bytearray([0xD0,0x07,0x00,0x00])     #  ms ( Decimal to Hex to little endian) 
    #https://www.rapidtables.com/convert/number/decimal-to-hex.html 
    #https://www.scadacore.com/tools/programming-calculators/online-hex-converter/
    commonWavNum = bytearray([0x07,0x00,0x00,0x00]) #4096 points used for the wave number
    opticalGain = bytearray([0x00,0x00,0x00,0x00])  #using optical gain settings saved on the DVK
    apodizationSel = bytearray([0x00,0x00,0x00,0x00])   #Boxcar Apodization window
    GeneralData = bytearray([0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00])
                            
    pr = Operation +resolution + Mode + zeroPadding + scanTime + commonWavNum + opticalGain + apodizationSel + GeneralData
    sk.send(pr)
    print("Bytes Sent : {}".format(len(pr)))
    sk.close()

    dataAll1 = sk2.recv(4096)
    dataAll2 = sk2.recv(4096)
    dataAll3 = sk2.recv(4096)
    dataAll4 = sk2.recv(4096)
    dataAll5 = sk2.recv(4096)
    dataAll6 = sk2.recv(4096)
    dataAll7 = sk2.recv(4096)
    dataAll8 = sk2.recv(4096)
    dataAll9 = sk2.recv(4096)
    dataAll10 = sk2.recv(4096)
    dataAll11 = sk2.recv(4096)
    dataAll12 = sk2.recv(4096)
    dataAll13 = sk2.recv(4096)
    dataAll14 = sk2.recv(4096)
    dataAll15 = sk2.recv(4096)
    dataAll16 = sk2.recv(4096)
    dataAll17 = sk2.recv(4096)
    dataAll18 = sk2.recv(4096)
    dataAll19 = sk2.recv(4096)
    dataAll20 = sk2.recv(4096)
    dataAll21 = sk2.recv(4096)
    dataAll22 = sk2.recv(4096)
    dataAll23 = sk2.recv(4096)
    dataAll24 = sk2.recv(4096)
    dataAll25 = sk2.recv(4096)
    dataAll26 = sk2.recv(4096)
    dataAll27 = sk2.recv(4096)
    dataAll28 = sk2.recv(4096)
    dataAll29 = sk2.recv(4096)
    dataAll30 = sk2.recv(4096)


    dataAll = dataAll1 + dataAll2 + dataAll3 + dataAll4 + dataAll5 + dataAll6 + dataAll7 + dataAll8 + dataAll9 + dataAll10\
                + dataAll11 + dataAll12 + dataAll13 + dataAll14 + dataAll15 + dataAll16 + dataAll17 + dataAll18 + dataAll19 + dataAll20\
                + dataAll21 + dataAll22 + dataAll23 + dataAll24 + dataAll25 + dataAll26 + dataAll27 + dataAll28 + dataAll29 + dataAll30\

    dataBytes = dataAll[12:]
    dataList = list(dataAll)
    print("LENGTH of data : {}".format(dataList[0:4]))
    print("STATUS : {}".format(dataList[4:8]))
    print("Length absorbance of waveNumber : {}".format(dataList[8:12]))

        # Recovery of Absorbance values, each is coded on 8 bytes
        # Conversion of each 8 bytes => one value
        # Returned values ​​are quantized. It should be divided by 2 power (33) to de-quantize them.
    j= 0
    absorbance = []
    for i in range(4096):
        val_1 = dataBytes[j:(j+8)]
        j+=8
        val_1 = int.from_bytes(val_1, "little")
        val_1 /= (2**33)
        absorbance.append(float("%.3f"%val_1))
    absorbance.reverse()
    sk.close()


        # Recovery of the waveNumber values, each one is coded on 8 bytes
        # Conversion of each 8 bytes => one value
        # Returned values ​​are quantized. It should be divided by 2 power (30) to de-quantize them.
    k = 4096*8
    wavNum = []
    for i in range(4096):
        val_2 = int.from_bytes(dataBytes[k:(k+8)], byteorder='little')
        k+=8
        val_2/=(2**30)
        ## Conversion from wavenumber (cm-1) to wavelength (nm)
        val_2 = (10000000/val_2)
        wavNum.append(float("%.3f"%val_2))
    wavNum.reverse()

    # Writing .csv file
    name=input("File name:")
    directory=(r'C:\\Users\\siewty\\Desktop\\Current_Projects\\FMCG\\Sensor-Integration-master\\Actimax Char\\')
    with open(directory , name+"_dataRunAbsorbance.csv", "w", newline="") as myFile:
        myFile = csv.writer(dt, myFile)
        myFile.writerow(wavNum)
        myFile.writerow(absorbance)
        
    # Display on the graph
    plt.title(name+"Spectre")
    plt.plot(wavNum, absorbance)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Absorbance')
    plt.grid(True)
    fig1 = plt.gcf()
    plt.show()
    plt.draw()
    fig1.savefig(name+'_absorbance.png')

    sk2.close()
        # Return function for send by Bluetooth
    return (wavNum, absorbance)


        # Operation number 6
def runGainAdj():
    connect()
    print("**** runGainAdj ****\n")
    Operation = bytearray([0x06,0x00,0x00,0x00])
    pr = Operation
    sk.send(pr)
    print("Octets envoyes : {}".format(len(pr)))
    sk.close()
    x = sk2.recv(1024)
    x = list(x)
    print("LENGTH of data : {}".format(x[0:4]))
    print("STATUS : {}".format(x[4:5]))
    print("Gain code : {}".format(x[5:7]))
    sk2.close()

        # Operation number 7
def BurnGain():
    connect()
    print("**** BurnGain ****\n")
    Operation = bytearray([0x07,0x00,0x00,0x00])
    pr = Operation
    sk.send(pr)
    print("Octets envoyes : {}".format(len(pr)))
    sk.close()
    x = sk2.recv(1024)
    x = list(x)
    print("LENGTH of data : {}".format(x[0:4]))
    print("STATUS : {}".format(x[4:]))
    sk2.close()

        # Operation number 8
def BurnSelf():
    connect()
    print("**** BurnGain ****\n")
    Operation = bytearray([0x08,0x00,0x00,0x00])
    pr = Operation
    sk.send(pr)
    print("Octets envoyes : {}".format(len(pr)))
    sk.close()
    x = sk2.recv(1024)
    x = list(x)
    print("LENGTH of data : {}".format(x[0:4]))
    print("STATUS : {}".format(x[4:]))
    sk2.close()

        # Operation number 9
def runWLN():
    connect()
    print("**** runWLN ****\n")
    Operation = bytearray([0x09,0x00,0x00,0x00])
    pr = Operation
    sk.send(pr)
    print("Octets envoyes : {}".format(len(pr)))
    sk.close()
    x = sk2.recv(1024)
    x = list(x)
    print("LENGTH of data : {}".format(x[0:4]))
    print("STATUS : {}".format(x[4:]))
    sk2.close()


        # Operation number 10
def runSelfCorr():
    connect()
    print("**** runSelfCorr ****\n")
    Operation = bytearray([0x0A,0x00,0x00,0x00])
    resolution = bytearray([0x00,0x00,0x00,0x00])
    zeroPadding = bytearray([0x03,0x00,0x00,0x00])
    scanTime = bytearray([0xD0,0x07,0x00,0x00])
    commonWavNum = bytearray([0x07,0x00,0x00,0x00])
    opticalGain = bytearray([0x00,0x00,0x00,0x00])
    apodizationSel = bytearray([0x00,0x00,0x00,0x00])
    
    pr = Operation +resolution + zeroPadding + scanTime + commonWavNum + opticalGain + apodizationSel 
    sk.send(pr)
    print("Bytes Sent : {}".format(len(pr)))
    sk.close()
    x = sk2.recv(1024)
    x = list(x)
    print("LENGTH of data : {}".format(x[0:4]))
    print("STATUS : {}".format(x[4:]))
    sk2.close()

        # Operation number 11
def runWavelengthCorrBG():
    connect()
    print("**** runWavelengthCorrBG ****\n")
    Operation = bytearray([0x0B,0x00,0x00,0x00])    #Operation 11
    resolution = bytearray([0x00,0x00,0x00,0x00])   #Resolution 0
    Mode = bytearray([0x00,0x00,0x00,0x00])         #Not Req
    zeroPadding = bytearray([0x03,0x00,0x00,0x00])  #32k points
    scanTime = bytearray([0xD0,0x07,0x00,0x00])
    commonWavNum = bytearray([0x07,0x00,0x00,0x00])
    opticalGain = bytearray([0x00,0x00,0x00,0x00])
    apodizationSel = bytearray([0x00,0x00,0x00,0x00])
    GeneralData = bytearray([0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00])
    pr = Operation +resolution + Mode + zeroPadding + scanTime + commonWavNum + opticalGain + apodizationSel + GeneralData
    sk.send(pr)
    print("Octets envoyes : {}".format(len(pr)))
    sk.close()
    x = sk2.recv(1024)
    x = list(x)
    print("LENGTH of data : {}".format(x[0:4]))
    print("STATUS : {}".format(x[4:]))
    sk2.close()

        # Operation number 13
def restoreDefault():
    connect()
    print("**** restoreDefault ****\n")
    Operation = bytearray([0x0D,0x00,0x00,0x00])
    pr = Operation
    sk.send(pr)
    print("Bytes Sent : {}".format(len(pr)))
    sk.close()
    x = sk2.recv(1024)
    x = list(x)
    print("LENGTH of data : {}".format(x[0:4]))
    print("STATUS : {}".format(x[4:]))
    sk2.close()

        # Operation number 14
def readSoftwareVersion():
    connect()
    print("**** readSoftwareVersion ****\n")
    Operation = bytearray([0x0E,0x00,0x00,0x00])
    pr = Operation
    sk.send(pr)
    print("Bytes Sent : {}".format(len(pr)))
    sk.close()
    version = sk2.recv(1024)
    dvk = version[4:8]
    pi = version[8:12]
    version = list(version)
    print("LENGTH of data : {}".format(version[0:4]))
    print("DVK version : {}".format(version[4:8]))
        # coversion of each byte in character
    x = version[4:8]
    for i in x:
        print(chr(i), end=' ')
    print("\n")
    print("Pi version : {}".format(version[8:12]))
        # coversion of each byte in character
    x = version[8:12]
    for i in x:
        print(chr(i), end=' ')
    print("\n")
    sk2.close()
    return (dvk,pi)
def SourceSettings():
    connect()
    print("**** SourceSettings ****\n")
    Operation = bytearray([0x16,0x00,0x00,0x00])
    resolution = bytearray([0x00,0x00,0x00,0x00])   #16nm resolution
    Mode = bytearray([0x00,0x00,0x00,0x00])         #Using single run mode
    zeroPadding = bytearray([0x00,0x00,0x00,0x00])  #32k points used in the FFT
    scanTime = bytearray([0x00,0x00,0x00,0x00])     #  ms ( Decimal to Hex to little endian) 
    #https://www.rapidtables.com/convert/number/decimal-to-hex.html 
    #https://www.scadacore.com/tools/programming-calculators/online-hex-converter/
    commonWavNum = bytearray([0x00,0x00,0x00,0x00]) #4096 points used for the wave number
    opticalGain = bytearray([0x00,0x00,0x00,0x00])  #using optical gain settings saved on the DVK
    apodizationSel = bytearray([0x00,0x00,0x00,0x00])   #Boxcar Apodization window
    GeneralData = bytearray([0x02,0x00,0x00,0x00, 0x0E,0x0A,0x02,0x01, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00])
                            #data type = int[40]
    pr = Operation + resolution + Mode + zeroPadding + scanTime + commonWavNum + opticalGain + apodizationSel + GeneralData
    sk.send(pr)
    print("Bytes Sent : {}".format(sk.send(pr)))
    sk.close()
    back = sk2.recv(1024)
    back = list(back)
    print("LENGTH of data : {}".format(back[0:4]))
    print("STATUS : {}".format(back[4:])) # Status 0 = No error
    sk2.close()
def setOpticalSettings():
    connect()
    print("**** runOpticalSettings ****\n")
    Operation = bytearray([0x1B,0x00,0x00,0x00])
    GeneralData = bytearray([0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00,\
                            0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00])
    pr = Operation + GeneralData
    sk.send(pr)
    print("Bytes Sent : {}".format(len(pr)))
    sk.close()
    x = sk2.recv(1024)
    x = list(x)
    print("LENGTH of data : {}".format(x[0:4]))
    print("STATUS : {}".format(x[4:]))
    sk2.close()