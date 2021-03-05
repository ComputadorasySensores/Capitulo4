from gpiozero import Buzzer
from gpiozero import MotionSensor

buzzer_zumbador = Buzzer(24)
pir = MotionSensor(23)
buzzer_zumbador.off()

while True:
    pir.wait_for_motion()
    print("Movimiento detectado")
    buzzer_zumbador.on()
    pir.wait_for_no_motion()
    buzzer_zumbador.off()
    print("Movimiento no detectado")
    
