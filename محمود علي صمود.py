import socket

def HostInfo():
    # الحصول على اسم الجهاز
    hostname = socket.gethostname()
    
    # الحصول على عنوان IP للجهاز
    ip_address = socket.gethostbyname(hostname)
    
    # طباعة معلومات الجهاز
    print("اسم الجهاز:", hostname)
    print("عنوان IP:", ip_address)

# استدعاء الدالة
HostInfo()
