import platform


def banner(hostname):
    return (
        f"Host: {hostname}\n"
        f"OS: {platform.system()}\n"
        f"Python: {platform.python_version()}"
    )


if __name__ == "__main__":
    host = input("Hostname: ").strip()
    print(banner(host))
