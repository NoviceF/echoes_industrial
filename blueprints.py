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
                 lusteringAlloy=0, gleamingAlloy=0, preciousAlloy=0,
                 condensedAlloy=0,
                 motleyCompound=0, sheenCompound=0, crystalCompound=0,
                 opulentCompound=0, glossyCompound=0,
                 baseMetals=0, heavyMetals=0, nobleMetals=0, reactiveMetals=0,
                 toxicMetals=0,
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
    def __init__(self, name, productionStartCost, planetary=Planetary(),
                 minerals=Minerals(tritanium=0,
                                   pyerite=0,
                                   mexallon=0)):
        self.name = name
        self.planetary = planetary
        self.minerals = minerals
        self.productionStartCost = productionStartCost


def applyFactorOnBP(factor, bp):
    modifiedBP = BluePrint(bp.name, productionStartCost=bp.productionStartCost)
    modifiedBP.planetary.dictionary = {
        key: math.ceil(value / 150 * factor) for key, value in
        bp.planetary.dictionary.items()}
    modifiedBP.minerals.dictionary = {
        key: math.ceil((value / 150 * factor)) for key, value in
        bp.minerals.dictionary.items()}

    return modifiedBP


bpListBase = [
    BluePrint(name='Harbinger Prototype Blueprint',
              productionStartCost=25000000,
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
              productionStartCost=25000000,
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
              productionStartCost=200000000,
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
              productionStartCost=1500000,
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
    BluePrint(name='Vexor Navy Issue Blueprint',
              productionStartCost=6500000,
              planetary=Planetary(
                  lusteringAlloy=13463,
                  sheenCompound=14504,
                  opulentCompound=15351,
                  heavyMetals=14504,
                  reactiveMetals=3818
              ),
              minerals=Minerals(
                  tritanium=2465163,
                  pyerite=674229,
                  mexallon=219267,
                  isogen=36293,
                  nocxium=10347
              )
              ),
    BluePrint(name='Gila Blueprint',
              productionStartCost=200000000,
              planetary=Planetary(
                  condensedAlloy=127337,
                  preciousAlloy=99780,
                  opulentCompound=127337,
                  reactiveMetals=31662,
                  toxicMetals=31401
              ),
              minerals=Minerals(
                  tritanium=57888200,
                  pyerite=17355749,
                  mexallon=5693337,
                  isogen=921447,
                  nocxium=230264,
                  zydrine=91305,
                  megacyte=39183
              )
              ),
    BluePrint(name='Vigilant Blueprint',
              productionStartCost=200000000,
              planetary=Planetary(
                  condensedAlloy=119403,
                  preciousAlloy=93563,
                  opulentCompound=119403,
                  reactiveMetals=29690,
                  toxicMetals=29445
              ),
              minerals=Minerals(
                  tritanium=53697600,
                  pyerite=15534594,
                  mexallon=5287262,
                  isogen=828404,
                  nocxium=247812,
                  zydrine=87201
              )
              ),
    BluePrint(name='Nereus High Mobility Blueprint',
              productionStartCost=3000000,
              planetary=Planetary(
                  lusteringAlloy=6107,
                  condensedAlloy=6963,
                  opulentCompound=6963,
                  reactiveMetals=1733,
                  toxicMetals=1718
              ),
              minerals=Minerals(
                  tritanium=1118181,
                  pyerite=305826,
                  mexallon=99459,
                  isogen=16463,
                  nocxium=4694
              )
              ),
    BluePrint(name='Retriever Blueprint',
              productionStartCost=15000000,
              planetary=Planetary(
                  condensedAlloy=13409,
                  preciousAlloy=10508,
                  opulentCompound=13409,
                  reactiveMetals=3335,
                  toxicMetals=3308
              ),
              minerals=Minerals(
                  tritanium=3925214,
                  pyerite=966006,
                  mexallon=331332,
                  isogen=49862,
                  nocxium=16247,
                  zydrine=5091
              )
              ),
    BluePrint(name='Succubus Blueprint',
              productionStartCost=55000000,
              planetary=Planetary(
                  condensedAlloy=44192,
                  preciousAlloy=34628,
                  fiberComposite=44192,
                  reactiveMetals=10988,
                  toxicMetals=10898
              ),
              minerals=Minerals(
                  tritanium=25921650,
                  pyerite=5146985,
                  mexallon=1861805,
                  isogen=287084,
                  nocxium=75672
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
