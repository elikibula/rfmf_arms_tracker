from django.db import models

gender_Choices = (
    ("male", "Male"),
    ("female", "Female")
)

armtype_Choices = (
    ("revolver", "Revolver"),
    ("pistol", "Pistol"),
    ("holster", "Holster"),
    ("machine_gun", "Machine Gun"),
    ("shot_gun", "Shot Gun"), 
    ("rifle", "Rifle"), 
    ("air_gun", "Air Gun"),
    ("grenade_launcher", "Grenade Launcher"),
    ("smg", "SMG"),
    ("lmg", "LMG"),
    ("mortar", "Mortar"),
    ("craft_gun", "Craft Gun"), 
    ("sniper_rifle", "Sniper Rifle") 
    
)

arm_action_Choices = (
    ("semi_auto", "Semi Automatic"),
    ("lever_action", "Lever Action"),
    ("fully_automatic", "Fully Automatic"),
    ("close_bolt", "Close Bolt"),
    ("break_action", "Break Action"), 
    ("revolver", "Revolver"), 
    ("pistol_single_shot", "Pistol Single Shot"),
    ("gas_operated", "Gas Operated"),
    ("open_bolt", "Open Bolt"),
    ("brech_load", "Brech Load"),
    ("single_shot", "Single Shot"),
    ("artillery", "Artillery"), 
    ("gas_regulated", "Gas Regulated"), 
    
)

arm_status_Choices = (
    ("damaged", "Damaged"),
    ("lost", "Lost"),
    ("misplaced", "Misplaced"),
    ("serviceable", "Serviceable"),
    ("unserviceable", "Unserviceable"), 
    ("held_for_destruction", "Held For Destruction"), 
    ("destroyed", "Destroyed"),
    ("return", "Return"),
    ("registered", "Registered"),    
)

license_category_Choices = (
    ("long_arm", "Long Arm"),
    ("handgun", "Handgun"),
    ("sport_shooting", "Sport Shooting"),
    ("hunting", "Hunting"),    
)

genuine_reason_Choices = (
    ("rfmf_personnel", "RFMF Personnel"),
    ("navy_personnel", "Navy Personnel"),
    ("police_personnel", "Police Personnel"),
    ("civillian_personnel", "Civillian Personnel"),    
)

rank_Choices = (
    ("major_general", "Major General"),
    ("rear_admiral", "Rear Admiral"),
    ("brigadier", "Brigadier"),
    ("commodore", "Commodore"),
    ("colonel", "Colonel"), 
    ("lt_colonel", "LT Colonel"), 
    ("major", "Major"),
    ("chief_of_navy", "Chief of Navy"),
    ("padre", "Padre"),
    ("captain", "Captain"),
    ("commander", "Commander"),
    ("lt_commander", "LT Commander"), 
    ("leutenant ", "Leutenant"), 
    ("sub_leutenant", "Sub Leutenant"),
    ("ensign", "Ensign"),
    ("midshipman", "Midshipman"), 
    ("cadet", "Cadet"), 
    ("warrant_officer_I", "Warrant Officer I"),
    ("warrant_officer_II", "Warrant Officer II"),
    ("staff_sergeant", "Staff Sergeant"),
    ("sergeant", "Sergeant"),
    ("corporal", "Corporal"),
    ("lance_corporal", "Lance Corporal"),
    ("private", "Private"), 
    ("leutenant ", "Leutenant"), 
    ("rsm_army", "RSM Army"),
    ("master_arm_navy", "Master at Arm Navy"), 
    ("ordinary_seaman", "Ordinary Seaman Navy"), 
)

ammunition_Choices = (
    ("damage", "Damage"),
    ("dispose", "Dispose"),
    ("expended", "Expended"),
    ("issue", "Issue"), 
    ("returned", "Returned"),
    ("expired", "Expired"),      
)

arm_source_Choices = (
    ("confiscated", "Confiscated"),
    ("previously_unregistered", "Previously Unregistered"),
    ("surrendered", "Surrendered"),
    ("imported", "Imported"),   
)

location_Choices = (
    ("engineers", "Engineers [Nabuni]"),
    ("ftg_nasinu", "FTG Nasinu"),
    ("lsu_qeb_nabua", "LSU QEB Nabua"),
    ("3fir_qeb_nabua", "3 FIR QEB Nabua"),
    ("naval_base_walubay", "Naval Base Walubay"), 
    ("togalevu_naval_base", "Togalevu Naval Base"), 
    ("lautoka", "Lautoka Echo"),
    ("nadi", "Nadi Delta"),
    ("black_rock", "Black Rock"),  
    ("labasa", "Labasa Golf"),  

)

idtypes_Choices = (
    ("passport", "Passport"),
    ("driving_license", "Driving License"),
    ("voter_id", "Voter ID"),
    ("rfmf_id", "RFMF ID"), 
    ("police_id", "Police ID"),   
)


class Arm(models.Model):
    arm_type = models.CharField(choices=armtype_Choices, max_length=200)
    arm_action = models.CharField(choices=arm_action_Choices, max_length=200)
    arm_status = models.CharField(choices=arm_status_Choices,max_length=200)
    license_category = models.CharField(choices=license_category_Choices,max_length=200)
    genuine_reason = models.CharField(choices=genuine_reason_Choices,max_length=200)
    regimental_number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    rank = models.CharField(choices=rank_Choices,max_length=200)
    gender = models.CharField(choices=gender_Choices, max_length=50, blank=True)
    unit = models.CharField(max_length=200)
    ammunition_status = models.CharField(choices=ammunition_Choices, max_length=50, blank=True)
    license_type = models.CharField(max_length=200)
    arm_source = models.CharField(choices=arm_source_Choices,max_length=200)
    location = models.CharField(choices=location_Choices,max_length=200)
    archive_reason = models.CharField(max_length=200)
    id_types = models.CharField(choices=idtypes_Choices,max_length=200)

    


    def __str__(self):
        return self.name