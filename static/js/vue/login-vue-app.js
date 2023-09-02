const loginApp = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
      return {
        start: "Primer comentario",
      };
    },
  });

  loginApp.mount("#login-app");
  
  