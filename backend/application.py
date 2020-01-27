from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy # new
from flask_marshmallow import Marshmallow # new
from flask_cors import CORS
from flask_restful import Api, Resource

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///score.db' # new
db = SQLAlchemy(app) # new
ma = Marshmallow(app) # new
api = Api(app)

# Define a class for the Artist table
class Score(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	highest_score = db.Column(db.Integer)
	last_update = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
	total_score = db.Column(db.Integer)
	attempt_count = db.Column(db.Integer);
	

# Create data abstraction layer
class ScoreSchema(ma.Schema):
	class Meta:
		fields = ("id", "name", "highest_score", "last_update", "total_score", "attempt_count")


score_schema = ScoreSchema()
scores_schema = ScoreSchema(many=True)

class ScoreListResource(Resource):
	def get(self):
		scores = Score.query.all()
		scores = scores_schema.dump(scores)
		print(scores)
		for s in scores.data:
			print(s['last_update'])
			if s['last_update']:
				s['last_update'] = str(s['last_update'].now())
		return scores

	def post(self):
		score_id = None
		score = None
		print(request.json)
		if 'id' in request.json: 
			print('inside if')
			score_id = request.json['id']
		else:
			print('inside else')
		current_score = int(request.json['score'])
		name = request.json['name'];

		print('score_id', score_id)

		if score_id:
			try:
				score = Score.query.get_or_404(score_id)
			except e:
				print(e)

		if score:
			new_entry = score
			if new_entry.highest_score < current_score:
				new_entry.highest_score = current_score
			if new_entry.total_score == None:
				new_entry.total_score = current_score
			else:
				new_entry.total_score += current_score

			if new_entry.attempt_count == None:
				new_entry.attempt_count = 1
			else:
				new_entry.attempt_count += 1
		else:
			new_entry = Score(
				name=request.json['name'],
				highest_score=request.json['score'],
				last_update=db.func.now(),
				total_score = current_score,
				attempt_count = 1
			)
			db.session.add(new_entry)
		db.session.commit()
		return score_schema.dump(new_entry)

class ScoreResource(Resource):
    def get(self, score_id):
        score = Score.query.get_or_404(score_id)
        score = score_schema.dump(score)
        print (score)
        if score.data: score.data['last_update'] = str(score.data['last_update'])
        return score

api.add_resource(ScoreResource, '/scores/<int:score_id>')
api.add_resource(ScoreListResource, '/scores')


if __name__ == '__main__':
	app.run(debug=True)

# Create the table. Only once. Comment after that.
db.create_all()

