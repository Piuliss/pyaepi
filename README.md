#Documentation
Pyapi is purposed to be used a Internet speed meter. For checking if our ISP provide the Internet speed that they sell us. 
Pyapi is a webapp built to be executed on Raspberry Pi 24/7 or in any PC with `python3`.

##Getting Started
* clone repository
* `cd pyaepi`
* `pip install -r requirements.txt`
* For creating SQlite DB: `python manage.py db upgrade`
* `python appserver.py`
* You should see a empty chart. Go to browser: `<RPI_IP>:5000`
* Check if scripts works: 

`cd scripts/python; chmod u+x speedtest-cron.sh; ./speedtest-cron.sh`
* Configure crontab:
    * `crontab -e`
    * Add a line: 
    Each 20 min it will check for download/upload measurements
    
    `*/20 * * * * <PYAEPI/PATH/PROJECT>/scripts/python/speedtest-cron.sh`
    
    