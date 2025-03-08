const app = Vue.createApp({
    data() {
        return {
            email: "",
            password: "",
            message: "",
            messageClass: ""
        };
    },
    methods: {
        async login() {
            try {
                const response = await fetch("http://127.0.0.1:8000/login", {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify({ email: this.email, password: this.password })
                });

                const data = await response.json();

                if (data.token) {  // Se o token for recebido, login foi bem-sucedido
                    this.message = "Login realizado com sucesso!";
                    this.messageClass = "success";
                    
                    sessionStorage.setItem("token", data.token); // Salva o token

                    setTimeout(() => {
                        window.location.href = "home.html"; // Redireciona após 1,5s
                    }, 1500);
                } else {
                    this.message = data.detail || "Erro ao realizar login!";
                    this.messageClass = "error";
                }
            } catch (error) {
                this.message = "Erro ao conectar ao servidor!";
                this.messageClass = "error";
            }
        }
    }
});

app.mount("#app");