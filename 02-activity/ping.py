import subprocess
import platform

class Ping():

    def __init__(self, hostname:str, numberOfPackages:int=None):
        self.__hostname = hostname
        self.__numberOfPackages = int(numberOfPackages)

    def getHostname(self):
        return self.__hostname

    def getNumberOfPackages(self):
        return self.__numberOfPackages

    def ping(self):
        
        command = ['ping', self.getHostname()];
        state = False;
        result = 'No info could be retrieved from \"' + self.getHostname() + '\"';

        if self.getNumberOfPackages() != None: 
            command = ['ping', '-n' if platform.system() == 'Windows' else '-c' , str(self.getNumberOfPackages()) , self.getHostname()]
        try:
            
            # Source: https://docs.python.org/3/library/subprocess.html
            
            # On this way we check the complete feedback with its information, we would need to initialize it though
            #   and return it on the bottom so it can be reached by both sides.
            #
            #   response = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            #

            result = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True);
            result = self.resultParser(result);
            state = True;
        except Exception as e:
            print("\nThe hostname: " + self.getHostname() + " could not be found.")
            return None
        
        return { "outputInfo": result, "state": state }; 

        

    def resultParser(self, result):

        fullResult = result.strip().splitlines()

        # We do this for taking out the first lines of code that say the
        #   message of "Pinging example.com [1.1.1.1]..." and "Answer from 1.1.1.1"

        # we start getting the initial index that doesnt includes this lines
        # for that, we create a "innitialIndex" that will allow us to start from that point

        innitialIndex = (len(fullResult) + 2) - (len(fullResult) - self.getNumberOfPackages()) ;
        
        # After getting the innitialIndex we filter it on the original List

        filteredArray = fullResult[innitialIndex:];

        # Thanks to this, we can now take out all the information we want; since it its filtered, 
        # there will be no reason to do it at once, since its always going to be the same.
        
        ipDirection = '.'.join(((filteredArray[0]).split(" ")[4]).split(":")[:1]);

        sendedPackages = int(((filteredArray[1]).strip().split(" ")[3])[:1]);
        reciebedPackages = int(((filteredArray[1]).strip().split(" ")[6])[:1]);
        lostPackages = int(((filteredArray[1]).strip().split(" ")[9])[:1]);

        estimatedPercentage = (filteredArray[2]).strip().split("(")[1].split(")")[0]

        minTime = (filteredArray[4]).strip().split(" ")[2][:4];
        maxTime = (filteredArray[4]).strip().split(" ")[5][:4];
        averageTime = (filteredArray[4]).strip().split(" ")[8];

        return {
            "ipDirection": ipDirection,
            "sendedPackages": sendedPackages,
            "reciebedPackages": reciebedPackages,
            "lostPackages": lostPackages,
            "estimatePercentage": estimatedPercentage,
            "minTime": minTime,
            "maxTime": maxTime,
            "averageTime": averageTime,
        };  