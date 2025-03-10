const app = Vue.createApp({
    data() {
        return {
            checklist: [
                { pergunta: "Qual a placa do Carro?", tipo: "texto", resposta: "" },
                { pergunta: "Qual o hodômetro atual?", tipo: "texto", resposta: "" },
                { pergunta: "Qual o nível de combustível?", tipo: "texto", resposta: "" },
                { pergunta: "Qual a validade do IPVA?", tipo: "texto", resposta: "" },
                { pergunta: "Qual seu nome completo?", tipo: "texto", resposta: "" },
                { pergunta: "Qual trecho você trabalha?", tipo: "texto", resposta: "" },
                { pergunta: "Qual a data da última manutenção?", tipo: "texto", resposta: "" },
                { pergunta: "Conservação Geral do Carro", tipo: "opcao", resposta: "" },
                { pergunta: "O ar condicionado funciona?", tipo: "opcao", resposta: "" },
                { pergunta: "Você possui o cartão de abastecimento?", tipo: "opcao", resposta: "" },
                { pergunta: "A chave de ignição está ok?", tipo: "opcao", resposta: "" },
                { pergunta: "O cinto de segurança está ok?", tipo: "opcao", resposta: "" },
                { pergunta: "Os faróis e lanternas estão ok?", tipo: "opcao", resposta: "" },
                { pergunta: "Como está a limpeza do interior do veículo?", tipo: "opcao", resposta: "" },
                { pergunta: "O parabrisa está ok?", tipo: "opcao", resposta: "" },
                { pergunta: "Os pneus estão ok?", tipo: "opcao", resposta: "" },
                { pergunta: "O veículo possui chave de roda?", tipo: "opcao", resposta: "" },
                { pergunta: "Os retrovisores estão ok?", tipo: "opcao", resposta: "" },
                { pergunta: "O veículo possui tag do SemParar?", tipo: "opcao", resposta: "" },
                { pergunta: "Como está o triângulo de sinalização?", tipo: "opcao", resposta: "" },
                { pergunta: "Qual o estado geral dos vidros do veículo?", tipo: "opcao", resposta: "" },
                { pergunta: "O veículo possui macaco?", tipo: "opcao", resposta: "" },
                { pergunta: "Qual o estado do funcionamento geral do veículo?", tipo: "opcao", resposta: "" },
                { pergunta: "O limpador do para-brisa está ok?", tipo: "opcao", resposta: "" },
                { pergunta: "O esguicho de água do para-brisa funciona?", tipo: "opcao", resposta: "" },
                { pergunta: "O rack da escada está em boas condições?", tipo: "opcao", resposta: "" },
                { pergunta: "Qual o estado geral do veículo?", tipo: "opcao", resposta: "" }
            ],
            observacoes: "",
            mensagem: ""
        };
    },
    methods: {
        async enviarChecklist() {
            const placa = this.checklist.find(item => item.pergunta === "Qual a placa do Carro?")?.resposta;
            const nome = this.checklist.find(item => item.pergunta === "Qual seu nome completo?")?.resposta;

            if (!placa || !nome) {
                this.mensagem = "Por favor, preencha a placa do carro e seu nome.";
                return;
            }

            const placaRegex = /^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$/; // Placa nova Mercosul
            const placaAntigaRegex = /^[A-Z]{3}-[0-9]{4}$/; // Placa antiga Brasileira

            if (!placaRegex.test(placa.toUpperCase()) && !placaAntigaRegex.test(placa.toUpperCase())) {
                this.mensagem = "Por favor, insira uma placa válida.";
                return;
            }

            const respostasIncompletas = this.checklist.some(item => item.resposta === "");
            
            if (respostasIncompletas) {
                this.mensagem = "Por favor, preencha todas as respostas antes de enviar.";
                return;
            }

            const payload = {
                placa_carro: placa,
                nome_completo: nome,
                trecho: this.checklist.find(item => item.pergunta === "Qual trecho você trabalha?")?.resposta,
                data_ultima_manutencao: this.checklist.find(item => item.pergunta === "Qual a data da última manutenção?")?.resposta,
                hodometro: this.checklist.find(item => item.pergunta === "Qual o hodômetro atual?")?.resposta,
                nivel_combustivel: this.checklist.find(item => item.pergunta === "Qual o nível de combustível?")?.resposta,
                validade_ipva: this.checklist.find(item => item.pergunta === "Qual a validade do IPVA?")?.resposta,
                conservacao_veiculo: this.checklist.find(item => item.pergunta === "Conservação Geral do Carro")?.resposta,
                ar_condicionado: this.checklist.find(item => item.pergunta === "O ar condicionado funciona?")?.resposta,
                cartao_abastecimento: this.checklist.find(item => item.pergunta === "Você possui o cartão de abastecimento?")?.resposta,
                chave_ignicao: this.checklist.find(item => item.pergunta === "A chave de ignição está ok?")?.resposta,
                cinto_seguranca: this.checklist.find(item => item.pergunta === "O cinto de segurança está ok?")?.resposta,
                farol_lanternas: this.checklist.find(item => item.pergunta === "Os faróis e lanternas estão ok?")?.resposta,
                limpeza_interior: this.checklist.find(item => item.pergunta === "Como está a limpeza do interior do veículo?")?.resposta,
                parabrisa: this.checklist.find(item => item.pergunta === "O parabrisa está ok?")?.resposta,
                pneus: this.checklist.find(item => item.pergunta === "Os pneus estão ok?")?.resposta,
                chave_roda: this.checklist.find(item => item.pergunta === "O veículo possui chave de roda?")?.resposta,
                retrovisor: this.checklist.find(item => item.pergunta === "Os retrovisores estão ok?")?.resposta,
                tag_sem_parar: this.checklist.find(item => item.pergunta === "O veículo possui tag do SemParar?")?.resposta,
                triangulo_sinalizacao: this.checklist.find(item => item.pergunta === "Como está o triângulo de sinalização?")?.resposta,
                vidros: this.checklist.find(item => item.pergunta === "Qual o estado geral dos vidros do veículo?")?.resposta,
                macaco: this.checklist.find(item => item.pergunta === "O veículo possui macaco?")?.resposta,
                funcionamento_geral: this.checklist.find(item => item.pergunta === "Qual o estado do funcionamento geral do veículo?")?.resposta,
                limpador_parabrisa: this.checklist.find(item => item.pergunta === "O limpador do para-brisa está ok?")?.resposta,
                esguicho_agua: this.checklist.find(item => item.pergunta === "O esguicho de água do para-brisa funciona?")?.resposta,
                rack_escada: this.checklist.find(item => item.pergunta === "O rack da escada está em boas condições?")?.resposta,
                estado_geral: this.checklist.find(item => item.pergunta === "Qual o estado geral do veículo?")?.resposta,
                descricao_avarias: this.observacoes
            };

            try {

                console.log("Payload enviado:", JSON.stringify(payload, null, 2));

                const response = await fetch("http://127.0.0.1:8000/checklist", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(payload)
                });

                if (!response.ok) throw new Error("Erro ao enviar checklist.");

                this.mensagem = `Checklist de ${nome} (Placa: ${placa.toUpperCase()}) enviado com sucesso!`;
            } catch (error) {
                this.mensagem = error.message.includes("Failed to fetch") 
                    ? "Falha na conexão com o servidor."
                    : "Erro ao enviar checklist.";
                console.error(error);
            }
        }
    }
});

app.mount("#app");