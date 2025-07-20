from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h2>Ürün: Kulaklık X200</h2>
    <form method="POST" action="/comment">
        İsminiz: <input name="username"><br>
        Yorumunuz: <input name="comment"><br>
        <input type="submit" value="Yorum Yap">
    </form>
    '''

@app.route('/comment', methods=['POST'])
def comment():
    username = request.form['username']
    comment = request.form['comment']
    
    # Maskeleme ve SSTI zafiyeti burada
    masked_name = username[0] + "*" * (len(username) - 1)
    template = f"<p><strong>{masked_name}</strong> adlı kullanıcı dedi ki: {comment}</p>"

    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)
