from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

SCT_post_dt = [
    {
        'id': 0,
        'img': 'blog-3.jpg',
        'name': 'ali',
        'title': 'hesam khafan hamishe gade',
        'more': 'this good and selling forosh khafani dashte ...'
    },
    {
        'id': 1,
        'img': 'blog-3.jpg',
        'name': 'ali',
        'title': 'hesam god hamishe gade',
        'more': 'thisdsdasdasds good asd asd adasd asdasdasdasd daaaadashte ...'
    },
    {
        'id': 2,
        'img': 'blog-3.jpg',
        'name': 'ali',
        'title': 'hesam god hamishe gade',
        'more': 'thisdsdasdasds good asd asd adasd asdasdasdasd daaaadashte ...'
    },
    {
        'id': 3,
        'img': 'blog-3.jpg',
        'name': 'ali',
        'title': 'hesam god hamishe gade',
        'more': 'thisdsdasdasds good asd asd adasd asdasdasdasd daaaadashte ...'
    }
]

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'data': SCT_post_dt})



if __name__ == '__main__':
    app.run()
