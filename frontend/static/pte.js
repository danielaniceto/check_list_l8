const { createApp, reactive } = Vue;

createApp({
    setup() {
        const formData = reactive({
            pte_numero: "",
            validade: "",
            atividades: [],
            data_abertura: "",
            hora_abertura: "",
            hora_fechamento: "",
            local_trabalho: "",
            autorizado: "",
            riscos: [],
            outros_riscos: "",
            equipamentos: [],
            outros_equipamentos: "",
            trabalho_altura: [],
            outros_trabalho_altura: "",
            trabalho_energia: [],
            outros_trabalho_energia: "",
            abastecimento_geradores: [],
            outros_abastecimento_geradores: ""
        });

        const atividades = [
            "Trabalhos em Altura superior a 2 metros",
            "Trabalho com Energia Elétrica",
            "Abastecimento de Geradores"
        ];

        const riscos = [
            "Animais Peçonhentos",
            "Exposição a Produtos Químicos",
            "Incêndio ou Explosão",
            "Cortes",
            "Atropelamento",
            "Prensamento",
            "Choque Elétrico",
            "Contato com Superfícies Quentes",
            "Esforço Físico Intenso",
            "Exposição a Ruídos",
            "Iluminação Inadequada",
            "Queda em Diferença de Nível",
            "Impacto de Pessoa contra Objetos",
            "Queda ou Projeção de Objetos"
        ];

        const equipamentos = [
            "Andaimes",
            "Caminhão",
            "Escada Extensível",
            "Ferramentas Manuais",
            "Guindaste/Guindauto",
            "Lixadeira/Parafusadeira/Furadeira",
            "Plataforma/Cesto Aéreo"
        ];

        const trabalho_altura = [
            "Andaime possui guarda corpo, piso, rodapé travas?",
            "Avaliar risco de queda de objetos sobre pessoas",
            "Bandeira PARE e SIGA?",
            "As escadas estão em bom estado?",
            "Instalar cabos guias e trava quedas nos andaimes e torres",
            "Instalar passarela sobre o telhado",
            "Isolar e sinalizar a área de trabalho e abaixo dela",
            "Manter as ferramentas em uso sempre amarradas",
            "Plataforma elevatória: O Operador e certificado?",
            "Verificar instalação de guardo corpo"
        ];

        const trabalho_energia = [
            "Todo o circuito elétrico foi Anulado/Checado/Testado?",
            "Manter seccionadoras abertas",
            "Vestimentas adequadas para eletricidade, Antichamas NR10",
            "Isolar e sinalizar a área com cones e fitas",
            "Utilizar cadeado e identificação para bloqueio do circuito",
            "Conferir ferramentas antes e depois dos trab. da atividade manual",
            "Proibido o uso de adorno e lentes de contato",
            "O ambiente está livre de umidade?",
            "Andaime plataforma possui projeto e ART?"
        ];

        const abastecimento_geradores = [
            "Verificar o tanque e se entorno, identificando vazamentos",
            "Usar bomba elétrica de transferência de combustíveis",
            "Isolar área de trabalho",
            "Funcionário treinamento em NR20?",
            "Fazer uso do kit para abastecimento dos geradores",
            "Antes de entrar no ambiente, abrir a porta e aguardar 5 minutos"
        ];

        function submitForm() {
            formData.pte_numero = formData.pte_numero.trim(); // Remove espaços antes de validar

            if (!formData.pte_numero) {
                alert("O campo 'PTE Número' não pode estar vazio ou conter apenas espaços.");
                return;
            }

            console.log("Dados enviados:", formData); // Exibe os dados no console para ver o que foi preenchido
            alert("Formulário enviado com sucesso!");
        }

        return { formData, atividades, riscos, equipamentos, trabalho_altura, trabalho_energia, abastecimento_geradores, submitForm };
    }
}).mount("#app");