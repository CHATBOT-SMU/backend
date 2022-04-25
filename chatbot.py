
from nltk.chat.util import Chat, reflections

building = [
    ['my name is (.*)', ['Hi %1 , I am the SMU chatbot Ezzdine']],
    ['(hi|hello|hey|holla|hola)', ['Hey there', 'Hi there', 'Hey, how may I help you today?']],
    ['(.*)(help)(.*)', ['In the Building section you can ask about the following topics:\n- Teachers offices\n- Administration\n- Other locations\n- Contact']],
    ['(.*)(Teachers offices|offices)(.*)', ['Please type the name of the professor']],
    ['(.*)(Administration)(.*)', ['Please type the name of the administrator']],
    ['(.*)(Other locations|Other location|location)(.*)', ['Please type the exact name of the location needed (e.g.,Maker space, Student life, Finance department)']],
    ['(.*)(Marwa Amri)(.*)', ['The office of Ms Marwa Amri is B-208']],
    ['(.*)(Cyrine Turki)(.*)', ['The office of Ms Cyrine Turki is B-208']],
    ['(.*)(Mohamed Amine Mbarek)(.*)', ['The office of Mr Mohamed Amine Mbarek is B-208']],
    ['(.*)(Imed Hammouda)(.*)', ['The office of the Dean Imed Hammouda is B-209']],
    ['(.*)(Nurse)(.*)', ['You can find the Nurse is M.A01']],
    ['(.*)(Mohamed Zoghlemi)(.*)', ['The office of Mr Mohamed Zoghlemi is A001, at the entry of MSB']],
    ['(.*)(Sana Chaieb)(.*)', ['The office of Ms Sana Chaieb is B-208']],
    ['(.*)Noura Baccar(.*)', ['The office of Ms Noura Baccar is B-201, located on the second floor of Medtech building']],
    ['(.*)(Heger Arfaoui)(.*)', ['The office of Ms Heger Arfaoui is B-212']],
    ['(.*)(Salma Hamza)(.*)', ['The office of Ms Salma Hamza is B-212']],
    ['(.*)(Hanen Ahmadi)(.*)', ['The office of Ms Hanen Ahmadi is B-201']],
    ['(.*)(Yasmine Guefrachi)(.*)', ['The office of Ms Yasmine Guefrachi is B-205 BIS']],
    ['(.*)(Leila Costel)(.*)', ['The office of Ms Leila Costel is B-205 BIS']],
    ['(.*)(Rim Gouia Zarrad)(.*)', ['The office of Ms Rim Gouia Zarrad is B-203']],
    ['(.*)(Syrine Ben Meskina)(.*)', ['The office of Ms Syrine Ben Meskina is B-203']],
    ['(.*)(Amina Mseddi)(.*)', ['The office of Ms Amina Mseddi is B-414']],
    ['(.*)(Nadia Ben Youssef)(.*)', ['The office of Ms Nadia Ben Youssef is B-414']],
    ['(.*)(Rim Gharbi)(.*)', ['The office of Ms Rim Gharbi is B-421']],
    ['(.*)(Jihen Bennaceur)(.*)', ['The office of Ms Jihen Bennaceur is B-421']],
    ['(.*)(Houda Nsir)(.*)', ['The office of Ms Houda Nsir is B-214']],
    ['(.*)(Lamia Bouaziz)(.*)', ['The office of Ms Lamia Bouaziz is B-214']],
    ['(.*)(Said Eddine Mannai)(.*)', ['The office of Mr Said Eddine Mannai is B-215']],
    ['(.*)(Wajdi Ben Slama)(.*)', ['The office of Mr Wajdi Ben Slama is B-215']],
    ['(.*)(Nejib Chennoufi)(.*)', ['The office of Mr Nejib Chennoufi is B-215']],
    ['(.*)(Mohamed Amine Ben Sassi)(.*)', ['The office of Mr Mohamed Amine Ben Sassi is B-215']],
    ['(.*)(Asma Amdouni)(.*)', ['The office of Ms Asma Amdouni is B-205']],
    ['(.*)(Karama Jeribi)(.*)', ['The office of Ms Karama Jeribi is B-205']],
    ['(.*)(Dorra Louti)(.*)', ['The office of Ms Dorra Louti is B-205']],
    ['(.*)(Hassen Hamrouni)(.*)', ['The office of Mr Hassen Hamrouni is A203 BIS']],
    ['(.*)(Sofien Sahraoui)(.*)', ['The office of Mr Sofien Sahraoui is A204 BIS']],
    ['(.*)(Maha Chaieb)(.*)', ['The office of Ms Maha Chaieb is A406']],
    ['(.*)(Achref Kloula)(.*)', ['The office of Mr Achref Kloula is A001']],
    ['(.*)(Aycha Elouni)(.*)', ['The office of Ms Aycha Elouni is A001']],
    ['(.*)(Kolthoum Mezlini)(.*)', ['The office of Ms Kolthoum Mezlini is A004']],
    ['(.*)(Hanen Ben Aicha)(.*)', ['The office of Ms Hanen Ben Aicha is CM007']],
    ['(.*)(Ameni Ganzouai)(.*)', ['The office of Ms Ameni Ganzouai is CM007']],
    ['(.*)(Ikram Milad)(.*)', ['The office of Ms Ikram Milad is CM006']],
    ['(.*)(Sofia Bahri)(.*)', ['The office of Ms Sofia Bahri is CM006']],
    ['(.*)(Salma Sghairi)(.*)', ['The office of Ms Salma Sghairi is C003']],
    ['(.*)(Maleke Fourati)(.*)', ['The office of Ms Maleke Fourati is 306 BIS']],
    ['(.*)(Ilyess Mechlaoui)(.*)', ['The office of Ms Ilyess Mechlaoui is B-103']],
    ['(.*)(Dorra Abidi)(.*)', ['The office of Ms Dorra Abidi is 306 BIS']],
    ['(.*)(Leila Becha)(.*)', ['The office of Ms Leila Becha is A-301']],
    ['(.*)(Zied Khabtheni)(.*)', ['The office of Mr Zied Khabtheni is A-302']],
    ['(.*)(Lamia Ben Fdhila)(.*)', ['The office of Ms Lamia Ben Fdhila is A-303']],
    ['(.*)(Mohamed Fadhel Djlassi)(.*)', ['The office of Mr Mohamed Fadhel Djlassi is B-415']],
    ['(.*)(Abdelaziz Fourati)(.*)', ['The office of Mr Abdelaziz Fourati is B-415']],
    ['(.*)(Fatma Abdelkaoui)(.*)', ['The office of Ms Fatma Abdelkaoui is B-304']],
    ['(.*)(Mouna Sammoud)(.*)', ['The office of Ms Mouna Sammoud is B-304']],
    ['(.*)(Mouhamed Mahjouib)(.*)', ['The office of Mr Mouhamed Mahjouib is B-302']],
    ['(.*)(Mawa Khadrani)(.*)', ['The office of Ms Mawa Khadrani is B-302']],
    ['(.*)(Nizar Hichri)(.*)', ['The office of Mr Nizar Hichri is B-301']],
    ['(.*)(Wissem Aloui)(.*)', ['The office of Mr Wissem Aloui is B-301']],
    ['(.*)(Mike Watson)(.*)', ['The office of Mr Mike Watson is B-407 BIS']],
    ['(.*)(Amin Dridi)(.*)', ['The office of Mr Amin Dridi is B-408']],
    ['(.*)(Imed Souid)(.*)', ['The office of Mr Imed Souid is CM005']],
    ['(.*)(Ezzdine Righi)(.*)', ['The office of Mr Ezzdine Righi is CM005']],
    ['(.*)(Dorra Ben Hmida)(.*)', ['The office of Ms Dorra Ben Hmida is A102']],
    ['(.*)(Amira Elhichri)(.*)', ['The office of Ms Amira Elhichri is A102']],
    ['(.*)(Hiba Triki)(.*)', ['The office of Ms Hiba Triki is A104']],
    ['(.*)(Naziha Boughdiri)(.*)', ['The office of Ms Naziha Boughdiri is A104']],
    ['(.*)(Ilia Bouraoui)(.*)', ['The office of Ms Ilia Bouraoui is A104']],
    ['(.*)(Yosra Dallagi)(.*)', ['The office of Ms Yosra Dallagi is A104']],
    ['(.*)(Elhem Bouchrida)(.*)', ['The office of Ms Elhem Bouchrida is A104']],
    ['(.*)(Ridha Hachana)(.*)', ['The office of Mr Ridha Hachana is A104']],
    ['(.*)(Ramzi Hosni)(.*)', ['The office of Mr Ramzi Hosni is B-104']],
    ['(.*)(Ghassen Ben Hamida)(.*)', ['The office of Mr Ghassen Ben Hamida is B-104']],
    ['(.*)(Malek Boulaabi)(.*)', ['The office of Mr Malek Boulaabi is B-102']],
    ['(.*)(Mohamed Dhaker)(.*)', ['The office of Mr Mohamed Dhaker is B-102']],
    ['(.*)(Belgacem Harbi)(.*)', ['The office of Mr Belgacem Harbi is B-102']],
    ['(.*)(Mouadh Riahi)(.*)', ['The office of Mr Mouadh Riahi is B-102']],
    ['(.*)(Jihen Belhaj)(.*)', ['The office of Ms Jihen Belhaj is BOX 106']],
    ['(.*)(Rim Masmoudi)(.*)', ['The office of Ms Rim Masmoudi is BOX 106']],
    ['(.*)(Marwa Jlidi)(.*)', ['The office of Ms Marwa Jlidi is A-317']],
    ['(.*)(Yasmine Mghirbi)(.*)', ['The office of Ms Yasmine Mghirbi is A-317']],
    ['(.*)(Houda Boubaker)(.*)', ['The office of Ms Houda Boubaker is A-309']],
    ['(.*)(Emna Jerbi)(.*)', ['The office of Ms Emna Jerbi is A-309']],
    ['(.*)(Fadwa Bougerra)(.*)', ['The office of Ms Fadwa Bougerra is A-308']],
    ['(.*)(Nouhaine Nefzi)(.*)', ['The office of Ms Nouhaine Nefzi is A-308']],
    ['(.*)(Taieb Touati)(.*)', ['The office of Mr Taieb Touati is CM002']],
    ['(.*)(Nadhir Ben Halima)(.*)', ['The office of Mr Nadhir Ben Halima is CM002']],
    ['(.*)(maker space)(.*)', ['The make space is at the first left door at the MSB entry (parking lot door)']],
    ['(.*)program management(.*)msb', ['The Program Management office of MSB is located on the first floor of MSB building']],
    ['(.*)finance(.*)', ['The Finance Department of SMU is located in the first floor of MSB building']],
    ['(.*)student life(.*)', ['The Student life Department is located right next to Hyppodrome Cafe inside the University']],
    ['(.*)(contact|number|phone|address)(.*)', ['The address of SMU is: Avenue De LEuro, les Berges du Lac 2, Tunis, Tunisia\nPhone: 70 016 100\nThe maps link: https://goo.gl/maps/WaJcTbw8FjirNnpk8']],
    ['(.*)(maps|google maps)(.*)', ['https://goo.gl/maps/WaJcTbw8FjirNnpk8']],
    ['(.*)(Thanks|thank you)(.*)', ['Anytime ^^', 'You are welcome ^^']]
]
academics = [
    ['my name is (.*)', ['Hi %1 , I am the SMU chatbot Ezzdine']],
    ['(hi|hello|hey|holla|hola)', ['Hey there', 'Hi there', 'Hey, how may I help you today?']],
    ['(.*)(help)(.*)', ['In the Academics section you can ask about the following topics:\n- Programs\n- Forms\n- Useful Websites']],
    ['(.*)(programs|fields)(.*)', ['The following programs are available at Medtech:\n- Pre-Engineering\n- Engineering Program\n- Licence in Computer Science\n- Master Programs\n- Transfer & double degree.']],
    ['(.*)(preengineering|pre-engineering|pre engineering)(.*)', ['The pre-engineering program provides a basic foundation in the fundamental sciences, engineering basics, and computer and communication skills. It is designed to prepare the students for the challenging demands of the engineering specializations that will follow.']],
    ['(.*)(engineering program)(.*)', ['The engineering programs at Medtech are:\n- Software Engineering\n- Computer Systems Engineering\n- Renewable Energy Engineering']],
    ['(.*)(cs engineering|computer systems|computer engineering|computer systems engineering)(.*)', ['The Computer Systems Engineering CSE program at MedTech prepares students for a productive career in the computing industry. It focuses on the key principles and techniques underlying the design, evaluation, and application of computer systems within a project-based approach. The curriculum covers the important areas of electronic circuits and systems, digital system design, computer architecture, networks, algorithms, and software systems.\n']],
    ['(.*)(renewable|renewable energy|renewable energy engineering|renewable engineering|energy engineering)(.*)', ['MedTech’s Renewable Energy Engineering REE program provides a combination of advanced technical and theoretical knowledge in the rapidly expanding area of renewable energy engineering with a clear Electrical Engineering focus']],
    ['(.*)(Licence in Computer Science|cs license|cs bachelor|computer science|bachelor)(.*)', ['MedTech’s Licence in Computer Science seeks to meet the dual objective of ensuring a solid basic training in fundamental areas, such as mathematics and programming, as well as specifics of Computer Engineering. The program helps students to develop a broad spectrum of skills required for pursuing advanced studies or initiating their professional careers.']],
    ['(.*)(Master Programs|masters)(.*)', ['The master programs at Medtech are:\nMaster in Blockchain and Artificial Intelligence\n- Master in Cyber Security\n- Master in Software Engineering\n- Master in Energy Management and Sustainability']],
    ['(.*)(Master in Blockchain and Artificial Intelligence|blockchain|artificial intelligence)(.*)', ['The Master aims at specialized training mainly in the following topics: Blockchain, Artificial Intelligence, Financial and Analytics Technology, Digital Business, and IT & General Management']],
    ['(.*)(Master in Cyber Security|cyber|security|cybersecurity)(.*)', ['The Master program in Cyber Security aims at specialized training in Informatics Security Cybersecurity. Giving response to a set of initiatives that have been developed at the National and International level, targeting the development of knowledge competencies in the field of Cybersecurity (e.g. IFC-UTICA Directive, US Cybersecurity Information Sharing Act, EU Directive for security across the Union) as a way to support the growth of the digital economy, preserving the privacy of citizens, and combat and prevent cybercrime and cyberterrorism']],
    ['(.*)(master in software engineering|master software engineering|master engineering)(.*)', ['The master’s in Software Engineering MSE follows international curriculum recommendations of the Association for Computer Machinery (ACM) and the Institute for Electrical and Electronic Engineers (IEEE), adapting these to national needs, the mobility in the European space, and the recommendations gathered from a wide panel of recruiters (in particular EDP, PT, Deloitte, PT-SAPO, ISA, Tapestry, Critical Software, WiT Software).']],
    ['(.*)(Software Engineering)(.*)', ['MedTech’s Software Engineering SWE program provides a combination of advanced technical and theoretical knowledge, best engineering practices, and emerging technologies to develop software that meet high quality standards.']],
    ['(.*)(Master in Energy Management and Sustainability|master in energy|sustainability)(.*)', ['The Master in Energy Management and Sustainability at the Mediterranean Institute of Technology MedTech aims at developing its students abilities to contribute to interdisciplinary interventions in areas such as the efficient use of energy, centralized or decentralized energy production, or the distribution of energy, always under a sustainable development perspective.']],
    ['(.*)(Transfer & double degree|Transfer and double degree|Transfer|partner universities)(.*)', ['Transfer & double degree programs at Medtech are:\n- Double Degree with the University of Michigan Dearborn\n- IESEG SCHOOL OF MANAGEMENT\n- KEDGE BUSINESS SCHOOL']],
    ['(.*)(Double Degree with the University of Michigan Dearborn|Michigan|Michigan Dearborn)(.*)', ['MedTech and UMD established a collaborative education initiative defined as a Dual Diploma Program. Qualified students enrolled at MedTech will be accepted into selected fields of study in the College of Engineering and Computer Science at UMD to finish the required education curriculum. They will qualify for their Engineering Degree awarded by MedTech and a Master’s degree conferred by the Regents of the University of Michigan upon the recommendation of the Horace H. Rackham School of Graduate Studies and UMD. According to this agreement, MedTech students will enjoy the in-state tuition fees.']],
    ['(.*)(IESEG SCHOOL OF MANAGEMENT|IESEG)(.*)', ['MedTech students interested in going to IESEG have the opportunity to obtain a Master of Science at IESEG various tracks. Students must meet the IESEG eligibility requirements, and all candidates are eligible to apply for and receive a discount on the tuition alongside other advantages. This partnership is designed to promote interest in business for engineering students and highlight the advantages of the engineering manager profile.']],
    ['(.*)(Kedge business school|KEDGE|Business)(.*)', ['MedTech students interested in going to KEDGE have the opportunity to obtain a Master of Science with 22 different tracks to choose from. Students must meet the KEDGE eligibility requirements, and all candidates are eligible to receive a discount throughout our partnership. This partnership is designed to promote interest in business for engineering students and highlight the advantages of the engineering manager profile.']],
    ['(.*)(forms|forum)(.*)', ['Please type which form you need:\n- Certificate (Attendance, Enrollment, Success)\n- Extended leave Request Form\n- Group Change Request Form\n- Course Withdrawal Request Form\n- Appeal Request Form']],
    ['(.*)(Certificate (Attendance, Enrollment, Success)|Certificate|Attendance|Enrollment|Success)(.*)', ['https://forms.office.com/Pages/ResponsePage.aspx?id=0rdWlefyskOgtaoX-SZ67TYGp7Tmvv1HqbdsyuGv_lRUODZVVFBER0E3QUM1VU1KWTNYRTJEWEdTMS4u']],
    ['(.*)(Extended leave|Leave|Leave request)(.*)', ['https://forms.office.com/Pages/ResponsePage.aspx?id=0rdWlefyskOgtaoX-SZ67cZJ01AHcNZBoqsGHxq1oshUNjUwVkZNMkFFNzNHTU5KRERCTkFXTkM0Ry4u']],
    ['(.*)(Group Change Request|Group Change|Change Request)(.*)', ['https://forms.office.com/Pages/ResponsePage.aspx?id=0rdWlefyskOgtaoX-SZ67cZJ01AHcNZBoqsGHxq1oshUNkhVMTc1NlBHVk1CN0c5R0haSENWQTJONS4u']],
    ['(.*)(Course Withdrawal Request|Course Withdrawal|Withdrawal Request)(.*)', ['https://forms.office.com/Pages/ResponsePage.aspx?id=0rdWlefyskOgtaoX-SZ67cZJ01AHcNZBoqsGHxq1oshUNElJVVoxNkxBNUw2OFk3MDk3WkRQTDFMNS4u']],
    ['(.*)(Appeal Request|Appeal)(.*)', ['https://forms.office.com/Pages/ResponsePage.aspx?id=0rdWlefyskOgtaoX-SZ67cZJ01AHcNZBoqsGHxq1oshUMVFHM0ZKMEFXQVhNUTZPRVFMRTIwSDUzOS4u']],
    ['(.*)(Useful Websites|Websites|links)(.*)', ['Please type which link you need:\n- Moodle\n- SMU Website\n- Medtech Website\n- Upcoming Events\n- Students Portal\n- VR TOUR)']],
    ['(.*)(Moodle)(.*)', ['https://moodle.medtech.tn/']],
    ['(.*)(SMU Website|SMU)(.*)', ['https://www.smu.tn/']],
    ['(.*)(Medtech Website|medtec website)(.*)', ['https://www.smu.tn/medtech']],
    ['(.*)(Upcoming Events|Events)(.*)', ['https://www.smu.tn/medtech/events']],
    ['(.*)(Students Portal|portal)(.*)', ['https://msbtn.sharepoint.com/sites/MEDTECHAcademicsIntranet/students']],
    ['(.*)(VR TOUR|TOUR)(.*)', ['https://www.google.com/maps/place/Mediterranean+School+of+Business+(MSB)/@36.8458514,10.2693854,3a,75y,347.85h,74.87t/data=!3m6!1e1!3m4!1sAF1QipP_eLqe_-i3GC4MPaOyfs4POqF3sdx0vikAa7ds!2e10!7i13200!8i6600!4m7!3m6!1s0x12fd4aae661385b5:0xfa55e957eda5970c!8m2!3d36.8457839!4d10.2690516!14m1!1BCgIgARICCAI']],
    ['(.*)(Thanks|thank you)(.*)', ['Anytime ^^', 'You are welcome ^^']]
]

finance = [
    ['my name is (.*)', ['Hi %1 , I am the SMU chatbot Ezzdine']],
    ['(hi|hello|hey|holla|hola)', ['Hey there', 'Hi there']],
    ['(.*)(help)(.*)', ['This section is under development']]
]

def academiaChat(val):
    chat = Chat(academics, reflections)
    response = chat.respond(val)
    return response

def buildingChat(val):
    chat = Chat(building, reflections)
    response = chat.respond(val)
    return response

def financeChat(val):
    chat = Chat(finance, reflections)
    response = chat.respond(val)
    return response