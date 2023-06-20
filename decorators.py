import urllib.request

class Candidate:
    def __init__(self, first_name, last_name, email, tech_stack, main_skill, main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @classmethod
    def generate_candidates(cls, file_path):
        candidates = []

        response = urllib.request.urlopen(file_path)
        data = response.read().decode('utf-8')

        with open(file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            candidate_data = line.strip().split(',')
            first_name = candidate_data[0]
            last_name = candidate_data[1]
            email = candidate_data[2]
            tech_stack = candidate_data[3].split(';')
            main_skill = candidate_data[4]
            main_skill_grade = candidate_data[5]

            candidate = cls(first_name, last_name, email, tech_stack, main_skill, main_skill_grade)
            candidates.append(candidate)

        return candidates


candidate = Candidate("Dasha", "Kovl", "dashyn@test.com", "Python, JavaScript", "Programming Development", "A")
print(candidate.full_name)

url = 'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'
candidates = Candidate.generate_candidates(url)