import random

def dlc_1_list_return(Location):
    """Возвращает лист первого дополнения лист"""
    location_list = []
    name = "1-ый дополнительный список"
    terrorists_base = Location("Стрип-клуб","dlc/images/strip.png" )
    location_list.append(terrorists_base)
    bank = Location("Зона 51","dlc/images/area_51.png" )
    location_list.append(bank)
    hospital = Location("Зоопарк","dlc/images/zoopark.png"  )
    location_list.append(hospital)
    film_studio = Location("Стройплощадка","dlc/images/stroika.png"  )
    location_list.append(film_studio)
    corporate_disco = Location("Тюрьма", "dlc/images/aye.png" )
    location_list.append(corporate_disco)
    cons_lager = Location("Ночной клуб","dlc/images/club.png"  )
    location_list.append(cons_lager)
    partisane_team = Location("Бар","dlc/images/bar.png"  )
    location_list.append(partisane_team)
    train = Location("Метро", "dlc/images/metro.png")
    location_list.append(train)
    pirate_ship = Location("Кинотеатр","dlc/images/kino.png"  )
    location_list.append(pirate_ship)

    embassy = Location("Кузница""dlc/images/kyznica.png" )
    location_list.append(embassy)
    restoran = Location("Музей","dlc/images/museim.png"  )
    location_list.append(restoran)
    # supermarket = Location("Вписка", "supermarket")
    # location_list.append(supermarket)
    theater = Location("Лес","dlc/images/forest.png"  )
    location_list.append(theater)
    university = Location("Спортзал","dlc/images/gym.png"  )
    location_list.append(university)

    crusaders_army = Location("Столовая","dlc/images/stolovka.png"  )
    location_list.append(crusaders_army)
    casino = Location("ЗАГС", "dlc/images/zags.png" )
    location_list.append(casino)
    ocean_liner = Location("Суд","dlc/images/syd.png"  )
    location_list.append(ocean_liner)
    # orbital_station = Location("Гей-клуб", "space_station")
    # location_list.append(orbital_station)
    hotel = Location("Свалка","dlc/images/pomoika.png"  )
    location_list.append(hotel)
    beach = Location("Рок-концерт","dlc/images/consert.png"  )
    location_list.append(beach)
    underwater_ship = Location("Псих-больница", "dlc/images/psih.png" )
    location_list.append(underwater_ship)
    police_station = Location("Пустыня", "dlc/images/duna.png" )
    location_list.append(police_station)
    plane = Location("Рай", "dlc/images/heaven.png" )
    location_list.append(plane)
    spa_saloon = Location("Ад","dlc/images/strip.png"  )
    location_list.append(spa_saloon)
    sto = Location("Чернобыль","dlc/images/stalker.png"  )
    location_list.append(sto)
    chirch = Location("Завод","dlc/images/zavod.png"  )
    location_list.append(chirch)

    school = Location("Худ. мастерская","dlc/images/art_room.png"  )
    location_list.append(school)
    ferm = Location("Ферма","dlc/images/rancho.png"  )
    location_list.append(ferm)
    cladbishe = Location("Кладбище", "dlc/images/grave.png" )
    location_list.append(cladbishe)
    boloto = Location("Болото","dlc/images/boloto.png"  )
    location_list.append(boloto)
    castle = Location("Замок","dlc/images/castle.png"  )
    location_list.append(castle)
    bania = Location("Баня","dlc/images/banya.png" )
    location_list.append(bania)
    # Шпион
    spy = Location("Шпион", "spy")
    return location_list,name