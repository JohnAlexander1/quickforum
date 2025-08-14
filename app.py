from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    content = request.form.get('content')
    if title and content:
        posts.append({'title': title, 'content': content})
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
