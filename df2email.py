import pandas as pd
import numpy as np
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from datetime import date

def df2email(df, sender, password, to):

  if len(df.index) > 0:

    Date = date.today().strftime("%m/%d/%Y")

    table_header = ''
    for column in df.columns:
      table_header = table_header + '<th>' + column + '</th>'

    table_data = ''
    for row in range(len(df.index)):
      table_data = table_data + '<tr>'
      for col in range(len(df.columns)):
        table_data = table_data + '<td>'+str(df.iloc[row,col])+'</td>'
      table_data = table_data + '<tr>'

    HTML = """
          <!DOCTYPE html>
          <html>
            <head>
              <meta charset="utf-8" />
                  <style type="text/css">
                table {
                  background: white;
                  border-radius:3px;
                  border-collapse: collapse;
                  height: auto;
                  max-width: 900px;
                  padding:5px;
                  width: 100%;
                  animation: float 5s infinite;
                }
                th {
                  color:#D5DDE5;;
                  background:#1b1e24;
                  border-bottom: 4px solid #9ea7af;
                  font-size:14px;
                  font-weight: 300;
                  padding:10px;
                  text-align:center;
                  vertical-align:middle;
                }
                tr {
                  border-top: 1px solid #C1C3D1;
                  border-bottom: 1px solid #C1C3D1;
                  border-left: 1px solid #C1C3D1;
                  color:#666B85;
                  font-size:16px;
                  font-weight:normal;
                }
                tr:hover td {
                  background:#4E5066;
                  color:#FFFFFF;
                  border-top: 1px solid #22262e;
                }
                td {
                  background:#FFFFFF;
                  padding:10px;
                  text-align:left;
                  vertical-align:middle;
                  font-weight:300;
                  font-size:13px;
                  border-right: 1px solid #C1C3D1;
                }
              </style>
            </head>
            <body>
              Hello Sourabh,<br> <br>
              Insert whatever you like to:<br><br>
              <table>
                <thead>
                  <tr style="border: 1px solid #1b1e24;">
                  """+table_header+"""
                  </tr>
                </thead>
                <tbody>
                  """+table_data+"""
                </tbody>
              </table>
              <br><br>
              For more assistance, please get in touch -
              <a href='mailto:sourabh.amancha@gmail.com'>sourabh.amancha@gmail.com</a>.<br> <br>
              Thank you!
            </body>
          </html>
          """
    def sendEmail(_from,_to,_subj,_body) :
        msg = MIMEMultipart("alternative", None, [MIMEText(HTML, 'html')])
        #msg = MIMEText(str(_body))
        msg['Subject'] = _subj
        msg['From'] = _from
        msg['To'] = _to

        s = smtplib.SMTP('smtp.gmail.com', 587) #SMTP gmail server and port
        s.ehlo()
        s.starttls()
        s.login(sender, password) #Sender gmail username and password
        s.sendmail(_from, [_to], msg.as_string())
        s.quit()


    try:
      sendEmail(sender, to, 'Email from df2email - ' + Date, '')
    except:
      print("Unexpected error")


df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])

df2email(df, 'sender@gmail.com', 'password', 'receiver@email.com')

