import psutil
import shutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / (1024 * 1024 * 1024) 
    total = du.total / (1024 * 1024 * 1024)  
    return free > 1, free, total 

def check_cpu_usage():
    cu = psutil.cpu_percent(1)
    return cu, cu < 75 

def check_ram_usage():
    ram = psutil.virtual_memory()  
    available = ram.available / (1024 * 1024 * 1024) 
    total = ram.total / (1024 * 1024 * 1024)  
    return available > 2, available, total  

name = input("Enter disk name = ") +':'
cu, cpu_result = check_cpu_usage()
ram_result, ram_available, ram_total = check_ram_usage()
disk_result, disk_free, disk_total = check_disk_usage(name)

print(f"CPU usage: {cu}%")
print(f"RAM: {ram_available:.2f} GB / {ram_total:.2f} GB")
print(f"Disk space on {name}: {disk_free:.2f} GB / {disk_total:.2f} GB")

if cpu_result and ram_result and disk_result:
    print("Everything is OK!")
    
else:
    print("ERROR!")
