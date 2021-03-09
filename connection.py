import pyodbc
conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=EARNWSQRDEV12.AUS.AMER.DELL.COM;'
                      'Database=CSG_ANLYTCL_MDL_DB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('select top 10 * from [CSG_ANLYTCL_MDL_DB].[dbo].[TBL_NPSVERBATIM_AUTOSCRUB_FEBFY22]')

for row in cursor:
    print(row)