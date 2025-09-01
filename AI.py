from flask import Flask, request, jsonify, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Hardcoded medical Q&A (keywords + full questions)
qa_data = {

    # Infectious diseases
    "malaria": "Malaria symptoms include fever, chills, headache, sweating, nausea, and fatigue. Prevention: sleep under treated nets, use repellents, and take antimalarial drugs when prescribed.",
    "covid": "COVID-19 is caused by SARS-CoV-2. Symptoms: fever, cough, fatigue, loss of taste/smell, and breathing issues. Prevention: masks, hand washing, distancing, and vaccines.",
    "flu": "Flu symptoms include sneezing, cough, fever, body aches, and fatigue. Treatment: rest, fluids, and sometimes antiviral meds.",

    # General health
    "headache": "Headaches can be caused by stress, dehydration, or eye strain. Treatment: rest, hydrate, and take pain relievers if necessary.",
    "stomach ache": "Causes include indigestion, ulcers, constipation, or infections. Relief: rest, hydration, avoid spicy food, and seek medical help if severe.",
    "sleep": "Better sleep comes from a regular schedule, avoiding caffeine, and keeping your room dark/quiet.",

    # Chronic conditions
    "diabetes": "Diabetes is when the body cannot regulate blood sugar properly. Symptoms: thirst, frequent urination, fatigue, blurred vision.",
    "hypertension": "Hypertension is high blood pressure. Often has no symptoms, but can cause headaches or chest pain in severe cases.",

    # First aid
    "burns": "Cool burns with running water, cover with a clean cloth, avoid applying oils, and seek care if severe.",
    "snake bite": "Keep calm, immobilize the limb, don’t suck venom, and get urgent medical help.",
    "fracture": "Immobilize the area with a splint, avoid moving the limb, and go to the hospital immediately.",
    "bleeding": "Apply direct pressure with a clean cloth, raise the injured area, and seek medical care if severe.",

    # Nutrition & lifestyle
    "diet": "A balanced diet has carbs, proteins, fats, vitamins, and minerals in the right proportions.",
    "exercise": "Exercise controls weight, lowers disease risk, boosts mood, and strengthens the heart.",
    "water": "On average, adults should drink about 2–3 liters per day, depending on activity and climate.",

    # Mental health
    "depression": "Depression causes sadness, loss of interest, sleep/appetite changes. Seek counseling or medical help.",
    "stress": "Manage stress with relaxation, exercise, talking to trusted people, and resting.",
    "malaria": "Common symptoms include fever, chills, headache, sweating, and nausea. Prevention: sleep under treated mosquito nets, take prophylaxis if recommended.",
    "typhoid": "Symptoms: prolonged fever, abdominal pain, weakness, constipation or diarrhea. Spread through contaminated food and water.",
    "tuberculosis": "Symptoms: persistent cough (sometimes with blood), chest pain, night sweats, and weight loss. Spread through air from an infected person.",
    "covid": "Prevention: wear a mask, wash hands regularly, keep social distance, and get vaccinated. Symptoms: fever, cough, loss of taste or smell.",
    "hiv": "HIV attacks the immune system. Early signs may include flu-like illness. Long-term, it weakens immunity. Prevention: safe sex, avoid sharing needles.",
    "cholera": "Causes watery diarrhea and dehydration. Spread through contaminated water or food. Prevention: clean water, sanitation, and hygiene.",
    
    # Chronic diseases
    "diabetes": "A condition where the body cannot properly regulate blood sugar. Symptoms: frequent urination, thirst, fatigue, blurred vision.",
    "hypertension": "Also called high blood pressure. Often has no symptoms but can cause headaches, dizziness, and increase risk of stroke or heart disease.",
    "asthma": "A condition where airways narrow and swell, causing difficulty in breathing, wheezing, and coughing. Triggers: dust, pollen, smoke.",
    "cancer": "Uncontrolled growth of abnormal cells. Symptoms vary by type but may include lumps, unexplained weight loss, or chronic fatigue.",
    
    # Common issues
    "headache": "Causes: dehydration, stress, eye strain, or illness. Relief: rest, hydration, pain relievers. Seek medical help if severe or persistent.",
    "stomach ache": "Possible causes: indigestion, ulcers, infections, or food poisoning. Severe or persistent pain should be checked by a doctor.",
    "flu": "Caused by influenza virus. Symptoms: fever, cough, sore throat, runny nose, body aches. Prevention: annual vaccination.",
    "allergy": "Immune reaction to substances like dust, pollen, or food. Symptoms: sneezing, itching, rash, swelling.",
    "migraine": "A severe headache often accompanied by nausea, sensitivity to light and sound. Triggers include stress, certain foods, and lack of sleep.",
    
    # First aid / lifestyle
    "burns": "Cool the burn under running water, avoid breaking blisters, cover with a clean cloth. Seek medical help for severe burns.",
    "fracture": "Immobilize the affected area, apply a splint, and seek urgent medical care.",
    "dehydration": "Causes: lack of fluids, excessive sweating, diarrhea. Symptoms: dry mouth, dizziness, dark urine. Solution: drink water, oral rehydration.",
    "nutrition": "Eat a balanced diet with fruits, vegetables, proteins, and whole grains. Limit processed foods and sugar.",
    "exercise": "At least 30 minutes a day helps improve cardiovascular health, strength, and mood.",
    "Thank You":"Welcome. Glad youre satisfied by the response"
}

# --- Function to fetch answers based on keyword match ---
def get_answer(user_input):
    user_input = user_input.lower()
    for keyword, answer in qa_data.items():
        if keyword in user_input:  # simple keyword check
            return answer
    return "Sorry, I don’t have info on that. Please consult a medical professional."


# Users dictionary (username: {password, plan})
users = {"admin": {"password": "1234", "plan": "Free"}}

@app.route("/home")
def home():
    username = session.get("username")

    if not username or username not in users:
        return redirect(url_for("login"))  # user not logged in or doesn't exist

    user_plan = users[username]["plan"]
    return render_template("index.html", username=username, plan=user_plan)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username]["password"] == password:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            return "User already exists!"
        
        # new user gets free plan by default
        users[username] = {"password": password, "plan": "Free"}  
        session["username"] = username
        return redirect(url_for("home"))
    
    return render_template("signup.html")


@app.route("/payment", methods=["GET", "POST"])
def payment():
    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        plan = request.form["plan"]
        username = session["username"]
        users[username]["plan"] = plan
        return render_template("success.html", username=username, plan=plan)

    return render_template("payment.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


@app.route("/ask", methods=["POST"])
def ask():
    if "username" not in session:
        return jsonify({"answer": "Unauthorized. Please log in."}), 401
    
    user_q = request.json.get("question", "").lower()
    answer = get_answer(user_q)  # use keyword-based lookup
    return jsonify({"answer": answer})


@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("home"))
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
