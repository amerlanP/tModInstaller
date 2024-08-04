import zipfile
import shutil
import json
from pathlib import Path

packName = "TrialNumber69"

def unzipMoveModPack(tPath):
    zipfile.ZipFile(".\\"+ packName +".zip").extractall(tPath + "\\Mods\\ModPacks\\" + packName)

def backupPlayers(tPath):
    src = tPath + "Players"
    dst = str(Path.home()) + "\\Desktop\\players_backup"
    shutil.copytree(src, dst, dirs_exist_ok=True)

def setActiveModpack(tPath):
    config_path = tPath + "config.json"
    new_pack_path = tPath + "Mods\\ModPacks\\" + packName
    enabled_path = tPath + "Mods\\enabled.json"
    
    tModLoaderConfig = open(config_path)
    tConfigJson = json.load(tModLoaderConfig)
    tConfigJson["ModPackActive"] = new_pack_path
    json.dump(tConfigJson, open(config_path, "w"), indent=2)
    open(enabled_path, "w").write(
'''[
  "androLib",
  "AnglerShopsAlternative",
  "AssortedCrazyThings",
  "Autofish",
  "BetterExtractinator",
  "BInfoAcc",
  "BlueMoon",
  "BossChecklist",
  "BossCursor",
  "BossesAsNPCs",
  "BoundNPCImmunity",
  "CalamityBardHealer",
  "CalamityMod",
  "CalamityModMusic",
  "CalamityOverhaul",
  "CalValEX",
  "CatalystMod",
  "CeleryManPets",
  "ClamExtraMusic",
  "CollisionLib",
  "Consolaria",
  "DecorativePotions",
  "DisplayLuckCount",
  "EvilPylon",
  "ExpandedInventory",
  "ExpandedTerraria",
  "ExtraPylons",
  "Fargowiltas",
  "FargowiltasCrossmod",
  "FargowiltasSouls",
  "FishGunsPlus",
  "FishinRodZenith",
  "HookStatsAndWingStats",
  "ItemChecklist",
  "LansUnlimitedBuffSlots",
  "Luminance",
  "MagicStorage",
  "MirrorOfReturn",
  "MoreZenith",
  "NoxusBoss",
  "OneStopNPCShop",
  "ParticleLibrary",
  "PotionFountains",
  "RecipeBrowser",
  "RecipeBrowserToMagicStorage",
  "Roommates",
  "SerousCommonLib",
  "SharedMap",
  "ShieldsOfCthulhu",
  "ShoeSlot",
  "ShopExpander",
  "SmarterCursor",
  "SpiritMod",
  "StarsAbove",
  "StockableShops",
  "StructureHelper",
  "SubworldLibrary",
  "ThoriamityConvergenceREDUX",
  "ThoriumMod",
  "ThoriumRework",
  "TownNPCHome",
  "Trinkets",
  "Twaila",
  "VacuumBags",
  "VacuumOreBag",
  "Verdant",
  "WhatAmmoDoesThisUse",
  "Wikithis",
  "WingSlotExtra",
  "WMITF",
  "WoB",
  "WorldGenMod",
  "Zenith_pickaxe",
  "ZenithGunReturn",
  "ZenithHamaxe",
  "ZoneTitles"
]''')

    tModLoaderConfig.close()

if __name__ == "__main__":
    tModLoaderPath = str(Path.home()) + "\\Documents\\My Games\\Terraria\\tModLoader\\"

    unzipMoveModPack(tModLoaderPath)
    setActiveModpack(tModLoaderPath)
    # backupPlayers(tModLoaderPath)
