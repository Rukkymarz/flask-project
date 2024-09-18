from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    experience = request.form['experience']

    resume_content = f"""
    **{name}**
    {email}
    {phone}

    **Experience:**
    * {experience} years of experience in DevOps engineering

    **Skills:**
    * Cloud platforms (AWS, GCP, Azure)
    * Configuration management (Ansible, Puppet, Chef)
    * Containerization (Docker, Kubernetes)
    * CI/CD pipelines (Jenkins, GitLab CI)
    * Scripting (Bash, Python)
    """

    return render_template('resume.html', resume_content=resume_content)

if __name__ == '__main__':
    app.run(debug=True)