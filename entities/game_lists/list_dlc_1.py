from entities.location import Location


class List_dlc_1():
    def __init__(self):
        self.list_name = ""
        self.list_of_location = []

    def fill_lications(self):
        self.list_name = "1-ый дополнительный"
        terrorists_base = Location("Стрип-клуб", "dlc/images/strip.png")
        self.list_of_location.append(terrorists_base)
        bank = Location("Зона 51", "dlc/images/area_51.png")
        self.list_of_location.append(bank)
        hospital = Location("Зоопарк", "dlc/images/zoopark.png")
        self.list_of_location.append(hospital)
        film_studio = Location("Стройплощадка", "dlc/images/stroika.png")
        self.list_of_location.append(film_studio)
        corporate_disco = Location("Тюрьма", "dlc/images/aye.png")
        self.list_of_location.append(corporate_disco)
        cons_lager = Location("Ночной клуб", "dlc/images/club.png")
        self.list_of_location.append(cons_lager)
        partisane_team = Location("Бар", "dlc/images/bar.png")
        self.list_of_location.append(partisane_team)
        train = Location("Метро", "dlc/images/metro.png")
        self.list_of_location.append(train)
        pirate_ship = Location("Кинотеатр", "dlc/images/kino.png")
        self.list_of_location.append(pirate_ship)
        embassy = Location("Кузница", "dlc/images/kyznica.png")
        self.list_of_location.append(embassy)
        restoran = Location("Музей", "dlc/images/museim.png")
        self.list_of_location.append(restoran)
        # supermarket = Location("Вписка", "supermarket")
        # location_list.append(supermarket)
        theater = Location("Лес", "dlc/images/forest.png")
        self.list_of_location.append(theater)
        university = Location("Спортзал", "dlc/images/gym.png")
        self.list_of_location.append(university)

        crusaders_army = Location("Столовая", "dlc/images/stolovka.png")
        self.list_of_location.append(crusaders_army)
        casino = Location("ЗАГС", "dlc/images/zags.png")
        self.list_of_location.append(casino)
        ocean_liner = Location("Суд", "dlc/images/syd.png")
        self.list_of_location.append(ocean_liner)
        # orbital_station = Location("Гей-клуб", "space_station")
        # location_list.append(orbital_station)
        hotel = Location("Свалка", "dlc/images/pomoika.png")
        self.list_of_location.append(hotel)
        beach = Location("Рок-концерт", "dlc/images/consert.png")
        self.list_of_location.append(beach)
        underwater_ship = Location("Псих-больница", "dlc/images/psih.png")
        self.list_of_location.append(underwater_ship)
        police_station = Location("Пустыня", "dlc/images/duna.png")
        self.list_of_location.append(police_station)
        plane = Location("Рай", "dlc/images/heaven.png")
        self.list_of_location.append(plane)
        spa_saloon = Location("Ад", "dlc/images/strip.png")
        self.list_of_location.append(spa_saloon)
        sto = Location("Чернобыль", "dlc/images/stalker.png")
        self.list_of_location.append(sto)
        chirch = Location("Завод", "dlc/images/zavod.png")
        self.list_of_location.append(chirch)

        school = Location("Худ. мастерская", "dlc/images/art_room.png")
        self.list_of_location.append(school)
        ferm = Location("Ферма", "dlc/images/rancho.png")
        self.list_of_location.append(ferm)
        cladbishe = Location("Кладбище", "dlc/images/grave.png")
        self.list_of_location.append(cladbishe)
        boloto = Location("Болото", "dlc/images/boloto.png")
        self.list_of_location.append(boloto)
        castle = Location("Замок", "dlc/images/castle.png")
        self.list_of_location.append(castle)
        bania = Location("Баня", "dlc/images/banya.png")
        self.list_of_location.append(bania)
