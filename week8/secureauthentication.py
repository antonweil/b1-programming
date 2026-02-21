import hashlib
from datetime import datetime
#imports for hashing and fetching datetime for log generation

class user:
    def __init__(self, name, password, priv):
        self.__name = name
        self.__hash = self.__generate_hash(password)
        self.__priv = priv
        self.__attempts = 0
        self.__status = True
        self.__log = []
        #constructor doesnt store password, but rather hashes it right away
        #variables are also private

    #admin_pw: 23mj§.§ for reference
    admin_hash = "bf018d8c2efa83a45d33377c7c107203201fa5297ed78f6bfa62073465cb983d"
    hierarchy = {'guest':0, 'user':1, 'admin':2}

    #call sha256 function to generate hashes in private function
    def __generate_hash(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    #checks if account locked and compares hashed passwords, acts and logs accordingly
    def authenticate(self, password):
        if self.__status == False:
            self.__log_activity('Tried to Login to locked Account')
            return False

        if self.__hash == self.__generate_hash(password):
            self.__log_activity('Authentication Successful')
            return True
        else:
            self.__log_activity('authentication failed')
            self.__attempts = self.__attempts+1
            if self.__attempts >= 3:
                self.lock_account()
            return False

    #may be called whenever an account needs to be locked
    def lock_account(self):
        self.__status = False
        self.__log_activity('Account locked due to failed login attempts')

    #generates logs based on datetime and the provided message, appending them to self.__log
    def __log_activity(self, message):
        self.__log.append(f"{datetime.now()}: {message}")
    
    #compares required to actual priviledge level, returns True or False accordingly
    def check_priv(self, req):
        return user.hierarchy.get(self.__priv, 0) >= user.hierarchy.get(req, 0)

    #authenticates using admin_pw, resets account if successful and logs
    def reset_login_attempts(self, admin_pw):
        if user.admin_hash == self.__generate_hash(admin_pw):
            self.__attempts = 0
            self.__status = True
            self.__log_activity('Account login attempts reset & Account unlocked')
        else:
            self.__log_activity('Admin Authentication Failed')
    
    def get_username(self):
        return self.__name

class device:
    def __init__(self, id, type, version, owner):
        self.__id = id
        self.__type = type
        self.__version = version
        self.__compliance = False
        self.__owner = owner
        self.__last_scan = None
        self.__active = True
        self.__log = []

    def authorize_access(self, user):
        if self.__active == False:
            self.__log_activity(user.get_username(), 'Access Denied: Inactive Device')
            return False
        
        if self.__compliance != True:
            self.__log_activity(user.get_username(), 'Access Denied: Noncomliant device')
            return False

        if self.__owner == user.get_username():
            self.__log_activity(user.get_username(), 'Access Granted')
        else:
            self.__log_activity(user.get_username(), 'Access Denied: user is not owner')


    def update_firmware(self, new_version, user):
        if not user.check_priv('admin'):
            self.__log_activity(user.get_username(), 'Firmware Update Denied: Insufficient Privilege')
            return False
        self.__version = new_version
        self.__log_activity(user.get_username(), f'Firmware updated to {new_version}')
        return True
    
    def security_scan(self):
        self.__last_scan = datetime.now()
        self.__compliance = True
        self.__log_access('SYSTEM', 'Security scan completed')

    def check_comliance(self):
        if self.__last_scan is None:
            self.__compliance = None
            return False
        days_since_scan = (datetime.now() - self.__last_scan).days
        if days_since_scan > 30:
            self.__compliance = False
            return False
        return self.__compliance == True
    
    def quarantine(self, user):
        if not user.check_priv('admin'):
            self.__log_activity(user.get_username(), 'Quarantine Denied: Insufficient Privilege')
            return False
        else:
            self.__active = False
            self.__log_activity(user.get_username(), 'Device Quarantined')

    def get_device_info(self):
        return {
        'device_id': self.__device_id,
        'device_type': self.__device_type,
        'firmware_version': self.__firmware_version,
        'compliance_status': self.__compliance_status,
        'owner': self.__owner,
        'is_active': self.__is_active
        }
    
    def __log_activity(self, username, message):
        self.__log.append(f"{datetime.now()}: {username} - {message}")

class DeviceManager:
    def __init__(self):
        self.__devices = {}

    def add_device(self, device):
        device_info = device.get_device_info()
        self.__devices[device_info['device_id']] = device

    def remove_device(self, id, user):
        if not user.check_priv == 'admin':
            return False
        if id in self.__devices:
            del self.__devices [id]
            return True
        return False
    
    def generate_report(self, user):
        if not user.check_priv == 'admin':
            return None
        report = []
        for id, device in self.__devices:
            device.check_compliance()
            info = device.get_device_info()
            report.append(info)
        return info


p = user("john", "zz3+4", 1)

p.authenticate("zz3+4e")

q = device(1, 'laptop', '11.3.2', p.get_username())

q.authorize_access(p)

print(q._device__log)