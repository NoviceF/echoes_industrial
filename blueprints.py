import math

PLANETARY_TO_INGAME_NAME = {
    'lusteringAlloy': 'Lustering Alloy',
    'gleamingAlloy': 'Gleaming Alloy',
    'preciousAlloy': 'Precious Alloy',
    'condensedAlloy': 'Condensed Alloy',
    'motleyCompound': 'Motley Compound',
    'sheenCompound': 'Sheen Compound',
    'crystalCompound': 'Crystal Compound',
    'opulentCompound': 'Opulent Compound',
    'glossyCompound': 'Glossy Compound',
    'darkCompound': 'Dark Compound',
    'baseMetals': 'Base Metals',
    'heavyMetals': 'Heavy Metals',
    'nobleMetals': 'Noble Metals',
    'reactiveMetals': 'Reactive Metals',
    'toxicMetals': 'Toxic Metals',
    'fiberComposite': 'Fiber Composite',
}

MINERALS_TO_INGAME_NAME = {
    'tritanium': 'Tritanium',
    'pyerite': 'Pyerite',
    'mexallon': 'Mexallon',
    'isogen': 'Isogen',
    'nocxium': 'Nocxium',
    'zydrie': 'Zydrine',
    'megacyte': 'Megacyte',
    'morphite': 'Morphite'
}


class Planetary:
    def __init__(self,
                 lusteringAlloy=0, gleamingAlloy=0, preciousAlloy=0, condensedAlloy=0,
            motleyCompound=0, sheenCompound=0, crystalCompound=0,
            opulentCompound=0, glossyCompound=0,
            baseMetals=0, heavyMetals=0, nobleMetals=0, reactiveMetals=0, toxicMetals=0,
            fiberComposite=0):

        self.dictionary = {
            'lusteringAlloy': lusteringAlloy,
            'gleamingAlloy': gleamingAlloy,
            'preciousAlloy': preciousAlloy,
            'condensedAlloy': condensedAlloy,
            'motleyCompound': motleyCompound,
            'sheenCompound': sheenCompound,
            'crystalCompound': crystalCompound,
            'opulentCompound': opulentCompound,
            'glossyCompound': glossyCompound,
            'baseMetals': baseMetals,
            'heavyMetals': heavyMetals,
            'nobleMetals': nobleMetals,
            'reactiveMetals': reactiveMetals,
            'toxicMetals': toxicMetals,
            'fiberComposite': fiberComposite
        }


class Minerals:
    def __init__(self, tritanium, pyerite, mexallon, isogen=0,
                 nocxium=0, zydrine=0, megacyte=0, morphite=0):
        self.dictionary = {
            'tritanium': tritanium,
            'pyerite': pyerite,
            'mexallon': mexallon,
            'isogen': isogen,
            'nocxium': nocxium,
            'zydrie': zydrine,
            'megacyte': megacyte,
            'morphite': morphite
        }


class BluePrint:
    def __init__(self, name, planetary=Planetary(), minerals=Minerals(tritanium=0,
                                                                      pyerite=0,
                                                                      mexallon=0)):
        self.name = name
        self.planetary = planetary
        self.minerals = minerals


def applyFactorOnBP(factor, bp):
    modifiedBP = BluePrint(bp.name)
    modifiedBP.planetary.dictionary = {
        key: math.ceil(value / 150 * factor) for key, value in
        bp.planetary.dictionary.items()}
    modifiedBP.minerals.dictionary = {
        key: math.ceil((value / 150 * factor)) for key, value in
        bp.minerals.dictionary.items()}

    return modifiedBP


bpListBase = [
    BluePrint(name='Harbinger Prototype Blueprint',
              planetary=Planetary(
                  sheenCompound=32526,
                  preciousAlloy=26975,
                  glossyCompound=30385,
                  heavyMetals=32526,
                  reactiveMetals=8561
              ),
              minerals=Minerals(
                  tritanium=9767015,
                  pyerite=1889577,
                  mexallon=605636,
                  isogen=127322,
                  nocxium=36041,
                  zydrine=11763
              )
    ),
    BluePrint(name='Prophecy Blueprint',
              planetary=Planetary(
                  sheenCompound=30114,
                  preciousAlloy=24975,
                  glossyCompound=28131,
                  heavyMetals=30114,
                  reactiveMetals=7926
              ),
              minerals=Minerals(
                  tritanium=12169986,
                  pyerite=2055663,
                  mexallon=749352,
                  isogen=121068,
                  nocxium=38235,
                  zydrine=8580
              )
    ),
    BluePrint(name='Ashimmu Blueprint',
              planetary=Planetary(
                  condensedAlloy=125826,
                  preciousAlloy=98597,
                  opulentCompound=125826,
                  reactiveMetals=31286,
                  toxicMetals=31029
              ),
              minerals=Minerals(
                  tritanium=73808367,
                  pyerite=14655336,
                  mexallon=5301234,
                  isogen=891743,
                  nocxium=258560
              )
    ),
    BluePrint(name='Venture III Blueprint',
              planetary=Planetary(
                  condensedAlloy=2345,
                  preciousAlloy=1838,
                  fiberComposite=2345,
                  reactiveMetals=584,
                  toxicMetals=579
              ),
              minerals=Minerals(
                  tritanium=376418,
                  pyerite=102951,
                  mexallon=33482,
                  isogen=5543,
                  nocxium=1581
              )
    ),
]

bpNames = [x.name for x in bpListBase]

bpList = dict(
    enumerate(sorted(bpListBase, key=lambda x: x.name), 0)
)

# dict(('key{}'.format(index), val) for index, val in enumerate(range(3)))


# BluePrint(name='xxx Blueprint',
#           planetary=Planetary(
#           ),
#           minerals=Minerals(
#           )
#
#           ),
