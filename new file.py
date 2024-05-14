import psutil
def scan_background_apps():
    all_process=psutil.process_iter()
    
    background_apps={}
    
    for process in all_process:
        try:
            process_name=process.name()
            if process_name.startswith('python')or process_name=='pythonw':
                continue
            else:
                cpu_percent=process.cpu_percent()
                memory_usage=process.memory_info().rss/(1024*1024)
                background_apps[process_name]=('cpu_percent',cpu_percent,'memory_usage',memory_usage)
            
            
        except( psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
                pass
            
    return background_apps
