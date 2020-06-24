import sim
import sys
import time
import cv2
import numpy as np

print ('Programa inicio')
sim.simxFinish(-1) # cerrar todas las conexiones
# Conectar a CoppeliaSim
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5)
if clientID!=-1:
    print ('Conectado al API del servidor remoto')

    #Guardar la referencia de la camara
    _, camhandle = sim.simxGetObjectHandle(clientID, 'Vision_sensor', sim.simx_opmode_oneshot_wait)
    _, resolution, image = sim.simxGetVisionSensorImage(clientID, camhandle, 0, sim.simx_opmode_streaming)
    time.sleep(1)
    while(1):
        #Guardar frame de la camara, rotarlo y convertirlo a BGR
        _, resolution, image=sim.simxGetVisionSensorImage(clientID, camhandle, 0, sim.simx_opmode_buffer)
        img = np.array(image, dtype = np.uint8)
        img.resize([resolution[0], resolution[1], 3])
        #img = np.rot90(img,2)
        img = np.fliplr(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        #Mostrar frame y salir con "ESC"
        cv2.imshow('Image', img)
        tecla = cv2.waitKey(5) & 0xFF
        if tecla == 27:
            break
    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)
else:
    sys.exit('Failed connecting to remote API server')
print ('Program ended')
