# Main file
from App.POC.Poc_ETL import poc_etl
from App.POC.Poc_modelado import poc_modelado


def poc():
    poc_etl()
    poc_modelado()


if __name__ == '__main__':
    poc()
