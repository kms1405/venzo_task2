from rest_framework.response import Response
from rest_framework.views import APIView

from sqlalchemy import create_engine
import pandas as pd
import random
import pdb
class ImportCsv(APIView):
    """Create Driver check_in object.
    EndPoint:
        API: api/import-csv/
    """

    def post(self, request):
        hostname = "localhost"
        dbname = "public1"
        uname = "root"
        pwd = "Kms)(1405"

        # Create dataframe
        df = pd.DataFrame(data=[[111, 'Thomas', '35', 'United Kingdom'],
                                [222, 'Ben', 42, 'Australia'],
                                [333, 'Harry', 28, 'India']],
                          columns=['id', 'name', 'age', 'country'])

        # Create SQLAlchemy engine to connect to MySQL Database
        sqlEngine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                               .format(host=hostname, db=dbname, user=uname, pw=pwd))

        print("sdffffffffffffffffffffffffffffffffffffffffffff")
        dbConnection = sqlEngine.connect()
        pdb.set_trace()
        # Convert dataframe to sql table
        df.to_sql('users123', dbConnection,  if_exists="replace")
        data = self.request.data
        return Response({'status': "status", 'message': "message"})
