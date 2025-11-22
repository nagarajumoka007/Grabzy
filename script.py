import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Grabzy.settings')
django.setup()

from home.models import Product, ProductFeatures
from django.utils.text import slugify

# Your product data
products = [
    

    {
        "id": "prod_04",
        "name": "Boldfit Full Face Helmet Mask",
        "image": "/images/products/Boldfit full face mask.jpg",
        "price": "226",
        "rating": 4.3,
        "company": "BoldFit",
        "category": "BikeAccessory",
        "about": [
            "FULL FACE MASK COVERAGE - A balaclava for men & women is a perfect accessory for bike riding, cycling, winter sports as a ski mask. It provides a full face coverage, keeping your face protected from high speeds when riding or other high-velocity sports. It even protects against the sun, pollution, dust and more.",
            "SOFT & STRETCHABLE FABRIC - Made from a soft fabric that covers the full face except the eyes. It can stretch over every head and face size to make for the perfect fit for men or women. The soft and stretchable fabric is incredibly breathable, facilitating all-day wear under your helmet, be it as a bike accessories, ski mask accessories or cycling accessories.",
            "ULTIMATE PROTECTION - The quick dry technology of the mask allows for all-day use and under all kinds of conditions. It provides wearers who use it as bike riding accessories, cycling accessories or ski mask accessories complete protection. You will be safe from harsh heat from the sun, dust, pollution and winter.",
            "MULTI-PURPOSE USE - Get your hands on this extremely versatile, multi-purpose use balaclava. This mask can be used as a bike riding gear, ski mask gear, cycling accessories by either men or women. It has a quick-dry and moisture wicking technology that keeps you comfortable. The full face mask coverage never fails to keep your protected from the elements when engaging in bike riding, cycling, skiing or more.",
            "EASY-TO WEAR AND WASH - The perfect under helmet full face mask that is super easy-to wear with no hassle. It can be easily washed multiple times without losing its softness and stretchability. It is the ultimate essential for bike riding, cycling, winter sports and more. Just wear it under the helmet and off you go."
        ],
        "features": {
            "productDimensions": "32 x 22 x 1 cm; 45 g",
            "dateFirstAvailable": "9 January 2023",
            "manufacturer": "Boldfit",
            "ASIN": "B0BRY84H2H",
            "itemModelNumber": "BalaclavaMaskBlack",
            "countryOfOrigin": "India",
            "department": "Women",
            "manufacturerFull": "Boldfit, Boldfit, Bangalore, 560041, support@boldfit.in, 08043702806",
            "packer": "Boldfit, Bangalore, 560041, support@boldfit.in, 08043702806",
            "importer": "Boldfit, Bangalore, 560041, support@boldfit.in, 08043702806",
            "itemWeight": "45 g",
            "itemDimensionsLxWxH": "32 x 22 x 1 Centimeters",
            "netQuantity": "1 count",
            "genericName": "BalaclavaMaskBlack"
        }
    },




    {
        "id": "prod_05",
        "name": "Royal Enfield Urban Hustler V2 Riding Gloves",
        "image": "/images/products/V2 Riding Gloves.jpg",
        "price": "1690",
        "rating": 4.3,
        "company": "Royal Enfield",
        "category": "BikeAccessory",
        "about": [
            "Material: Made with 100% Polyester Air Mesh for optimum ventilation Microsuede patch for added reinforcement and better grip",
            "Poly Stretch fabric for better flexibility and comfort",
            "Protection: TPR (Thermoplastic rubber) Knuckle protectors provide protection against impacts and abrasion 3mm Rubber sponge at palm for reinforcement",
            "Microsuede grip patch constructed with 50% polyamide & 50% polyurethane ensures secure and comfortable hold.",
            "WASH AND CARE INSTRUCTIONS: Dampen a paper towel or clean cloth Use a mild soap to create a lather with the cloth Rub the gloves with the cloth gently Use a clean, damp cloth to remove the soap and dirt Do not wash Do not iron the gloves Do not bleach the gloves Do not wring the gloves Do not place near any direct heat source or in the sun Dry in shade"
        ],
        "features": {
            "brandName": "Royal Enfield",
            "sportType": "Cycling",
            "gloveType": "Cycling",
            "hand": "Ambidextrous",
            "asin": "B0D81FNF8S",
            "importerContactInformation": "DYI CO.LTD.2FL ,KP.KRAJAN RT/RW 06/03 DS CIKOPO KEC,INDONESIA,41181",
            "itemTypeName": "Riding gloves",
            "whatsInTheBox": "1 Pair Riding Gloves",
            "itemHeight": "50 Millimeters",
            "manufacturer": "DYI CO LTD, DYI CO.LTD.2FL ,KP.KRAJAN RT/RW 06/03 DS CIKOPO KEC,INDONESIA,41181",
            "manufacturerContactInformation": "DYI CO.LTD.2FL ,KP.KRAJAN RT/RW 06/03 DS CIKOPO KEC,INDONESIA,41181",
            "packerContactInformation": "DYI CO.LTD.2FL ,KP.KRAJAN RT/RW 06/03 DS CIKOPO KEC,INDONESIA,41181",
            "unitCount": "1 Piece",
            "warrantyDescription": "6 months"
        }
    },

    {
        "id": "prod_06",
        "name": "TVS Racing Xplorer Riding Gloves",
        "image": "/images/products/TVS Gloves.jpg",
        "price": "1950",
        "rating": 4.1,
        "company": "TVS",
        "category": "BikeAccessory",
        "about": [
            "Tailored Comfort: Our gloves, designed with a blend of perforated Goat Nappa leather, faux leather, textiles with spandex, poly-corduroy fabric, and mesh, ensuring a comfortable and snug fit. This intricate design allows for effective internal climate control, making them the ideal riding gloves for long journeys.",
            "Robust Safety: While on the road, safety is paramount. These gloves for men riding come equipped with PVC and CARBON reinforced protection on the knuckles, palm, and fingers, ensuring you remain protected throughout your journey.",
            "Flex and Grip: The accordion construction on the fingers of these bike gloves promises unmatched flexibility, ensuring you maintain the perfect grip on every ride.",
            "Secure Wrist Closure: The hook and loop wrist closure system ensure that your bike riding gloves remain securely in place, allowing you to focus solely on the journey ahead.",
            "Stay Connected: In this digital age, our hand gloves for bike are touch screen compatible on the index finger, letting you stay connected without the hassle of removing your gloves."
        ],
        "features": {
            "brandName": "TVS",
            "sportType": "Motorcycle Racing",
            "gloveType": "Biking",
            "ageRangeDescription": "Adult",
            "hand": "Ambidextrous",
            "ASIN": "B0BQ6S798N",
            "importerContactInformation": "Harita accessories, Plot no 21-22, Sipcot industrial complex, Phase 1, Hosur TN , 635128",
            "itemTypeName": "Riding Gloves",
            "whatsInTheBox": "1 Pair of Gloves",
            "itemHeight": "50 Millimeters",
            "manufacturer": "Harita Accessories, Harita accessories, Plot no 21-22, Sipcot industrial complex, Phase 1, Hosur TN , 635128",
            "manufacturerContactInformation": "Harita accessories, Plot no 21-22, Sipcot industrial complex, Phase 1, Hosur TN , 635128",
            "packerContactInformation": "Harita accessories, Plot no 21-22, Sipcot industrial complex, Phase 1, Hosur TN , 635128",
            "unitCount": "1 Count"
        }
    },
    {
        "id": "prod_07",
        "name": "Vivo V60 5G",
        "image": "/images/products/Vivo V60 5G.jpg",
        "price": "38999",
        "rating": 4.2,
        "company": "VIVO",
        "category": "Mobiles",
        "about": [
            "[CAMERA]: Rear Camera: 50 MP Zeiss OIS Main Camera: OIS; f/1.88; FOV 84°; 6P lens, 50 MP Zeiss Super Telephoto Camera: AF; OIS, f/2.65, FoV 33.1°, 4P lens 10X Telephoto Stage Portrait, 8 MP ZEISS Ultra Wide-Angle camera: f2.0, FoV 120° ± 3, 5P lens | Front Camera: 50 MP ZEISS Group Selfie Camera: AF, f/2.2, FoV 92° ± 3°, 5P lens | 4K/1080P/720P Video Recording Resolution",
            "[SCREEN & DISPLAY]: 17.20 cm (6.77\" inch) Slim Quad Curved AMOLED capacitive multi-touch Display | P3 wide colour gamut supported | 387 ppi high pixel density | 5000 nits peak local brightness | certified by SGS for Low Blue Light | 2392 X 1080 resolution",
            "[MEMORY & SIM]: 12GB RAM | 512GB Internal Memory | LPDDR4X | UFS 2.2 | Bluetooth 5.4 | USB 2.0 | 5G + 5G Dual SIM Dual Standby",
            "[BATTERY]: 6500 mAh battery | Li-ion battery",
            "[FAST CHARGING]: 90W Flash Charge | USB 2.0",
            "[AI]: AI Personal Assistant (AI Captions & AI Smart Call Assistant) | Gemini- Connected Apps & Gemini Live",
            "[IP RATING]: Top-grade IP68 and IP69 water resistance allows being submerged in still fresh water up to 1.5 meters deep for up to 120 minutes"
        ],
        "features": {
            "operatingSystem": "Funtouch OS 15",
            "memoryStorageCapacity": "256 GB",
            "colour": "Moonlit Blue",
            "simCardSlotCount": "Dual SIM",
            "connectorType": "USB Type C",
            "formFactor": "Bar",
            "waterResistanceLevel": "Not Water Resistant",
            "flashMemorySupportedSizeMaximum": "256 GB"
        }
    },
    {
        "id": "prod_08",
        "name": "Redmi A3X",
        "image": "/images/products/Redmi A3X.jpg",
        "price": "6950",
        "rating": 4.8,
        "company": "Redmi",
        "category": "Mobiles",
        "about": [
            "High performance Octa Core Chipset | 6.71\" HD+ 90Hz Display with GG3 Protection | Upto 8GB RAM including 4GB Virtual RAM |128GB Storage | Fast Side fingerprint sensor"
        ],
        "features": {
            "operatingSystem": "Android 14",
            "ramMemoryInstalled": "4 GB",
            "processorSeries": "Snapdragon",
            "processorSpeed": "1.8 GHz",
            "memoryStorageCapacity": "128 GB",
            "colour": "Ocean Green",
            "simCardSlotCount": "Dual SIM",
            "connectorType": "USB Type C",
            "formFactor": "Bar",
            "biometricSecurityFeature": "Side Fingerprint sensor",
            "simCardSize": "Nano",
            "headphonesJack": "3.5 mm"
        }
    },


    {
        "id": "prod_09",
        "name": "POCO C61",
        "image": "/images/products/POCO C61.jpg",
        "price": "6999",
        "rating": 2.5,
        "company": "POCO",
        "category": "Mobiles",
        "about": [
            "High performance MediaTek Helio G36, upto 2.2GHz | 6.71\" HD+ 90Hz Display with GG3 Protection | Upto 8GB RAM including 4GB Virtual RAM | 64GB Storage | Fast Side fingerprint sensor",
            "Display: Large 17.04 cm 90Hz dot display with Corning Gorilla Glass 3 protection | 500nits peak brightness | 180Hz Touch sampling Rate",
            "Camera: 8MP AI Dual camera with Google lens, Portrait mode and classic film filters | 5MP Front camera",
            "5000mAh (typ) battery and 10W charger in-box with USB Type-C",
            "Expandable Storage upto 1TB with Dedicated MicroSD card Slot | 3.5mm headphone jack | Android 14 | Side fingerprint sensor | MIUI Dialer"
        ],
        "features": {
            "operatingSystem": "Android 14",
            "ramMemoryInstalled": "4 GB",
            "processorSeries": "Others",
            "processorSpeed": "2.2 GHz",
            "memoryStorageCapacity": "64 GB",
            "colour": "Diamond Dust",
            "simCardSlotCount": "Dual SIM",
            "connectorType": "USB Type C",
            "formFactor": "Bar",
            "biometricSecurityFeature": "Side Fingerprint sensor",
            "humanInterfaceTypes": ["Touchscreen"],
            "simCardSize": "Nano",
            "waterResistanceLevel": "Water Resistant",
            "headphonesJack": "3.5 mm"
        }
    },
    {
        "id": "prod_10",
        "name": "Apple iPhone 13",
        "image": "/images/products/Apple iphone 13.webp",
        "price": "43900",
        "rating": 3.5,
        "company": "Apple",
        "category": "Mobiles",
        "about": [
            "15 cm (6.1-inch) Super Retina XDR display",
            "Cinematic mode adds shallow depth of field and shifts focus automatically in your videos",
            "Advanced dual-camera system with 12MP Wide and Ultra Wide cameras; Photographic Styles, Smart HDR 4, Night mode, 4K Dolby Vision HDR recording",
            "12MP TrueDepth front camera with Night mode, 4K Dolby Vision HDR recording",
            "A15 Bionic chip for lightning-fast performance"
        ],
        "features": {
            "operatingSystem": "iOS 14",
            "processorSpeed": "3.23 GHz",
            "memoryStorageCapacity": "128 GB",
            "colour": "Midnight",
            "connectorType": "Lightning",
            "formFactor": "Smartphone",
            "biometricSecurityFeature": "Face Recognition",
            "simCardSize": "Nano",
            "materialFeatures": "plastic",
            "waterResistanceLevel": "Water Resistant"
        }
    },
    {
        "id": "prod_11",
        "name": "OnePlus Nord CE4 Lite 5G",
        "image": "/images/products/OnePlus Nord CE4.jpg",
        "price": "43900",
        "rating": 3.7,
        "company": "OnePlus",
        "category": "Mobiles",
        "about": [
            "5500 mAh Battery & Reverse Charging: Ditch the power bank and press play all day with Nord CE4 Lite’s gigantic 5,500 mAh battery. You’ll even have enough juice to charge up your buddy’s phone with reverse wired charging",
            "80W SUPERVOOC Fast Charging: Add excitement to your day with 80W SUPERVOOC fast charging, which fully replenishes the hefty battery in just 20 minutes, ensuring a day's worth of power in no time",
            "Superior snaps by Sony: Harness the power of the 50MP Sony LYT-600 main camera, bringing the capability to capture stunning Sony-quality photos and videos directly into your palm",
            "Boosted Battery Health: Battery Health Engine, with its smart AI and hardware combo, learns how you charge. It extends your battery life to 4 years, even with daily charges up to 80% or more. Easily track and adjust settings to get the most out of your phone",
            "Super Bright AMOLED Display: Dive into the world of bold colors and crisp visuals with 6.67 inch 120Hz AMOLED Display. No more squinting outdoors or running for shade with our super-bright display that comes with 2,100 nits peak brightness",
            "Dual Stereo Speakers: Experience an astonishing 300% increase in volume with the OnePlus Nord CE4 Lite’s dual stereo speakers. You won’t need earplugs, but you might need to apologize to your neighbors for the party vibes!",
            "AI Smart Cutout: Use AI Smart Cutout to swiftly edit photos, choose and personalize cutout selections, and share them with a single tap",
            "OxygenOS14: OxygenOS 14 isn’t just smarter—it’s designed to deliver sustained smoothness and security with guaranteed support for two major Android updates and three years of essential security updates"
        ],
        "features": {
            "operatingSystem": "OxygenOS",
            "ramMemoryInstalled": "8 GB",
            "processorSeries": "Snapdragon",
            "processorSpeed": "2.2 GHz",
            "memoryStorageCapacity": "128 GB",
            "colour": "Mega Blue",
            "simCardSlotCount": "Dual SIM",
            "formFactor": "Bar",
            "biometricSecurityFeature": "Fingerprint Recognition",
            "simCardSize": "Nano",
            "waterResistanceLevel": "Water Resistant",
            "headphonesJack": "3.5 mm"
        }
    },
    {
        "id": "prod_12",
        "name": "Handcrafted Wooden Wall Clock",
        "image": "/images/products/Handcrafted Wooden Wall Clock.webp",
        "price": "2499",
        "rating": 4.5,
        "company": "Crafted Elegance",
        "category": "Home Decoration",
        "about": [
            "Beautifully handcrafted wooden wall clock made from premium quality teak wood",
            "Silent sweep quartz movement ensures no ticking noise",
            "Perfect for living room, bedroom, office, or gifting purposes",
            "Elegant design with natural wood finish that complements modern and traditional interiors",
            "Eco-friendly polish with long-lasting shine"
        ],
        "features": {
            "material": "Teak Wood",
            "shape": "Round",
            "style": "Vintage",
            "weight": "1.2 kg",
            "dimensions": "12 x 12 inches",
            "batteryRequired": "1 AA Battery (not included)",
            "waterResistanceLevel": "Not Water Resistant"
        }
    },
    {
        "id": "prod_13",
        "name": "Decorative Ceramic Flower Vase",
        "image": "/images/products/Decorative Ceramic Flower Vase.webp",
        "price": "1899",
        "rating": 4.3,
        "company": "Urban Deco",
        "category": "Home Decoration",
        "about": [
            "Premium quality ceramic vase with glossy white finish",
            "Elegant design perfect for artificial or fresh flowers",
            "Adds a modern and stylish look to your living room or dining table",
            "Durable and easy to clean with a soft cloth",
            "Ideal as a housewarming or wedding gift"
        ],
        "features": {
            "material": "Ceramic",
            "shape": "Cylinder",
            "colour": "Glossy White",
            "weight": "950 g",
            "dimensions": "10 x 10 x 25 cm",
            "waterResistanceLevel": "Water Resistant"
        }
    },

    {
        "id": "prod_14",
        "name": "Handmade Cotton Macrame Wall Hanging",
        "image": "/images/products/Handmade Cotton Macrame.webp",
        "price": "1599",
        "rating": 4.6,
        "company": "Boho Living",
        "category": "Home Decoration",
        "about": [
            "Handwoven macrame wall hanging made with 100% cotton cord",
            "Adds a bohemian touch to your bedroom or living room decor",
            "Eco-friendly, lightweight, and durable",
            "Perfect for gifting or personal use",
            "Comes with a wooden dowel for easy hanging"
        ],
        "features": {
            "material": "Cotton",
            "style": "Bohemian",
            "colour": "Off White",
            "weight": "600 g",
            "dimensions": "40 x 90 cm",
            "waterResistanceLevel": "Not Water Resistant"
        }
    },
    {
        "id": "prod_15",
        "name": "Vintage Metal Table Lamp",
        "image": "/images/products/Vintage Metal Table Lamp.webp",
        "price": "3299",
        "rating": 4.7,
        "company": "BrightNest",
        "category": "Home Decoration",
        "about": [
            "Antique-style table lamp with fabric shade",
            "Adds elegance and warmth to your living room or study table",
            "Durable metal base with golden finish",
            "Compatible with E27 bulbs (not included)",
            "Perfect gift for festivals or home decor lovers"
        ],
        "features": {
            "material": "Metal & Fabric",
            "style": "Vintage",
            "colour": "Golden & Beige",
            "weight": "2.5 kg",
            "dimensions": "40 x 20 x 20 cm",
            "bulbRequired": "1 x E27 (not included)",
            "waterResistanceLevel": "Not Water Resistant"
        }
    },
    {
        "id": "prod_16",
        "name": "Framed Abstract Wall Art Painting",
        "image": "/images/products/Framed Abstract Wall Art Painting.webp",
        "price": "2799",
        "rating": 4.4,
        "company": "Artify",
        "category": "Home Decoration",
        "about": [
            "High-quality abstract painting printed on canvas with wooden frame",
            "Perfect for living room, office, or bedroom decor",
            "Adds a modern and artistic vibe to interiors",
            "Durable wooden frame ensures long-lasting quality",
            "Ready to hang with included wall mount"
        ],
        "features": {
            "material": "Canvas & Wood",
            "style": "Abstract",
            "colour": "Multicolor",
            "weight": "1.8 kg",
            "dimensions": "60 x 40 cm",
            "waterResistanceLevel": "Not Water Resistant"
        }
    },
    {
        "id": "prod_17",
        "name": "Decorative LED String Lights",
        "image": "/images/products/Decorative LED String Lights.webp",
        "price": "1299",
        "rating": 4.8,
        "company": "GlowCraft",
        "category": "Home Decoration",
        "about": [
            "20-meter long LED string lights with warm white glow",
            "Perfect for festivals, parties, and everyday home decoration",
            "Energy-efficient and long-lasting LED bulbs",
            "Flexible wire for easy installation indoors or outdoors",
            "Safe, eco-friendly, and stylish decorative lighting"
        ],
        "features": {
            "material": "Copper Wire & Plastic",
            "style": "Modern",
            "colour": "Warm White",
            "length": "20 meters",
            "powerSource": "Electric (Plug-in)",
            "waterResistanceLevel": "Water Resistant"
        }
    },
    {
        "id": "prod_18",
        "name": "boAt Airdopes 141 Bluetooth TWS Earbuds",
        "image": "/images/products/boAt Airdopes 141.webp",
        "price": "1499",
        "rating": 4.2,
        "company": "boAt",
        "category": "Mobile Accessories",
        "about": [
            "Enjoy up to 42 hours of playtime with ASAP fast charging that gives 75 minutes of playtime in just 5 minutes of charge.",
            "Immerse yourself in boAt Signature Sound with 8mm drivers delivering immersive audio.",
            "Equipped with ENx technology for crystal clear calls.",
            "IWP technology ensures instant connection the moment you open the case lid.",
            "IPX4 water & sweat resistance makes it perfect for workouts."
        ],
        "features": {
            "connectorType": "Bluetooth 5.0",
            "formFactor": "In-Ear",
            "waterResistanceLevel": "IPX4",
            "batteryLife": "42 Hours",
            "chargingPort": "Type C",
            "color": "Bold Black"
        }
    },
    {
        "id": "prod_19",
        "name": "Samsung 25W USB Type-C Fast Charger Adapter",
        "image": "/images/products/Samsung 25W USB Type-C.webp",
        "price": "1299",
        "rating": 4.5,
        "company": "Samsung",
        "category": "Mobile Accessories",
        "about": [
            "Super-fast charging up to 25W for compatible devices.",
            "Compact and lightweight design, ideal for travel.",
            "Universal compatibility with Type-C enabled devices.",
            "Adaptive Fast Charging ensures safe and efficient charging.",
            "Official Samsung accessory for long-lasting performance."
        ],
        "features": {
            "connectorType": "USB Type-C",
            "powerOutput": "25W",
            "compatibility": "All USB-C Devices",
            "color": "White",
            "weight": "70g"
        }
    },
    {
        "id": "prod_20",
        "name": "Mi 10000mAh Power Bank 3i (Midnight Black)",
        "image": "/images/products/Mi 10000mAh Power Bank.webp",
        "price": "999",
        "rating": 4.3,
        "company": "Mi",
        "category": "Mobile Accessories",
        "about": [
            "High-capacity 10000mAh Lithium Polymer battery.",
            "Dual input with Type-C and Micro-USB ports.",
            "Supports 18W fast charging.",
            "Dual output with two USB-A ports for charging multiple devices.",
            "Advanced 12-layer chip protection ensures safety against overheating and overcharging."
        ],
        "features": {
            "capacity": "10000 mAh",
            "inputPorts": "Type-C, Micro USB",
            "outputPorts": "Dual USB-A",
            "fastCharging": "18W",
            "weight": "251g",
            "color": "Midnight Black"
        }
    },
    {
        "id": "prod_21",
        "name": "Spigen Liquid Air Armor Case for iPhone 14 (Matte Black)",
        "image": "/images/products/Spigen Liquid Air Armor Case for iPhone 14.webp",
        "price": "1599",
        "rating": 4.6,
        "company": "Spigen",
        "category": "Mobile Accessories",
        "about": [
            "Made with flexible TPU for a slim and lightweight fit.",
            "Air Cushion Technology for shock absorption.",
            "Matte black finish with anti-fingerprint texture.",
            "Raised bezels to protect screen and camera.",
            "Precise cutouts for easy access to all buttons and ports."
        ],
        "features": {
            "compatibleDevices": "iPhone 14",
            "material": "TPU",
            "color": "Matte Black",
            "formFactor": "Back Cover",
            "protection": "Shock Absorption"
        }
    },
    {
        "id": "prod_22",
        "name": "Noise ColorFit Pulse 2 Max Smartwatch (Jet Black)",
        "image": "/images/products/Noise ColorFit Pulse 2 Max Smartwatch.webp",
        "price": "2499",
        "rating": 4.1,
        "company": "Noise",
        "category": "Mobile Accessories",
        "about": [
            "Massive 1.85” TFT display with 550 nits brightness.",
            "Bluetooth calling with quick dial pad.",
            "150+ cloud-based watch faces.",
            "100 sports modes and SpO2 monitoring.",
            "Up to 10 days of battery life."
        ],
        "features": {
            "displaySize": "1.85 inch",
            "connectivity": "Bluetooth Calling",
            "sportsModes": "100+",
            "batteryLife": "10 Days",
            "color": "Jet Black",
            "waterResistanceLevel": "IP68"
        }
    },
    {
        "id": "prod_23",
        "name": "SanDisk Ultra 128GB microSDXC UHS-I Card",
        "image": "/images/products/SanDisk Ultra 128GB.webp",
        "price": "1099",
        "rating": 4.4,
        "company": "SanDisk",
        "category": "Mobile Accessories",
        "about": [
            "High-performance 128GB microSD card with read speeds up to 120MB/s.",
            "Ideal for Android smartphones and tablets.",
            "A1-rated for faster app performance.",
            "Full HD video recording and playback supported.",
            "Durable: waterproof, temperature-proof, shockproof, and X-ray-proof."
        ],
        "features": {
            "storageCapacity": "128 GB",
            "readSpeed": "120 MB/s",
            "applicationPerformance": "A1 Rated",
            "compatibility": "Smartphones, Tablets",
            "durability": "Waterproof, Shockproof"
        }
    }

]

# Save products to database
for item in products:
    name = item['name']
    price = float(item['price'])
    rating = float(item['rating'])
    image = item['image']
    description = "\n".join(item['about'])
    print(name, price)

    p = Product.objects.get(name = name)
    p.rating = rating
    p.save()

    # product = Product.objects.update(
    #     rating=rating
    # )

#     print(name, price, rating, description.strip(), sep='\n')

#     for feature, value in item['features'].items():
#         ProductFeatures.objects.create(
#             product=product,
#             feature=feature,
#             feature_value=value
#         )
#         print(feature, value)

# # Add slugs to products
# for prod in Product.objects.all():
#     prod.slug = slugify(prod.name)
#     prod.save()
#     print(prod.slug)
