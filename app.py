from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anime.db'
db = SQLAlchemy(app)

class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(500))
    seasons = db.Column(db.Integer)
    episodes_per_season = db.Column(db.String(100))

    def __init__(self, name, description, seasons, episodes_per_season):
        self.name = name
        self.description = description
        self.seasons = seasons
        self.episodes_per_season = episodes_per_season

@app.route('/')
def hello():
    return "Welcome to the API!"

@app.route('/anime', methods=['GET'])
def get_anime():
    anime_list = []
    anime = Anime.query.all()
    for item in anime:
        anime_data = {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'seasons': item.seasons,
            'episodes_per_season': item.episodes_per_season
        }
        anime_list.append(anime_data)
    return jsonify(anime_list)

@app.route('/anime', methods=['POST'])
def add_anime():
    data = request.get_json()
    name = data['name']
    description = data['description']
    seasons = data['seasons']
    episodes_per_season = data['episodes_per_season']
    anime = Anime(name=name, description=description, seasons=seasons, episodes_per_season=episodes_per_season)
    db.session.add(anime)
    db.session.commit()
    return jsonify({'message': 'Anime added successfully'})

@app.route('/anime/<int:anime_id>', methods=['GET'])
def get_single_anime(anime_id):
    anime = Anime.query.get(anime_id)
    if not anime:
        return jsonify({'message': 'Anime not found'})
    anime_data = {
        'id': anime.id,
        'name': anime.name,
        'description': anime.description,
        'seasons': anime.seasons,
        'episodes_per_season': anime.episodes_per_season
    }
    return jsonify(anime_data)

@app.route('/anime/<int:anime_id>', methods=['PUT'])
def update_anime(anime_id):
    anime = Anime.query.get(anime_id)
    if not anime:
        return jsonify({'message': 'Anime not found'})

    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    seasons = data.get('seasons')
    episodes_per_season = data.get('episodes_per_season')

    if name:
        anime.name = name
    if description:
        anime.description = description
    if seasons:
        anime.seasons = seasons
    if episodes_per_season:
        anime.episodes_per_season = episodes_per_season

    db.session.commit()
    return jsonify({'message': 'Anime updated successfully'})

@app.route('/anime/<int:anime_id>', methods=['DELETE'])
def delete_anime(anime_id):
    anime = Anime.query.get(anime_id)
    if not anime:
        return jsonify({'message': 'Anime not found'})

    db.session.delete(anime)
    db.session.commit()
    return jsonify({'message': 'Anime deleted successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
