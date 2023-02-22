import pdb

import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView
from sqlalchemy import create_engine

import mysql.connector
import datetime


# Creating connection object


class ImportCsv(APIView):
    """Create Driver check_in object.
    EndPoint:
        API: api/import-csv/
    """

    def post(self, request):
        csv_file = request.data.get("csv_file")
        schema = request.data.get("schema")
        create_usr_id = request.data.get("create_usr_id")

        hostname = "localhost"
        dbname = "public"
        uname = "root"
        pwd = "Kms)(1405"

        df = pd.read_csv(csv_file)
        df.insert(len(df.columns), 'create_usr_id', create_usr_id)
        date, time = str(datetime.datetime.now()).split()
        time = time.split(".")[0]
        table_name = schema + "_" + str(date).replace("-", "_") + "_" + str(time).replace(":", "_")

        # Create SQLAlchemy engine to connect to MySQL Database
        sqlEngine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                                  .format(host=hostname, db=dbname, user=uname, pw=pwd))
        dbConnection = sqlEngine.connect()

        status = True
        mesage = "csv has been uploaded successfully"
        try:
            df.to_sql(table_name, dbConnection, index=False, if_exists="replace")
            dbConnection.close()
        except Exception as e:
            status = False
            mesage = str(e)

        return Response({'status': status, 'message': mesage})
