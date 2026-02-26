import pandas as pd
import numpy as np

def get_county_data():
    # EXHAUSTIVE 2026 PROJECT MAPPING
    project_map = {
        "Nairobi": [
            "Starehe Point", "Pangani Estate", "Kibera Soweto B", "Shauri Moyo A", 
            "Mukuru Met Site", "Embakasi AHP", "Mathare Lot 1", "Mathare Lot 2", 
            "Mbotela Estate", "Kasarani Lot 4", "Kibra Southlands", "Mariguini Informal Settlement"
        ],
        "Kiambu": [
            "Kikuyu Township", "Thika Bustani", "Gatundu Town Estate", "Kings Boma Ruiru", 
            "Kamiti Lot 1", "Kamiti Lot 2", "Kiambu Town Estate", "Limuru AHP", 
            "Gachie Honeybee", "Kikuyu Gitaru", "Ruiru Town Phase 2", "Karuri AHP"
        ],
        "Mombasa": [
            "Buxton Point", "Hobley Estate", "Mtwapa City Phase 1", "Changamwe AHP", 
            "Likoni AHP", "Nyali Executive Units"
        ],
        "Nakuru": [
            "Bahati Nakuru", "Bondeni Estate", "Elburgon Project", "Gilgil AHP", 
            "Buffalo Mall Phase 1", "Molo Michinda", "Naivasha Karagita", "Nakuru City Phase 2"
        ],
        "Uasin Gishu": [
            "Kimumu AMS", "Eldoret Railway City", "Kidiwa Phase 2", "Eldoret Town Center"
        ],
        "Kisumu": [
            "Lumumba Estate", "Kisumu City Phase 1", "Milimani Kisumu", "Kibuye Market Site"
        ],
        "Machakos": [
            "Machakos Township Phase 1", "Machakos Town Phase 2", "Mavoko Sustainable Housing", 
            "Malaa Riverside", "Athi River Stoni Athi", "Syokimau Gateway"
        ],
        "Nandi": ["Chesumei Estate", "Emgwen Project", "Nandi Hills AHP", "Kapsabet Pool Housing"],
        "Garissa": ["Garissa Township", "Garissa Public Works", "Masalani AHP", "Garissa HQ"],
        "Kilifi": ["Bofa Estate", "Mtwapa Mini City", "Watamu Beach Rd", "Malindi AHP"],
        "Nyeri": ["Blue Valley Nyeri", "Mukurwe-ini Project", "Wamagana AHP", "Nyeri County HQ"],
        "Baringo": ["Marigat Estate", "Kabarnet AHP"],
        "Busia": ["Busia ATC Phase 1", "Busia ATC Phase 2", "Funyula AHP", "Nasewa Industrial Park"],
        "Kirinyaga": ["Wamumu AHP", "Sagana AHP", "Kerugoya NHC", "Kirinyaga Town"],
        "Kakamega": ["Lurambi Milimani", "Mumias Smart City", "Matunda AHP", "Kakamega Old Airstrip"]
    }

    all_counties = ["Mombasa", "Kwale", "Kilifi", "Tana River", "Lamu", "Taita-Taveta", "Garissa", "Wajir", "Mandera", "Marsabit", "Isiolo", "Meru", "Tharaka-Nithi", "Embu", "Kitui", "Machakos", "Makueni", "Nyandarua", "Nyeri", "Kirinyaga", "Murang'a", "Kiambu", "Turkana", "West Pokot", "Samburu", "Trans-Nzoia", "Uasin Gishu", "Elgeyo-Marakwet", "Nandi", "Baringo", "Laikipia", "Nakuru", "Narok", "Kajiado", "Kericho", "Bomet", "Kakamega", "Vihiga", "Bungoma", "Busia", "Siaya", "Kisumu", "Homa Bay", "Migori", "Kisii", "Nyamira", "Nairobi"]

    rows = []
    for county in all_counties:
        # Get specific projects OR default to constituency-level landbanks
        projects = project_map.get(county, [f"{county} HQ AHP", f"{county} Constituency AHP"])
        for p in projects:
            rows.append({
                "County": county,
                "Project": p,
                "Units": np.random.randint(400, 5000) if county in project_map else np.random.randint(200, 400),
                "Status": np.random.choice(["Ongoing", "Completed", "Planned"], p=[0.70, 0.20, 0.10]),
                "Risk": np.random.randint(0, 35)
            })
    
    return pd.DataFrame(rows)

def get_msme_impact_data():
    impact = {"budget": "KES 11.0B", "jobs": 428000, "items": 79}
    supply = pd.DataFrame({
        'Component': ['Steel Doors', 'Windows', 'Ballustrades', 'Tiles', 'Paint'],
        'Value': [4.4, 3.2, 1.2, 0.9, 0.8],
        'Cluster': ['Kamukunji', 'Kariobangi', 'Gikomba', 'Kanduyi', 'Eldoret']
    })
    return impact, supply
