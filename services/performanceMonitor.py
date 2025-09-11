import time
import math

try:
    import psutil
    _HAS_PSUTIL = True
except Exception:
    _HAS_PSUTIL = False

try:
    import resource
    _HAS_RESOURCE = True
except Exception:
    _HAS_RESOURCE = False

try:
    import tracemalloc
    _HAS_TRACEMALLOC = True
except Exception:
    _HAS_TRACEMALLOC = False

def _format_bytes(n):
    # formato legible
    if n is None:
        return "N/A"
    if n < 1024:
        return f"{n} B"
    for unit in ["KB","MB","GB","TB"]:
        n /= 1024.0
        if n < 1024.0:
            return f"{n:.2f} {unit}"
    return f"{n:.2f} PB"

def obtener_metricas():
    """
    Devuelve un diccionario con métricas de memoria y tiempos CPU.
    Usa psutil si está disponible, si no intenta usar resource/tracemalloc.
    """
    now = time.time()
    metrics = {"timestamp": now}

    if _HAS_PSUTIL:
        proc = psutil.Process()
        mem_info = proc.memory_info()
        cpu_times = proc.cpu_times()
        metrics.update({
            "mem_rss": mem_info.rss,
            "mem_vms": getattr(mem_info, "vms", None),
            "cpu_user": getattr(cpu_times, "user", None),
            "cpu_system": getattr(cpu_times, "system", None),
            "cpu_percent": proc.cpu_percent(interval=None),
            "num_threads": proc.num_threads()
        })
    else:
        metrics.update({"mem_rss": None, "mem_vms": None, "cpu_user": None, "cpu_system": None, "cpu_percent": None, "num_threads": None})
        if _HAS_RESOURCE:
            usage = resource.getrusage(resource.RUSAGE_SELF)
            metrics["ru_maxrss"] = getattr(usage, "ru_maxrss", None)
            metrics["cpu_user"] = getattr(usage, "ru_utime", None)
            metrics["cpu_system"] = getattr(usage, "ru_stime", None)
        if _HAS_TRACEMALLOC:
            current, peak = tracemalloc.get_traced_memory()
            metrics["tracemalloc_current"] = current
            metrics["tracemalloc_peak"] = peak

    return metrics

def loggear_metricas(loggerPerf, etiqueta="snapshot"):
    m = obtener_metricas()
    msg = (f"[{etiqueta}] mem_rss={_format_bytes(m.get('mem_rss'))} "
           f"mem_vms={_format_bytes(m.get('mem_vms'))} "
           f"cpu_user={m.get('cpu_user')} cpu_sys={m.get('cpu_system')} "
           f"cpu_pct={m.get('cpu_percent')} threads={m.get('num_threads')}")
    loggerPerf.info(msg)
    return m
