import psutil
import win32service

from typing import Optional

def getPidByServiceName(service) -> Optional[int]:
    try:

        service = win32service.OpenService(
            win32service.OpenSCManager(None, None, win32service.SC_MANAGER_ALL_ACCESS),
            service,
            win32service.SERVICE_QUERY_STATUS
        )

        status = win32service.QueryServiceStatusEx(service)
        pid = status['ProcessId']

        if pid != 0:
            return pid

    except Exception as e:
        pass
    return None


def getServiceNameByPID(pid) -> Optional[str]:
    try:
        process = psutil.Process(pid)
        return process.name()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            return None