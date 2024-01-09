import psutil
import GPUtil
print("[GPU]")
GPUtil.showUtilization()
print("\n[RAM]")
mem_usage = psutil.virtual_memory()
print(f"Total RAM: {mem_usage.total/(1024**3):.2f}G")
print(f"Free RAM: {mem_usage.free/(1024**3):.2f}G")
print(f"Used RAM: {mem_usage.used/(1024**3):.2f}G")
print(f"RAM Usage: {mem_usage.percent}%")

print(f"\n[CPU]")
per_cpu = psutil.cpu_percent(percpu=True,interval=1)
avg = 0
for idx, usage in enumerate(per_cpu):
    avg += usage
    
print(f"CORE_avg: {avg/(idx+1)}%\n")
for idx, usage in enumerate(per_cpu):
    print(f"CORE_{idx}: {usage}%")
