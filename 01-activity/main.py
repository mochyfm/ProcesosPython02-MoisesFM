import os, platform
import sys
from multiprocessing import Process
from time import sleep

def padre(customNumber):

    if platform.system() == "Windows":
        
        print("WINDOWS (PADRE) -> PID:", os.getpid(), '\n');

        for idx in range(customNumber):
            print("Llamando al", str(idx + 1) + "º proceso.")
            process = Process(target=hijo);
            process.start();
            process.join(0);

    elif platform.system() == "Linux":

        print("LINUX (PADRE) -> PID:", os.getpid());

        for idx in range(customNumber):
            print("Llamando al", (idx + 1), "º proceso.")
            newPid = os.fork();
            if newPid == 0:
                hijo();

def hijo():
    print('\n > Hijo con PID:', os.getpid(), '\n');
    sleep(5);
    print('\nEl proceso con PID:', os.getpid(), "ha muerto.\n")
    sys.exit(0);

if __name__ == "__main__":

    userNumber = int(input("\nDame un número de procesos que quieras abrir: "));
    padre(userNumber);