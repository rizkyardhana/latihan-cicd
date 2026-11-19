VERSION = "2.0"
STATUS = "Broken"
MESSAGE = "Error: konfigurasi salah!"

def run():
    print(f"Version : {VERSION}")
    print(f"Status  : {STATUS}")
    print(f"Message : {MESSAGE}")
    raise RuntimeError("Simulasi kegagalan pada versi 2.0")

if __name__ == "__main__":
    run()
