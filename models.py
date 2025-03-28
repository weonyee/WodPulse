from app import newdb

class Exercise(newdb.Model):
    id = newdb.Column(newdb.Integer, primary_key=True)
    name = newdb.Column(newdb.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<Exercise '{self.name}'>"

class Record(newdb.Model):
    id = newdb.Column(newdb.Integer, primary_key=True)
    date = newdb.Column(newdb.String(100), nullable=False)
    weight = newdb.Column(newdb.Float, nullable=False)
    memo = newdb.Column(newdb.String(500), nullable=True)
    exercise_id = newdb.Column(newdb.Integer, newdb.ForeignKey('exercise.id'), nullable=False)

    def __repr__(self):
        return f"<Record {self.date} - {self.weight}kg - {self.exercise.name}>"
