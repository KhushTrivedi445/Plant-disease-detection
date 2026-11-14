"""
disease_info.py — Curated knowledge base for all 38 plant disease classes.

Each entry maps the raw class label (e.g. "Apple___Apple_scab") to a dict:
    {
        "plant":       str,       # crop species
        "disease":     str,       # human-readable disease / condition name
        "is_healthy":  bool,
        "symptoms":    list[str], # visible symptoms on the leaf
        "causes":      str,       # pathogen / agent
        "treatment":   list[str], # actionable agronomic advice
        "prevention":  list[str], # long-term measures
    }
"""

from __future__ import annotations

DISEASE_INFO: dict[str, dict] = {

    # ===========================  APPLE  ===========================

    "Apple___Apple_scab": {
        "plant": "Apple",
        "disease": "Apple Scab",
        "is_healthy": False,
        "symptoms": [
            "Olive-green to dark-brown velvety spots on leaves",
            "Leaves may curl, distort, or drop prematurely",
            "Dark, scabby lesions on fruit surface",
        ],
        "causes": "Fungus Venturia inaequalis — spreads via wind-borne ascospores in spring.",
        "treatment": [
            "Apply fungicides (captan, myclobutanil) at green-tip through petal fall",
            "Remove and destroy fallen infected leaves in autumn",
            "Prune canopy to improve air circulation",
        ],
        "prevention": [
            "Plant scab-resistant apple cultivars (e.g., Liberty, Enterprise)",
            "Maintain orchard sanitation — rake and compost fallen debris",
            "Use protective fungicide sprays before rain events",
        ],
    },

    "Apple___Black_rot": {
        "plant": "Apple",
        "disease": "Black Rot",
        "is_healthy": False,
        "symptoms": [
            "Purple or reddish-brown spots on leaves with concentric rings ('frog-eye')",
            "Black, sunken, expanding lesions on fruit",
            "Cankers on limbs and trunk",
        ],
        "causes": "Fungus Botryosphaeria obtusa — overwinters in mummified fruit and cankers.",
        "treatment": [
            "Prune and destroy infected branches and mummified fruits",
            "Apply captan or thiophanate-methyl during early season sprays",
            "Maintain balanced fertility to reduce stress",
        ],
        "prevention": [
            "Remove dead wood, cankers, and mummy fruits from the orchard",
            "Avoid wounding trees during cultivation",
            "Ensure good drainage and air flow around trees",
        ],
    },

    "Apple___Cedar_apple_rust": {
        "plant": "Apple",
        "disease": "Cedar Apple Rust",
        "is_healthy": False,
        "symptoms": [
            "Bright orange-yellow spots on upper leaf surface",
            "Small, tube-like projections (aecia) on leaf undersides",
            "Premature defoliation in severe cases",
        ],
        "causes": "Fungus Gymnosporangium juniperi-virginianae — requires both apple and cedar/juniper hosts.",
        "treatment": [
            "Apply fungicides (myclobutanil, mancozeb) from pink bud through 2 weeks after petal fall",
            "Remove nearby juniper/eastern red cedar if feasible",
            "Scout and prune galls on junipers in late winter",
        ],
        "prevention": [
            "Plant rust-resistant apple varieties",
            "Eliminate alternate juniper hosts within a 2-mile radius",
            "Maintain a regular fungicide programme during spring",
        ],
    },

    "Apple___healthy": {
        "plant": "Apple",
        "disease": "Healthy",
        "is_healthy": True,
        "symptoms": ["No visible disease symptoms — leaf appears normal and healthy."],
        "causes": "N/A",
        "treatment": ["No treatment required — continue standard orchard management."],
        "prevention": [
            "Maintain balanced fertilisation and irrigation",
            "Monitor regularly for early signs of pest or disease pressure",
            "Follow an integrated pest management (IPM) programme",
        ],
    },

    # ===========================  BLUEBERRY  ===========================

    "Blueberry___healthy": {
        "plant": "Blueberry",
        "disease": "Healthy",
        "is_healthy": True,
        "symptoms": ["No visible disease symptoms — leaf appears normal and healthy."],
        "causes": "N/A",
        "treatment": ["No treatment required — continue standard blueberry care."],
        "prevention": [
            "Maintain soil pH between 4.5 and 5.5",
            "Use mulch to retain moisture and suppress weeds",
            "Prune annually for vigour and airflow",
        ],
    },

    # ===========================  CHERRY  ===========================

    "Cherry_(including_sour)___Powdery_mildew": {
        "plant": "Cherry",
        "disease": "Powdery Mildew",
        "is_healthy": False,
        "symptoms": [
            "White powdery coating on young leaves and shoots",
            "Leaves may curl upward and become distorted",
            "Stunted shoot growth in severe infections",
        ],
        "causes": "Fungus Podosphaera clandestina — favours warm, dry days with cool, humid nights.",
        "treatment": [
            "Apply sulphur-based or triazole fungicides at first sign of infection",
            "Remove and destroy heavily infected shoots",
            "Avoid excessive nitrogen fertilisation",
        ],
        "prevention": [
            "Select resistant cherry cultivars",
            "Improve air circulation through proper pruning and spacing",
            "Apply preventive fungicide sprays before bloom",
        ],
    },

    "Cherry_(including_sour)___healthy": {
        "plant": "Cherry",
        "disease": "Healthy",
        "is_healthy": True,
        "symptoms": ["No visible disease symptoms — leaf appears normal and healthy."],
        "causes": "N/A",
        "treatment": ["No treatment required."],
        "prevention": [
            "Maintain proper irrigation and nutrition",
            "Prune for light penetration and air movement",
            "Monitor for pests such as cherry fruit fly",
        ],
    },

    # ===========================  CORN / MAIZE  ===========================

    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "plant": "Corn (Maize)",
        "disease": "Cercospora Leaf Spot / Gray Leaf Spot",
        "is_healthy": False,
        "symptoms": [
            "Long, narrow, rectangular grey-to-tan lesions running parallel to veins",
            "Lesions may coalesce, blighting large leaf areas",
            "Lower leaves affected first, progressing upward",
        ],
        "causes": "Fungus Cercospora zeae-maydis — thrives in humid, warm environments with residue on the soil surface.",
        "treatment": [
            "Apply foliar fungicides (strobilurins, triazoles) at or before tasselling",
            "Rotate crops away from continuous corn",
            "Incorporate or remove corn residue after harvest",
        ],
        "prevention": [
            "Plant resistant or tolerant hybrids",
            "Practise 2-year crop rotation",
            "Tillage to bury infected residue where erosion risk is low",
        ],
    },

    "Corn_(maize)___Common_rust_": {
        "plant": "Corn (Maize)",
        "disease": "Common Rust",
        "is_healthy": False,
        "symptoms": [
            "Cinnamon-brown, oval to elongated pustules on both leaf surfaces",
            "Pustules may rupture, releasing powdery reddish-brown spores",
            "Severe infection can cause premature leaf senescence",
        ],
        "causes": "Fungus Puccinia sorghi — spores are wind-borne from southern regions each season.",
        "treatment": [
            "Apply fungicides (azoxystrobin, propiconazole) if infection is detected before tasselling",
            "Scout fields regularly during mid-vegetative stages",
        ],
        "prevention": [
            "Plant rust-resistant hybrids",
            "Timely planting to avoid peak spore arrival",
            "Monitor weather forecasts for rust-favourable conditions",
        ],
    },

    "Corn_(maize)___Northern_Leaf_Blight": {
        "plant": "Corn (Maize)",
        "disease": "Northern Leaf Blight",
        "is_healthy": False,
        "symptoms": [
            "Large (2–15 cm) cigar-shaped, grey-green to tan lesions on leaves",
            "Lesions may coalesce and kill entire leaves",
            "Usually starts on lower leaves",
        ],
        "causes": "Fungus Exserohilum turcicum — survives in corn debris and spreads via wind-borne conidia.",
        "treatment": [
            "Apply foliar fungicides at early tassel if disease is progressing rapidly",
            "Remove crop residues",
            "Rotate to non-host crops",
        ],
        "prevention": [
            "Select hybrids with Ht resistance genes",
            "Practise crop rotation and residue management",
            "Avoid planting corn after corn in high-risk fields",
        ],
    },

    "Corn_(maize)___healthy": {
        "plant": "Corn (Maize)",
        "disease": "Healthy",
        "is_healthy": True,
        "symptoms": ["No visible disease symptoms — leaf appears normal and healthy."],
        "causes": "N/A",
        "treatment": ["No treatment required."],
        "prevention": [
            "Use certified seed with appropriate disease resistance traits",
            "Follow balanced fertilisation programmes",
            "Scout fields regularly from V6 through grain fill",
        ],
    },

    # ===========================  GRAPE  ===========================

    "Grape___Black_rot": {
        "plant": "Grape",
        "disease": "Black Rot",
        "is_healthy": False,
        "symptoms": [
            "Circular reddish-brown leaf spots with dark borders",
            "Black, shrivelled, mummified berries ('mummies')",
            "Tiny black pycnidia visible on lesions and mummies",
        ],
        "causes": "Fungus Guignardia bidwellii — overwinters in mummified fruit and cane lesions.",
        "treatment": [
            "Apply fungicides (mancozeb, myclobutanil) from bud break to 4 weeks post-bloom",
            "Remove mummified berries and infected canes",
            "Improve canopy management for air circulation",
        ],
        "prevention": [
            "Sanitation — remove mummies, infected tendrils, and canes during dormancy",
            "Open canopy via shoot positioning and leaf removal",
            "Use resistant cultivars where available",
        ],
    },

    "Grape___Esca_(Black_Measles)": {
        "plant": "Grape",
        "disease": "Esca (Black Measles)",
        "is_healthy": False,
        "symptoms": [
            "Interveinal chlorosis and necrosis giving a 'tiger-stripe' pattern on leaves",
            "Dark spots or streaks on berry skin",
            "Sudden vine wilt (apoplexy) in severe cases",
        ],
        "causes": "Complex of fungi including Phaeomoniella chlamydospora and Phaeoacremonium spp. — infects through pruning wounds.",
        "treatment": [
            "No curative chemical treatment available",
            "Remove and replace severely affected vines",
            "Protect pruning wounds with sealant or biocontrol (Trichoderma)",
        ],
        "prevention": [
            "Delay pruning to late dormancy to reduce wound susceptibility",
            "Apply wound protectant immediately after pruning",
            "Use healthy, certified planting material",
        ],
    },

    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "plant": "Grape",
        "disease": "Leaf Blight (Isariopsis Leaf Spot)",
        "is_healthy": False,
        "symptoms": [
            "Small, dark brown to black angular spots on leaves",
            "Spots may merge into large necrotic patches",
            "Premature defoliation reduces vine vigour",
        ],
        "causes": "Fungus Pseudocercospora vitis (syn. Isariopsis clavispora) — favoured by warm, wet conditions.",
        "treatment": [
            "Apply protective copper or mancozeb fungicides",
            "Remove fallen infected leaves from vineyard floor",
            "Improve air circulation through canopy management",
        ],
        "prevention": [
            "Maintain open canopy architecture",
            "Balanced nutrition to promote plant resilience",
            "Regular scouting from véraison onwards",
        ],
    },

    "Grape___healthy": {
        "plant": "Grape",
        "disease": "Healthy",
        "is_healthy": True,
        "symptoms": ["No visible disease symptoms — leaf appears normal and healthy."],
        "causes": "N/A",
        "treatment": ["No treatment required."],
        "prevention": [
            "Practise balanced canopy management",
            "Monitor for powdery/downy mildew and other threats",
            "Maintain soil health and proper irrigation",
        ],
    },

    # ===========================  ORANGE  ===========================

    "Orange___Haunglongbing_(Citrus_greening)": {
        "plant": "Orange",
        "disease": "Huanglongbing (Citrus Greening)",
        "is_healthy": False,
        "symptoms": [
            "Asymmetric blotchy mottling and yellowing of leaves",
            "Small, lopsided, bitter, and green-tinged fruit",
            "Twig dieback and overall tree decline",
        ],
        "causes": "Bacterium Candidatus Liberibacter asiaticus — transmitted by the Asian citrus psyllid (Diaphorina citri).",
        "treatment": [
            "No cure exists — manage psyllid vectors with systemic insecticides",
            "Nutritional therapy (foliar micronutrients) to sustain tree productivity",
            "Remove severely symptomatic trees to reduce inoculum",
        ],
        "prevention": [
            "Plant certified disease-free nursery stock",
            "Control psyllid populations with area-wide management programmes",
            "Scout regularly for psyllids and HLB symptoms",
        ],
    },

    # ===========================  PEACH  ===========================

    "Peach___Bacterial_spot": {
        "plant": "Peach",
        "disease": "Bacterial Spot",
        "is_healthy": False,
        "symptoms": [
            "Small, angular, water-soaked spots on leaves that turn dark and necrotic",
            "Shot-hole effect as necrotic tissue drops out",
            "Sunken, cracked lesions on fruit",
        ],
        "causes": "Bacterium Xanthomonas arboricola pv. pruni — spread by wind-driven rain.",
        "treatment": [
            "Apply copper-based bactericides at petal fall (use cautiously to avoid phytotoxicity)",
            "Oxytetracycline sprays during early fruit development",
            "Remove and destroy severely infected shoots",
        ],
        "prevention": [
            "Plant resistant cultivars adapted to your region",
            "Avoid overhead irrigation",
            "Improve air movement with proper spacing and pruning",
        ],
    },

    "Peach___healthy": {
        "plant": "Peach",
        "disease": "Healthy",
        "is_healthy": True,
        "symptoms": ["No visible disease symptoms — leaf appears normal and healthy."],
        "causes": "N/A",
        "treatment": ["No treatment required."],
        "prevention": [
            "Maintain proper pruning and thinning for good air circulation",
            "Apply dormant copper/lime-sulphur spray for general disease prevention",
            "Monitor for peach leaf curl, brown rot, and insect pests",
        ],
    },

    # ===========================  PEPPER (BELL)  ===========================

    "Pepper,_bell___Bacterial_spot": {
        "plant": "Bell Pepper",
        "disease": "Bacterial Spot",
        "is_healthy": False,
        "symptoms": [
            "Small, irregular, dark, water-soaked lesions on leaves",
            "Lesions may coalesce causing leaf yellowing and drop",
            "Raised, scab-like lesions on fruit surface",
        ],
        "causes": "Bacterium Xanthomonas campestris pv. vesicatoria — spread by rain splash, contaminated seed, and transplants.",
        "treatment": [
            "Apply copper-based sprays + mancozeb tank mix",
            "Remove and discard infected plant material",
            "Use hot-water seed treatment (50 °C for 25 min)",
        ],
        "prevention": [
            "Use certified pathogen-free seed and transplants",
            "Rotate with non-solanaceous crops for ≥2 years",
            "Avoid working in wet fields; use drip irrigation",
        ],
    },

    "Pepper,_bell___healthy": {
        "plant": "Bell Pepper",
        "disease": "Healthy",
        "is_healthy": True,
        "symptoms": ["No visible disease symptoms — leaf appears normal and healthy."],
        "causes": "N/A",
        "treatment": ["No treatment required."],
        "prevention": [
            "Practise crop rotation",
            "Maintain consistent watering and mulch",
            "Scout for aphids, thrips, and bacterial/fungal diseases weekly",
        ],
    },

    # ===========================  POTATO  ===========================

    "Potato___Early_blight": {
        "plant": "Potato",
        "disease": "Early Blight",
        "is_healthy": False,
        "symptoms": [
            "Dark brown, concentric-ringed (target-board) lesions on older leaves",
            "Yellowing around lesions; lower leaves affected first",
            "Premature defoliation reduces tuber yield",
        ],
        "causes": "Fungus Alternaria solani — survives in crop debris and soil; favoured by warm, humid weather.",
        "treatment": [
            "Apply chlorothalonil, mancozeb, or azoxystrobin fungicides on schedule",
            "Remove infected lower foliage",
            "Harvest tubers promptly after vine kill",
        ],
        "prevention": [
            "Practise 3-year crop rotation away from solanaceous crops",
            "Use certified seed tubers; select tolerant cultivars",
            "Adequate spacing and balanced fertilisation (avoid N excess)",
        ],
    },

    "Potato___Late_blight": {
        "plant": "Potato",
        "disease": "Late Blight",
        "is_healthy": False,
        "symptoms": [
            "Large, irregular, water-soaked, dark green-to-brown lesions",
            "White fuzzy sporulation on leaf undersides in humid conditions",
            "Rapid leaf and stem collapse; brown rot in tubers",
        ],
        "causes": "Oomycete Phytophthora infestans — spreads explosively in cool, wet weather via airborne sporangia.",
        "treatment": [
            "Apply protective fungicides (chlorothalonil, mancozeb) preventively",
            "Use systemic fungicides (metalaxyl, cymoxanil) curatively if needed",
            "Destroy infected plants immediately — do NOT compost",
        ],
        "prevention": [
            "Plant resistant cultivars; use certified disease-free seed",
            "Destroy volunteer potato plants and cull piles",
            "Monitor late-blight forecasting models and spray accordingly",
        ],
    },

    "Potato___healthy": {
        "plant": "Potato",
        "disease": "Healthy",
        "is_healthy": True,
        "symptoms": ["No visible disease symptoms — leaf appears normal and healthy."],
        "causes": "N/A",
        "treatment": ["No treatment required."],
        "prevention": [
            "Use certified seed tubers",
            "Hill plants to protect tubers from light and blight spores",
            "Rotate crops and manage volunteer plants",
        ],
    },

    # ===========================  RASPBERRY  ===========================

    "Raspberry___healthy": {
        "plant": "Raspberry",
        "disease": "Healthy",
        "is_healthy": True,
        "symptoms": ["No visible disease symptoms — leaf appears normal and healthy."],
        "causes": "N/A",
        "treatment": ["No treatment required."],
        "prevention": [
            "Ensure good drainage and avoid overhead watering",
            "Remove spent floricanes after harvest",
            "Maintain weed control and proper plant spacing",
        ],
    },

    # ===========================  SOYBEAN  ===========================

    "Soybean___healthy": {
        "plant": "Soybean",
        "disease": "Healthy",
        "is_healthy": True,
        "symptoms": ["No visible disease symptoms — leaf appears normal and healthy."],
        "causes": "N/A",
        "treatment": ["No treatment required."],
        "prevention": [
            "Use treated, certified seed",
            "Rotate with corn or small grains",
            "Scout regularly for soybean rust, SDS, and insect pests",
        ],
    },

    # ===========================  SQUASH  ===========================

    "Squash___Powdery_mildew": {
        "plant": "Squash",
        "disease": "Powdery Mildew",
        "is_healthy": False,
        "symptoms": [
            "White to grey powdery fungal growth on upper leaf surfaces",
            "Leaves yellow, wilt, and die prematurely",
            "Reduced fruit size and quality",
        ],
        "causes": "Fungi Podosphaera xanthii / Erysiphe cichoracearum — favoured by warm days, cool nights, and moderate humidity.",
        "treatment": [
            "Apply sulphur, potassium bicarbonate, or triazole fungicides at first sign",
            "Remove and destroy heavily infected leaves",
            "Spray neem oil as an organic alternative",
        ],
        "prevention": [
            "Plant resistant varieties",
            "Space plants widely for maximum airflow",
            "Avoid overhead irrigation; water early in the day",
        ],
    },

    # ===========================  STRAWBERRY  ===========================

    "Strawberry___Leaf_scorch": {
        "plant": "Strawberry",
        "disease": "Leaf Scorch",
        "is_healthy": False,
        "symptoms": [
            "Small, dark purple spots on upper leaf surface",
            "Spots enlarge and merge; affected tissue turns brown and dry ('scorched')",
            "Severe defoliation weakens plants and reduces yield",
        ],
        "causes": "Fungus Diplocarpon earlianum — spread by rain splash; overwinters in infected leaf debris.",
        "treatment": [
            "Apply captan or thiram fungicides during fruiting season",
            "Remove and destroy heavily infected older leaves after harvest",
            "Renovate beds by mowing and thinning",
        ],
        "prevention": [
            "Plant resistant varieties; use certified disease-free transplants",
            "Maintain proper row spacing for air movement",
            "Avoid overhead irrigation; use drip systems",
        ],
    },

    "Strawberry___healthy": {
        "plant": "Strawberry",
        "disease": "Healthy",
        "is_healthy": True,
        "symptoms": ["No visible disease symptoms — leaf appears normal and healthy."],
        "causes": "N/A",
        "treatment": ["No treatment required."],
        "prevention": [
            "Maintain clean straw mulch around plants",
            "Renovate beds annually",
            "Scout for leaf spot, powdery mildew, and spider mites",
        ],
    },

    # ===========================  TOMATO  ===========================

    "Tomato___Bacterial_spot": {
        "plant": "Tomato",
        "disease": "Bacterial Spot",
        "is_healthy": False,
        "symptoms": [
            "Small, dark, water-soaked, greasy-looking spots on leaves",
            "Spots may merge; severely affected leaves yellow and drop",
            "Raised, scab-like lesions on green fruit",
        ],
        "causes": "Xanthomonas spp. — spread by rain, overhead irrigation, and contaminated seed/transplants.",
        "treatment": [
            "Apply copper hydroxide + mancozeb sprays on schedule",
            "Use hot-water seed treatment (50 °C, 25 min)",
            "Remove and destroy severely infected plants",
        ],
        "prevention": [
            "Use pathogen-free certified seed and transplants",
            "Rotate to non-solanaceous crops for ≥2 years",
            "Use drip irrigation; avoid working in wet fields",
        ],
    },

    "Tomato___Early_blight": {
        "plant": "Tomato",
        "disease": "Early Blight",
        "is_healthy": False,
        "symptoms": [
            "Dark brown concentric-ringed (bull's-eye) lesions on lower leaves",
            "Yellowing around lesions; progressive defoliation upward",
            "Stem lesions and fruit calyx-end rot possible",
        ],
        "causes": "Fungus Alternaria solani — overwinters in soil debris; favoured by warm, humid conditions.",
        "treatment": [
            "Apply chlorothalonil or mancozeb preventively every 7–10 days",
            "Remove infected lower leaves and stake plants for airflow",
            "Mulch to reduce soil-splash inoculum",
        ],
        "prevention": [
            "Practise 3-year rotation with non-solanaceous crops",
            "Use resistant/tolerant varieties",
            "Keep adequate spacing and avoid overhead watering",
        ],
    },

    "Tomato___Late_blight": {
        "plant": "Tomato",
        "disease": "Late Blight",
        "is_healthy": False,
        "symptoms": [
            "Large, irregular, pale green to brown water-soaked lesions on leaves",
            "White fuzzy mould on leaf undersides during wet weather",
            "Rapid plant collapse; greasy brown lesions on stems and fruit",
        ],
        "causes": "Oomycete Phytophthora infestans — same pathogen as potato late blight; explosive in cool, wet weather.",
        "treatment": [
            "Apply chlorothalonil, mancozeb, or copper fungicides preventively",
            "Use metalaxyl-based products curatively",
            "Destroy infected plants immediately — bag and dispose, do NOT compost",
        ],
        "prevention": [
            "Plant resistant cultivars (e.g., Defiant, Mountain Magic)",
            "Avoid planting near potato fields",
            "Stake and prune for maximum air circulation",
        ],
    },

    "Tomato___Leaf_Mold": {
        "plant": "Tomato",
        "disease": "Leaf Mold",
        "is_healthy": False,
        "symptoms": [
            "Pale green to yellowish diffuse spots on upper leaf surface",
            "Olive-green to greyish-brown velvety mould on leaf undersides",
            "Leaves may curl, wither, and drop; mostly lower/inner canopy",
        ],
        "causes": "Fungus Passalora fulva (syn. Fulvia fulva) — thrives in high humidity (>85 %) and poor ventilation (greenhouses).",
        "treatment": [
            "Improve ventilation and reduce humidity in greenhouses",
            "Apply fungicides (chlorothalonil, copper) at first sign",
            "Remove and destroy heavily infected leaves",
        ],
        "prevention": [
            "Grow resistant cultivars carrying Cf resistance genes",
            "Space plants generously; prune lower leaves",
            "Use drip irrigation; avoid wetting foliage",
        ],
    },

    "Tomato___Septoria_leaf_spot": {
        "plant": "Tomato",
        "disease": "Septoria Leaf Spot",
        "is_healthy": False,
        "symptoms": [
            "Numerous small (~2–3 mm) circular spots with dark borders and grey centres",
            "Tiny black pycnidia visible in spot centres with a hand lens",
            "Lower leaves affected first; severe defoliation possible",
        ],
        "causes": "Fungus Septoria lycopersici — survives on crop debris and solanaceous weeds.",
        "treatment": [
            "Apply chlorothalonil, mancozeb, or copper fungicides",
            "Remove and destroy infected lower leaves",
            "Mulch around plants to prevent soil splash",
        ],
        "prevention": [
            "Rotate crops — avoid planting tomatoes in the same spot for ≥3 years",
            "Eliminate solanaceous weeds (nightshade, ground cherry)",
            "Stake plants and use drip irrigation",
        ],
    },

    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "plant": "Tomato",
        "disease": "Spider Mites (Two-Spotted Spider Mite)",
        "is_healthy": False,
        "symptoms": [
            "Fine stippling (tiny yellow/white dots) on upper leaf surface",
            "Leaves become bronzed, dry, and brittle",
            "Fine webbing visible on leaf undersides and between leaves",
        ],
        "causes": "Arachnid Tetranychus urticae — not a pathogen but a pest; thrives in hot, dry, dusty conditions.",
        "treatment": [
            "Spray insecticidal soap or horticultural oil to smother mites",
            "Use miticides (abamectin, bifenazate) for heavy infestations",
            "Release predatory mites (Phytoseiulus persimilis) as biocontrol",
        ],
        "prevention": [
            "Maintain adequate irrigation to reduce plant stress",
            "Avoid broad-spectrum insecticides that kill mite predators",
            "Monitor undersides of leaves weekly with a hand lens",
        ],
    },

    "Tomato___Target_Spot": {
        "plant": "Tomato",
        "disease": "Target Spot",
        "is_healthy": False,
        "symptoms": [
            "Small, water-soaked spots that enlarge into brown lesions with concentric rings",
            "Lesions may have a yellow halo",
            "Severe defoliation in warm, wet weather",
        ],
        "causes": "Fungus Corynespora cassiicola — favoured by prolonged warm, wet conditions.",
        "treatment": [
            "Apply chlorothalonil, mancozeb, or azoxystrobin fungicides",
            "Remove and destroy infected leaves",
            "Improve canopy airflow by pruning",
        ],
        "prevention": [
            "Use tolerant varieties where available",
            "Rotate crops and manage debris",
            "Avoid overhead irrigation",
        ],
    },

    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "plant": "Tomato",
        "disease": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "is_healthy": False,
        "symptoms": [
            "Severe upward curling and cupping of leaves",
            "Leaf margins yellow; interveinal chlorosis",
            "Stunted, bushy growth; flower drop; drastic yield loss",
        ],
        "causes": "Begomovirus (TYLCV) — transmitted by the whitefly Bemisia tabaci (silverleaf whitefly).",
        "treatment": [
            "No cure — remove and destroy infected plants promptly",
            "Control whitefly with insecticides (imidacloprid, spiromesifen) or reflective mulch",
            "Use yellow sticky traps to monitor and reduce whitefly populations",
        ],
        "prevention": [
            "Plant TYLCV-resistant cultivars (e.g., carrying Ty-1/Ty-3 genes)",
            "Use insect-proof netting in nurseries and greenhouses",
            "Eliminate weed hosts and volunteer tomatoes",
        ],
    },

    "Tomato___Tomato_mosaic_virus": {
        "plant": "Tomato",
        "disease": "Tomato Mosaic Virus (ToMV)",
        "is_healthy": False,
        "symptoms": [
            "Light and dark green mosaic mottling on leaves",
            "Leaf distortion (puckering, fern-leaf symptoms)",
            "Reduced fruit set; fruit may show internal browning",
        ],
        "causes": "Tobamovirus (ToMV) — extremely stable; spread by mechanical contact, contaminated tools, and seed.",
        "treatment": [
            "No chemical cure — remove and destroy infected plants",
            "Disinfect tools and hands with 10 % trisodium phosphate or milk solution",
            "Avoid handling healthy plants after touching infected ones",
        ],
        "prevention": [
            "Use ToMV-resistant cultivars (Tm-2² gene)",
            "Soak seed in 10 % trisodium phosphate for 15 min before planting",
            "Do not smoke or handle tobacco near tomato plants",
        ],
    },

    "Tomato___healthy": {
        "plant": "Tomato",
        "disease": "Healthy",
        "is_healthy": True,
        "symptoms": ["No visible disease symptoms — leaf appears normal and healthy."],
        "causes": "N/A",
        "treatment": ["No treatment required — continue standard tomato care."],
        "prevention": [
            "Practise crop rotation and use disease-free seed/transplants",
            "Stake, prune, and mulch for airflow and reduced soil splash",
            "Scout weekly for pests, nutritional deficiencies, and diseases",
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def get_disease_info(class_name: str) -> dict:
    """Look up disease info by raw class label; return a default if not found."""
    if class_name in DISEASE_INFO:
        return DISEASE_INFO[class_name]

    # Fallback — construct minimal entry from name
    parts = class_name.split("___")
    plant = parts[0].replace("_", " ")
    condition = parts[1].replace("_", " ").title() if len(parts) > 1 else "Unknown"
    return {
        "plant": plant,
        "disease": condition,
        "is_healthy": "healthy" in class_name.lower(),
        "symptoms": ["Information not available for this class."],
        "causes": "Information not available.",
        "treatment": ["Consult a local agricultural extension service."],
        "prevention": ["Practise good crop hygiene and regular scouting."],
    }

