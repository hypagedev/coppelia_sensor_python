import sim
import sys
import time

print ('Programa inicio')
sim.simxFinish(-1) # cerrar todas las conexiones
# Conectar a CoppeliaSim
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5)
if clientID!=-1:
    print ('Conectado al API del servidor remoto')

    _  , prox_handle = sim.simxGetObjectHandle(clientID, "Proximity_sensor", sim.simx_opmode_oneshot_wait)

    for i in range(100):
        _, sta, point, objh, vec = sim.simxReadProximitySensor(clientID, prox_handle, sim.simx_opmode_streaming)
        print((sta, point))
        time.sleep(0.1)
    # Ahora cerrar la conexion a CoppeliaSim:
    sim.simxFinish(clientID)
else:
    sys.exit('Fallo conectando al API del servidor remoto')
print ('Programa finalizado')
