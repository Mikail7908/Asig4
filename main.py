import logging
from app import app

def main():
    app.run(debug=True)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info('Script started')
    main()
    logging.info('Script finished')