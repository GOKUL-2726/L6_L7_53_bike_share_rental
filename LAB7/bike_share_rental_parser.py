def parse_ride_duration(text):
    """
    Converts a ride duration written as HH:MM into minutes.
    Assumes text always has exactly one colon with digits on both sides.
    Hardened against invalid/malformed inputs.
    """
    try:
        if not isinstance(text, str):
            return None
        text = text.strip()
        if ':' not in text:
            return None
        parts = text.split(':')
        if len(parts) != 2:
            return None
        hours_str, minutes_str = parts[0].strip(), parts[1].strip()
        if not hours_str.isdigit() or not minutes_str.isdigit():
            return None
        hours = int(hours_str)
        minutes = int(minutes_str)
        if hours < 0 or minutes < 0:
            return None
        return hours * 60 + minutes
    except Exception:
        return None

def format_station_code(code):
    """
    Formats a station code as ZONE-NUMBER, e.g. 'a12' -> 'A-12'.
    Assumes code is a non-empty string.
    Hardened against invalid/malformed inputs.
    """
    try:
        if not isinstance(code, str):
            return None
        code = code.strip().upper()
        if not code:
            return None
        return code[0] + '-' + code[1:]
    except Exception:
        return None

def parse_ride_log(line):
    """
    Parses 'bike_type,minutes,subscriber' into a tuple.
    Assumes all three fields are present and minutes is an integer.
    Hardened against invalid/malformed inputs.
    """
    try:
        if not isinstance(line, str):
            return None
        parts = line.split(',')
        if len(parts) != 3:
            return None
        bike_type = parts[0].strip()
        minutes_str = parts[1].strip()
        if not bike_type or not minutes_str:
            return None
        minutes = int(minutes_str)
        if minutes < 0:
            return None
        is_subscriber = parts[2].strip().lower() == 'yes'
        return bike_type, minutes, is_subscriber
    except Exception:
        return None

def main():
    print("==== Running parse_ride_duration ====")
    value = input("Enter a ride duration as HH:MM (e.g. 01:15): ")
    print("Duration in minutes:", parse_ride_duration(value))

    print("\n==== Running format_station_code ====")
    value = input("Enter a station code (e.g. a12): ")
    print("Formatted station code:", format_station_code(value))

    print("\n==== Running parse_ride_log ====")
    value = input("Enter a ride log line as type,minutes,subscriber (e.g. electric,45,yes): ")
    print("Parsed ride log:", parse_ride_log(value))

if __name__ == "__main__":
    main()
