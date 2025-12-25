
import ntplib 

from time import ctime  






import time

def print_time():
    ntp_client= ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
   # print(ctime(response.tx_time))



    local_time = time.time()
    drift = local_time - response.tx_time
    print(f' Local time {ctime(local_time)}')
    print(f'NTP Time {ctime(response.tx_time)}')
    print(f'Drift {round (drift, 2)} seconds')
    
    if(abs(drift)>5):
        print("Clock drift detected")
    else:
        print("Clock in sync")


 

if __name__ == '__main__':
    print_time()
    

