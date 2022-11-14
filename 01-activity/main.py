import os, platform
import sys
from multiprocessing import Process
from time import sleep

def callProcessNumber(loopNumber):

    platformOs = platform.system()
    print(platformOs.capitalize() + " (PADRE) -> PID:", os.getpid(), '\n');

    for idx in range(loopNumber):
        print("Llamando al", str(idx + 1) + "º proceso.")
        if platformOs == "Windows":
            process = Process(target=hijo);
            process.start();
            process.join(0);
        elif platformOs == "Linux":
            newPid = os.fork();
            if newPid == 0:
                hijo();
        else:
            print('No se ejecutar procesos en tu OS.')
            break;
    
def padre(customNumber):
    callProcessNumber(customNumber);
    print('\nYa he terminado de llamar.');

def hijo():
    
    processId = str(os.getpid());

    print('\n > Hijo con PID: ' + processId + '\n');
    sleep(5);
    print('\nEl proceso con PID: ' + processId + " ha muerto.\n")
    sys.exit(0);

if __name__ == "__main__":

    userNumber = int(input("\nDame un número de procesos que quieras abrir: "));
    padre(userNumber);