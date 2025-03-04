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
                const response = await fetch("http://127.0.0.1:8000/api/login", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ email: this.email, password: this.password })
                });

                const data = await response.json();

                if (response.ok) {
                    this.message = "Login realizado com sucesso!";
                    this.messageClass = "success";
                    localStorage.setItem("token", data.token); // Salva o token no localStorage
                    
                    // Redireciona para a página home após 2 segundos
                    setTimeout(() => {
                        window.location.href = "/home.html";
                    }, 2000);
                } else {
                    this.message = data.message || "Erro ao fazer login!";
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