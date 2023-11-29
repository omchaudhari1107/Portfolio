from home.models import *
import random as r

programming_shloks = [
    "न त्वेवाहं जातु नासं न त्वं नेमे जनाधिपाः ।splitन चैव नभविष्यामः सर्वे वयमतः परम् ॥ १२ ॥splitNever was there a time when I did not exist, nor you, nor all these kings; nor in the future shall any of us cease to be.split2.12",
    "देहिनोऽस्मिन्यथा देहे कौमारं यौवनं जरा ।splitतथा देहान्तरप्राप्तिर्धीरस्तत्र न मुह्यति ॥ १३ ॥split As the embodied soul continuously passes, in this body, from boyhood to youth to old age, the soul similarly passes into another body at death. A sober person is not bewildered by such a change.split2.13",
    "मात्रास्पर्शास्तु कौन्तेय शीतोष्णसुखदुःखदाः ।splitआगमापायिनोऽनित्यास्तांस्तितिक्षस्व भारत ॥ १४ ॥splitO son of Kuntī, the nonpermanent appearance of happiness and distress, and their disappearance in due course, are like the appearance and disappearance of winter and summer seasons. They arise from sense perception, O son of Bharata, and one must learn to tolerate them without being disturbed.split2.14",
    "नासतो विद्यते भावो नाभावो विद्यते सतः ।splitउभयोरपि दृष्टोऽन्तस्त्वनयोस्तत्त्वदर्शिभिः ॥ १६ ॥splitThose who are seers of the truth have concluded that of the nonexistent [the material body] there is no endurance and of the eternal [the soul] there is no change. This they have concluded by studying the nature of both. split 2.16",
    "न जायते म्रियते वा कदाचि-न्नायं भूत्वा भविता वा न भूयः ।splitअजो नित्यः शाश्वतोऽयं पुराणो न हन्यते हन्यमाने शरीरे ॥ २० ॥ split For the soul there is neither birth nor death at any time. He has not come into being, does not come into being, and will not come into being. He is unborn, eternal, ever-existing and primeval. He is not slain when the body is slain.split2.20",
    "वासांसि जीर्णानि यथा विहाय नवानि गृह्णाति नरोऽपराणि ।splitतथा शरीराणि विहाय जीर्णा-न्यन्यानि संयाति नवानि देही ॥ २२ ॥splitAs a person puts on new garments, giving up old ones, the soul similarly accepts new material bodies, giving up the old and useless ones.split2.22",
    "नैनं छिन्दन्ति शस्त्राणि नैनं दहति पावकः ।splitन चैनं क्ल‍ेदयन्त्यापो न शोषयति मारुतः ॥ २३ ॥splitThe soul can never be cut to pieces by any weapon, nor burned by fire, nor moistened by water, nor withered by the wind.split2.23",
    "दुःखेष्वनुद्विग्न‍मनाः सुखेषु विगतस्पृहः ।splitवीतरागभयक्रोध: स्थिधीर्मुनिरुच्यते ॥ ५६ ॥ split One who is not disturbed in mind even amidst the threefold miseries or elated when there is happiness, and who is free from attachment, fear and anger, is called a sage of steady mind. split 2.56",
    "तानि सर्वाणि संयम्य युक्त आसीत मत्परः ।splitवशे हि यस्येन्द्रियाणि तस्य प्रज्ञा प्रतिष्ठिता ॥ ६१ ॥splitOne who restrains his senses, keeping them under full control, and fixes his consciousness upon Me, is known as a man of steady intelligence.split2.61   ",
    "यज्ञार्थात्कर्मणोऽन्यत्र लोकोऽयं कर्मबन्धनः ।splitतदर्थं कर्म कौन्तेय मुक्तसङ्गः समाचर ॥ ९ ॥splitWork done as a sacrifice for Viṣṇu has to be performed; otherwise work causes bondage in this material world. Therefore, O son of Kuntī, perform your prescribed duties for His satisfaction, and in that way you will always remain free from bondage.split3.9",
    "अन्नाद्भ‍वन्ति भूतानि पर्जन्यादन्नसम्भवः ।splitयज्ञा‍द्भ‍‍वति पर्जन्यो यज्ञः कर्मसमुद्भ‍वः ॥ १४ ॥splitAll living bodies subsist on food grains, which are produced from rains. Rains are produced by performance of yajña [sacrifice], and yajña is born of prescribed duties.split3.14",
    "यद्यदाचरति श्रेष्ठस्तत्तदेवेतरो जनः ।splitस यत्प्रमाणं कुरुते लोकस्तदनुवर्तते ॥ २१ ॥splitWhatever action a great man performs, common men follow. And whatever standards he sets by exemplary acts, all the world pursues.split3.21",
    "प्रकृतेः क्रियमाणानि गुणैः कर्माणि सर्वशः ।splitअहङ्कारविमूढात्मा कर्ताहमिति मन्यते ॥ २७ ॥splitThe spirit soul bewildered by the influence of false ego thinks himself the doer of activities that are in actuality carried out by the three modes of material nature.split3.27",
    "श्री भगवानुवाच split काम एष क्रोध एष रजोगुणसमुद्भ‍वः ।splitमहाशनो महापाप्मा विद्ध्येनमिह वैरिणम् ॥ ३७ ॥split The Supreme Personality of Godhead said: It is lust only, Arjuna, which is born of contact with the material mode of passion and later transformed into wrath, and which is the all-devouring sinful enemy of this world.split3.37",
    "श्रीभगवानुवाच split इमं विवस्वते योगं प्रोक्तवानहमव्ययम् । split विवस्वान्मनवे प्राह मनुरिक्ष्वाकवेऽब्रवीत् ॥ १ ॥split The Personality of Godhead, Lord Śrī Kṛṣṇa, said: I instructed this imperishable science of yoga to the sun-god, Vivasvān, and Vivasvān instructed it to Manu, the father of mankind, and Manu in turn instructed it to Ikṣvāku.split4.1",
    "एवं परम्पराप्राप्तमिमं राजर्षयो विदुः । split स कालेनेह महता योगे नष्टः परन्तप ॥ २ ॥split This supreme science was thus received through the chain of disciplic succession, and the saintly kings understood it in that way. But in course of time the succession was broken, and therefore the science as it is appears to be lost. split4.2   ",
    "जन्म कर्म च मे दिव्यमेवं यो वेत्ति तत्त्वतः । split त्यक्त्वा देहं पुनर्जन्म नैति मामेति सोऽर्जुन ॥ ९ ॥ split One who knows the transcendental nature of My appearance and activities does not, upon leaving the body, take his birth again in this material world, but attains My eternal abode, O Arjuna. split 4.9",
    "स एवायं मया तेऽद्य योगः प्रोक्तः पुरातनः ।split भक्तोऽसि मे सखा चेति रहस्यं ह्येतदुत्तमम् ॥ ३ ॥ split That very ancient science of the relationship with the Supreme is today told by Me to you because you are My devotee as well as My friend and can therefore understand the transcendental mystery of this science. split 4.3",
    "अजोऽपि सन्नव्ययात्मा भूतानामीश्वरोऽपि सन् ।split प्रकृतिं स्वामधिष्ठाय सम्भवाम्यात्ममायया ॥ ६ ॥split Although I am unborn and My transcendental body never deteriorates, and although I am the Lord of all living entities, I still appear in every millennium in My original transcendental form. split 4.6",
    "वीतरागभयक्रोधा मन्मया मामुपाश्रिताः ।splitबहवो ज्ञानतपसा पूता मद्भ‍ावमागताः ॥ १० ॥ Being freed from attachment, fear and anger, being fully absorbed in Me and taking refuge in Me, many, many persons in the past became purified by knowledge of Me – and thus they all attained transcendental love for Me. split 4.10",
    "ये यथा मां प्रपद्यन्ते तांस्तथैव भजाम्यहम् ।split मम वर्त्मानुवर्तन्ते मनुष्याः पार्थ सर्वशः ॥ ११ ॥ split As all surrender unto Me, I reward them accordingly. Everyone follows My path in all respects, O son of Pṛthā. split 4.11",
    "चातुर्वर्ण्यं मया सृष्टं गुणकर्मविभागशः ।split तस्य कर्तारमपि मां विद्ध्यकर्तारमव्ययम् ॥ १३ ॥ split According to the three modes of material nature and the work associated with them, the four divisions of human society are created by Me. And although I am the creator of this system, you should know that I am yet the nondoer, being unchangeable. split 3.13",
    "तद्विद्धि प्रणिपातेन परिप्रश्न‍ेन सेवया ।split उपदेक्ष्यन्ति ते ज्ञानं ज्ञानिनस्तत्त्वदर्शिनः ॥ ३४ ॥ split Just try to learn the truth by approaching a spiritual master. Inquire from him submissively and render service unto him. The self-realized souls can impart knowledge unto you because they have seen the truth. split 4.34",
    "मन्मना भव मद्भ‍क्तो मद्याजी मां नमस्कुरु ।split मामेवैष्यसि युक्त्वैवमात्मानं मत्परायण: ॥ ३४ ॥ split Engage your mind always in thinking of Me, become My devotee, offer obeisances to Me and worship Me. Being completely absorbed in Me, surely you will come to Me. split 9.34",
    "अहं सर्वस्य प्रभवो मत्त: सर्वं प्रवर्तते ।splitइति मत्वा भजन्ते मां बुधा भावसमन्विता: ॥ ८ ॥ split I am the source of all spiritual and material worlds. Everything emanates from Me. The wise who perfectly know this engage in My devotional service and worship Me with all their hearts. split 10.8",
    "यद्यद्विभूतिमत्सत्त्वं श्रीमदूर्जितमेव वा ।split तत्तदेवावगच्छ त्वं मम तेजोऽशसम्भवम् ॥ ४१ ॥ split Know that all opulent, beautiful and glorious creations spring from but a spark of My splendor. split 10.41",
    "मय्येव मन आधत्स्व मयि बुद्धिं निवेशय ।split निवसिष्यसि मय्येव अत ऊर्ध्वं न संशय: ॥ ८ ॥split Just fix your mind upon Me, the Supreme Personality of Godhead, and engage all your intelligence in Me. Thus you will live in Me always, without a doubt. split 12.8",
    "सर्वयोनिषु कौन्तेय मूर्तय: सम्भवन्ति या: ।split तासां ब्रह्म महद्योनिरहं बीजप्रद: पिता ॥ ४ ॥ split It should be understood that all species of life, O son of Kuntī, are made possible by birth in this material nature, and that I am the seed-giving father. split 14.4",
    "निर्मानमोहा जितसङ्गदोषा अध्यात्मनित्या विनिवृत्तकामा: ।splitद्वन्द्वैर्विमुक्ता: सुखदु:खसंज्ञै-र्गच्छन्त्यमूढा: पदमव्ययं तत् ॥ ५ ॥ split Those who are free from false prestige, illusion and false association, who understand the eternal, who are done with material lust, who are freed from the dualities of happiness and distress, and who, unbewildered, know how to surrender unto the Supreme Person attain to that eternal kingdom. split 15.5",
    "न तद्भ‍ासयते सूर्यो न शशाङ्को न पावक: ।splitयद्ग‍त्वा न निवर्तन्ते तद्धाम परमं मम ॥ ६ ॥ split That supreme abode of Mine is not illumined by the sun or moon, nor by fire or electricity. Those who reach it never return to this material world. split 15.6",
    "ममैवांशो जीवलोके जीवभूत: सनातन: ।splitमन:षष्ठानीन्द्रियाणि प्रकृतिस्थानि कर्षति ॥ ७ ॥ split The living entities in this conditioned world are My eternal fragmental parts. Due to conditioned life, they are struggling very hard with the six senses, which include the mind. split 15.7",
    "सर्वस्य चाहं हृदि सन्निविष्टो मत्त: स्मृतिर्ज्ञानमपोहनं च ।splitवेदैश्च सर्वैरहमेव वेद्यो वेदान्तकृद्वेदविदेव चाहम् ॥ १५ ॥split I am seated in everyone’s heart, and from Me come remembrance, knowledge and forgetfulness. By all the Vedas, I am to be known. Indeed, I am the compiler of Vedānta, and I am the knower of the Vedas. split 15.15",
    "यो मामेवमसम्मूढो जानाति पुरुषोत्तमम् ।splitस सर्वविद्भ‍जति मां सर्वभावेन भारत ॥ १९ ॥ split Whoever knows Me as the Supreme Personality of Godhead, without doubting, is the knower of everything. He therefore engages himself in full devotional service to Me, O son of Bharata. split 15.19",
    "भक्त्य‍ा मामभिजानाति यावान्यश्चास्मि तत्त्वत: ।splitततो मां तत्त्वतो ज्ञात्वा विशते तदनन्तरम् ॥ ५५ ॥ split One can understand Me as I am, as the Supreme Personality of Godhead, only by devotional service. And when one is in full consciousness of Me by such devotion, he can enter into the kingdom of God. split 18.55",
    "ईश्वर: सर्वभूतानां हृद्देशेऽर्जुन तिष्ठति ।splitभ्रामयन्सर्वभूतानि यन्‍त्रारूढानि मायया ॥ ६१ ॥ split The Supreme Lord is situated in everyone’s heart, O Arjuna, and is directing the wanderings of all living entities, who are seated as on a machine, made of the material energy. split 18.61",
    "मन्मना भव मद्भ‍क्तो मद्याजी मां नमस्कुरु ।splitमामेवैष्यसि सत्यं ते प्रतिजाने प्रियोऽसि मे ॥ ६५ ॥ split Always think of Me, become My devotee, worship Me and offer your homage unto Me. Thus you will come to Me without fail. I promise you this because you are My very dear friend. split 18.65",
    "सर्वधर्मान्परित्यज्य मामेकं शरणं व्रज ।splitअहं त्वां सर्वपापेभ्यो मोक्षयिष्यामि मा श‍ुच: ॥ ६६ ॥ split Abandon all varieties of religion and just surrender unto Me. I shall deliver you from all sinful reactions. Do not fear. split 18.66",
    "यत्र योगेश्वर: कृष्णो यत्र पार्थो धनुर्धर: ।splitतत्र श्रीर्विजयो भूतिर्ध्रुवा नीतिर्मतिर्मम ॥ ७८ ॥ split Wherever there is Kṛṣṇa, the master of all mystics, and wherever there is Arjuna, the supreme archer, there will also certainly be opulence, victory, extraordinary power, and morality. That is my opinion. split 18.78",
]


def Random_shlok():
    shlok = programming_shloks[int(r.randint(0, len(programming_shloks) - 1))]
    return shlok


def Insert(name, mail, contact, comment):
    a = Contact.objects.create(name=name, email=mail, co_no=contact, comment=comment)
    return a


def read_contacts():
    contacts_list = []

    for contact in Contact.objects.all():
        contact_dict = {
            "id": contact.id,
            "name": contact.name,
            "email": contact.email,
            "co_no": contact.co_no,
            "comment": contact.comment,
        }
        contacts_list.append(contact_dict)

    return contacts_list


def Read():
    # for i in range(0, len(Contact.objects.all())):
    #     c = Contact.objects.all()[i]
    return read_contacts()

    # return c
    # print(f"{c.id}. {c.name} | {c.email} | {c.co_no} | {c.comment}")


def Delete():
    Contact.objects.all().delete()
