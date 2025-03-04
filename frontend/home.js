const app = Vue.createApp({
    mounted() {
        if (!localStorage.getItem("token")) {
            window.location.href = "/login.html";
        }
    },
    methods: {
        logout() {
            localStorage.removeItem("token");
            window.location.href = "/login.html";
        }
    }
});

app.mount("#app");