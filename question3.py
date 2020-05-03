import os
import signal
import multiprocessing

#For example we have 4 cores but CPU have in addition to these 4 logical cores. So we multiply with two.

load1, load5, load15 = os.getloadavg()
print("5min loadavg value: ", load5)
print("Real core count: ", multiprocessing.cpu_count())
core_count = cpuCount = multiprocessing.cpu_count() * 2
print("Core count with logic cores: ", core_count)

if load5 >= core_count:
  pid = os.fork()
  if pid :
    print("\nIn parent process")
    os.kill(pid, signal.SIGSTOP)
    print("Signal sent, child stopped.") 
    info = os.waitpid(pid, os.WSTOPPED)
    stopSignal = os.WSTOPSIG(info[1]) 
    print("Child stopped due to signal no:", stopSignal) 
    print("Signal name:", signal.Signals(stopSignal).name)
    os.kill(pid, signal.SIGCONT)  
    print("\nSignal sent, child continued.") 

  else:      
    print("\nIn child process") 
    print("Process ID:", os.getpid()) 
    print("Hello ! Geeks") 
    print("Exiting")

else:
  print("We do not have any problem :)")