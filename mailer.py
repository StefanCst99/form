import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request
import os

app = Flask(__name__)

myEmail = 'costy1199.ci@gmail.com'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

template_dir = 'templates'
template_path = os.path.join(template_dir, 'index.html')

@app.route('/')
def index():
    with open(template_path, 'r') as file:
        html_content = file.read()
    return render_template('index.html', html_content=html_content)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        nume = request.form['nume']
        dep = request.form['dep']
        con = request.form['con']
        int1 = request.form['int1']
        int2 = request.form['int2']
        int3 = request.form['int3']
        int4 = request.form['int4']
        int5 = request.form['int5']
        int6 = request.form['int6']
        int7 = request.form['int7']


        # Build HTML table for the email body
        email_body = f"""
        <html>
        <body>
            <p><strong>Formular Propuneri Îmbunătățiri:</strong></p>
            <table border="1" cellpadding="10">
                <tr>
                    <td><strong>Nume, Prenume:</strong></td>
                    <td>{nume}</td>
                </tr>
                <tr>
                    <td><strong>Departament, Funcție:</strong></td>
                    <td>{dep}</td>
                </tr>
                <tr>
                    <td><strong>Acord:</strong></td>
                    <td>{con}</td>
                </tr>
                <tr>
                    <td><strong>1.Cum ai descrie mediul de lucru actual și în ce mod crezi că ar putea fi îmbunătățit pentru a facilita activitățile zilnice?</strong></td>
                    <td>{int1}</td>
                </tr>
                <tr>
                    <td><strong>2.Există anumite sarcini sau aspecte ale muncii tale care consideri că ar putea fi simplificate sau automatizate pentru a reduce efortul depus?</strong></td>
                    <td>{int2}</td>
                </tr>
                <tr>
                    <td><strong>3.Ce resurse sau instrumente adiționale crezi că ar putea fi adăugate pentru a sprijini eficiența în îndeplinirea sarcinilor de zi cu zi?</strong></td>
                    <td>{int3}</td>
                </tr>
                <tr>
                    <td><strong>4.Ai sugestii pentru a îmbunătăți comunicarea și colaborarea în echipă la locul de muncă?</strong></td>
                    <td>{int4}</td>
                </tr>
                <tr>
                    <td><strong>5.Există aspecte ale infrastructurii tehnologice sau ale echipamentelor pe care le-ai dori să le vezi îmbunătățite pentru a-ți ușura munca?</strong></td>
                    <td>{int5}</td>
                </tr>
                <tr>
                    <td><strong>6.Crezi că ar fi benefic să se ofere training sau resurse suplimentare pentru a vă dezvolta abilitățile și pentru a face față mai eficient sarcinilor de lucru?</strong></td>
                    <td>{int6}</td>
                </tr>
                <tr>
                    <td><strong>7.Care sunt cele mai mari provocări cu care te confrunți în timpul zilei de lucru și cum crezi că ar putea fi gestionate mai bine?</strong></td>
                    <td>{int7}</td>
                </tr>
      
            </table>
        </body>
        </html>
        """

        # Trimiterea emailului
        msg = MIMEMultipart()
        msg.attach(MIMEText(email_body, 'html'))  # Set the content type to HTML

        msg['Subject'] = 'Propuneri îmbunătățiri'
        msg['From'] = myEmail
        msg['To'] = 'costin.iancu@inspet-ploiesti.ro'

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(myEmail, 'ecsfzztsektsqzwj')
            server.sendmail(myEmail, 'costin.iancu@inspet-ploiesti.ro', msg.as_string())
            server.quit()

            return render_template('submit.html')  # Redirecționează la șablonul de mulțumire
        except Exception as e:
            return f"Eroare la trimiterea e-mailului: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
