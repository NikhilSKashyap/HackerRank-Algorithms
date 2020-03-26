from datetime import datetime

def timeConversion(s):
    s = datetime.strptime(s, "%I:%M:%S%p")
    s = datetime.strftime(s, "%H:%M:%S")
    return s

if __name__ == '__main__':
    s = "07:05:45PM"
    result = timeConversion(s)
    print(result)