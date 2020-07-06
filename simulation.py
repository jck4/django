from datetime import datetime, timedelta 
import uuid 
import time

class World:

    def __init__(self, name):
        self.name = name
        self.properties = self.initWorldProperties()

    def initWorldProperties(self):
        
        properties = {
            "popModifer" : 1.01,
            "devastation" : 0.0,
            "danger" : 0.0,
            "pawns" : 2.0,
            "specialChance" : 0.0001, 
            "colonies" : [],
            "leaderPawns" : [],
            "specialPawns": []
        }

        return properties


    def getWorldSize(self):
        pass


    def getWorldDevastation(self):
        pass


    def getWorldColonies(self):
        pass


    def getWorldPawns(self):
        return self.properties["pawns"]


    def getWorldProperties(self):

        return self.properties

    
    def simulate(self):

        
        pawns = self.getWorldPawns()

        pawns = pawns * (self.properties['popModifer'])
        
        self.properties['pawns'] = pawns

        print(round(pawns))


class Colony:

    def __init__(self, name):
        self.name = name




if __name__ == "__main__":

    worlds = []

    world1 = World("yeet1")
    
    lastTime = datetime.now()

    while (1):

        world1.simulate()

        time.sleep(1)



# Homelessness? Colonies effect pawns, pawns effect colonies.

# Colonies affect world.

# seudo life simulation

# .io game? user selects specialization/focus to grow/improve/populate a planet

# paralell realities expanding until realities touch. When realities touch, one reality can absorb another.

# border friction. massive debuff for 2 or more realities. The longer realities touch, the worse the debuff gets. Effects realities in a chaotic way.


# colony{

#     developement

#     beurocracy

#     liberty
    
# }



# environment{

#     devestation    

# }

# pawn {
#     industrialist

#     environmentalist

#     ingenuity

#     creativity
    
#     inspiration
    
#     risk aversion

#     technology - technology type influenced by 
#         - war
#         - economy
#         - communication
#         - control        

# }



# ScheduledExecutorService ses = Executors.newSingleThreadScheduledExecutor();

# ses.scheduleAtFixedRate(new Runnable() {
#     @Override
#     public void run() {
#         // code to run
#     }
# }, 0, 1, TimeUnit.SECONDS);