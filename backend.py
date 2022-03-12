import json

jsonData = '''


    {
        "medicines": [
    {
        "medicines": "asthalin",
        "scientific name":"Albuterol(Sabumoterol)",
        "uses": "treat asthma cases, and general asthamatic problems",
        "side effects":"headache, nausea"

    },
    {
        "medicines": "imodium ",
        "uses": "This medication is used to treat sudden diarrhea (including traveler's diarrhea). It works by slowing down the movement of the gut",
        "scientific name":"loperamide hydrochloride capsules",
        "side effects":"dizziness,drowsiness,tiredness,"

    },   
    {
        "medicines": "ferium",
        "scientific name":"hydroxide polymaltose complex and folic acid tablets",
        "uses": "helps in deficiency of red blood cells",
        "side effects":"Loss Of Appetite,Dry Mouth."

    },
    {
        "medicines": "rantac",
        "scientific name":"ranitinide tablets",
        "uses": "Rantac tablets are used for Heartburn, Indigestion and acidity.",
        "side effects":"Headache, Diarrhea or Constipation."

    },
    {
        "medicines": "ondem",
        "scientific name":"rondansetron tablets",
        "uses": "Used for treating nausea and vomiting.",
        "side effects":"headache, dizzyness"

    },
    {
        "medicines": "Zanocin",
        "scientific name":"Ofloxacin",
        "uses": "Used to treat illness caused by bacteria such as pneumonia and gonorrhea.",
        "side effects":"Sleep Problems, Headache, Vomiting."

    },
    {
        "medicines": "Dolo 650",
        "scientific name":"Acetaminophin/ Paracetamol",
        "uses": "Used to treat high pains and aches as well as Fever too.",
        "side effects":"Dark Urine, Low Fever."

    },
    {
        "medicines": "zeredol-p",
        "scientific name":"paracetomol ",
        "uses": "Zerodol-P Tablet is a pain-relieving medicine. It is used to reduce pain and inflammation in conditions like rheumatoid arthritis, ankylosing spondylitis, and osteoarthritis. It may also be used to relieve muscle pain, back pain, toothache, or pain in the ear and throat.",
        "side effects":"-"

    },
    {
        "medicines": "zincovit",
        "scientific name":"zincovit",
        "uses": "helps in treating vitamin defincinecy, and helps increasing amount of vitamin-C, this medicin helps improve metabolism as well",
        "side effects":""

    },
    {
        "medicines": "allegra",
        "scientific name":"Fexofenadine hydrochloride tablets.",
        "uses": "",
        "side effects":"headache, nausea"

    },
    {
        "medicines": "asthalin",
        "scientific name":"Albuterol(Sabumoterol)",
        "uses": "treat asthma cases, and general asthamatic problems",
        "side effects":"headache, nausea"

    },
    {
        "medicines": "asthalin",
        "scientific name":"Albuterol(Sabumoterol)",
        "uses": "treat asthma cases, and general asthamatic problems",
        "side effects":"headache, nausea"

    }
]
}

'''

Medicine = input("Whats the Scientific Name of the Medicine that you want to use?: ")

data = json.loads(jsonData)

... (20 lines left)