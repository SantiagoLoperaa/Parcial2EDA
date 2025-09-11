import logging
import os

def configurar_loggers(nivel_consola=logging.INFO):
    carpeta_logs = "logs"
    os.makedirs(carpeta_logs, exist_ok=True)

    formato = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    logger_sistema = logging.getLogger("parcial.sistema")
    logger_sistema.setLevel(logging.INFO)
    fh_sistema = logging.FileHandler(os.path.join(carpeta_logs, "sistema.log"), encoding="utf-8")
    fh_sistema.setFormatter(formato)
    if not logger_sistema.handlers:
        logger_sistema.addHandler(fh_sistema)

    logger_tiempos = logging.getLogger("parcial.tiempos")
    logger_tiempos.setLevel(logging.INFO)
    fh_tiempos = logging.FileHandler(os.path.join(carpeta_logs, "tiempos.log"), encoding="utf-8")
    fh_tiempos.setFormatter(formato)
    if not logger_tiempos.handlers:
        logger_tiempos.addHandler(fh_tiempos)

    logger_perf = logging.getLogger("parcial.performance")
    logger_perf.setLevel(logging.INFO)
    fh_perf = logging.FileHandler(os.path.join(carpeta_logs, "performance.log"), encoding="utf-8")
    fh_perf.setFormatter(formato)
    if not logger_perf.handlers:
        logger_perf.addHandler(fh_perf)

    console = logging.StreamHandler()
    console.setLevel(nivel_consola)
    console.setFormatter(formato)
    root_logger = logging.getLogger()
    if not any(isinstance(h, logging.StreamHandler) for h in root_logger.handlers):
        root_logger.addHandler(console)
        root_logger.setLevel(logging.INFO)

    return logger_sistema, logger_tiempos, logger_perf

loggerSistema, loggerTiempos, loggerPerformance = configurar_loggers()
