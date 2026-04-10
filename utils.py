import whisper
import re

# Load model once (good practice ✅)
model = whisper.load_model("base")

medical_dict = {
    "feaver": "fever",
    "diabitic": "diabetic",
    "paracetmol": "paracetamol",
    "bp": "blood pressure"
}

def correct_text(text):
    text = text.lower()  # normalize
    for wrong, correct in medical_dict.items():
        text = text.replace(wrong, correct)
    return text

def transcribe_audio(file_path):
    result = model.transcribe(file_path, fp16=False)
    text = result["text"]

    text = re.sub(r'\s+', ' ', text)
    text = correct_text(text)

    return text

def extract_medical_info(text):
    data = {
        "symptoms": [],
        "medications": [],
    }

    symptoms_list = ["fever", "cough", "headache"]
    meds_list = ["paracetamol", "ibuprofen"]

    for s in symptoms_list:
        if s in text:
            data["symptoms"].append(s)

    for m in meds_list:
        if m in text:
            data["medications"].append(m)

    return data