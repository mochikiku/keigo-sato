import speech_recognition
import pyttsx3
import datetime
import locale


locale.setlocale(locale.LC_TIME, 'ja_JP')

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

def change_voice(engine, language, gender='VoiceGenderFemale'):
  for voice in engine.getProperty('voices'):
    if language in voice.languages and gender == voice.gender:
      engine.setProperty('voice', voice.id)
      return True
  raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))

while True:
  with speech_recognition.Microphone() as mic:
    print("ロボット: 聞いています。")
    audio = robot_ear.record(mic, duration = 2)

  print("ロボット: ...")
  try:
    you = robot_ear.recognize_google(audio, language='ja_JP')
  except:
    you = "..."
  print("自分: " + you)

  if "..." in you:
    robot_brain = "聞き取れないのでもう一度話してください。"
  elif "こんにちは" in you:
    robot_brain = "こんにちは、ズオン。"
  elif "今日" in you:
    robot_brain = datetime.datetime.now().strftime("%B %d, %Y")
  elif "天気" in you:
    robot_brain = "寒くて、雪が降りそうです。"
  elif "バイバイ" in you:
    robot_brain = "また、ズオン。"
    print("ロボット: " + robot_brain)
    change_voice(robot_mouth, "ja_JP", "VoiceGenderFemale")
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    break
  else:
    robot_brain = "はっきり発音してください。"

  print("ロボット: " + robot_brain)

  change_voice(robot_mouth, "ja_JP", "VoiceGenderFemale")
  robot_mouth.say(robot_brain)
  robot_mouth.runAndWait()
