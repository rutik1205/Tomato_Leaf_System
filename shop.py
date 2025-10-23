import streamlit as st
from google_translate import translations

def Shop(lang_code) :

    t = translations[lang_code]

    st.title ( t["shop-page"] )
    st.write ( t["shop-description"] )

    general_solutions = [
        {
            'name' : {
                "en" : "Bacterial Speck & Spot Treatment (Agri-mycin)",
                "hi" : "बैक्टीरियल स्पेक और स्पॉट ट्रीटमेंट (एग्री-मायसिन)",
                "mr" : "बॅक्टेरियल स्पेक आणि स्पॉट ट्रीटमेंट (अ‍ॅग्री-मायसिन)"
            },
            'price' : '₹1588.17',
            'image' : './image/Agri_mycin.jpg',
            'usage' : {
                "en" : "Use Agri-mycin to control bacterial speck and spot. Apply as a foliar spray.",
                "hi" : "बैक्टीरियल स्पेक और स्पॉट को नियंत्रित करने के लिए एग्री-मायसिन का उपयोग करें। इसे फोलियर स्प्रे के रूप में लगाएं।",
                "mr" : "बॅक्टेरियल स्पेक आणि स्पॉट नियंत्रित करण्यासाठी अ‍ॅग्री-मायसिन वापरा. फोलियर स्प्रे म्हणून लागू करा."
            },
            'payment_link' : 'https://example.com/payment/Agri-mycin'
        },
        {
            'name' : {
                "en" : "Copper Tank-mixed with Mancozeb",
                "hi" : "कॉपर टैंक-मिश्रण मैनकोजेब के साथ",
                "mr" : "कॉपर टँक-मिश्रण मँकोझेब सह"
            },
            'price' : '₹1877.50',
            'image' : './image/Mancozeb.jpg',
            'usage' : {
                "en" : "Copper-based pesticide combined with Mancozeb for controlling various fungal and bacterial diseases.",
                "hi" : "तांबे-आधारित कीटनाशक मैनकोजेब के साथ मिलाकर विभिन्न फंगल और बैक्टीरियल रोगों को नियंत्रित करता है।",
                "mr" : "तांबे-आधारित कीटकनाशक मँकोझेबसह मिसळून विविध बुरशीजन्य आणि जिवाणूजन्य रोग नियंत्रित करतो."
            },
            'payment_link' : 'https://example.com/payment/Mancozeb'
        },
        {
            'name' : {
                "en" : "Damping-Off Treatment (Previcur Flex)",
                "hi" : "डैंपिंग-ऑफ उपचार (प्रेविक्यूर फ्लेक्स)",
                "mr" : "डॅंपिंग-ऑफ उपचार (प्रेविक्यूर फ्लेक्स)"
            },
            'price' : '₹1992.00',
            'image' : './image/Previcur Flex.jpg',
            'usage' : {
                "en" : "Apply Previcur Flex as a directed spray to lower stems and soil for controlling damping-off caused by Pythium.",
                "hi" : "पायथियम के कारण होने वाले डैंपिंग-ऑफ को नियंत्रित करने के लिए प्रेविक्यूर फ्लेक्स को निचले तनों और मिट्टी पर स्प्रे करें।",
                "mr" : "पायथियममुळे होणाऱ्या डॅंपिंग-ऑफला नियंत्रित करण्यासाठी प्रेविक्यूर फ्लेक्सला खालच्या देठांवर आणि मातीत फवारणी करा."
            },
            'payment_link' : 'https://example.com/payment/Previcur-Flex'
        },
        {
            'name' : {
                "en" : "Damping-Off (Ranman)",
                "hi" : "डैंपिंग-ऑफ (रैनमैन)",
                "mr" : "डॅंपिंग-ऑफ (रॅनमन)"
            },
            'price' : '₹2199.50',
            'image' : './image/Ranman.jpg',
            'usage' : {
                "en" : "Apply Ranman as a drench to seeding trays anytime from seeding to 1 week before transplanting for damping-off control.",
                "hi" : "बीज रोपण से एक सप्ताह पहले तक डैंपिंग-ऑफ नियंत्रण के लिए बीज ट्रे पर रैनमैन को ड्रेंच करें।",
                "mr" : "डॅंपिंग-ऑफ नियंत्रणासाठी रोपांची ट्रे भिजवण्यासाठी रोपणापासून 1 आठवडा आधी रॅनमन लागू करा."
            },
            'payment_link' : 'https://example.com/payment/Ranman'
        },
        {
            'name' : {
                "en" : "Gray Mold Control (Botrytis) Treatment",
                "hi" : "ग्रे फफूंदी नियंत्रण (बोट्राइटिस) उपचार",
                "mr" : "ग्रे बुरशी नियंत्रण (बोट्रायटिस) उपचार"
            },
            'price' : '₹1642.25',
            'image' : './image/Botrytis.jpg',
            'usage' : {
                "en" : "Use fungicides specifically designed for gray mold (Botrytis) control on tomatoes.",
                "hi" : "टमाटर में ग्रे फफूंदी (बोट्राइटिस) नियंत्रण के लिए विशेष रूप से डिज़ाइन किए गए कवकनाशी का उपयोग करें।",
                "mr" : "टोमॅटोमध्ये ग्रे बुरशी (बोट्रायटिस) नियंत्रणासाठी विशेषतः डिझाइन केलेले बुरशीनाशक वापरा."
            },
            'payment_link' : 'https://example.com/payment/Botrytis'
        },
        {
            'name' : {
                "en" : "Powdery Mildew Treatment (Sulfur-based Fungicide)",
                "hi" : "पाउडरी मिल्ड्यू उपचार (सल्फर-आधारित कवकनाशी)",
                "mr" : "पावडरी मिल्ड्यू उपचार (सल्फर-आधारित बुरशीनाशक)"
            },
            'price' : '₹1270.90',
            'image' : './image/Sulfur-based Fungicide.jpg',
            'usage' : {
                "en" : "Sulfur-based fungicides to control powdery mildew and other fungal diseases.",
                "hi" : "पाउडरी मिल्ड्यू और अन्य फंगल रोगों को नियंत्रित करने के लिए सल्फर-आधारित कवकनाशी।",
                "mr" : "पावडरी मिल्ड्यू आणि इतर बुरशीजन्य रोग नियंत्रित करण्यासाठी सल्फर-आधारित बुरशीनाशके."
            },
            'payment_link' : 'https://example.com/payment/Sulfur-based-Fungicide'
        },
        {
            'name' : {
                "en" : "Chlorothalonil for Early Blight",
                "hi" : "प्रारंभिक ब्लाइट के लिए क्लोरोथालोनिल",
                "mr" : "लवकर ब्लाइटसाठी क्लोरोथालोनिल"
            },
            'price' : '₹1701.50',
            'image' : './image/Chlorothalonil.jpg',
            'usage' : {
                "en" : "Effective for controlling early blight and other fungal diseases like leaf spot caused by Alternaria solani.",
                "hi" : "प्रारंभिक ब्लाइट और अन्य फंगल रोगों को नियंत्रित करने के लिए प्रभावी, जैसे अल्टरनेरिया सोलानी द्वारा लीफ स्पॉट।",
                "mr" : "लवकर ब्लाइट आणि अल्टरनेरिया सोलानीमुळे होणाऱ्या पानांवरील डागासारख्या इतर बुरशीजन्य रोग नियंत्रित करण्यासाठी प्रभावी."
            },
            'payment_link' : 'https://example.com/payment/Chlorothalonil'
        },

        {
            'name' : {
                "en" : "Mancozeb for Late Blight",
                "hi" : "लेट ब्लाइट के लिए मैंकोज़ेब",
                "mr" : "लेट ब्लाइटसाठी मॅनकोझेब"
            },
            'price' : '₹1743.00',
            'image' : './image/Mancozeb2.jpg',
            'usage' : {
                "en" : "Broad-spectrum fungicide that controls late blight, anthracnose, and other fungal diseases in tomatoes.",
                "hi" : "लेट ब्लाइट, एन्थ्राक्नोज और अन्य फंगल रोगों को नियंत्रित करने वाला व्यापक स्पेक्ट्रम कवकनाशी।",
                "mr" : "लेट ब्लाइट, अँथ्रॅक्नोज आणि टोमॅटोवरील इतर बुरशीजन्य रोग नियंत्रित करणारे व्यापक स्पेक्ट्रम बुरशीनाशक."
            },
            'payment_link' : 'https://example.com/payment/Mancozeb'
        },
        {
            'name' : {
                "en" : "Copper-based Fungicides for Leaf Spot",
                "hi" : "लीफ स्पॉट के लिए कॉपर-आधारित कवकनाशी",
                "mr" : "लीफ स्पॉटसाठी कॉपर-आधारित बुरशीनाशक"
            },
            'price' : '₹1618.50',
            'image' : './image/Copper Fungicides.jpg',
            'usage' : {
                "en" : "Effective against fungal and bacterial diseases like septoria leaf spot and bacterial wilt.",
                "hi" : "सेप्टोरिया लीफ स्पॉट और बैक्टीरियल विल्ट जैसे फंगल और बैक्टीरियल रोगों के खिलाफ प्रभावी।",
                "mr" : "सेप्टोरिया लीफ स्पॉट आणि बॅक्टेरियल विल्ट यांसारख्या बुरशीजन्य आणि जीवाणूजन्य रोगांवर प्रभावी."
            },
            'payment_link' : 'https://example.com/payment/Copper-Fungicides'
        },
        {
            'name' : {
                "en" : "Avid (Acaricide) for Spider Mites",
                "hi" : "स्पाइडर माइट्स के लिए एविड (अकारिसाइड)",
                "mr" : "स्पायडर माइट्ससाठी एविड (अॅकारिसाइड)"
            },
            'price' : '₹2241.00',
            'image' : './image/Acaricide.jpg',
            'usage' : {
                "en" : "Used to control spider mites, which are common pests on tomato plants.",
                "hi" : "टमाटर के पौधों पर पाए जाने वाले आम कीट स्पाइडर माइट्स को नियंत्रित करने के लिए उपयोग किया जाता है।",
                "mr" : "टोमॅटोच्या झाडांवर आढळणाऱ्या सामान्य किडींपैकी स्पायडर माइट्स नियंत्रित करण्यासाठी वापरले जाते."
            },
            'payment_link' : 'https://example.com/payment/Acaricide'
        },
        {
            'name' : {
                "en" : "Onager (Acaricide) for Spider Mites",
                "hi" : "स्पाइडर माइट्स के लिए ओनागर (अकारिसाइड)",
                "mr" : "स्पायडर माइट्ससाठी ओनागर (अॅकारिसाइड)"
            },
            'price' : '₹2407.00',
            'image' : './image/Onager.jpg',
            'usage' : {
                "en" : "Effective for controlling spider mites and other related pests on tomato plants.",
                "hi" : "स्पाइडर माइट्स और अन्य संबंधित कीटों को नियंत्रित करने के लिए प्रभावी।",
                "mr" : "स्पायडर माइट्स आणि इतर संबंधित किडी नियंत्रित करण्यासाठी प्रभावी."
            },
            'payment_link' : 'https://example.com/payment/Onager'
        },
        {
            'name' : {
                "en" : "Neem Oil for Insect Control",
                "hi" : "कीट नियंत्रण के लिए नीम का तेल",
                "mr" : "किड नियंत्रणासाठी नीम तेल"
            },
            'price' : '₹1334.17',
            'image' : './image/Neem Oil.jpg',
            'usage' : {
                "en" : "Organic pesticide effective against aphids, whiteflies, and other insects, as well as fungal infections like powdery mildew.",
                "hi" : "एफिड्स, व्हाइटफ्लाइज और अन्य कीटों के खिलाफ प्रभावी जैविक कीटनाशक, साथ ही पाउडरी मिल्ड्यू जैसी फंगल संक्रमण को भी नियंत्रित करता है।",
                "mr" : "एफिड्स, व्हाइटफ्लाय आणि इतर किडींवर प्रभावी असलेले सेंद्रिय कीटकनाशक, तसेच पावडरी मिल्ड्यूसारख्या बुरशीजन्य संसर्गावर प्रभावी."
            },
            'payment_link' : 'https://example.com/payment/Neem-Oil'
        },
        {
            'name' : {
                "en" : "Cow Dung (Organic Fertilizer)",
                "hi" : "गाय का गोबर (जैविक उर्वरक)",
                "mr" : "गाईचे शेण (सेंद्रिय खत)"
            },
            'price' : '₹500.00',
            'image' : './image/Cow Dung.jpg',
            'usage' : {
                "en" : "Use as an organic fertilizer for tomato plants to improve soil health and growth.",
                "hi" : "मिट्टी के स्वास्थ्य और वृद्धि में सुधार के लिए टमाटर के पौधों के लिए जैविक उर्वरक के रूप में उपयोग करें।",
                "mr" : "मातीचे आरोग्य आणि वाढ सुधारण्यासाठी टोमॅटोच्या झाडांसाठी सेंद्रिय खत म्हणून वापरा."
            },
            'payment_link' : 'https://example.com/payment/Cow-Dung'
        },
        {
            'name' : {
                "en" : "Organic Fertilizer",
                "hi" : "जैविक उर्वरक",
                "mr" : "सेंद्रिय खत"
            },
            'price' : '₹750.00',
            'image' : './image/Organic Fertilizer.jpg',
            'usage' : {
                "en" : "Use as an organic fertilizer to boost tomato plant growth and yield.",
                "hi" : "टमाटर के पौधों की वृद्धि और उपज बढ़ाने के लिए जैविक उर्वरक के रूप में उपयोग करें।",
                "mr" : "टोमॅटोच्या झाडांची वाढ आणि उत्पादन वाढवण्यासाठी सेंद्रिय खत म्हणून वापरा."
            },
            'payment_link' : 'https://example.com/payment/Organic-Fertilizer'
        },
        {
            'name' : {
                "en" : "Premium Cow Dung Fertilizer",
                "hi" : "प्रीमियम गाय का गोबर उर्वरक",
                "mr" : "प्रीमियम गाईचे शेण खत"
            },
            'price' : '₹600.00',
            'image' : './image/Premium Cow Dung.jpg',
            'usage' : {
                "en" : "Premium quality cow dung fertilizer for enriching soil, improving plant health, and increasing tomato yields.",
                "hi" : "मिट्टी को समृद्ध करने, पौधों के स्वास्थ्य को सुधारने और टमाटर की उपज बढ़ाने के लिए प्रीमियम गुणवत्ता वाला गाय का गोबर उर्वरक।",
                "mr" : "माती समृद्ध करण्यासाठी, वनस्पतींचे आरोग्य सुधारण्यासाठी आणि टोमॅटोच्या उत्पादनासाठी प्रीमियम गुणवत्ता असलेले गाईचे शेण खत."
            },
            'payment_link' : 'https://example.com/payment/Premium-Cow-Dung'
        }
    ]

    row1_col1, row1_col2, row1_col3 = st.columns ( 3 )
    row2_col1, row2_col2, row2_col3 = st.columns ( 3 )
    row3_col1, row3_col2, row3_col3 = st.columns ( 3 )
    row4_col1, row4_col2, row4_col3 = st.columns ( 3 )
    row5_col1, row5_col2, row5_col3 = st.columns ( 3 )

    with row1_col1 :
        st.image ( general_solutions[0]['image'], width=250 )
        st.write ( f"**{general_solutions[0]['name'][lang_code]}**" )
        st.write ( f"**{t['price']}:** {general_solutions[0]['price']}" )
        st.write ( f"**{t['usage']}:** {general_solutions[0]['usage'][lang_code]}" )


    with row1_col2 :
        st.image ( general_solutions[1]['image'], width=250 )
        st.write ( f"**{general_solutions[1]['name'][lang_code]}**" )
        st.write ( f"**{t['price']}:** {general_solutions[1]['price']}" )
        st.write ( f"**{t['usage']}:** {general_solutions[1]['usage'][lang_code]}" )


    with row1_col3 :
        st.image ( general_solutions[2]['image'], width=250 )
        st.write ( f"**{general_solutions[2]['name'][lang_code]}**" )
        st.write ( f"**{t['price']}:** {general_solutions[2]['price']}" )
        st.write ( f"**{t['usage']}:** {general_solutions[2]['usage'][lang_code]}" )


    with row2_col1 :
        st.image ( general_solutions[3]['image'], width=250 )
        st.write ( f"**{general_solutions[3]['name'][lang_code]}**" )
        st.write ( f"**{t['price']}:** {general_solutions[3]['price']}" )
        st.write ( f"**{t['usage']}:** {general_solutions[3]['usage'][lang_code]}" )

    with row2_col2 :
        st.image ( general_solutions[4]['image'], width=250 )
        st.write ( f"**{general_solutions[4]['name'][lang_code]}**" )
        st.write ( f"**{t['price']}:** {general_solutions[4]['price']}" )
        st.write ( f"**{t['usage']}:** {general_solutions[4]['usage'][lang_code]}" )

    with row2_col3 :
        st.image ( general_solutions[5]['image'], width=250 )
        st.write ( f"**{general_solutions[5]['name'][lang_code]}**" )
        st.write ( f"**{t['price']}:** {general_solutions[5]['price']}" )
        st.write ( f"**{t['usage']}:** {general_solutions[5]['usage'][lang_code]}" )


    with row3_col1 :
        st.image ( general_solutions[6]['image'], width=250 )
        st.write ( f"**{general_solutions[6]['name'][lang_code]}**" )
        st.write ( f"**{t['price']}:** {general_solutions[6]['price']}" )
        st.write ( f"**{t['usage']}:** {general_solutions[6]['usage'][lang_code]}" )


    with row3_col2 :
        st.image ( general_solutions[7]['image'], width=250 )
        st.write ( f"**{general_solutions[7]['name'][lang_code]}**" )
        st.write ( f"**{t['price']}:** {general_solutions[7]['price']}" )
        st.write ( f"**{t['usage']}:** {general_solutions[7]['usage'][lang_code]}" )


    with row3_col3 :
        st.image ( general_solutions[8]['image'], width=250 )
        st.write ( f"**{general_solutions[8]['name'][lang_code]}**" )
        st.write ( f"**{t['price']}:** {general_solutions[8]['price']}" )
        st.write ( f"**{t['usage']}:** {general_solutions[8]['usage'][lang_code]}" )


    with row4_col1 :
        st.image ( general_solutions[9]['image'], width=250 )
        st.write ( f"**{general_solutions[9]['name'][lang_code]}**" )
        st.write ( f"**{t['price']}:** {general_solutions[9]['price']}" )
        st.write ( f"**{t['usage']}:** {general_solutions[9]['usage'][lang_code]}" )


    with row4_col2 :
        st.image ( general_solutions[10]['image'], width=250 )
        st.write ( f"**{general_solutions[10]['name'][lang_code]}**" )
        st.write ( f"**{t['price']}:** {general_solutions[10]['price']}" )
        st.write ( f"**{t['usage']}:** {general_solutions[10]['usage'][lang_code]}" )


    with row4_col3 :
        st.image ( general_solutions[11]['image'], width=250 )
        st.write ( f"**{general_solutions[11]['name'][lang_code]}**" )
        st.write ( f"**{t['price']}:** {general_solutions[11]['price']}" )
        st.write ( f"**{t['usage']}:** {general_solutions[11]['usage'][lang_code]}" )


    with row5_col1 :
        st.image ( general_solutions[12]['image'], width=250 )
        st.write ( f"**{general_solutions[12]['name'][lang_code]}**" )
        st.write ( f"**{t['price']}:** {general_solutions[12]['price']}" )
        st.write ( f"**{t['usage']}:** {general_solutions[12]['usage'][lang_code]}" )


    with row5_col2 :
        st.image ( general_solutions[13]['image'], width=250 )
        st.write ( f"**{general_solutions[3]['name'][lang_code]}**" )
        st.write ( f"**{t['price']}:** {general_solutions[13]['price']}" )
        st.write ( f"**{t['usage']}:** {general_solutions[13]['usage'][lang_code]}" )


    with row5_col3 :
        st.image ( general_solutions[14]['image'], width=250 )
        st.write ( f"**{general_solutions[14]['name'][lang_code]}**" )
        st.write ( f"**{t['price']}:** {general_solutions[14]['price']}" )
        st.write ( f"**{t['usage']}:** {general_solutions[14]['usage'][lang_code]}" )


