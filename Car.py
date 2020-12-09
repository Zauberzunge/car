# Es wird eine Klasse "Car" erstellt

class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.gef_km = 0
        self.time = 0
        self.tankinhalt = 30
        self.verbrauch_100km = 8
        self.verbrauch = 0.0

    def status(self):
        print("Ich fahre %u km/h" %(self.speed))

    def beschleunigen(self):
        self.speed = self.speed + 5

    def bremsen(self):
        self.speed = self.speed - 5

    def tacho(self):
        self.gef_km = self.gef_km + self.speed
        self.time = self.time + 1

    def avg_speed(self):
        if self.time != 0:
            return self.gef_km / self.time
        else:
            pass

    def tanken(self, liter):
        self.tankinhalt = self.tankinhalt + liter
        return self.tankinhalt

    def status_verbrauch(self):
        self.verbrauch = float(self.gef_km * self.verbrauch_100km / 100)
        print("Der Verbrauch beträgt %f Liter." %(self.verbrauch))

if __name__ == "__main__":
    my_car = Car() # ein neues Objekt der Klasse "Car" wird erzeugt
    print("Ich bin ein Auto")

    while True:
        action = input("Was möchten Sie tun ? [B]eschleunigen, [L]angsamer, [G]efahrene km"
                        " oder [D]urchschnittsgeschwindigkeit anzeigen ?").upper()
        if action not in "BLGD" or len(action) != 1:
            print("Ich weiß nicht was Sie tun möchten !")
            continue
        if action == "B":
            my_car.beschleunigen()
        elif action == "L":
            my_car.bremsen()
        elif action == "G":
            print("Dieses Auto ist {} km gefahren." . format(my_car.gef_km))
        elif action == "D":
            print("Das Auto hat eine Durchschnittsgeschwindigkeit von {} km/h." . format(my_car.avg_speed()))


        tankvorgang = input("Haben Sie getankt ? [J]a oder [N]ein").upper()
        if tankvorgang == "J":
            liter = int(input("Wieviele Liter haben Sie getankt ?"))
            my_car.tanken(liter)
            print("In Ihrem Tank befinden sich jetzt %i Liter Sprit." %(my_car.tankinhalt))

        my_car.tacho()
        my_car.status()
        my_car.status_verbrauch()
