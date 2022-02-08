
def lang_master(lang):
    lang_data = []
    if lang == "tt":
        lang_data = {
            "TITLE_NEWS": "Noticia",
            "LBL_FUND": "FUNDUS",
            "LINK_SUM_VER": "Sumariu Verifikasaun",
            "LINK_SUM_INS": "Sumariu Inspeksaun",
            "LINK_PJ_PO": "Donu Projetu",
            "LINK_PJ_DT": "Relatoriu Projetu",
            "LINK_PJ_MP": "Mapa Projetu",
            "LINK_PJ_RnD": "Estandarizasaun no Pesquiza",
            "LBL_OTHER_INFO": "Informasaun Seluk",
            "LBL_OTHER_INFO2": "laiha informasaun no vaga",
            "LBL_RND": "Estandarizasaun no Pesquiza",
            "LBL_IMG": "Imajen",
            "LBL_PHONE": "Telemovel",
            "LBL_LINK_EXTERNAL": "Link Externa",
            "LBL_OTHER_SYSTEM": "ADN Aplikasaun Sira",
            "LBL_PUBLIC": "Publiku",
            "LBL_LOCAL": "Local",
            "LBL_SOCIAL": "Rede Sosial",
            "LBL_DESIGN_BY": "Desenvolve husi",
            "LBL_ADDRESS": "Enderesu",
            "LBL_CONTACT": "Kontaktu",
            "LBL_MUN": "Municipiu",
            "LBL_RESPONSIBLE": "Responsavel",
            "LBL_ARCHIVE": "Arkivu Noticia",
            "LBL_POWNER": "Dono Projetu",
            "LBL_PCAT": "Kategoria Projetu",
            "LBL_PMUN": "Projetu tuir Municipiu",
            "LBL_CHART_V": [
                "TOTAL PROJECTU TUIR LIVRU OGE","TOTAL DOKUMENTOS SUBMETE MAI ADN",
                "TOTAL DOKUMENTU VERIFICADO HUSI ADN","TOTAL DOKUMENTU DEVOLVE",
                "TOTAL DOKUMENTU IHA PROSESU VERIFIKASAUN","TOTAL DOKUMENTU SEIDAUK SUBMETE & DEVOLVE"
            ],
            "LBL_CHART_I": [
                "TOTAL PROJETU EM CURSO","TOTAL PROJETU SOLICITADO BA PAGAMENTO",
                "TOTAL PEDIDU PAGAMENTU SUBMETE ONA MAI ADN","TOTAL DOKUMENTU REKOMENDA ONA HUSI ADN",
                "TOTAL DOKUMENTU DEVOLVE","TOTAL DOKUMENTU IHA PROSESU INSPEKSAUN ADN"
            ],
        }
    elif lang == "pt":
        lang_data = {
            "TITLE_NEWS": "Notícias",
            "LBL_FUND": "FUNDOS",
            "LINK_SUM_VER": "Sumário de Verificação",
            "LINK_SUM_INS": "Sumário Inspeção",
            "LINK_PJ_PO": "Dono Projeto",
            "LINK_PJ_DT": "Relatório Projeto",
            "LINK_PJ_MP": "Mapa do Projeto",
            "LINK_PJ_RnD": "Documentos RnD",
            "LBL_OTHER_INFO": "Outra informação",
            "LBL_OTHER_INFO2": "sem vaga ou competição",
            "LBL_RND": "Documentos RnD",
            "LBL_IMG": "Imagens",
            "LBL_PHONE": "Telemovel",
            "LBL_LINK_EXTERNAL": "Links Externos",
            "LBL_OTHER_SYSTEM": "ADN Outros Aplicativos",
            "LBL_PUBLIC": "Público",
            "LBL_LOCAL": "Local",
            "LBL_SOCIAL": "Redes Sociais",
            "LBL_DESIGN_BY": "Desenvolvido por",
            "LBL_NACIONAL": "Desenvolvido por",
            "LBL_ADDRESS": "Endereço",
            "LBL_CONTACT": "Contacto",
            "LBL_MUN": "Município",
            "LBL_RESPONSIBLE": "Responsável",
            "LBL_ARCHIVE": "Arquiva Notícias",
            "LBL_POWNER": "Dono Projeto",
            "LBL_PCAT": "Categoria Projetos",
            "LBL_PMUN": "Projeto em Municípios",
            "LBL_CHART_V": [
                "TOTAL NOVO PROJETOS DE","TOTAL DOCUMENTOS SUBMETIDO AO ADN","TOTAL DOCUMENTOS VERIFICADO PELO ADN",
                "TOTAL DOCUMENTOS DEVOLVIDO","TOTAL DOCUMENTOS EM PROCESSO DE VERIFICAÇÃO","TOTAL DOCUMENTOS DEVOLVIDOS E NÃO SUBMETIDO"
            ],
            "LBL_CHART_I": [
                "TOTAL PROJETOS EM CURSO","TOTAL DO PROJETO SOLICITADO PARA PAGAMENTO",
                "TOTAL PEDIDO DE PAGAMENTO SUBMETIDO AO ADN",
                "TOTAL DOCUMENTOS RECOMENDADO PELO ADN", "TOTAL DOCUMENTOS DEVOLVIDO",
                "TOTAL DOCUMENTOS EM PROCESSO DE INSPEÇÃO"
            ],
        }
    elif lang == "en":
        lang_data = {
            "TITLE_NEWS": "News",
            "LBL_FUND": "FUND",
            "LINK_SUM_VER": "Verification Summary",
            "LINK_SUM_INS": "Inspection Summary",
            "LINK_PJ_PO": "Project Owner",
            "LINK_PJ_DT": "Project Report",
            "LINK_PJ_MP": "Project Map",
            "LINK_PJ_RnD": "RnD Documents",
            "LBL_OTHER_INFO": "Other Information",
            "LBL_OTHER_INFO2": "no vacancy or competition",
            "LBL_RND": "RnD Documents",
            "LBL_IMG": "Images",
            "LBL_PHONE": "Phone",
            "LBL_LINK_EXTERNAL": "External Links",
            "LBL_OTHER_SYSTEM": "ADN Others Applications",
            "LBL_PUBLIC": "Public",
            "LBL_LOCAL": "Local",
            "LBL_SOCIAL": "Social Networks",
            "LBL_DESIGN_BY": "Developed by",
            "LBL_ADDRESS": "Address",
            "LBL_CONTACT": "Contact",
            "LBL_MUN": "Municipality",
            "LBL_RESPONSIBLE": "Responsible",
            "LBL_ARCHIVE": "News Archive",
            "LBL_POWNER": "Project Owners",
            "LBL_PCAT": "Project Categories",
            "LBL_PMUN": "Project by Municipalites",
            "LBL_CHART_V": [
                "TOTAL OF NEW PROJECT OF","TOTAL OF SUBMITTED DOCUMENTS","TOTAL OF VERIFIED DOCUMENTS",
                "TOTAL OF RETURNED DOCUMENTS","TOTAL OF DOCUMENTS IN VERIFICATION PROCESS","TOTAL OF RETURNED & NOT SUBMITTED"
            ],
            "LBL_CHART_I": [
                "TOTAL PROJECTS IN PROGRESS","TOTAL PROJECT REQUESTED FOR PAYMENT",
                "TOTAL PAYMENT REQUEST SUBMITTED TO ADN",
                "TOTAL DOCUMENTS RECOMMENDED BY DNA","TOTAL OF RETURNED DOCUMENTS",
                "TOTAL DOCUMENTS UNDER INSPECTION PROCESS"
            ],
        }
    # lang_data.append([LANG_NEWS])
    return lang_data