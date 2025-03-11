import os
import shutil

base_folder = '/Applications/World of Warcraft/_retail_/Interface/AddOns/SharedMedia_ONS/sound'
subfolder = os.path.join(base_folder,'unusedSounds' )

# checking to ssee the subfolder exists
os.makedirs(subfolder, exist_ok=True)

file_to_move = [
    '318_MoveToSkull.mp3',
    '319_MoveToCross.mp3',
    '320_MoveToMoon.mp3',
    '321_MoveToStar.mp3',
    '322_MoveToCircle.mp3',
    '323_MoveToTriangle.mp3',
    '324_MoveToSquare.mp3',
    '325_MoveToDiamond.mp3',
    '326_StackOnSkull.mp3',
    '327_StackOnCross.mp3',
    '328_StackOnMoon.mp3',
    '329_StackOnStar.mp3',
    '330_StackOnCircle.mp3',
    '331_StackOnTriangle.mp3',
    '332_StackOnSquare.mp3',
    '333_StackOnDiamond.mp3',
    '334_PickUpEssence.mp3',
    '335_PickUpEssenceSoon.mp3',
    '313_InfestSoon.mp3',
    '314_Infest.mp3',
    '315_Liquefy.mp3',
    '291_Spinnerets.mp3',
    '292_SpinneretsStrands.mp3',
    '282_Decimate.mp3',
    '283_QueensBane.mp3',
    '284_QueensBaneA.mp3',
    '285_QueensBaneB.mp3',
    '274_ExperimentalDosage.mp3',
    '275_Dosage.mp3',
    '276_Regicide.mp3',
    '277_TwilightMasacre.mp3',
    '278_Masacre.mp3',
    '279_Assasination.mp3',
    '280_PhaseBlades.mp3',
    '237_VolcanicHeart.mp3',
    '238_Volcanic.mp3',
    '226_Corrupted.mp3',
    '222_Magma.mp3',
    '223_Tantrum.mp3',
    '214_Essence.mp3',
    '208_BlackHole.mp3',
    '209_Ascension.mp3',
    '210_AscensionSoon.mp3',
    '204_StaffSpawning.mp3',
    '201_BreakEggs.mp3',
    '182_BadBlaze.mp3',
    '183_Ducked.mp3',
    '177_Blaze.mp3',
    '178_BlazeHit.mp3',
    '103_GravityBomb.mp3',
    '86_DropSeeds.mp3',
    '87_CollectSeeds.mp3',
    '88_CorruptedSeeds.mp3',
    '242_FullyBuffed.mp3',
    '61_FlareBomb.mp3',
    '85_Seeds.mp3'
]

for file_name in file_to_move:
    src = os.path.join(base_folder, file_name)
    dst = os.path.join(subfolder, file_name)

    # check to make sure the file exists before we move the files 
    if os.path.exists(src):
        shutil.move(src, dst)
        print(f"\033[92mMoved {file_name} to {subfolder}\033[0m")
    else:
        print(f"\033[91m{file_name} does not exist in {base_folder}\033[0m")

