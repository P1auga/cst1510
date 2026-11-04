def classify_logs(logs):
    errors = infos = warnings = 0

    for entry in logs:
        timestamp = entry.split("]")[0].strip("[")
        message = entry.split("] ", 1)[1]
        print("Timestamp:", timestamp)

        if message.startswith("ERROR"):
            errors += 1
        elif message.startswith("INFO"):
            infos += 1
        elif message.startswith("WARNING"):
            warnings += 1

    return errors, infos, warnings


logs = [
    "[14:32:05] ERROR: Disk full",
    "[14:32:10] INFO: Server started",
    "[14:33:01] WARNING: High memory usage",
    "[14:33:15] INFO: Backup complete",
    "[14:34:00] ERROR: Connection refused",
    "[14:35:22] WARNING: CPU at 90%"
]

errors, infos, warnings = classify_logs(logs)
print("ERROR:", errors, "INFO:", infos, "WARNING:", warnings)
