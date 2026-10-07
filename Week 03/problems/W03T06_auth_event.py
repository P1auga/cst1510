from datetime import datetime


def log_event(username, action):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{stamp}] {action.upper()} user={username}"


if __name__ == "__main__":
    user = input("Username: ").strip()
    act = input("Action (LOGIN/LOGOUT): ").strip()
    print(log_event(user, act))
