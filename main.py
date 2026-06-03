from app import scanner
from app.database.insert import inserir_dados
from app.comparison import current_devices, new_devices, comparison

def main():

    #scanner.scanner_network()

    comparison(
        current_devices,
        new_devices
    )

    inserir_dados()


if __name__ == "__main__":
    main()
    
