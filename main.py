# İçeri Aktar
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Form sonuçları 
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # seçilen resmi almak
        selected_image = request.form.get('image-selector')
        Bottom_Text = request.form.get('textBottom')
        Upper_Text = request.form.get('textTop')
        # Görev #2. Metni almak
        color = request.form.get('color-selector')
        # Görev #3. Metnin konumunu almak
       

        # Görev #3. Metnin rengini almak
        

        return render_template('index.html', 
                               # Seçilen resmi görüntüleme
                               selected_image=selected_image, 

                               # Görev #2. Metni görüntüleme
                               Bottom_Text = Bottom_Text,
                               Upper_Text = Upper_Text,

                               # Görev #3. Rengi görüntüleme
                               color = color
                               
                               # Görev #3. Metnin konumunu görüntüleme

                               )
    else:
        # Varsayılan olarak ilk resmi görüntüleme
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
