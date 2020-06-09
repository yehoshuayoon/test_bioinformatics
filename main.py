l_switch = ['TIME', 'summary_of_raw_DB']#'UMLS']#'GOA']#'TRRUST'] #'KEGG'

if __name__ == "__main__":

    if 'TIME' in l_switch:
        import yehoshuayoon as yy
        # 2020-05-13
        # default code
        start_time, date_today = yy.date_today()
        print(date_today)

    if 'summary_of_raw_DB' in l_switch:
        print('Data')
        # UMLS
        # MeSH
        print('Networks')
        # BioGRID
        # TRRUST
        # GRN (파일 찾자!)
        # KEGG
        # GOA
        # MEDLINE
        


    if 'KEGG' in l_switch:
        # 2020-05-12
        # input: KEGG database
        # output: KGML files in KGML folder
        from basic.networks.KEGG import download_KGML
        url_KEGG_human_pathways = 'http://rest.kegg.jp/list/pathway/hsa'
        # compoundsUrl = "http://rest.kegg.jp/list/compound"
        # reactionsUrl = "http://rest.kegg.jp/list/reaction"
        # glycanUrl = "http://rest.kegg.jp/list/glycan"
        listUrls = [url_KEGG_human_pathways]
        lists = [download_KGML.getContents(url) for url in listUrls]
        for content in lists:
            for line in content:
                rawID, Name = line
                ID = rawID[5:]
                # download_KGML.getKGMLfile(ID)

        # 2020-05-13
        # input: KGML files
        # output: SIF(Simple Interaction Format) files
        from basic.networks.KEGG import convert_fromKGML_toSIF
        example = './kgml2sif -g conv/gene2symbol.tsv -c conv/compound2name.tsv examples/Apoptosis/Apoptosis.xml'
        p_fi_gene2symbol = 'basic/networks/KEGG/conv/gene2symbol.tsv'
        p_fi_compound2name = 'basic/networks/KEGG//conv/compound2name.tsv'
        p_fo_KGML = 'basic/networks/KEGG/KGML/'
        p_fo_SIF = './basic/networks/KEGG/SIF/'
        yy.createFolder(p_fo_SIF)
        convert_fromKGML_toSIF.convert(p_fi_gene2symbol=p_fi_gene2symbol, p_fi_compound2name=p_fi_compound2name, p_fo_KGML=p_fo_KGML, p_fo_SIF=p_fo_SIF)

    if 'KEGG' in l_switch:
        # 2020-05-14
        # input: tree of pathway.txt
        #   https://www.kegg.jp/kegg-bin/get_htext#A2
        #       click button that is [Download htext]
        # output: tree of pathway_mod.txt
        from basic.networks.KEGG import modify_tree_of_pathways
        p_fi_tree_of_pathway = './basic/networks/KEGG/tree of ID/tree of pathway.txt'
        p_fi_tree_of_pathway_mod = './basic/networks/KEGG/tree of ID/tree of pathway_mod.txt'
        modify_tree_of_pathways.modify(p_fi_tree_of_pathway, p_fi_tree_of_pathway_mod)

    if 'GOA' in l_switch:
        from basic.networks import parse
        p_fi_rawFile = './basic/networks/GO/goa_human.gaf'
        p_fi_parsedFile = './basic/networks/GO/goa_human_parsed.tsv'
        p_fi_summary_of_parsedFile = './basic/networks/GO/goa_human_summary.txt'
        p_fi_evidence_list = './basic/networks/GO/evidence_list.txt'
        d_evidence_code = parse.load_evidence_code(p_fi_evidence_list, ['experimental evidence'], ['IC']) # search in 1st col, search in 3rd col
        l_annotation_word = ['positively_regulates', 'directly_positively_regulates', 'negatively_regulates', 'directly_negatively_regulates']
        parse.GOA(p_fi_rawFile, p_fi_parsedFile, p_fi_summary_of_parsedFile, d_evidence_code, l_annotation_word)

    if 'TRRUST' in l_switch:
        from basic.networks import conflict
        p_fi_rawFile = './basic/networks/TRRUST/trrust_rawdata.human.tsv'
        p_fi_conflict = './basic/networks/TRRUST/trrust_conflict.txt'
        p_fi_summary_of_conflict = './basic/networks/TRRUST/summary_trrust_conflict.txt'
        conflict.check_TRRUST(p_fi_rawFile, p_fi_conflict, p_fi_summary_of_conflict)

    if 'MEDLINE' in l_switch:
        from basic.networks import parse
        p_fi_rawFile = './basic/networks/MEDLINE/summary_CoOccurs_2019.txt'
        p_fi_rawFile_sum = './basic/networks/MEDLINE/summary_CoOccurs_asPctOverall_2019.txt'
        p_fi_parsedFile_freq = './basic/networks/MEDLINE/summary_CoOccurs_2019_freq.txt'
        p_fi_parsedFile_freq_starred_and_qualified = './basic/networks/MEDLINE/summary_CoOccurs_2019_freq_starred_and_qualified.txt'
        p_fi_summary_of_parsedFile = './basic/networks/MEDLINE/summary_CoOccurs_2019_summary.txt'
        mode_freq = 'Frequency Starred Qualifiers'
        # parse.MEDLINE_summary(p_fi_rawFile, p_fi_parsedFile_freq_starred_and_qualified)
        parse.MEDLINE_summary_overall(p_fi_rawFile_sum, p_fi_parsedFile_freq)

    if 'UMLS' in l_switch:
        from basic.networks import parse
        p_fi_rawFile = './basic/data/UMLS/MRCONSO.RRF'
        p_fi_parsedFile_freq = './basic/data/UMLS/CUI__(GO and Disease).txt'
        parse.UMLS(p_fi_rawFile, p_fi_parsedFile_freq)

    if 'MeSH' in l_switch:
        from basic.networks import parse
        p_fi_rawFile = './basic/data/MeSH/desc2020.xml'
        p_fi_MSH_in_disease = './basic/data/MeSH/MeSH_in_disease.txt'
        parse.MeSH__in_disease(p_fi_rawFile, p_fi_MSH_in_disease)

    if 'TIME' in l_switch:
        # 2020-05-13
        # default code
        yy.time_spent(start_time)

#test
