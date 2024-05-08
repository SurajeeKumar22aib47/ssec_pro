import speech_recognition as sr
from django.shortcuts import render

recognizer = sr.Recognizer()

def get_voice_input():
    with sr.Microphone() as source:
        print("Please say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def fetch_answer(request):
    if request.method == 'GET':
        question = request.GET.get('question', None)
        voice_input = request.GET.get('voice_input', None)

        if not question and voice_input:
            question = get_voice_input()

        if question:
            # Process the question here
            file_path = r"C:/Users/Success/Desktop/custom-huggingface-model-main/custom-huggingface-model-main/boyQA.txt"
            qa_pairs = read_qa_pairs(file_path)
            answer = qa_pairs.get(question.strip(), "Sorry, I don't know the answer to that.")
            return render(request, 'question_answer.html', {'question': question, 'answer': answer})
        else:
            return render(request, 'question_answer.html', {'error': 'No question provided.'})
    else:
        return render(request, 'question_answer.html', {'error': 'Invalid request method.'})
