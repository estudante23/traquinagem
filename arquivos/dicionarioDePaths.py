paths = {
	"loginUsuario": "/html/body/hb-frotas/hb-login/div/div/form/div/div[1]/div/div/input",
	"loginSenha": "/html/body/hb-frotas/hb-login/div/div/form/div/div[2]/div/div/input",
	"loginConfirm": "/html/body/hb-frotas/hb-login/div/div/form/div/div[3]/div/button",
	"dropOutInspecao": '/html/body/hb-frotas/hb-master-layout/div/hb-top-bar/div/div/div[1]/div/ul/li[2]	',
	"inspecaoLiBotao": '//*[@id="wrapper"]/hb-top-bar/div/div/div[1]/div/ul/li[2]/a/ul/li[8]',
	"botaoNovo": '//*[@id="wrapper"]/hb-pneu-inspecao-list/div/div/section/div[1]/button',
	"conferenteInput": '//*[@id="wrapper"]/hb-pneu-inspecao-form/div[2]/div/div/div/tabset/div/tab[1]/form/div/div[1]/div/div/div[1]/hb-typeahead-borracheiro/input',
	"dataInput": '//*[@id="wrapper"]/hb-pneu-inspecao-form/div[2]/div/div/div/tabset/div/tab[1]/form/div/div[1]/div/div/div[2]/hb-datepicker/div/input',
	"botaoAvancar": '//*[@id="wrapper"]/hb-pneu-inspecao-form/div[2]/div/div/div/tabset/div/tab[1]/form/div/div[2]/button[1]',
	"placaVeiculo": '//*[@id="wrapper"]/hb-pneu-inspecao-form/div[2]/div/div/div/tabset/div/tab[2]/form/div/div[1]/div/div/div/hb-typeahead-veiculo/input',
	##################################################################################################
	"calibragemEncontrada": '//*[@id="wrapper"]/hb-pneu-inspecao-form/div[2]/div/div/div/tabset/div/tab[2]/form/div/div[2]/div[2]/form/div/div/div[2]/div/input',
	"calibragemRealizada": '//*[@id="wrapper"]/hb-pneu-inspecao-form/div[2]/div/div/div/tabset/div/tab[2]/form/div/div[2]/div[2]/form/div/div/div[3]/div/input',
	"alinhamento": '//*[@id="wrapper"]/hb-pneu-inspecao-form/div[2]/div/div/div/tabset/div/tab[2]/form/div/div[2]/div[2]/form/div/div/div[5]/div/select',
	"laudo": '//*[@id="wrapper"]/hb-pneu-inspecao-form/div[2]/div/div/div/tabset/div/tab[2]/form/div/div[2]/div[2]/form/div/div/div[6]/div/select',
	"adicionarInspecao": '//*[@id="wrapper"]/hb-pneu-inspecao-form/div[2]/div/div/div/tabset/div/tab[2]/form/div/div[2]/div[2]/form/div/div/div[7]/div/button[1]',
	"placaSelecionada": '//*[@id="wrapper"]/hb-pneu-inspecao-form/div[2]/div/div/div/tabset/div/tab[2]/form/div/div[1]/div/div/div/hb-typeahead-veiculo/typeahead-container/table/tbody/tr[2]',
	"eixos": '//*[@id="wrapper"]/hb-pneu-inspecao-form/div[2]/div/div/div/tabset/div/tab[2]/form/div/div[2]/div[1]/div/div/hb-chassi-drawer/div',
	"sulcos": (lambda i: f'//*[@id="wrapper"]/hb-pneu-inspecao-form/div[2]/div/div/div/tabset/div/tab[2]/form/div/div[2]/div[2]/form/div/div/div[4]/div/input[{i}]'),
	"botaoSalvar": '//*[@id="wrapper"]/hb-pneu-inspecao-form/div[2]/div/div/div/tabset/div/tab[2]/form/div/div[4]/button[2]'
}