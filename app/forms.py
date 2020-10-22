from django import forms
#Bibliotecas Country

#My imports here
from .models import CadastroEgresso
#Dados Pessoais
PAIS_CHOICES = [
	('AF', 'Afeganistão'), ('ZA', 'África do Sul'), ('AL', 'Albânia'), ('DE', 'Alemanha'), ('AD', 'Andorra'), ('AO', 'Angola'),
    ('AI', 'Anguilla'), ('AQ', 'Antártida'), ('AG', 'Antígua e Barbuda'), ('AN', 'Antilhas Holandesas'), ('SA', 'Arábia Saudita'),
    ('DZ', 'Argélia'), ('AR', 'Argentina'), ('AM', 'Armênia'), ('AW', 'Aruba'), ('AU', 'Austrália'), ('AT', 'Áustria'),
    ('AZ', 'Azerbaijão'), ('BS', 'Bahamas'), ('BH', 'Bahrein'), ( 'BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'),
    ('BE', 'Bélgica'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermudas'), ('BO', 'Bolívia'),('BA', 'Bósnia-Herzegóvina'),
    ('BW', 'Botsuana'), ('BR', 'Brasil'), ('BN', 'Brunei'), ('BG', 'Bulgária'), ('BF', 'Burkina Fasso'), ('BI', 'Burundi'),
    ('BT', 'Butão'), ('CV', 'Cabo Verde'), ('CM', 'Camarões'), ('KH', 'Camboja'), ('CA', 'Canadá'), ('KZ', 'Cazaquistão'),
    ('TD', 'Chade'), ('CL', 'Chile'), ('CN', 'China'), ('CY', 'Chipre'), ('SG', 'Cingapura'), ('CO', 'Colômbia'), ('CG', 'Congo'),
    ('KP', 'Coréia do Norte'), ('KR', 'Coréia do Sul'), ('CI', 'Costa do Marfim'), ('CR', 'Costa Rica'), ('HR', 'Croácia (Hrvatska)'),
    ('CU', 'Cuba'), ('DK', 'Dinamarca'), ('DJ', 'Djibuti'), ('DM', 'Dominica'), ('EG', 'Egito'), ('SV', 'El Salvador'),
    ('AE', 'Emirados Árabes Unidos'), ('EC', 'Equador'), ('ER', 'Eritréia'), ('SK', 'Eslováquia'), ('SI', 'Eslovênia'),
    ('ES', 'Espanha'), ('US', 'Estados Unidos'), ('EE', 'Estônia'), ('ET', 'Etiópia'), ('FJ', 'Fiji'), ('PH', 'Filipinas'),
    ('FI', 'Finlândia'), ('FR', 'França'), ('GA', 'Gabão'), ('GM', 'Gâmbia'), ('GH', 'Gana'), ('GE', 'Geórgia'), ('GI', 'Gibraltar'),
    ('GB', 'Grã-Bretanha (Reino Unido, UK)'), ('GD', 'Granada'), ('GR', 'Grécia'), ('GL', 'Groelândia'), ('GP', 'Guadalupe'),
    ('GU', 'Guam (Território dos Estados Unidos)'), ('GT', 'Guatemala'), ('G', 'Guernsey'), ('GY', 'Guiana'), ('GF', 'Guiana Francesa'),
    ('GN', 'Guiné'), ('GQ', 'Guiné Equatorial'), ('GW', 'Guiné-Bissau'), ('HT', 'Haiti'), ('NL', 'Holanda'), ('HN', 'Honduras'),
    ('HK', 'Hong Kong'), ('HU', 'Hungria'), ('YE', 'Iêmen'), ('BV', 'Ilha Bouvet (Território da Noruega)'), ('IM', 'Ilha do Homem'),
    ('CX', 'Ilha Natal'), ('PN', 'Ilha Pitcairn'), ('RE', 'Ilha Reunião'), ('AX', 'Ilhas Aland'), ('KY', 'Ilhas Cayman'),
    ('CC', 'Ilhas Cocos'), ('KM', 'Ilhas Comores'), ('CK', 'Ilhas Cook'), ('FO', 'Ilhas Faroes'), ('FK', 'Ilhas Falkland (Malvinas)'),
    ('GS', 'Ilhas Geórgia do Sul e Sandwich do Sul'), ('HM', 'Ilhas Heard e McDonald (Território da Austrália)'),
    ('MP', 'Ilhas Marianas do Norte'), ('MH', 'Ilhas Marshall'), ('UM', 'Ilhas Menores dos Estados Unidos'), ('NF', 'Ilhas Norfolk'),
    ('SC', 'Ilhas Seychelles'), ('SB', 'Ilhas Solomão'), ('SJ', 'Ilhas Svalbard e Jan Mayen'), ('TK', 'Ilhas Tokelau'),
    ('TC', 'Ilhas Turks e Caicos'), ('VI', 'Ilhas Virgens (Estados Unidos)'), ('VG', 'Ilhas Virgens (Inglaterra)'),
    ('WF', 'Ilhas Wallis e Futuna'), ('IN', 'índia'), ('ID', 'Indonésia'), ('IR', 'Irã'), ('IQ', 'Iraque'), ('IE', 'Irlanda'),
    ('IS', 'Islândia'), ('IL', 'Israel'), ('IT', 'Itália'), ('JM', 'Jamaica'), ('JP', 'Japão'), ('JE', 'Jersey'), ('JO', 'Jordânia'),
    ('KE', 'Kênia'), ('KI', 'Kiribati'), ('KW', 'Kuait'), ('LA', 'Laos'), ('LV', 'Látvia'), ('LS', 'Lesoto'), ('LB', 'Líbano'), 
    ('LR', 'Libéria'), ('LY', 'Líbia'), ('LI', 'Liechtenstein'), ('LT', 'Lituânia'), ('LU', 'Luxemburgo'), ('MO', 'Macau'),
    ('MK', 'Macedônia (República Yugoslava)'), ('MG', 'Madagascar'), ('MY', 'Malásia'), ('MW', 'Malaui'), ('MV', 'Maldivas'),
    ('ML', 'Mali'), ('MT', 'Malta'), ('MA', 'Marrocos'), ('MQ', 'Martinica'), ('MU', 'Maurício'), ('MR', 'Mauritânia'),
    ('YT', 'Mayotte'), ('MX', 'México'), ('FM', 'Micronésia'), ('MZ', 'Moçambique'), ('MD', 'Moldova'), ('MC', 'Mônaco'),
    ('MN', 'Mongólia'), ('ME', 'Montenegro'), ('MSR', 'MS', 'Montserrat'), ('MM', 'Myanma'), ('NA', 'Namíbia'), ('NR', 'Nauru'),
    ('NP', 'Nepal'), ('NI', 'Nicarágua'), ('NE', 'Níger'), ('NG', 'Nigéria'), ('NU', 'Niue'), ('NO', 'Noruega'), ('NC', 'Nova Caledônia'),
    ('NZ', 'Nova Zelândia'), ('OM', 'Omã'), ('PA', 'Panamá'), ('PG', 'Papua-Nova Guiné'), ('PK', 'Paquistão'), ('PY', 'Paraguai'),
    ('PE', 'Peru'), ('PF', 'Polinésia Francesa'), ('PL', 'Polônia'), ('PR', 'Porto Rico'), ('PT', 'Portugal'), ('QA', 'Qatar'),
    ('KG', 'Quirguistão'), ('CF', 'República Centro-Africana'), ('CD', 'República Democrática do Congo'), ('DO', 'República Dominicana'),
    ('CZ', 'República Tcheca'), ('RO', 'Romênia'), ('RW', 'Ruanda'), ('RU', 'Rússia (antiga URSS) - Federação Russa'),
    ('EH', 'Saara Ocidental'), ('VC', 'Saint Vincente e Granadinas'), ('AS', 'Samoa Americana'), ('WS', 'Samoa Ocidental'),
    ('SM', 'San Marino'), ('SH', 'Santa Helena'), ('LC', 'Santa Lúcia'), ('BL', 'São Bartolomeu'), ('KN', 'São Cristóvão e Névis'),
    ('MF', 'São Martim'), ('ST', 'São Tomé e Príncipe'), ('SN', 'Senegal'), ('SL', 'Serra Leoa'), ('RS', 'Sérvia'),
    ('SY', 'Síria'), ('SO', 'Somália'), ('LK', 'Sri Lanka'), ('PM', 'St. Pierre and Miquelon'), ('SZ', 'Suazilândia'),
    ('SD', 'Sudão'), ('SE', 'Suécia'), ('CH', 'Suíça'), ('SR', 'Suriname'), ('TJ', 'Tadjiquistão'), ('TH', 'Tailândia'),
    ('TW', 'Taiwan'), ('TZ', 'Tanzânia'), ('IO', 'Território Britânico do Oceano índico'), ('TF', 'Territórios do Sul da França'),
    ('PS', 'Territórios Palestinos Ocupados'), ('TP', 'Timor Leste'), ('TG', 'Togo'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'),
    ('TN', 'Tunísia'), ('TM', 'Turcomenistão'), ('TR', 'Turquia'), ('TV', 'Tuvalu'), ('UA', 'Ucrânia'), ('UG', 'Uganda'),
    ('UY', 'Uruguai'), ('UZ', 'Uzbequistão'), ('VU', 'Vanuatu'), ('VA', 'Vaticano'), ('VE', 'Venezuela'), ('VN', 'Vietnã'),
    ('ZM', 'Zâmbia'), ('ZW', 'Zimbábue'),
]

ESTADOS_CHOICES = [
	('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), 
	('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), 
	('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
	('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), 
	('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), 
	('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), 
	('SE', 'Sergipe'), ('TO', 'Tocantins'),
]

#Dados Acadêmicos
YES_NO_CHOICES = [
	('nao', 'Não'),
	('sim', 'Sim'),
]

INGRESSO_CHOICES = [
	('Sim, na área de Ciência da Computação', 'Sim, na área de Ciência da Computação'),
	('Sim, em uma área diferente', 'Sim, em uma área diferente'),
	('Não, estou com outras ideias para minha vida', 'Não, estou com outras ideias para minha vida')
]

#Dados Profissionais
MERCADO_CHOICES = [
	('AF', 'Atuo na minha área de formação'),
	('AC', 'Atuo em área correlata à minha da formação'),
	('AD', 'Atuo em área diferente da minha formação'),
	('AP', 'Estou aposentado'),
	('NO', 'Não estou trabalhando'),
]

AREA_CHOICES = [
	('EngApp', 'Engenheiro de Aplicativos em Computação'),
	('EngEquip', 'Engenheiro de Equipamentos em Computação'),
	('EngSO', 'Engenheiros de Sistemas Operacionais em Computação'),
	('AdmDB', 'Administrador de Banco de Dados'),
	('AdmR', 'Administrador de Redes'),
	('AdmSO', 'Administrador de Sistemas Operacionais'),
	('AdmInfo', 'Administrador em Segurança da Informação'),
	('AnalDS', 'Analista de Desenvolvimento de Sistemas'),
	('AnalRCD', 'Analista de Redes e de Comunicação de Dados'),
	('AnalAuto', 'Analista de Sistemas de Automação'),
	('AnalSC', 'Analista de Suporte Computacional'),
	('AnalTI', 'Analista de Testes de Tecnologia da Informação'),
	('ArqTI', 'Arquiteto de Soluções de Tecnologia da Informação'),
	('Não atuo na área', 'Não trabalho na área de Ciência da Computação'),
]

TRABALHO_CHOICES = [
	('autonomo', 'Autônomo'),
	('empregado', 'Empregado'),
	('servidor', 'Servidor Público'),
	('empresario', 'Empresário'),
]

class CadastroEgressoForm(forms.ModelForm):
	#Dados Pessoais
	pais = forms.ChoiceField(choices=PAIS_CHOICES, widget=forms.RadioSelect())

	#Dados Acadêmicos
	outraFormacao = forms.ChoiceField(choices=YES_NO_CHOICES, widget=forms.Select())
	ingressoPos = forms.ChoiceField(choices=INGRESSO_CHOICES, widget=forms.RadioSelect())
	#Dados Profissionais
	opcaoMercado = forms.ChoiceField(choices=MERCADO_CHOICES, widget=forms.RadioSelect())
	areaAtuacao = forms.ChoiceField(choices=AREA_CHOICES, widget=forms.RadioSelect())
	formaTrabalho = forms.ChoiceField(choices=TRABALHO_CHOICES, widget=forms.RadioSelect())
	

	class Meta:
		model = CadastroEgresso
		fields =  '__all__'
