import random
from urllib import response

R_EATING = "Non mi piace mangiare perché sono un bot, ovviamente"
R_COSE = "The international space station, also known as ISS, is a space station in low earth orbit that is dedicated to scientific research. The ISS is administered as a joint project between five different space agencies: NASA (National Aeronautics and Space Administration), RKA, ESA, JAXA(Japan Aerospace Exploration Agency)  e CSA-ASC (Canadian Space Agency)."
R_VITA = "The astronauts on the ISS follow intense work rates that are scanned hour per hour and they have to sleep at least 8 hours per day. Sleeping weightless is difficult and the astronauts sleep closed in sleeping bags attached in special cabins. Their work day is most dedicated to science."
R_ARRIVO = "To get on board the space station, astronauts have to travel around 9 minutes aboard a rocket, which is only launched from the Baikonur cosmodrome, Russian owned. The spacecraft that carries the astronauts to the ISS is called Soyuz, and it is one of the most used means in the space exploration story. Soyuz is a Russian word whose meaning is “union”: both the launcher, so the set of rockets for the launch, and the spacecraft, that materially does the docking to the ISS, have the name “Soyuz”. It is 50 meters length and 10 meters wide, it is divided into 3 stages, that is 3 sections that at the precise moments during the launch separate to give the necessary thrust to continue the journey, and it weighs 310 tons."
R_GIRI = "The ISS makes one revolution approximately every 92 minutes. Indeed the astronauts see everyday 16 sunsets and 16!"
R_VEDUTA = "The best moment to observe the international space station is a little bit before the dawn or immediately after the sunset, when who observes is already in dim light, while the ISS, being higher up, is well lit by the sun."
R_ESISTENZA = "NASA has said that the goal is to develop and to test technologies for the space exploration and also to develop technologies capable of keeping alive a crew in missions beyond Earth's orbit and gain operational experience for long-duration space flights. Moreover the ISS is also a research laboratory in a microgravity environment, in which the crews can lead biology, chemestry, medicine, physiology and physics experiments and can do astronomy and metereology observations."
R_ASSEMBLY = "The assembly of ISS was a great space architecture effort, started in November 1988. The Russian modules, except the Rassvet module, have been put in orbit through launchers without crew and they hooked automatically. All the other elements have been carried thanks to space shuttle flights e they have been assembled by the crew members of the shuttle or the station by means of extravehicular activities and using the robotic arm. As of 5 June 2011, a total of 159 space walks were carried out finalized to assembly for a total of 1000 hours of work, 127 of this space walks originated from the station, the remaining 32 originated from the shuttle anchored to the ISS."
R_COSTO = "The total amount eximated by ESA is around 100 bilions of euros for 30 years building and maintance."
R_POLI = "The orbit of the ISS stays within the envelope of the lower Van Allen belt. If the inclination were greater, above 52°, the radiation exposure of the crew would be elevated severely, to the point where the health risk would be unacceptable."

def unknown():
    response = ["Puoi ripetere per favore?", 
                "..."
                "Cosa vuol dire?"][random.randrange(100)]
    return response