import unittest
import spacy
import timeit

from models.spacy.Spacy import SpacyModel
from test.ConfusionMatrix import ConfusionMatrix


class TestEj3Es(unittest.TestCase):
    corpus = ""
    expected = ['04/11/2019-151:161',
                '4 de noviembre-705:719',
                '23/12/2016-1284:1294',
                '3 de octubre-3494:3506',
                '19/01/2018-22229:22239',
                '05/06/19-22529:22537',
                '9-6-2014-22896:22904',
                '30-7-2018-23207:23216',
                '30 de septiembre-23266:23282',
                '14 de octubre de 2019-23291:23312',
                'diciembre del año 2012-34593:34615',
                '8 de octubre de 2014-34691:34711',
                '13/07/2011-35864:35874',
                'septiembre del año 2009-35989:36012',
                'febrero de 2012-36029:36044',
                '14 de julio de 2014-37966:37985',
                'marzo de 2010-39172:39185',
                'agosto de 2012-39188:39202',
                '15 de julio de 2014-40666:40685',
                '17/02/2005-41439:41449',
                '20/01/2010-41661:41671',
                '19/11/2004-41829:41839',
                '27/02/2012-41856:41866',
                '14 de julio de 2014-43874:43893',
                '20/06/2008-44454:44464',
                '19/04/2012-44474:44484',
                'octubre del año 2010-44678:44698',
                'enero de 2011 hasta abril de 2012-44717:44750',
                'abril de 2012-45830:45843',
                '14 de julio de 2014-46574:46593',
                '17/07/2008-47823:47833',
                '03/07/2011-47839:47849',
                '14 de julio de 2014-49078:49097',
                '31-05-2010-49954:49964',
                'abril de 2010-50118:50131',
                'noviembre de 2012-50134:50151',
                '14 de julio de 2014-51588:51607',
                'febrero del 2009 a septiembre del 2011-53174:53212',
                '14 de julio de 2014-54293:54312',
                '13/7/2011-54755:54764',
                'noviembre de 2010 a noviembre de 2011-54824:54861',
                '14 de julio de 2014-55560:55579',
                'julio de 2012-56757:56770',
                'noviembre del año 2011-58404:58426',
                'noviembre del año 2011-59273:59295',
                '14 de julio de 2014-59564:59583',
                'noviembre del año 2011-60654:60676',
                'noviembre del año 2011-61507:61529',
                '14 de julio de 2014-61816:61835',
                '08/07/2005-65909:65919',
                '04/01/2012-65923:65933',
                '14-07-2005-65971:65981',
                '01-01-2012-65991:66001',
                '14 de julio de 2014-68109:68128',
                '04/01/2011-68829:68839',
                '29/11/2011-68849:68859',
                '15 de julio de 2014-69927:69946',
                'abril del año 2007-70990:71008',
                'junio del año 2012-71025:71043',
                '18/01/2012-73745:73755',
                '07/05/2012-73765:73775',
                '14 de julio de 2014-74583:74602',
                '5 de septiembre del 2011-75866:75890',
                '23 de julio del 2012-75896:75916',
                '14 de julio de 2014-76938:76957',
                '15/08/2009-78094:78104',
                '26/10/2012-78114:78124',
                'septiembre de 2009-78248:78266',
                'agosto del 2012-78269:78284',
                'septiembre de 2009 hasta agosto del 2012-79080:79120',
                '14 de julio de 2014-79363:79382',
                '24/09/2007-80424:80434',
                'mayo de 2012-81362:81374',
                'junio de 2007-82173:82186',
                'febrero de 2012-82203:82218',
                '14 de julio de 2014-82991:83010',
                '1 de enero-84083:84093',
                '6 de julio de 2012-84096:84114',
                '14 de julio de 2014-84911:84930',
                'mayo de 2011-86272:86284',
                'diciembre de 2011-86287:86304',
                '14 de julio de 2014-87916:87935',
                'diciembre de 2011-88948:88965',
                '14 de julio de 2014-90483:90502',
                '16 de marzo del 2010-91480:91500',
                '12 de marzo del 2011-91506:91526',
                '14 de julio de 2014-92706:92725',
                '18/08/2011-94342:94352',
                '18/04/2012-94399:94409',
                'febrero del año 2012-96534:96554',
                '15/07/2014-96911:96921',
                'julio de 2011 a febrero de 2012-97771:97802',
                '14 de julio de 2014-98625:98644',
                'octubre de 2007-99245:99260',
                'diciembre de 2012-99263:99280',
                '14 de julio de 2014-99762:99781',
                '14 de julio de 2014-100743:100762',
                '14 de julio de 2014-102604:102623',
                'mayo de 2012-103631:103643',
                '14 de julio de 2014-104572:104591',
                '14 de julio de 2014-106392:106411',
                '02/05/2009-108840:108850',
                'mayo del año 2009-109021:109038',
                'febrero de 2011-109056:109071',
                '14 de julio de 2014-111279:111298',
                '23/09/2008-112186:112196',
                'agosto del año 2008-112271:112290',
                'diciembre de 2010-112307:112324',
                '14 de julio de 2014-113184:113203',
                '03/01/2012-114165:114175',
                '06/07/2012-114179:114189',
                '03/01/2012-116158:116168',
                '06/07/2012-116172:116182',
                '31/07/2009-117363:117373',
                '20/07/2012-117379:117389',
                'enero de 2011 a julio de 2012-117460:117489',
                'julio del año 2012-118384:118402',
                '14 de julio de 2014-118865:118884',
                '02/01/2012-119864:119874',
                '12/07/2012-119878:119888',
                '14 de julio de 2014-121128:121147',
                '1 de enero-122428:122438',
                '11 de julio-122460:122471',
                '14 de julio de 2014-123619:123638',
                'octubre del 2012-124660:124676',
                '14 de julio de 2014-125875:125894',
                'marzo del año 2006-128232:128250',
                'junio de 2012-128267:128280',
                'diciembre del año 2005-129148:129170',
                'octubre de 2012-129187:129202',
                '14 de julio de 2014-129439:129458',
                '18/10/2011-130346:130356',
                '19/2/2012-130366:130375',
                '14 de julio de 2014-131118:131137',
                'diciembre de 2008 a junio de 2011-132184:132217',
                '14 de julio de 2014-132816:132835',
                'Noviembre de 2011 hasta Febrero de 2012-134106:134145',
                'febrero de 2012-134588:134603',
                '18 de enero-135415:135426',
                '02 de julio de 2012-135429:135448',
                'junio de 2012-135490:135503',
                '29/06/2011-137708:137718',
                '28/06/2012-137728:137738',
                '14 de julio de 2014-138784:138803',
                '29/05/2009-140111:140121',
                '02/07/2012-140127:140137',
                'enero del año 2011-140148:140166',
                'junio del año 2012-140169:140187',
                'junio del año 2012-140386:140404',
                '14 de julio de 2014-140863:140882',
                'noviembre del año 2006-141939:141961',
                'octubre de 2012-141979:141994',
                'enero del año 2011-145696:145714',
                'julio de 2011-145731:145744',
                '14 de julio de 2014-147139:147158',
                '01 de Enero del 2010-147601:147621',
                '31 de Julio-147627:147638',
                'octubre de 2009 hasta julio de 2012-148474:148509',
                '01 de Enero del 2007-149413:149433',
                '31 de Enero del 2013-149439:149459',
                '14 de julio de 2014-151178:151197',
                '23/04/2011-152085:152095',
                '03/09/2012-152105:152115',
                'julio de 2012-152275:152288',
                'junio del año 2011-154000:154018',
                'julio del año 2012-154021:154039',
                'febrero del año 2011-156160:156180',
                'junio de 2012-156198:156211',
                'febrero de 2011-157068:157083',
                'junio del año 2012-157086:157104',
                '16/07/2014-157463:157473',
                'junio del año 2012-158970:158988',
                '10/01/2012-162003:162013',
                '25/06/2012-162023:162033',
                '14 de julio de 2014-163665:163684',
                'julio de 2011-165149:165162',
                '14 de julio de 2014-167005:167024',
                '03/01/2012-168225:168235',
                '01/06/2012-168245:168255',
                '15 de julio de 2014-169076:169095',
                '02/01/2012-170620:170630',
                '31/05/2012-170637:170647',
                '15 de julio de 2014-171609:171628',
                '11 de enero del 2008-173614:173634',
                '23 de septiembre del 2011-173640:173665',
                '10 de diciembre del 2007-173728:173752',
                '23 de septiembre del 2011-173756:173781',
                'agosto de 2012-179323:179337',
                '14 de julio de 2014-180048:180067',
                'diciembre del año 2011-181203:181225',
                'febrero de 2012-181228:181243',
                '07 de enero del 2009-182823:182843',
                '07 de diciembre del 2012-182849:182873',
                '14 de julio de 2014-185017:185036',
                '13/07/2011-186096:186106',
                'marzo del año 2009-186168:186186',
                'noviembre de 2012-186203:186220',
                '14 de julio de 2014-188698:188717',
                '14 de julio de 2014-191273:191292',
                'febrero de 2010 a junio de 2011-192450:192481',
                '14 de julio de 2014-193318:193337',
                'enero de 2011-194451:194464',
                'agosto del 2012-194467:194482',
                'enero de 2011-194662:194675',
                'agosto de 2012-194678:194692',
                '14 de julio de 2014-195384:195403',
                '23/02/2012-196609:196619',
                '11/07/2012-196645:196655',
                'julio del año 2012-196695:196713',
                '14 de julio de 2014-197723:197742',
                '06 de junio-198562:198573',
                '17 de octubre de 2011-198576:198597',
                'octubre del 2011-198626:198642',
                'octubre del año 2009-201903:201923',
                'mayo de 2011-201940:201952',
                '14 de julio de 2014-203848:203867',
                'junio de 2009 hasta junio de 2010-204509:204542',
                'junio de 2009-204757:204770',
                'agosto de 2010-204773:204787',
                '14 de julio de 2014-207247:207266',
                '15/04/2011-208404:208414',
                '22 de julio del año 2011-208564:208588',
                '10 de febrero de 2012-208603:208624',
                '1 de enero-209398:209408',
                '15 de febrero de 2012-209414:209435',
                '09/02/2012-210509:210519',
                '11/02/2012-210522:210532',
                '1 de enero del 2012-211291:211310',
                '15 de febrero del 2012-211316:211338',
                '1 de enero del 2012-212968:212987',
                '16 de febrero del 2012-212993:213015',
                '11/4/2008-214384:214393',
                '22/1/2013-214399:214408',
                '01-08-2012-215907:215917',
                'julio de 2012-217530:217543',
                'Octubre de 2011-218871:218886',
                '05 de abril del 2007-220333:220353',
                '23 de julio de 2012-220357:220376',
                '17 de agosto del 2006-221493:221514',
                '24 de julio del 2012-221517:221537',
                '14 de julio de 2014-221961:221980',
                'julio de 2012-222777:222790',
                '24 de mayo-223439:223449',
                '1 de agosto del año 2012-223453:223477',
                '14 de julio de 2014-223826:223845',
                'julio de 2012-224524:224537',
                'junio de 2012-224666:224679',
                '14 de julio de 2014-224850:224869',
                'junio del año 2012-225732:225750',
                'agosto de 2012-225768:225782',
                '14 de julio de 2014-227080:227099',
                '01 de marzo del 2012-227904:227924',
                '31 de agosto del 2012-227928:227949',
                '31 de octubre del 2011-230060:230082',
                '10 de abril del 2012-230088:230108',
                '14 de julio de 2014-230892:230911',
                'julio del 2012-231897:231911',
                '30/05/2005-232837:232847',
                '15/09/2011-232857:232867',
                '22/05/2012-234752:234762',
                '18/07/2012-234772:234782',
                '14 de julio de 2014-238974:238993',
                'enero del año 2012-240270:240288',
                'julio de 2012-240305:240318',
                '14 de julio de 2014-241149:241168',
                '11/05/2011-242389:242399',
                '22/07/2011-242403:242413',
                'julio de 2011-243212:243225',
                '14 de julio de 2014-244417:244436',
                'Marzo del año 2011-245367:245385',
                'Octubre de 2012-245402:245417',
                '14 de julio de 2014-246541:246560',
                '17/05/2012-247991:248001',
                '11/07/2012-248011:248021',
                'julio del año 2012-248113:248131',
                'julio del 2012-248370:248384',
                'diciembre de 2011-250727:250744',
                'enero de 2012-250747:250760',
                'septiembre de 2010-251769:251787',
                'mayo de 2012-251790:251802',
                '14 de julio de 2014-251982:252001',
                'mayo de 2012-253050:253062',
                'octubre de 2012-253065:253080',
                '14 de julio de 2014-254013:254032',
                'agosto de 2012-255069:255083',
                '04/06/2012-255285:255295',
                '27/08/2012-255305:255315',
                '09/06/2012-256037:256047',
                '03/09/2012-256068:256078',
                '14 de julio de 2014-256756:256775',
                'febrero de 2012-257992:258007',
                'octubre de 2012-258024:258039',
                '14 de julio de 2014-258697:258716',
                '12/01/2012-259828:259838',
                '03/07/2012-259842:259852',
                '14/01/2012-260352:260362',
                '03/07/2012-260375:260385',
                'mayo del año 2012-261413:261430',
                '22/05/2013-263350:263360',
                '15 de junio de 2012-263763:263782',
                '23 de agosto de 2012-263788:263808',
                '18 de junio de 2012-263846:263865',
                '28 de agosto-263877:263889',
                '17/09/2009-267377:267387',
                '12/03/2012-267397:267407',
                '14 de julio de 2014-269004:269023',
                '06 de abril del año 2012-270271:270295',
                '24 de octubre de 2012-270309:270330',
                '11/07/2012-273137:273147',
                'febrero del año 2012-274152:274172',
                'julio del año 2012-274175:274193',
                '18 de junio de 2009-276300:276319',
                '9 de mayo de 2011-276325:276342',
                'septiembre de 2011-277896:277914',
                'febrero de 2012-277917:277932',
                'febrero de 2012-279173:279188',
                '30/03/2011-279817:279827',
                '13/09/2012-279837:279847',
                'mayo de 2011 a septiembre de 2012-279855:279888',
                'septiembre del 2012-280139:280158',
                '14 de julio de 2014-280506:280525',
                'Noviembre de 2011 hasta Febrero de 2012-281615:281654',
                'febrero de 2012-282097:282112',
                '02/01/2012-282981:282991',
                '30/03/2012-282997:283007',
                '03-06-2011-283992:284002',
                'mayo del año 2005-284222:284239',
                'diciembre de 2011-284256:284273',
                '14 de julio de 2014-286012:286031',
                '14 de marzo-286684:286695',
                '29 de septiembre de 2011-286698:286722',
                '6/6/2016-288300:288308',
                '03/01/2012-288636:288646',
                '06/07/2012-288650:288660',
                '03/01/2012-290629:290639',
                '06/07/2012-290643:290653',
                'julio de 2012-291702:291715',
                '14 de julio de 2014-292392:292411',
                'marzo del 2010-293571:293585',
                'junio del año 2012-293588:293606',
                '14 de julio de 2014-294371:294390',
                'enero del 2011 hasta febrero del 2012-295479:295516',
                '1 de enero de 2007-296014:296032',
                '31 de enero de 2013-296038:296057',
                '24 de mayo-297626:297636',
                '1 de agosto-297640:297651',
                'mayo de 2012-298180:298192',
                'Mayo de 2012-299388:299400',
                '14/05/2005-300298:300308',
                '21/06/2012-300312:300322',
                '14 de julio de 2014-300974:300993',
                'junio de 2012-301857:301870',
                '14 de julio de 2014-302792:302811',
                '19 de enero de 2017-304096:304115',
                'diciembre de 2012-304312:304329',
                '1 de enero de 2004-308113:308131',
                '19 de enero de 2017-308137:308156',
                ]

    @classmethod
    def setUpClass(cls):
        print("\n######### RUNNING TESTS FOR EJ_3_ES #########")
        f = open("documents/ej_3_es_cleaned.txt", encoding="utf8")
        cls.corpus = f.read()
        f.close()

    def test_es_core_legal_sm(self):
        t1 = timeit.default_timer()
        spacy_nlp = spacy.load('models/custom_model/es_core_legal_sm')
        spacy_nlp.max_length = 2000000
        t2 = timeit.default_timer()

        print("\nModel es_core_legal_sm")
        print(f"Time to load : {t2 - t1}")

        ents = spacy_nlp(self.corpus).ents
        results = [f"{ent.text}-{ent.start_char}:{ent.end_char}" for ent in ents if ent.label_ == 'FECHA']

        cm = ConfusionMatrix(self.corpus, results, self.expected)
        cm.print()
        self.assertGreater(cm.F1, 0.8)

    def test_es_core_legal_md(self):
        t1 = timeit.default_timer()
        spacy_nlp = spacy.load('models/custom_model/es_core_legal_md')
        spacy_nlp.max_length = 2000000
        t2 = timeit.default_timer()

        print("\nModel es_core_legal_md")
        print(f"Time to load : {t2 - t1}")

        ents = spacy_nlp(self.corpus).ents
        results = [f"{ent.text}-{ent.start_char}:{ent.end_char}" for ent in ents if ent.label_ == 'FECHA']

        cm = ConfusionMatrix(self.corpus, results, self.expected)
        cm.print()
        self.assertGreater(cm.F1, 0.8)

    def test_blank_model(self):
        t1 = timeit.default_timer()
        spacy_nlp = spacy.load('models/custom_model/blank_model')
        spacy_nlp.max_length = 2000000
        t2 = timeit.default_timer()

        print("\nModel blank_model")
        print(f"Time to load : {t2 - t1}")

        ents = spacy_nlp(self.corpus).ents
        results = [f"{ent.text}-{ent.start_char}:{ent.end_char}" for ent in ents if ent.label_ == 'FECHA']

        cm = ConfusionMatrix(self.corpus, results, self.expected)
        cm.print()
        self.assertGreater(cm.F1, 0.9)

    def test_spacy(self):
        t1 = timeit.default_timer()
        spacy_model = SpacyModel()
        results = spacy_model.execute_core_algorithm(self.corpus)
        t2 = timeit.default_timer()

        print("\nSpacy")
        print(f"Time to load : {t2 - t1}")

        results = [f"{span.text}-{span.start_char}:{span.end_char}" for span in results]

        cm = ConfusionMatrix(self.corpus, results, self.expected)
        cm.print()
        self.assertGreater(cm.F1, 0.9)