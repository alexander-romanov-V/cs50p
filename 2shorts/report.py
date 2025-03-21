def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    print(create_report(spacecraft))

    spacecraft2 = {"name": "James Webb Space Telescope"}
    # spacecraft2["distance"] = 0.01
    spacecraft2.update({"distance": 0.01, "orbit": "Sun"})
 
    print(create_report(spacecraft2))

    spacecraft3 = {}
    print(create_report(spacecraft3))

def create_report(spacecraft):
    return f"""
    ======== REPORT ========
        
    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ========================
    """

main()