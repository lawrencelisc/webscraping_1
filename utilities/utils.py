from datetime import datetime, timezone, timedelta


def get_current_unix_ts():
    unix_ts = datetime.utcnow().timestamp()

    return int(unix_ts)


def convert_date_str(unix_ts: int, hour=8) -> str:
    tz = timezone(timedelta(hours=hour))

    return datetime.fromtimestamp(unix_ts, tz).strftime('%Y-%m-%d %H:%M:%S')