import socket
import pymysql

def test_dns_resolution(hostname):
    print(f"Testing DNS resolution for hostname: {hostname}")
    try:
        ip = socket.gethostbyname(hostname)
        print(f"DNS resolved: {hostname} -> {ip}")
        return ip
    except Exception as e:
        print(f"DNS resolution failed: {e}")
        return None

def test_mysql_connection(host, port, user, password, db_name):
    print(f"\nTesting MySQL connection to {host}:{port} ...")
    try:
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name,
            connect_timeout=5
        )
        print("MySQL connection successful!")
        conn.close()
    except Exception as e:
        print(f"MySQL connection failed: {e}")

if __name__ == "__main__":
    # Replace these with your actual DB credentials
    hostname = "mysql-24d6d5e3-bkmhmd12-c018.c.aivencloud.com"
    port = 16271
    user = "avnadmin"
    password = "your_password_here"
    database = "defaultdb"

    # Step 1: Test DNS resolution
    ip = test_dns_resolution(hostname)

    # Step 2: Use IP if DNS resolved, else fallback to hostname to test MySQL
    if ip:
        test_mysql_connection(ip, port, user, password, database)
    else:
        print("\nDNS resolution failed, trying MySQL connection using hostname directly:")
        test_mysql_connection(hostname, port, user, password, database)
