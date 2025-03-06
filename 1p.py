import requests
import RPi.GPIO as GPIO
import time

INT_PIN_BOARD = 12
INT_INTERVAL = 180
STR_NOTIFY_TOKEN = 'ipYbEJXcxfNy5txUZIepu99VOWMorw9kxTGWvvxfx8r'
STR_NOTICE_MESSAGE = 'LINEへのメッセージ'

def fnc_line_notify():
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {STR_NOTIFY_TOKEN}'}
    data = {'message': f'{STR_NOTICE_MESSAGE}'}
    requests.post(line_notify_api, headers=headers, data=data)
    return

def fnc_sensor_detect():
    while True:
        if GPIO.input(INT_PIN_BOARD) == GPIO.HIGH:
            print('Detect')
            break
        time.sleep(1)
    return

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(INT_PIN_BOARD, GPIO.IN)

    while True:
        fnc_sensor_detect()
        fnc_line_notify()
        time.sleep(INT_INTERVAL)

	 try:
        print ("処理キャンセルはCTRL+C")
        while True:
            # GPIO_PIN18と同値(センサーが動作を感知)
            if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
                with picamera.PiCamera() as camera:
                    #解像度の調整
                    camera.resolution = (1024, 768)
                    # 明るさの調整
                    #camera.brightness = 70
                    # ラズパイをモニターに接続していたらモニターに表示
                    camera.start_preview()
                    # カメラ撮影
                    camera.capture("picture.jpg")
                    # LineNotifyを使って撮影をINEに通知
                    #os.chdir("/home/user1/camera_iot")
                    line_notify_token = "LINE通知用のトークン"
                    line_notify_api = 'https://notify-api.line.me/api/notify'
                    message = '監視カメラの撮影通知'
                    payload = {'message': message}
                    headers = {'Authorization': 'Bearer ' + line_notify_token}
                    files = {'imageFile': open("/home/xxx/picture.jpg", "rb")}  
                    line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
                    time.sleep(INTERVAL) 
            else:
                time.sleep(SLEEPTIME)
    except KeyboardInterrupt:
        print("全処理終了")
    finally:
        GPIO.cleanup()