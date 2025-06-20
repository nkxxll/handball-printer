from escpos.printer import Network

# IP-Adresse deines Druckers (lokal im Netzwerk)
PRINTER_IP = "192.168.0.100"  # <- Ändere das auf die IP deines Druckers
PORT = 9100  # Standardport für viele Netzwerkkassendrucker

def drucke_testnachricht():
    try:
        printer = Network(PRINTER_IP, port=PORT)
        printer.set(align='center', font='a', width=2, height=2)
        printer.text("** TESTNACHRICHT **\n")
        printer.set(align='left', font='a', width=1, height=1)
        printer.text("Dies ist ein ESC/POS Testdruck.\n")
        printer.text("Datum/Zeit: 18.06.2025\n")
        printer.text("\nVielen Dank!\n")
        printer.cut()
        printer.close()
        print("Druck erfolgreich gesendet.")
    except Exception as e:
        print(f"Fehler beim Drucken: {e}")

def main():
    drucke_testnachricht()

if __name__ == "__main__":
    main()
