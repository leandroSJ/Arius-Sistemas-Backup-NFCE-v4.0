from datetime import datetime, date, timedelta, time
import shutil
import schedule
import os
import pyfiglet
import sys

class Backup:
        
    def stop(self):
        player_input = str(input('Presione <ENTER> para encerrar...'))
        if player_input != 0:
            sys.exit()
    
                        
BC = Backup()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
BC.CopyMatriz()
#BC.run()
#schedule.every(1).second.do(BC.CopyFilial)

#while 1:
    #schedule.run_pending()
    #time.sleep(1)
#schedule.every().day.at('07:45').do(BC.CopyKW)
#schedule.every().day.at('07:45').do(BC.CopyRetaguarda)