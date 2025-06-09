import random

class GenAIAgent:
    def reason(self, input_data):
        return "[GenAI reasoning applied]"

class ProfileAnalysisAgent(GenAIAgent):
    def analyze_profile(self, employee):
        print(f"Analyzing profile for {employee['name']}...")
        level = "Intermediate" if len(employee['skills']) > 2 else "Beginner"
        print(f"- Inferred level: {level} based on skills {employee['skills']}")
        print(self.reason(employee))
        return level

class AssessmentAgent(GenAIAgent):
    def run_assessment(self, level):
        print(f"Conducting {level} level assessment...")
        score = random.randint(50, 95)
        print(f"- Assessment Score: {score}%")
        print(self.reason(score))
        return score

class RecommendationAgent(GenAIAgent):
    def recommend(self, profile, score):
        print("Generating course recommendations...")
        if score > 85:
            courses = ["Advanced Angular", "System Design"]
        elif score > 60:
            courses = ["Angular Basics", "JavaScript Deep Dive"]
        else:
            courses = ["HTML/CSS Refresher", "Intro to Angular"]
        print(f"- Recommended Courses: {courses}")
        print(self.reason(courses))
        return courses

class ProgressTrackerAgent(GenAIAgent):
    def track(self, employee, courses):
        completed = random.sample(courses, k=1)
        print(f"Tracking progress for {employee['name']}...")
        print(f"- Completed: {completed}")
        print(f"- Pending: {list(set(courses) - set(completed))}")
        print(self.reason(courses))

# Simulated user
employee = {
    "id": "E123",
    "name": "Anita",
    "role": "Learner",
    "skills": ["Spring Boot", "MySQL"],
    "target": "Full Stack Developer"
}

# Simulated CLI Workflow
print("=== Personalized Learning CLI (GenAI Version) ===")

profile_agent = ProfileAnalysisAgent()
assessment_agent = AssessmentAgent()
recommendation_agent = RecommendationAgent()
tracker_agent = ProgressTrackerAgent()

level = profile_agent.analyze_profile(employee)
score = assessment_agent.run_assessment(level)
courses = recommendation_agent.recommend(employee, score)
tracker_agent.track(employee, courses)
